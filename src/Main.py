import Map
import SA
import LS
import time
import Read
import threading


list = []
t = 0
def algrun():
    global t, list
    time_start = time.time()

    map = Map.Map()

    x, y = Read.Read()
    map.path[0] = x
    map.path[1] = y

    # state == 0: SA,  state == 1: LS
    state = 0

    if state == 0:
        # SA(map, T, Coolrate)
        alg = SA.SA(map, 100, 0.001)
        alg.run()
    elif state == 1:
        # LS(map, state), state = 0: LS1, state = 1: LS2, state = 2: 2-OPT
        alg = LS.LS(map, 2)
        alg.run()
    list.append(alg.path.distance())
    time_end = time.time()
    t += (time_end - time_start)
    print('totally cost', time_end - time_start, 's')

n = 1
for i in range(n):
    algrun()
list.sort()
sum = 0
for dis in list:
    sum += dis
if n != 1:
    print(sum / 10)
    print(list[0], list[-1])
    print(t / n)

input()
