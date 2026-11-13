
import sqlite3
import csv

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        department TEXT,
        salary REAL CHECK(salary > 0),
        join_date TEXT DEFAULT CURRENT_DATE,
        is_active INTEGER DEFAULT 1
    )
''')
conn.commit()


def add_employee(name, email, department, salary):
    if '@' not in email:
        print("Enter a valid email.")
        return

    if salary <= 0:
        print("Salary must be greater than 0.")
        return

    try:
        cursor.execute('''
            INSERT INTO employees(name,email,department,salary)
            VALUES (?,?,?,?)
        ''', (name,email,department,salary))

        conn.commit()
        print("Employee added.")

    except sqlite3.IntegrityError:
        print("Email already exists.")


def view_employees():
    cursor.execute('''
        SELECT * FROM employees
        WHERE is_active = 1
    ''')

    employees = cursor.fetchall()

    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(employee)


def get_employee(employee_id):
    cursor.execute('''
        SELECT * FROM employees
        WHERE id = ? AND is_active = 1
    ''', (employee_id,))

    employee = cursor.fetchone()

    if employee:
        print(employee)
    else:
        print("Not found.")


def search_employee(keyword):
    cursor.execute('''
        SELECT * FROM employees
        WHERE LOWER(name) LIKE LOWER(?) AND is_active = 1
    ''', ('%' + keyword + '%',))

    employees = cursor.fetchall()

    if not employees:
        print("No matching employees found.")
    else:
        for employee in employees:
            print(employee)


def filter_by_department(dept):
    cursor.execute('''
        SELECT * FROM employees
        WHERE department = ? AND is_active = 1
    ''', (dept,))

    employees = cursor.fetchall()

    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(employee)


def filter_by_salary(min_salary, max_salary):
    cursor.execute('''
        SELECT * FROM employees
        WHERE salary BETWEEN ? AND ? AND is_active = 1
    ''', (min_salary,max_salary))

    employees = cursor.fetchall()

    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(employee)


def sort_employees(column, order):
    columns = ['name', 'salary', 'join_date']
    orders = ['ASC', 'DESC']

    column = column.lower()
    order = order.upper()

    if column not in columns or order not in orders:
        print("Invalid sorting option.")
        return

    query = '''
        SELECT * FROM employees
        WHERE is_active = 1
        ORDER BY ''' + column + ' ' + order

    cursor.execute(query)

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


def update_salary(employee_id, salary):
    if salary <= 0:
        print("Salary must be greater than 0.")
        return

    cursor.execute('''
        UPDATE employees
        SET salary = ?
        WHERE id = ? AND is_active = 1
    ''', (salary,employee_id))

    conn.commit()

    if cursor.rowcount == 0:
        print("No employee found.")
    else:
        print("Salary updated.")


def update_department(employee_id, department):
    cursor.execute('''
        UPDATE employees
        SET department = ?
        WHERE id = ? AND is_active = 1
    ''', (department,employee_id))

    conn.commit()

    if cursor.rowcount == 0:
        print("No employee found.")
    else:
        print("Department updated.")


def give_raise(department, percent):
    cursor.execute('''
        UPDATE employees
        SET salary = salary + (salary * ? / 100)
        WHERE department = ? AND is_active = 1
    ''', (percent,department))

    conn.commit()

    print(cursor.rowcount, "employees updated.")


def remove_employee(employee_id):
    cursor.execute('''
        SELECT id FROM employees
        WHERE id = ? AND is_active = 1
    ''', (employee_id,))

    employee = cursor.fetchone()

    if employee is None:
        print("No employee found.")
        return

    confirm = input("Are you sure you want to remove? (y/n): ")

    if confirm.lower() == 'y':
        cursor.execute('''
            UPDATE employees
            SET is_active = 0
            WHERE id = ?
        ''', (employee_id,))

        conn.commit()
        print("Employee removed.")
    else:
        print("Removal cancelled.")


def restore_employee(employee_id):
    cursor.execute('''
        UPDATE employees
        SET is_active = 1
        WHERE id = ? AND is_active = 0
    ''', (employee_id,))

    conn.commit()

    if cursor.rowcount == 0:
        print("No employee found.")
    else:
        print("Employee restored.")


def view_removed():
    cursor.execute('''
        SELECT * FROM employees
        WHERE is_active = 0
    ''')

    employees = cursor.fetchall()

    if not employees:
        print("No removed employees.")
    else:
        for employee in employees:
            print(employee)


def show_summary():
    cursor.execute('''
        SELECT COUNT(*), AVG(salary), MAX(salary), MIN(salary)
        FROM employees
        WHERE is_active = 1
    ''')

    result = cursor.fetchone()

    print("Total active employees:", result[0])

    if result[0] > 0:
        print("Average salary:", round(result[1], 2))
        print("Highest salary:", result[2])
        print("Lowest salary:", result[3])

    cursor.execute('''
        SELECT department, COUNT(*), AVG(salary)
        FROM employees
        WHERE is_active = 1
        GROUP BY department
    ''')

    departments = cursor.fetchall()

    print("\nDepartment Summary:")

    for dept in departments:
        print(dept[0], dept[1], round(dept[2], 2))


def top_earners(n):
    cursor.execute('''
        SELECT * FROM employees
        WHERE is_active = 1
        ORDER BY salary DESC
        LIMIT ?
    ''', (n,))

    employees = cursor.fetchall()

    for employee in employees:
        print(employee)


def export_to_csv(filename):
    cursor.execute('''
        SELECT * FROM employees
        WHERE is_active = 1
    ''')

    employees = cursor.fetchall()

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([
            'ID', 'Name', 'Email', 'Department',
            'Salary', 'Join Date', 'Is Active'
        ])

        writer.writerows(employees)

    print("Employees exported successfully.")


while True:
    print('''
    1. Add employee
    2. View all
    3. Search
    4. Filter by department
    5. Filter by salary
    6. Sort
    7. Update salary
    8. Give raise
    9. Remove employee
    10. Restore employee
    11. Summary report
    12. Top earners
    13. Export to CSV
    14. Exit
    ''')

    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            add_employee(name,email,department,salary)

        elif choice == '2':
            view_employees()

        elif choice == '3':
            keyword = input("Enter name to search: ")
            search_employee(keyword)

        elif choice == '4':
            dept = input("Enter department: ")
            filter_by_department(dept)

        elif choice == '5':
            min_salary = float(input("Enter minimum salary: "))
            max_salary = float(input("Enter maximum salary: "))
            filter_by_salary(min_salary,max_salary)

        elif choice == '6':
            column = input("Sort by (name/salary/join_date): ")
            order = input("Order (ASC/DESC): ")
            sort_employees(column,order)

        elif choice == '7':
            employee_id = int(input("Enter employee ID: "))
            salary = float(input("Enter new salary: "))
            update_salary(employee_id,salary)

        elif choice == '8':
            department = input("Enter department: ")
            percent = float(input("Enter raise percentage: "))
            give_raise(department,percent)

        elif choice == '9':
            employee_id = int(input("Enter employee ID: "))
            remove_employee(employee_id)

        elif choice == '10':
            employee_id = int(input("Enter employee ID: "))
            restore_employee(employee_id)

        elif choice == '11':
            show_summary()

        elif choice == '12':
            n = int(input("Enter number of top earners: "))
            top_earners(n)

        elif choice == '13':
            filename = input("Enter filename: ")

            if not filename.endswith('.csv'):
                filename += '.csv'

            export_to_csv(filename)

        elif choice == '14':
            conn.close()
            print("Connection closed.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid values.")
