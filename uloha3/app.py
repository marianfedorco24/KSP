import re, os

def load_input():
    with open("input.in", "r") as f:
        data = f.readlines()
        data = data[2:]
        data = [item.strip() for item in data]
    return (int(data[0]), [[j for j in i] for i in data[1:]])

def convert_arena_to_num(arena):
    arena_num = arena
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
    for i in range(time):
        row_i = 0
        for row in arena:
            point_i = 0
            for point in row:
                if type(arena_num[row_i][point_i]) == int:
                    row_i_new = row_i
                    point_i_new = point_i
                    match point:
                        case "A":
                            row_i_new -= 1
                        case "V":
                            row_i_new += 1
                        case "<":
                            point_i_new -= 1
                        case ">":
                            point_i_new += 1
                    
                    if row_i_new < 0 or row_i_new > len(arena - 1) or point_i_new < 0 or point_i_new > len(arena[0]):
                        pass

                point_i += 1

            row_i += 1


input_loaded = load_input()
time = input_loaded[0]
arena = input_loaded[1]
arena_num = convert_arena_to_num(arena)

display_arena(arena_num)
print(time)

print(type(arena_num[1][2]))

main()
