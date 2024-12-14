class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")

employees = []
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    position = input("Enter position: ")
    employee = Employee(name, age, position)
    employees.append(employee)

def display_all_employees():
    for employee in employees:
        employee.display_info()

while True:
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_employee()
    elif choice == 2:
        display_all_employees()
    elif choice == 3:
        break
