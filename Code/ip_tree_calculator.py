import random
import ip_calculator as ipc

s4096 = [[4096, 0, ],
         [4096, 1, ]]

s2048 = [[2048, 0, ],
         [2048, 1, ]]

s1024 = [[1024, 0, ],
         [1024, 1, ]]

s512 = [[512, 0, ],
        [512, 1, ]]

s256 = [[256, 0, ],
        [256, 1, ]]

s128 = [[128, 0, ],
        [128, 1, ]]

s64 = [[64, 0, ],
       [64, 1, ]]

s32 = [[32, 0, ],
       [32, 1, ]]

s16 = [[16, 0, ],
       [16, 1, ]]

s8 = [[8, 0, ],
      [8, 1, ]]

def add_value_to_matrix(value):
    matrices = [s4096, s2048, s1024, s512, s256, s128, s64, s32, s16, s8]
    matrix = random.choice(matrices)
    inner_list = random.choice(matrix)
    inner_list.append(value)
    return matrix

c1 = ipc.IP_Calculator()

str(c1)
