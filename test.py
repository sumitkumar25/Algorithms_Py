def calculateLamp(m, t):
    return m-(t[2] - t[1] + 1)


def gridlandMetro(n, m, k, track):
    lamp = 0
    combine = {}
    for t in track:
        lamp += calculateLamp(m, t)
        if t[0] in combine:
            if t[1] <= combine[t[0]][1]:
                lamp -= combine[t[0]][1] - t[1] + 1
        else:
            combine[t[0]] = t
    return lamp + (n - len(track)) * m

if __name__ == '__main__':
    text_file = open('input27.txt','r')
    lines = text_file.read()
    print(lines.split('\n'))
    text_file.close()
