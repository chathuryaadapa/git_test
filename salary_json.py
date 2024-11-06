import os
import json
import csv

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'position': self.position,
            'salary': self.salary
        }

def read_employees_from_csv(file_path):
    employees = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                employee = Employee(
                    employee_id=row['employee_id'],
                    name=row['name'],
                    position=row['position'],
                    salary=float(row['salary'])
                )
                employees.append(employee)
            except ValueError as e:
                print(f"Skipping row due to error: {e} in {row}")
    return employees

def save_employees_to_json(employees, output_file):
    with open(output_file, 'w') as file:
        json.dump([employee.to_dict() for employee in employees], file, indent=4)

def main():
    input_file = 'employees.csv'
    output_file = 'employees.json'

    try:
        employees = read_employees_from_csv(input_file)
        for employee in employees:
            employee.give_raise(5000)  # Give each employee a raise
        save_employees_to_json(employees, output_file)
        print(f"Employee data has been saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
  
