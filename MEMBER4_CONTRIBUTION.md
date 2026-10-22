# Member 4 Contribution Report

## Smart Evacuation Hazard Query & Critical Route Analysis System

**Team member:** Member 4 — Testing and Complexity Analysis  
**Project:** Smart Evacuation Hazard Query & Critical Route Analysis System using Quad Tree and Sparse Table  
**Language:** Python

## 1. My Role

As Member 4, my assigned responsibility is testing and complexity analysis. My work focuses on checking whether the system produces correct results for normal and edge-case inputs, documenting expected outputs, and explaining the time and space complexity of the data structures.

This role supports the reliability of the prototype. Test results should be recorded only after the tests have actually been run against the final project version.

## 2. Testing Scope

The program has two main components:

- **Quad Tree:** stores hazard locations and answers rectangular spatial queries.
- **Sparse Table:** preprocesses a route-risk profile and answers range minimum and maximum queries.

The sample route-risk profile is:

`[12, 18, 15, 31, 24, 27, 19, 35, 22, 16]`

The program's menu option **7** runs the built-in automated checks.

## 3. Test Cases

The following tests should be run against the final version of `smart_evacuation.py`.

| Test | Input / Action | Expected result |
|---|---|---|
| Rectangular hazard query | Query X = 10–40 and Y = 20–45 | H1 and H3 are returned |
| Hazard outside query | Check H5 at (35, 52) for the same rectangle | H5 is excluded because Y = 52 is greater than 45 |
| Inclusive boundary | Insert a hazard at (10, 10) and query the point rectangle (10, 10)–(10, 10) | The boundary hazard is returned |
| Duplicate coordinates | Insert two hazards at the same coordinate and query that point | Both hazards are returned |
| Maximum-risk query | Query sections 3–9 | Maximum risk is 35 at section 8 |
| Minimum-risk query | Query sections 3–9 | Minimum risk is 15 at section 3 |
| Single-section query | Query section 4–4 | Minimum and maximum are both 31 |
| Invalid range | Query section 0–4 | The program rejects the range with an input error |
| Empty risk profile | Construct `SparseTable([])` | A `ValueError` is raised |
| Invalid rectangle | Enter a minimum coordinate greater than its maximum | The program rejects the rectangle |

**Note:** These are the expected outcomes from the current implementation and sample data. Run the tests before reporting them as completed test results.

## 4. How to Run the Tests

1. Open a terminal in the folder containing `smart_evacuation.py`.
2. Run:

```bash
python smart_evacuation.py
```

3. Choose menu option **7** to run the built-in automated checks.
4. Try the manual menu options for spatial queries and range minimum/maximum queries.
5. Record the actual result and whether it matched the expected result.

The built-in checks currently cover the sample rectangular query, inclusive boundary handling, duplicate coordinates, maximum and minimum range queries, a single-element range, invalid range handling, and an empty risk profile.

## 5. Complexity Analysis

Let `n` be the number of hazards and `m` be the number of route-risk entries.

### Quad Tree

- **Insertion:** depends on tree depth and hazard distribution; worst case can be O(n).
- **Rectangular query:** can skip non-intersecting regions, but the worst case is O(n).
- **Storage:** O(n) for the hazard records and linear tree overhead in the usual implementation.

### Sparse Table

- **Preprocessing time:** O(m log m).
- **Storage:** O(m log m).
- **Range minimum/maximum value lookup:** O(1) after preprocessing.
- **Full current query method:** O(m) worst case, because the implementation scans the requested range to identify the first section containing the returned minimum or maximum value.

## 6. What I Will Demonstrate

During the project review, I can:

1. Run menu option **7** and show the automated test output.
2. Demonstrate a rectangular hazard query and compare the output with the expected result.
3. Demonstrate a maximum-risk query for sections 3–9.
4. Demonstrate a minimum-risk query for sections 3–9.
5. Show how boundary, duplicate-coordinate, single-section, and invalid-range cases are handled.
6. Explain why the Quad Tree query has a worst-case O(n) complexity.
7. Explain Sparse Table preprocessing, storage, and query complexity.

## 7. Contribution Record

**Assigned responsibility:** Testing, edge-case verification, and time/space complexity analysis.

**Work represented by this report:** A test plan, expected outcomes based on the sample data and current program, instructions for running tests, and complexity notes.

Only claim tests that you personally ran and results you personally observed. If the team makes changes to the code, rerun the relevant tests before submitting this report. This document should be committed to GitHub only after reviewing it and completing the work it describes.
