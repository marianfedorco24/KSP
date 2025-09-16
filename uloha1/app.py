from string import ascii_lowercase
alphabet = list(ascii_lowercase)


test = """5
tdipwbntftqplmbefnqpewpev
pqfsbdflvmpwzcmftlnvafabdju
ajusbcveftmvofdopnjtuznsblz
nbsjtftbibpeqsbizbaqplmbeop
abaobnfoboqplmftnpsbmlz"""

def clean_input(input):
    input_list = input.split("\n")
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

def main(input):
    input_clean = clean_input(input)
    for row in input_clean:
        rewritten_row = rewrite_row(row)
        if "poklad" in rewritten_row:
            print("ANO")
        else:
            print("NE")

main(test)