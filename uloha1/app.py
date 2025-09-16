from string import ascii_lowercase
alphabet = list(ascii_lowercase)

def load_input_file():
    with open("input.in", "r") as f:
        input_list = [line.strip() for line in f]
        input_list.pop(0)
    return input_list

def find_index_new(letter):
    global alphabet
    current_index = alphabet.index(letter)
    return current_index -1

def rewrite_row(row):
    global alphabet
    rewritten_row = ""
    for letter in row:
        new_letter = alphabet[find_index_new(letter)]
        rewritten_row += new_letter
    return rewritten_row

def main():
    input_clean = load_input_file()
    with open("output.txt", "w") as f:
        for row in input_clean:
            rewritten_row = rewrite_row(row)
            if "poklad" in rewritten_row:
                f.write("ANO\n")
                print("ANO")
            else:
                f.write("NE\n")
                print("NE")

main()