def load_input():
    with open("input.in", "r") as f:
        data = [row.strip() for row in f.readlines()]
        data.pop(0)
    return ([int(string) for string in data[0].split()], [int(string) for string in data[1].split()])

def main():
    data = load_input()
    print(data)

    shows = data[0]
    patients = data[1]

    patients.sort()

    shows_sum = sum(shows)
    patient_sum = 0
    patient_counter = 0
    for patient in patients:
        patient_sum += patient

        if patient_sum > shows_sum:
            break
        patient_counter += 1
    print(patient_counter)
    with open("output.txt", "w") as f:
        f.write(str(patient_counter))

main()