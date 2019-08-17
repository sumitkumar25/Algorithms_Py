# Algorithms_Py

1. Executer file main.py

``` python
    execute = Executer()
    execute.executeOption(graphOptionString)
```

## Sorting

### Insertion Sort

#### Concept

1. Assume one side is sorted. Starting with index `0` .
2. Compare all subsequent elements with the sorted array.
3. Insert and rearrange sorted array.

#### Psuedocode

``` 
INSERTION_SORT(A)
    for j = 1 to len(A) - 1
    current = A[j]
    i = j - 1
        while i >= 0 and A[i] > current
        swap(A[i + 1], A[i])
        i++
        end loop
    A[i + 1] = current
```

#### Analysis

#### Performance pointers

## Graph
1. Adjacency list implementation
2. graphOptionString = **'graph'**

### BFS

1. Construct
2. BFS
3. directory root/graph.

