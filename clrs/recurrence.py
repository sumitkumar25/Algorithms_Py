chip_type = [
    'g', 'g', 'g', 'b', 'g', 'g', 'b', 'b',
    'g', 'g', 'g', 'b', 'g', 'g', 'b', 'b',
    'g', 'g', 'g', 'b', 'g', 'g', 'b', 'b',
    'g', 'g', 'g', 'b', 'g', 'g', 'b', 'b']
chips = [{'type': chip_type[i], 'id':i} for i in range(len(chip_type))]
a1 = [37, 21, 53, 32, 43]
a2 = [23, 6, 34, 13, 21]
a3 = [24, 7, 30, 9, 15]
a4 = [32,  10, 31,  6, 8]
monge = [a1, a2, a3, a4]


class Recurrence:
    # 1. chip testing

    def createPairs(self, arr, l):
        start = 0
        end = l-1
        res = []
        while start < end:
            res.append((arr[start], arr[end]))
            start = start+1
            end = end - 1
        return res

    def chipTest(self, arr):
        res = []
        for i in arr:
            chipResult = [None, None]
            c1 = i[0]
            c2 = i[1]
            if c1['type'] == 'g':
                chipResult[1] = c2['type']
            else:
                chipResult[1] = 'g'
            if c2['type'] == 'g':
                chipResult[0] = c1['type']
            else:
                chipResult[0] = 'g'
            res.append(([chipResult[0], chipResult[1]]))
        return res

    def findGoodChip(self, arr):
        print(arr)
        # return last chip
        l = len(arr)
        if arr is None or l < 1:
            print("bad input arr")
            return
        elif l == 1:
            return arr[0]
        else:
            pairs = self.createPairs(arr, l)
            chip_test = self.chipTest(pairs)
            _arr = []
            for i in range(len(chip_test)):
                res = chip_test[i]
                if res[0] == 'g' and res[1] == 'g':
                    _arr.append(pairs[i])
            return self.findGoodChip([i[0] for i in _arr])
    # 2. Monge array

    def checkMonge(self, arr):
        rows = len(arr)
        for row in range(rows-2):
            for col in range(len(arr[row])-2):
                leftdiag = arr[row][col] + arr[row+1][col+1]
                rightdiag = arr[row+1][col] + arr[row][col+1]
                if leftdiag > rightdiag:
                    print('not monge at', row, col)

