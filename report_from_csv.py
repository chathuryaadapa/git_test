import csv

class Student
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

def read_students_from_csv(file_path):
    students = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name = row[0]
            scores = list(map(float, row[1:]))
            students.append(Student(name, scores))
    return students

def generate_report(students):
    report_lines = []
    report_lines.append("Student Name, Average Score")
    for student in students:
        avg_score = student.average_score()
        report_lines.append(f"{student.name}, {avg_score:.2f}")
    return report_lines

def save_report_to_file(report_lines, output_file):
    with open(output_file, mode='w') as file:
        for line in report_lines:
            file.write(line + '\n')

def main():
    input_file = 'students_scores.csv'
    output_file = 'students_report.csv'
    
    students = read_students_from_csv(input_file)
    report_lines = generate_report(students)
    save_report_to_file(report_lines, output_file)
    print("Report saved to" output_file)

if __name__ == "__main__":
main()

