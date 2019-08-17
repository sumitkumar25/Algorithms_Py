#Recurrence Problems.

#Problem 1 
Professor Diogenes has n supposedly identical VLSI chips that in principle are capable of testingeach other. The professor's test jig accommodates two chips at a time. When the jig is loaded, each chip tests the other and reports whether it is good or bad. A good chip always reports accurately whether the other chip is good or bad, but the answer of a bad chip cannot be trusted.

## Solution Recitation

1. two cases, even number and odd number of chips.
2. Good chip, g will report appropriate answer.
3. Bad chip, b will change good to bad and bad to good.
4. Possible pairs.

   - **g, g**, both are **g** or both are **b**.
   - **g, b**  one possible **b**
   - **b, g**, one possible **b**.
   - **b, b**, not possible with two **g** chips.

### n is even and |g| > |b| and |g| > n/2.

1. *|g| > |b| and |g| > n/2* ensures |g| pairs > |b| pairs by atleat 1.

2. Create n/2 pairs and proceed with the tests.

   - Keep only **g, g** status pairs for further evaluation.
   - Remove one half of each set and re-pair and test again.
   

``` psuedocode
chips = [g, g, g, g, g, g, g, b, b, b, b, b];
#iteration 1:
    ggPairs = []
    pairs = [          
            (0,1), res = (g,g) 
            (2,3), res = (g,g)
            (4,5), res = (g,g)
            (6,7), res = (b,g)
            (8,9), res = (g,g)
            (10,11), res = (g,g)
            ]
    selection if res == (g,g)
    ggPairs = [(0,1),(2,3),(4,5),(8,9),(10,11)]
# divide step: choose first element from each pair
#iteration 2:
    curr_chips_indexes = [0,2,4,8,10]
    ggPairs = []
    pairs = [          
            (0,2), res = (g,g) 
            (4,8), res = (b,g)
            ]
    selection if res == (g,g)
    ggPairs = [(0)]
#iteration 3:
    curr_chips_indexes = [0]
    return chip at index 0
 ```

