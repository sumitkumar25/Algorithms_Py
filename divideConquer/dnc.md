# Divide and conquer

# Geek for Geeks standard algorithms

01. Tiling Problem
02. Count Inversions
03. Calculate pow(x, n)
04. Closest Pair of Points **TODO**
05. Closest Pair of Points | O(nlogn) Implementation **TODO**
06. Multiply two polynomials **TODO**
07. Strassen’s Matrix Multiplication **TODO**
08. The Skyline Problem**TODO**
09. Maximum Subarray Sum
10. Longest Common Prefix
11. Search in a Row-wise and Column-wise Sorted 2D Array
12. Karatsuba algorithm for fast multiplication
13. Convex Hull (Simple Divide and Conquer Algorithm)
14. Quickhull Algorithm for Convex Hull
15. Distinct elements in subarray using Mo’s Algorithm

# Tiling Problem
Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using the 2 x 1 tiles.
A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile.

## Solution Recitation

Bottom up solution buildup

01. Board of size 2x1: **1 way**.
02. Board of size 2x2: **2 way**.
03. Board of size 2x3: **3 way**.
04. Board of size 2x4: **5 way**.
05. Board of size 2xn: **board n-1 + board n-2**.

### Complexity

2^n

### Complexity further reading for exponential and difficult recurrences.

[http://staff.cs.upt.ro/~ioana/algo/lab_analysis_approx.html].

#Count Inversions

## Solution Recitation

Using merge sort
modify the merge method to maintain an inversion count.

#Calculate pow(x, n)
We can modify our code and take advantage of this property of maths:-
We can write 2^6 as (2*2*2) * (2*2*2)
That means, we can call the power function as power(base, num/2)

#Closest Pair of Points **TODO**
#Multiply two polynomials **TODO**
#Strassen’s Matrix Multiplication **TODO**
#The Skyline Problem**TODO**

#Maximum Subarray Sum

## Solution Recitation

