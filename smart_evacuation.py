"""
Smart Evacuation Hazard Query & Critical Route Analysis System
DSA case study prototype using:
  1. Quad Tree for 2D hazard-region queries
  2. Sparse Table for static route-risk range minimum/maximum queries

Run:
    python smart_evacuation.py

No external packages or database required.
"""

from dataclasses import dataclass
from math import log2
from typing import List, Optional, Tuple


@dataclass
class Hazard:
    hazard_id: str
    x: float
    y: float
    hazard_type: str
    severity: str

    def __str__(self) -> str:
        return (
            f"{self.hazard_id} | {self.hazard_type:<14} | "
            f"{self.severity:<8} | ({self.x:g}, {self.y:g})"
        )


@dataclass
class Rect:
    xmin: float
    ymin: float
    xmax: float
    ymax: float

    def __post_init__(self) -> None:
        if self.xmin > self.xmax or self.ymin > self.ymax:
            raise ValueError("Invalid rectangle: minimum must not exceed maximum.")

    def contains(self, x: float, y: float) -> bool:
        """Boundary points are included."""
        return self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax

    def intersects(self, other: "Rect") -> bool:
        """True when rectangles overlap or touch at a boundary."""
        return not (
            self.xmax < other.xmin
            or self.xmin > other.xmax
            or self.ymax < other.ymin
            or self.ymin > other.ymax
        )


class QuadNode:
    def __init__(self, bounds: Rect, capacity: int = 4, depth: int = 0,
                 max_depth: int = 20) -> None:
        self.bounds = bounds
        self.capacity = capacity
        self.depth = depth
        self.max_depth = max_depth
        self.hazards: List[Hazard] = []
        self.children: Optional[List["QuadNode"]] = None

    def _subdivide(self) -> None:
        midx = (self.bounds.xmin + self.bounds.xmax) / 2
        midy = (self.bounds.ymin + self.bounds.ymax) / 2

        # NW, NE, SW, SE. Boundaries can overlap; each hazard is inserted
        # into exactly one child by _child_index().
        child_bounds = [
            Rect(self.bounds.xmin, midy, midx, self.bounds.ymax),  # NW
            Rect(midx, midy, self.bounds.xmax, self.bounds.ymax),  # NE
            Rect(self.bounds.xmin, self.bounds.ymin, midx, midy),  # SW
            Rect(midx, self.bounds.ymin, self.bounds.xmax, midy),  # SE
        ]
        self.children = [
            QuadNode(b, self.capacity, self.depth + 1, self.max_depth)
            for b in child_bounds
        ]

        old_hazards = self.hazards
        self.hazards = []
        for hazard in old_hazards:
            self.children[self._child_index(hazard.x, hazard.y)].insert(hazard)

    def _child_index(self, x: float, y: float) -> int:
        midx = (self.bounds.xmin + self.bounds.xmax) / 2
        midy = (self.bounds.ymin + self.bounds.ymax) / 2
        east = x >= midx
        north = y >= midy
        if north and not east:
            return 0  # NW
        if north and east:
            return 1  # NE
        if not north and not east:
            return 2  # SW
        return 3      # SE

    def insert(self, hazard: Hazard) -> None:
        if not self.bounds.contains(hazard.x, hazard.y):
            raise ValueError(
                f"Hazard {hazard.hazard_id} at ({hazard.x}, {hazard.y}) "
                "is outside the map bounds."
            )

        if self.children is not None:
            self.children[self._child_index(hazard.x, hazard.y)].insert(hazard)
            return

        # Keep a leaf at capacity if it cannot be subdivided further.
        same_point = all(
            h.x == hazard.x and h.y == hazard.y for h in self.hazards
        )
        if (
            len(self.hazards) < self.capacity
            or self.depth >= self.max_depth
            or same_point
            or self.bounds.xmin == self.bounds.xmax
            or self.bounds.ymin == self.bounds.ymax
        ):
            self.hazards.append(hazard)
            return

        self._subdivide()
        assert self.children is not None
        self.children[self._child_index(hazard.x, hazard.y)].insert(hazard)

    def query(self, query_rect: Rect, results: List[Hazard]) -> None:
        if not self.bounds.intersects(query_rect):
            return

        if self.children is None:
            for hazard in self.hazards:
                if query_rect.contains(hazard.x, hazard.y):
                    results.append(hazard)
            return

        for child in self.children:
            child.query(query_rect, results)


