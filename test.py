# students = [
#     [
#         "Sona",
#         -25.001],
#     ["Mona",
#      -25.0001],
#     ["Mini",
#      -25.000],
#     ["Rita",
#      -25.0]
# ]
# res = []
# # for i in range(0, int(input())):
# #     s = []
# #     for j in range(0, 2):
# #         s.append(input())
# #     students.append(s)
# students.sort(key=lambda s: (float(s[1])))
# min = students[0][1]
# min2 = False
# for j in range(1, len(students)):
#     print(j)
#     if students[j][1] > min and not min2:
#         min = students[j][1]
#         res.append(students[j][0])
#         min2 = True
#     elif min2 and students[j][1] == min:
#         res.append(students[j][0])

# if len(res) > 1:
#     res.sort(key=lambda s: (s[0]))

# for r in res:
#     print(r)

string = "ABCDCDC"
sub_string = "CDC"
print(type(string))