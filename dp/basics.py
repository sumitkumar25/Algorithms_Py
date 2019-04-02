# Dynamic programming basic eg.
""" 
# checklist
1. BF implementation.
2. recursive plus iterative sol.
3. dp both memoized (top down) and tabulated (bottom up)
4. complexity comparison.
---------------------------------------------------------
---------------------------------------------------------
Problem index
 1. fibo
"""


class Fibonacci:
    def nthFiboRecurse(self, n):
        if n < 1:
            return 0
        if n == 1:
            return 1
        else:
            return self.nthFiboRecurse(n - 1) + self.nthFiboRecurse(n - 2)

    def nthFiboIterative(self, n):
        if n < 0:
            return "invalid input"
        elif n < 3:
            return 1
        else:
            f1 = 1
            f2 = 1
            res = 0
            for i in range(3, n + 1):
                res = f1 + f2
                if i % 2 == 0:
                    f2 = res
                else:
                    f1 = res
            return res

    # Top down
    def nthFiboMemo(self, n, memo):
        if memo is None:
            memo = [None for i in range(n + 2)]
        if memo[n] is not None:
            return memo[n]
        elif n < 1:
            return 0
        elif n < 3:
            memo[n] = 1
            return 1
        else:
            memo[n] = self.nthFiboMemo(n - 1, memo) + self.nthFiboMemo(n - 2, memo)
            return memo[n]

    # bottom up
    def nthFiboTabulated(self, n):
        table = [None for i in range(n)]
        for i in range(n):
            if i < 2:
                table[i] = 1
            else:
                table[i] = table[i - 1] + table[i - 2]
        return table[n - 1]


# test
fibo = Fibonacci()
print("recursive 10 fibo number", fibo.nthFiboRecurse(10))
print("iterative -1 fibo number", fibo.nthFiboRecurse(-1))
print("iterative 10 fibo number", fibo.nthFiboRecurse(10))
print("iterative 1 fibo number", fibo.nthFiboRecurse(1))
print("iterative 2 fibo number", fibo.nthFiboRecurse(2))
print("iterative 3 fibo number", fibo.nthFiboRecurse(3))
print("tabu 10 fibo number", fibo.nthFiboTabulated(10))
print("tabu 1 fibo number", fibo.nthFiboTabulated(1))
print("tabu 2 fibo number", fibo.nthFiboTabulated(2))
print("tabu 3 fibo number", fibo.nthFiboTabulated(3))
