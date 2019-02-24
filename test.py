def binarySearch(item, sl, start, end):
    if(start <= end):
        mid = start + ((end-start)//2)
        curr = sl[mid]
        if(item == curr[0]):
            return curr
        elif item > curr[0]:
            return binarySearch(item, sl, mid+1, end)
        elif item < curr[0]:
            return binarySearch(item, sl, 0, mid-1)
    return None


def icecreamParlor(m, arr):
    sl = []
    for i in range(0, len(arr)):
        sl.append(tuple([arr[i], i]))
    for i in sl:
        a = i
        b = binarySearch(m-i[0], sl, 0, len(sl)-1)
        if a and b:
            if a[1] < b[1]:
                print("{} {}".format(a[1]+1, b[1]+1))
            else:
                print("{} {}".format(b[1]+1, a[1]+1))
            break
# def combineIntervals(tracks):
#     stack = [tracks[0]]
#     if(len(tracks) > 0):
#         for i in range(1, len(tracks)):
#             curr = tracks[i]
#             if curr[1] <= stack[len(stack)-1][2]:
#                 if curr[2] >= stack[len(stack)-1][2]:
#                     stack[len(stack)-1][2] = curr[2]
#             else:
#                 stack.append(curr)
#     return stack


# def formatTracks(tracks):
#     combine = {}
#     for t in tracks:
#         if t[2] < t[1]:
#             t[2] = t[1]+t[2]
#             t[1] = t[2] - t[1]
#             t[2] = t[2] - t[1]
#         if t[0] in combine:
#             combine[t[0]].append(t)
#         else:
#             combine[t[0]] = [t]
#     for k, v in combine.items():
#         v.sort(key=lambda x: x[1])
#         combine[k] = combineIntervals(v)
#     return combine


# def gridlandMetro(n, m, k, track):
#     lamp = 0
#     combinedIntervals = formatTracks(track)
#     for k, intervals in combinedIntervals.items():
#         temp = 0
#         for i in intervals:
#             temp += (i[2]-i[1] + 1)
#         lamp += m - temp
#     return lamp + (n - len(combinedIntervals))*m


if __name__ == '__main__':
    m = 4
    n = 5
    arr = [1, 4, 5, 3, 2]
    icecreamParlor(m, arr)
    m = 4
    n = 4
    arr = [2 ,2, 4, 3]
    icecreamParlor(m, arr)

    # text_file = open('input.txt', 'r')
    # lines = text_file.read().split('\n')
    # mnk = list(map(int, lines[0].split()))
    # tracks = []
    # for t in range(1, len(lines)):
    #     tracks.append(list(map(int, lines[t].split())))
    # print(len(tracks))
    # result = gridlandMetro(mnk[0], mnk[1], mnk[2], tracks)
    # print(result)
    # text_file.close()
# 838714881520430512
