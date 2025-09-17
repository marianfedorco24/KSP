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
    data = load_input()
    time = data[0]
    arena = data[1]
    
    

main()