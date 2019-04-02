# p = [4, 2, 5, 7, 4, 6, 2]
# n = len(p) - 1
# m = [[None for i in range(n)] for j in range(n)]
# s = [[None for i in range(n)] for j in range(n)]
# for i in range(n):
#     #     m[i][i] = "diag"
#     m[i][i] = 0

# for r in range(1, n):
#     for c in range(1, n - r):
#         j = c + r
#         # print("c,j-1", c, j - 1)
#         m[r][j] = 0
#         # m[r][j] = "test"
#         for k in range(c, j - 1):
#             print(m[c][k], m[k + 1][j])
#             q = m[c][k] + m[k + 1][j] + p[c - 1] * p[k] * p[j]
#             if q < m[c][j]:
#                 m[i, j] = q
#                 s[i, j] = k


# def printm():
#     for i in m:
#         print(i)


# printm()

m = [[(j, i) for i in range(4)] for j in range(4)]
n = 4
for l in range(1, 4):
    for i in range(n - l + 1):
        j = i + l -1
        m[i][j] = "test"
        for x in m:
                print(x)
        print('////////////////////////////////////////////')

