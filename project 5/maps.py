map_strnew = '''
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
01010101010101010
01010101010101010
01010101010101010
00000000000000000
'''


row = [0]*170
map = [row]
for i in range(282):
    map.append(row)


for i in range(24, 272):
    for j in range(18, 28):
        map[i][j] = 1
    for j in range(36, 46):
        map[i][j] = 1
    for j in range(54, 64):
        map[i][j] = 1
    for j in range(72, 82):
        map[i][j] = 1
    for j in range(90, 100):
        map[i][j] = 1
    for j in range(108, 118):
        map[i][j] = 1
    for j in range(126, 136):
        map[i][j] = 1
    for j in range(144, 154):
        map[i][j] = 1

for i in range(24):
    map[i] = [0]*170
for i in range(48, 56):
    map[i] = [0]*170
for i in range(80, 88):
    map[i] = [0]*170
for i in range(112, 120):
    map[i] = [0]*170
for i in range(144, 152):
    map[i] = [0]*170
for i in range(176, 184):
    map[i] = [0]*170
for i in range(208, 216):
    map[i] = [0]*170
for i in range(240, 248):
    map[i] = [0]*170
for i in range(272, 282):
    map[i] = [0]*170

def get_map(s):
    return [[int(i) for i in list(row)] for row in s.split()]


grid = get_map(map_strnew)
# grid = map

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    plt.figure(1)
    plt.imshow(grid, interpolation='nearest', cmap='YlGn')
    plt.grid(False)


    plt.show()
