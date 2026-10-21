# smart-evacuation-dsa
Smart Evacuation Hazard Query and Critical Route Analysis System using Quad Tree and Sparse Table
# Smart Evacuation Hazard Query & Critical Route Analysis System

## Requirements
- Python 3.9 or later
- No external libraries
- No database

## Run
Open a terminal in the folder containing `smart_evacuation.py` and run:

```bash
python smart_evacuation.py
```

## Features
- Quad Tree insertion and rectangular hazard queries
- Spatial pruning of Quad Tree regions that do not intersect a query
- Sparse Table preprocessing for static route-risk values
- O(1) range minimum and maximum queries after preprocessing
- Input validation and automated test checks

## Demo data
Hazards:
- H1: Flood, High, (18, 32)
- H2: Fire, Critical, (47, 36)
- H3: Blocked Road, Medium, (26, 24)
- H4: Flood, High, (62, 45)
- H5: Landslide, Critical, (35, 52)

Risk profile: `12 18 15 31 24 27 19 35 22 16`

For rectangle x=[10,40], y=[20,45], the correct result is H1 and H3.
H5 is outside because its y-coordinate is 52, greater than 45.

For rangeMaximum(3,9), the result is 35 at section 8.
For rangeMinimum(3,9), the result is 15 at section 3.

## Automated tests
Choose menu option 7. It checks the demo spatial query, inclusive boundary handling,
duplicate coordinates, maximum/minimum range queries, single-element ranges, invalid
ranges, and an empty risk profile.

## Complexity
- Quad Tree insertion: depends on tree depth and distribution; worst case O(n).
- Quad Tree rectangular query: depends on visited regions; worst case O(n).
- Sparse Table build: O(n log n) time and O(n log n) space.
- Sparse Table range min/max query: O(1) query time.