class QuadTree:
    def __init__(self, map_bounds: Rect, capacity: int = 4,
                 max_depth: int = 20) -> None:
        if capacity < 1:
            raise ValueError("Quad Tree capacity must be at least 1.")
        self.root = QuadNode(map_bounds, capacity, 0, max_depth)
        self.count = 0

    def insert(self, hazard: Hazard) -> None:
        self.root.insert(hazard)
        self.count += 1

    def query(self, query_rect: Rect) -> List[Hazard]:
        results: List[Hazard] = []
        self.root.query(query_rect, results)
        return sorted(results, key=lambda h: h.hazard_id)


class SparseTable:
    """Static range-minimum and range-maximum queries, using 0-based indices."""

    def __init__(self, values: List[int]) -> None:
        if not values:
            raise ValueError("Risk profile cannot be empty.")
        self.values = list(values)
        self.n = len(values)
        self.logs = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.logs[i] = self.logs[i // 2] + 1

        levels = self.logs[self.n] + 1
        self.max_table = [[0] * self.n for _ in range(levels)]
        self.min_table = [[0] * self.n for _ in range(levels)]

        for i, value in enumerate(values):
            self.max_table[0][i] = value
            self.min_table[0][i] = value

        j = 1
        while (1 << j) <= self.n:
            length = 1 << j
            half = length >> 1
            for i in range(self.n - length + 1):
                self.max_table[j][i] = max(
                    self.max_table[j - 1][i],
                    self.max_table[j - 1][i + half],
                )
                self.min_table[j][i] = min(
                    self.min_table[j - 1][i],
                    self.min_table[j - 1][i + half],
                )
            j += 1

    def _validate_range(self, left: int, right: int) -> None:
        # Public methods use 1-based section numbering to match the case study.
        if left < 1 or right > self.n or left > right:
            raise ValueError(
                f"Invalid range [{left}, {right}]. Use 1 <= L <= R <= {self.n}."
            )

    def range_maximum(self, left: int, right: int) -> Tuple[int, int]:
        self._validate_range(left, right)
        l, r = left - 1, right - 1
        k = self.logs[r - l + 1]
        block_start = r - (1 << k) + 1
        value = max(self.max_table[k][l], self.max_table[k][block_start])
        # Return the first section in the requested range containing the maximum.
        section = next(i + 1 for i in range(l, r + 1) if self.values[i] == value)
        return value, section

    def range_minimum(self, left: int, right: int) -> Tuple[int, int]:
        self._validate_range(left, right)
        l, r = left - 1, right - 1
        k = self.logs[r - l + 1]
        block_start = r - (1 << k) + 1
        value = min(self.min_table[k][l], self.min_table[k][block_start])
        section = next(i + 1 for i in range(l, r + 1) if self.values[i] == value)
        return value, section


def build_demo_data() -> Tuple[QuadTree, List[Hazard], List[int]]:
    map_bounds = Rect(0, 0, 100, 100)
    hazards = [
        Hazard("H1", 18, 32, "Flood", "High"),
        Hazard("H2", 47, 36, "Fire", "Critical"),
        Hazard("H3", 26, 24, "Blocked Road", "Medium"),
        Hazard("H4", 62, 45, "Flood", "High"),
        Hazard("H5", 35, 52, "Landslide", "Critical"),
    ]
    tree = QuadTree(map_bounds, capacity=2, max_depth=20)
    for hazard in hazards:
        tree.insert(hazard)
    risks = [12, 18, 15, 31, 24, 27, 19, 35, 22, 16]
    return tree, hazards, risks


def print_hazards(hazards: List[Hazard]) -> None:
    if not hazards:
        print("No hazards found in this area.")
        return
    print(f"{'ID':<5} | {'TYPE':<14} | {'SEVERITY':<8} | LOCATION")
    print("-" * 52)
    for hazard in hazards:
        print(hazard)


def run_tests() -> None:
    tree, _, risks = build_demo_data()
    sparse = SparseTable(risks)

    # Expected spatial query: H1 and H3 only. H5 has y=52, outside y<=45.
    result = tree.query(Rect(10, 20, 40, 45))
    assert [h.hazard_id for h in result] == ["H1", "H3"]

    # Inclusive boundary test.
    boundary_tree = QuadTree(Rect(0, 0, 10, 10), capacity=1)
    boundary_tree.insert(Hazard("B1", 10, 10, "Fire", "High"))
    assert [h.hazard_id for h in boundary_tree.query(Rect(10, 10, 10, 10))] == ["B1"]

    # Duplicate-coordinate test.
    boundary_tree.insert(Hazard("B2", 10, 10, "Flood", "Medium"))
    assert len(boundary_tree.query(Rect(10, 10, 10, 10))) == 2

    assert sparse.range_maximum(3, 9) == (35, 8)
    assert sparse.range_minimum(3, 9) == (15, 3)
    assert sparse.range_maximum(4, 4) == (31, 4)

    try:
        sparse.range_maximum(0, 4)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid range was not rejected.")

    try:
        SparseTable([])
    except ValueError:
        pass
    else:
        raise AssertionError("Empty risk profile was not rejected.")

    print("\nAll 7 automated checks passed.")


def main() -> None:
    tree, hazards, risks = build_demo_data()
    sparse = SparseTable(risks)

    while True:
        print("\n" + "=" * 54)
        print(" SMART EVACUATION HAZARD QUERY SYSTEM")
        print("=" * 54)
        print("1. Display all hazards")
        print("2. Insert a new hazard")
        print("3. Search hazards in a rectangular area")
        print("4. Display route risk profile")
        print("5. Find maximum risk in a range")
        print("6. Find minimum risk in a range")
        print("7. Run automated test cases")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        try:
            if choice == "1":
                print_hazards(hazards)

            elif choice == "2":
                hazard_id = input("Hazard ID: ").strip()
                if not hazard_id:
                    print("Error: Hazard ID cannot be empty.")
                    continue
                if any(h.hazard_id == hazard_id for h in hazards):
                    print("Error: That hazard ID already exists.")
                    continue
                x = float(input("X coordinate (0-100): "))
                y = float(input("Y coordinate (0-100): "))
                hazard_type = input("Hazard type: ").strip()
                severity = input("Severity: ").strip()
                if not hazard_type or not severity:
                    print("Error: Type and severity cannot be empty.")
                    continue
                hazard = Hazard(hazard_id, x, y, hazard_type, severity)
                tree.insert(hazard)
                hazards.append(hazard)
                print("Hazard inserted successfully.")

            elif choice == "3":
                xmin = float(input("X minimum: "))
                xmax = float(input("X maximum: "))
                ymin = float(input("Y minimum: "))
                ymax = float(input("Y maximum: "))
                query_rect = Rect(xmin, ymin, xmax, ymax)
                print("\nMatching hazards:")
                print_hazards(tree.query(query_rect))

            elif choice == "4":
                print("Section:", " ".join(str(i) for i in range(1, len(risks) + 1)))
                print("Risk:   ", " ".join(str(v) for v in risks))

            elif choice in ("5", "6"):
                left = int(input("Left section (1-based): "))
                right = int(input("Right section (1-based): "))
                if choice == "5":
                    value, section = sparse.range_maximum(left, right)
                    print(f"Maximum risk: {value} at section {section}")
                else:
                    value, section = sparse.range_minimum(left, right)
                    print(f"Minimum risk: {value} at section {section}")

            elif choice == "7":
                run_tests()

            elif choice == "8":
                print("Exiting. Good luck with your evaluation!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

        except ValueError as error:
            print(f"Input error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nProgram ended safely.")
            break


if __name__ == "__main__":
    main()
