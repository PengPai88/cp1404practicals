def load_subject_data():
    subject_data = []
    with open("subject_data.txt", 'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subject_data.append(parts)
    return subject_data

def display_subject_details(subject_data):
    for subject in subject_data:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")

def main():
    subject_data = load_subject_data()
    display_subject_details(subject_data)

if __name__ == "__main__":
    main()