import os, copy
from time import sleep
from itertools import chain

def load_input():
    with open("input.in", "r") as f:
        data = f.readlines()
        data = data[2:]
        data = [item.strip() for item in data]
    return (int(data[0]), [[j for j in i] for i in data[1:]])

def convert_arena_to_num():
    global arena
    arena_num = copy.deepcopy(arena)
    row_i = 0
    for row in arena_num:
        point_i = 0
        for point in row:
            if point in "AV<>":
                arena_num[row_i][point_i] = 1

            point_i += 1
        row_i += 1
    return arena_num

def display_arena(arena):
    os.system("clear")
    for row in arena:
        row = [str(i) for i in row]
        print(" ".join(row))

def main():
    global arena, arena_num, time
    arena_num_temp = copy.deepcopy(arena_num)
    for i in range(time):
        row_i = 0
        for row in arena:
            point_i = 0
            for point in row:
                if type(arena_num_temp[row_i][point_i]) == int:
                    row_i_new = row_i
                    point_i_new = point_i
                    point_new = ""
                    match point:
                        case "A":
                            row_i_new -= 1
                            point_new = "<"
                        case "V":
                            row_i_new += 1
                            point_new = ">"
                        case "<":
                            point_i_new -= 1
                            point_new = "V"
                        case ">":
                            point_i_new += 1
                            point_new = "A"
                    
                    is_out_of_arena = row_i_new < 0 or row_i_new > len(arena) - 1 or point_i_new < 0 or point_i_new > len(arena[0]) - 1
                    is_wall = None
                    if not is_out_of_arena:
                        is_wall = arena[row_i_new][point_i_new] == "#"




                    if is_out_of_arena or is_wall:
                        arena[row_i][point_i] = point_new
                    elif arena[row_i_new][point_i_new] == ".":
                        arena[row_i_new][point_i_new] = point
                        

                        arena_num[row_i_new][point_i_new] = arena_num[row_i][point_i]

                        arena[row_i][point_i] = "."
                        arena_num[row_i][point_i] = "."
                    else:
                        arena[row_i_new][point_i_new] = "A"
                        arena_num[row_i_new][point_i_new] += arena_num[row_i][point_i]

                        arena[row_i][point_i] = "."
                        arena_num[row_i][point_i] = "."

                point_i += 1

            row_i += 1

        arena_num_temp = copy.deepcopy(arena_num)

def count_result():
    result_nested = [[x for x in y if type(x) == int] for y in arena_num]
    result = list(chain.from_iterable(result_nested))
    result.sort()
    result_str = [str(i) for i in result]
    return " ".join(result_str)

input_loaded = load_input()
time = input_loaded[0]
arena = input_loaded[1]
arena_num = convert_arena_to_num()

main()

with open("output.txt", "w") as f:
    f.write(count_result())

