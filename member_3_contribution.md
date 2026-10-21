# Testing and Validation Report

## Smart Evacuation Hazard Query & Critical Route Analysis System

**Team member:** Member 3 --- Testing and Validation\
**Project language:** Python\
**Primary data structures:** Quad Tree and Sparse Table

## 1. Purpose

This document describes the test plan for checking the Smart Evacuation
program's main functions. The goal is to verify that spatial hazard
searches and route-risk range queries return sensible results and that
invalid or boundary inputs are handled appropriately.

> Before submission, run each test against the final version of
> `smart_evacuation.py` and update the **Observed result** column with
> what actually happened. Do not mark a test as passed unless you have
> run it.

## 2. Features to validate

-   Displaying the hazard records.
-   Searching for hazards inside a rectangular region using the Quad
    Tree.
-   Displaying the route-risk profile.
-   Finding the maximum risk over a selected range using the Sparse
    Table.
-   Finding the minimum risk over a selected range using the Sparse
    Table.
-   Running the program's built-in automated checks.
-   Handling boundary values and invalid ranges.

## 3. Test cases

  --------------------------------------------------------------------------------------------
  Test ID        Feature          Input / Action                 Expected       Observed
                                                                 result         result
  -------------- ---------------- ------------------------------ -------------- --------------
  T01            Program startup  Run                            The program    Fill in after
                                  `python smart_evacuation.py`   starts and     running
                                                                 displays its   
                                                                 menu.          

  T02            Display hazards  Select the menu option for     The stored     Fill in after
                                  displaying all hazards         hazard records running
                                                                 are displayed. 

  T03            Rectangular      Search with X from 10 to 40    Based on the   Fill in after
                 hazard search    and Y from 20 to 45            sample data    running
                                                                 described for  
                                                                 the project,   
                                                                 H1 at (18, 32) 
                                                                 and H3 at (26, 
                                                                 24) should be  
                                                                 included;      
                                                                 hazards        
                                                                 outside the    
                                                                 rectangle      
                                                                 should be      
                                                                 excluded.      

  T04            Maximum route    Query sections 3 through 9, if Expected       Fill in after
                 risk             using the sample risk profile  sample result: running
                                  in the project                 maximum risk   
                                                                 35 at section  
                                                                 8.             

  T05            Minimum route    Query sections 3 through 9, if Expected       Fill in after
                 risk             using the sample risk profile  sample result: running
                                  in the project                 minimum risk   
                                                                 15 at section  
                                                                 3.             

  T06            Single-section   Query a range whose left and   The minimum    Fill in after
                 range            right endpoints are the same   and maximum    running
                                  valid section                  should both    
                                                                 equal that     
                                                                 section's risk 
                                                                 value.         

  T07            Invalid range    Try a range with an invalid    The program    Fill in after
                                  endpoint or left endpoint      should reject  running
                                  greater than right endpoint,   the range or   
                                  if the program accepts those   display a      
                                  inputs                         clear error    
                                                                 rather than    
                                                                 return a       
                                                                 misleading     
                                                                 answer or      
                                                                 crash.         

  T08            Built-in checks  Select the program's           The program's  Fill in after
                                  automated-test menu option     built-in       running
                                                                 checks         
                                                                 complete and   
                                                                 report their   
                                                                 results.       
  --------------------------------------------------------------------------------------------

**Note:** T03--T05 use the sample coordinates and risk values discussed
for this project. Confirm they match the data in the final program
before treating the expected outputs as authoritative. T06--T08 are
validation scenarios; the exact behavior depends on the implementation.

## 4. How to run the tests

1.  Open the folder containing `smart_evacuation.py` in VS Code.

2.  Open **Terminal → New Terminal**.

3.  Run:

    ``` bash
    python smart_evacuation.py
    ```

4.  Use the displayed menu to run the hazard search and range-query
    tests.

5.  Select the built-in automated-test option, if available.

6.  Record the actual result for each test in the table above.

7.  If an expected result differs from the observed result, investigate
    it and report the discrepancy rather than changing the record to
    "Passed."

If `python` is not recognized on your computer, try
`python3 smart_evacuation.py`.

## 5. Complexity notes for the report

These are general algorithmic bounds; the exact implementation should be
reviewed before final submission.

-   **Quad Tree rectangular query:** worst case can be `O(n)` if many or
    all hazards must be examined.
-   **Sparse Table preprocessing:** typically `O(n log n)` time and
    `O(n log n)` space.
-   **Sparse Table range minimum/maximum query:** typically `O(1)` after
    preprocessing, when implemented with the standard
    overlapping-interval method for idempotent operations such as
    minimum and maximum.

Here, `n` is the number of hazards or route-risk entries, as applicable.

## 6. Limitations and scope

-   This is a test plan for the current Python prototype, not evidence
    of live GPS navigation.
-   Results depend on the hazard coordinates and risk values actually
    stored in the program.
-   The tests should be repeated after any code change.
-   A successful test run supports the tested behavior only; it does not
    prove that every possible input is correct.

## 7. Evaluation evidence checklist

Before the demonstration, prepare:

-   [ ] A screenshot of the program starting successfully.
-   [ ] A screenshot of the rectangular hazard query and its output.
-   [ ] A screenshot of a range maximum query.
-   [ ] A screenshot of a range minimum query.
-   [ ] A screenshot of the built-in test results.
-   [ ] This report with the **Observed result** column completed
    truthfully.

## 8. Contribution record

**My assigned responsibility:** Testing and validation documentation.

**Work represented by this document:** Preparing test scenarios,
defining expected outcomes, identifying boundary/invalid-input checks,
and documenting how to record test evidence.

After executing the tests, add the date of testing and any issues
discovered here. This document should only be committed as completed
testing evidence after the tests have actually been run.
