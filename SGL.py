import random

numberpool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

def play():
    result = []
    while len(result) != 6:
        draw = str(random.choices(numberpool, weights=(387, 335, 350, 340, 362, 356, 367, 376, 342, 340, 378, 349, 340, 322, 364, 348, 331, 355, 350, 339, 344, 369, 364, 343, 350, 359, 325, 330, 342, 320, 344, 346, 362, 348, 339, 352, 334, 348, 333, 368, 360, 363, 335, 306, 333), k=1))
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
