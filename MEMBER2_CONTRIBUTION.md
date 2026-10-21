# Member 2 Contribution Report

## Smart Evacuation Hazard Query & Critical Route Analysis System

**Team member:** Member 2 --- Sparse Table\
**Project:** Smart Evacuation Hazard Query & Critical Route Analysis
System using Quad Tree and Sparse Table\
**Language:** Python

## 1. My Role

As Member 2, my assigned responsibility is the **Sparse Table**
component. This data structure supports efficient range maximum and
range minimum queries on the route-risk profile used by the Smart
Evacuation prototype.

My focus is understanding and explaining how the risk data is
preprocessed, how a query finds the maximum or minimum risk within a
selected section range, and the time and space complexity of these
operations.

## 2. Work Area: Sparse Table

The program stores the sample route-risk profile:

`[12, 18, 15, 31, 24, 27, 19, 35, 22, 16]`

The public query methods use **1-based section numbering**. For example,
section 1 has risk 12 and section 8 has risk 35.

The `SparseTable` class builds two tables:

-   `max_table` stores maximum values for intervals of power-of-two
    lengths.
-   `min_table` stores minimum values for intervals of power-of-two
    lengths.

It also builds a `logs` array so the program can determine the
appropriate power-of-two interval size for a query.

## 3. Preprocessing

During initialization, the program:

1.  Rejects an empty risk profile with a `ValueError`.
2.  Copies the input values and records the number of sections.
3.  Precomputes logarithm values for interval lengths.
4.  Initializes the minimum and maximum tables.
5.  Fills level 0 with the original risk values.
6.  Builds larger intervals by combining two adjacent half-length
    intervals using `min()` and `max()`.

For a risk profile of length `n`, the standard Sparse Table
preprocessing time and space complexity are both **O(n log n)**.

## 4. Range Maximum Query

The `range_maximum(left, right)` method finds the maximum risk in an
inclusive section range.

It validates the range, converts the 1-based section numbers to 0-based
indices, selects the largest power-of-two interval that fits the range,
and compares the precomputed maximums of two overlapping intervals. It
returns both the maximum risk value and the first section in the
requested range containing that value.

**Example:** Query sections 3 through 9.

-   Expected maximum risk: **35**
-   Section: **8**

## 5. Range Minimum Query

The `range_minimum(left, right)` method follows the same process, using
the minimum table instead.

**Example:** Query sections 3 through 9.

-   Expected minimum risk: **15**
-   Section: **3**

For the standard overlapping-interval method, each range minimum or
maximum value can be found in **O(1)** time after preprocessing. In this
implementation, locating the first section containing the returned value
uses a subsequent scan of the selected range, so the full method can
take **O(n)** time in the worst case. The value query itself is O(1).

## 6. Input Validation and Edge Cases

The implementation checks that a query satisfies:

`1 <= left <= right <= n`

Invalid ranges raise a `ValueError` with an explanatory message. The
program catches `ValueError` in its menu loop and prints an input-error
message.

Important cases to understand and demonstrate:

-   **Single-section range:** querying section 4 through section 4
    should return risk 31 for both minimum and maximum.
-   **Invalid left endpoint:** querying from section 0 should be
    rejected.
-   **Reversed range:** a range where `left > right` should be rejected.
-   **Empty input profile:** constructing `SparseTable([])` should be
    rejected.

## 7. How I Will Demonstrate My Contribution

During the project review, I can:

1.  Open `smart_evacuation.py` and explain the `SparseTable` class.
2.  Show how the `logs`, `max_table`, and `min_table` arrays are built.
3.  Select menu option **4** to display the route-risk profile.
4.  Select menu option **5** and query sections 3 through 9 to show the
    maximum risk.
5.  Select menu option **6** and query sections 3 through 9 to show the
    minimum risk.
6.  Demonstrate a single-section query and an invalid range.
7.  Select menu option **7** to run the built-in automated checks.

Run the program from the project folder with:

``` bash
python smart_evacuation.py
```

If `python` is not recognized, try:

``` bash
python3 smart_evacuation.py
```

## 8. Complexity Summary

Let `n` be the number of route-risk entries.

  -----------------------------------------------------------------------
  Operation                                                    Complexity
  ------------------------------ ----------------------------------------
  Sparse Table preprocessing                                   O(n log n)
  time                           

  Sparse Table storage                                         O(n log n)

  Minimum/maximum value lookup                                       O(1)
  after preprocessing            

  Full current method, including                          O(n) worst case
  finding the first matching     
  section                        
  -----------------------------------------------------------------------

## 9. Contribution Record

**Assigned responsibility:** Sparse Table --- preprocessing and range
maximum/minimum queries.

**Work represented by this report:** Explanation of the Sparse Table
design used in the project, its preprocessing steps, query flow, input
validation, complexity, and demonstration plan.

Only claim coding, testing, or repository work that you personally
performed and can demonstrate. Before submission, run the relevant
operations and built-in checks against the final version of
`smart_evacuation.py`, and record the observed results truthfully.
