# MEMBER 1 CONTRIBUTION REPORT

## Smart Evacuation Hazard Query & Critical Route Analysis System Using Quad Tree and Sparse Table

**Team Role:** Member 1 --- 
**Programming Language:** Python\
**GitHub Repository:**
https://github.com/Kaushika09/smart-evacuation-dsa

------------------------------------------------------------------------

## 1. Introduction

The Smart Evacuation Hazard Query & Critical Route Analysis System is
designed to organize hazard-location information and support queries
that can help identify hazards in a selected area. The project uses two
data structures: a Quad Tree for spatial organization and searching, and
a Sparse Table for efficient range minimum and maximum queries over risk
values.

As Member 1 and team lead, my focus is on preparing to explain the Quad Tree component during the project review, project organization,
maintaining the shared GitHub repository, understanding the overall
workflow.


## 2. Project Overview

The system combines spatial hazard searching with risk-range analysis.

### 2.1 Quad Tree

A Quad Tree is used to organize two-dimensional spatial information.
Each hazard has coordinates, such as an x-coordinate and a y-coordinate.
When a node reaches its configured capacity, the region can be divided
into four smaller regions. This arrangement supports searching for
hazards within a rectangular area.

For example, a user can specify minimum and maximum x- and
y-coordinates. The system searches for hazard records that lie within
those bounds. This is useful when the user wants to inspect hazards in a
particular geographic area rather than examining every record manually.

### 2.2 Sparse Table

A Sparse Table is used for range queries over a sequence of risk values.
After preprocessing, it can answer range minimum and maximum queries
efficiently. In the project, this supports examining the risk values
associated with a selected range of sections.

### 2.3 How the Components Work Together

The Quad Tree handles location-based hazard queries, while the Sparse
Table handles range-based risk queries. Together, they demonstrate how
different data structures can be selected for different query types
within one application.

## 3. My Focus Area: Quad Tree

My technical focus for the review is understanding and explaining the
Quad Tree component.

### 3.1 Purpose

The Quad Tree is suitable for spatial data because it organizes records
according to their positions in two-dimensional space. It can subdivide
a region into smaller regions, allowing a search to focus on relevant
parts of the space.

### 3.2 Insertion

When a hazard is inserted, its coordinates determine where it belongs in
the tree. If the current node has room, the hazard can be stored there.
If the node reaches its capacity, the region is subdivided and records
are placed in the appropriate child regions, according to the
implementation.

### 3.3 Rectangular Search

A rectangular query specifies a search area using minimum and maximum x-
and y-coordinates. The query returns the hazards whose coordinates fall
inside the requested bounds. Regions that cannot contain matching points
can be skipped, depending on the implementation.

### 3.4 Why Use a Quad Tree?

-   It represents two-dimensional spatial data naturally.
-   It organizes hazard records by location.
-   It supports rectangular-region queries.
-   It provides a practical example of a tree-based data structure
    applied to a real-world-style problem.

## 4. Implementation and Demonstration Plan

For the project review, I can demonstrate the existing program and
explain its available operations. The demonstration should use the
actual program and its current output.

1.  Start the Python program.
2.  Display the available hazard records.
3.  Insert a hazard and explain how its coordinates are used.
4.  Run a rectangular query and explain the selected search bounds.
5.  Use the risk-range options to show the Sparse Table's minimum and
    maximum queries.
6.  Run the available automated tests and report the actual results.

This sequence demonstrates the spatial-query component and the
range-query component without requiring changes to the existing
implementation.

## 5. Time Complexity: Quad Tree

The time complexity of a Quad Tree operation depends on the tree's
shape, the distribution of the points, and how much of the tree a query
needs to visit.

-   **Insertion:** Depends on the depth of the tree. In an unbalanced or
    worst-case situation, insertion can take O(n).
-   **Rectangular query:** In the worst case, the search may examine all
    stored hazards, giving O(n) time.
-   **Space complexity:** The tree stores the hazard records and its
    nodes, so the required space grows with the amount of stored data.

These are worst-case explanations. The actual runtime depends on the
data and the tree structure.

## 6. GitHub and Collaboration Evidence

The GitHub repository is used to keep the source code, README, and
supporting documentation in one place. The repository also provides a
commit history that records saved changes.

Evidence I can show during evaluation includes:

-   The public project repository.
-   The uploaded Python source file and README.
-   The repository's commit history.
-   This contribution report.
-   A live run of the program and an explanation of the Quad Tree
    operations.

A repository invitation grants a teammate access after they accept it;
the invitation alone does not prove that the teammate has completed a
contribution. Each team member should document and commit work they
genuinely perform using their own GitHub account.

## 7. Learning and Review Preparation

To prepare for questions, I will be able to explain:

-   The problem the project addresses.
-   Why Quad Tree and Sparse Table are used for different types of
    queries.
-   How hazard coordinates guide spatial insertion and searching.
-   How rectangular query bounds are interpreted.
-   Why worst-case complexity can be O(n) for Quad Tree operations.
-   How the program demonstrates range minimum and maximum queries using
    a Sparse Table.
-   How the GitHub repository and commit history support project review.

## 8. Conclusion

My role as Member 1 focuses on coordinating the project repository,
organizing the shared implementation and documentation, and preparing to
explain the Quad Tree and the overall system workflow. The project
demonstrates the use of a Quad Tree for two-dimensional hazard searching
and a Sparse Table for efficient range risk analysis. During the review,
I will use the working program and repository evidence to explain the
system and the work I can substantiate.

------------------------------------------------------------------------

**Accuracy note:** This report describes repository and coordination
tasks and the technical area I am preparing to explain. I will claim
implementation, testing, or design work as personally completed only
where I actually performed that work and can demonstrate it.
