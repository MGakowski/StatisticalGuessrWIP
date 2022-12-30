import random

numberpool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]

def play():
    result = []
    while len(result) != 7:
        draw = str(random.choices(numberpool, weights=(6, 7, 5, 6, 8, 4, 5, 7, 9, 4, 8, 8, 5, 9, 5, 9, 7, 7, 8, 7, 10, 9, 11, 9, 7, 2, 9, 11, 7, 6, 7, 7, 8, 4, 5, 7, 11, 5, 7, 11, 6, 8, 3, 6, 8, 5, 7), k=1))
        #print(draw)
        if draw not in result:
            result.append(draw)
    res = [eval(i) for i in result]
    print(res)
    result = []
    res = 0

# Set how many plays
for x in range(12):
    play()
