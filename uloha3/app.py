import re
def load_input():
    with open("input.in", "r") as f:
        data = f.readlines()
        data = data[2:]
        data = [item.strip() for item in data]
    return (int(data[0]), data[1:])

def convert_arena_to_num(arena):
    regex = r"A|V|<|>"
    return re.sub(regex, 1, arena)

def main():
    data = load_input()
    time = data[0]
    arena = data[1]
    arena_num = convert_arena_to_num(arena)
    print(arena_num)

main()