class Dnc:
    floorTilingMap = {}

    def floorTiling(self, n):
        if n == 1 or n == 2:
            return n
        else:
            return self.floorTiling(n-1) + self.floorTiling(n-2)


test = Dnc()
print(test.floorTiling(1))
print(test.floorTiling(2))
print(test.floorTiling(3))
print(test.floorTiling(4))
print(test.floorTiling(5))
print(test.floorTiling(6))
print(test.floorTiling(7))
