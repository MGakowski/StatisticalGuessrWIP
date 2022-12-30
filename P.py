import random

numberpool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def play():
    result = []
    while len(result) != 7:
        draw = str(random.choices(numberpool, weights=(45, 58, 52, 48, 45, 44, 59, 45, 59, 52, 53, 44, 45, 54, 42, 54, 65, 45, 52, 49, 47, 50, 54, 47, 57, 48, 50, 53, 46, 43, 39, 51, 39, 42, 46), k=1))
        #print(draw)
        if draw not in result:
            result.append(draw)
    p = str(random.choices(p, weights=(8, 17, 18, 15, 8, 14, 15, 11, 12, 13, 14, 9, 13, 7, 13, 7, 10, 9, 19, 14), k=1))
    result.append(p)
    res = [eval(i) for i in result]
    print(res)
    result = []
    res = 0

# Set how many plays
for x in range(12):
    play()
