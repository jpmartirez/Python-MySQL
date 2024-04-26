import sys
import mysql.connector
import os


class Employee_management:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='0915',
            port='3306',
            database='dbemployee'
        )
        self.cursor = self.conn.cursor()
        self.main()


    def main(self):
        os.system('cls')

        print("====================================================")
        print("      EMPLOYEE MANAGEMENT INFORMATION SYSTEM        ")
        print("====================================================")


        while True:
            print("\n1. Add Employee")
            print("2. Search Employee")
            print("3. Show All Employee")
            print("4. Edit Employee")
            print("5. Delete Employee")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.search_emp()
            elif choice == '3':
                self.show_all()
            elif choice == '4':
                self.edit_employee()
            elif choice == '5':
                self.delete_employee()
            elif choice == '6':
                sys.exit()


    def add_employee(self):
        os.system('cls')
        print("==== ADD EMPLOYEE RECORD ====")
        try:
            while True:
                first = input("\nEnter First Name: ").title()
                middle = input("Enter Middle Name: ").title()
                last = input("Enter Last Name: ").title()
                age = int(input("Enter the Age: "))
                sex = int(input("Enter Sex [1. Male   2. Female]: "))
                address = input("Enter Address: ")
                email = input("Enter Email: ").lower()
                print("1. Finance")
                print("2. Marketing")
                print("3. Information Technology")
                print("4. Accounting")
                print("5. Production/Operation Department")
                dept = int(input("Enter Department: "))

                query = f'INSERT INTO employee (FirstName, MiddleName, LastName, Age, Sex_id, Address, Email, Department_id) VALUES ("{first}", "{middle}", "{last}", {age}, {sex}, "{address}", "{email}", {dept});'
                self.cursor.execute(query)
                self.conn.commit()
                os.system('cls')
                print('---Employee Save---')
                add_more = input("Do you want to add another employee [y/n]: ")

                if add_more == 'y':
                    self.add_employee()
                elif add_more == 'n':
                    break

        except mysql.connector.Error as err:
            print(err)
        else:
            self.cursor.close()
            self.conn.close()
            Employee_management()

    def search_emp(self):
        os.system('cls')
        print("==== SEARCH EMPLOYEE RECORD ====")

        try:
            while True:
                ids = input("\nEnter the Employee ID: ")
                query = f"""
    SELECT 
        e.FirstName,
        e.MiddleName,
        e.LastName,
        e.Age,
        s.sex AS Sex,
        e.Address,
        e.Email,
        d.departments AS Department
    FROM 
        employee e
    JOIN
        sex s ON e.Sex_id = s.sex_id
    JOIN
        department d ON e.Department_id = d.dept_id
    WHERE
        e.employee_id = {ids}"""

                self.cursor.execute(query)
                row = self.cursor.fetchone()

                if row is not None:
                    print(f'\nFirst Name: {row[0]}')
                    print(f'Middle Name: {row[1]}')
                    print(f'Last Name: {row[2]}')
                    print(f'Age: {row[3]}')
                    print(f'Sex: {row[4]}')
                    print(f'Address: {row[5]}')
                    print(f'Email: {row[6]}')
                    print(f'Department: {row[7]}')
                else:
                    print('\nEmployee Record Not Found.')

                search_more = input("\nDo you want to search another employee [y/n]: ")

                if search_more == 'y':
                    self.search_emp()
                elif search_more == 'n':
                    break

        except mysql.connector.Error as err:
            print(err)
        else:
            self.cursor.close()
            Employee_management()


    def show_all(self):
        os.system('cls')
        print("==== SHOW ALL EMPLOYEE RECORD ====")
        print()

        try:
            query = """
                SELECT 
                    e.FirstName,
                    e.MiddleName,
                    e.LastName,
                    e.Age,
                    s.sex AS Sex,
                    e.Address,
                    e.Email,
                    d.departments AS Department
                FROM 
                    employee e
                JOIN
                    sex s ON e.Sex_id = s.sex_id
                JOIN
                    department d ON e.Department_id = d.dept_id"""

            self.cursor.execute(query)
            row = self.cursor.fetchall()

            if row is not None:
                for rows in row:
                    print(f'\nFirst Name: {rows[0]}')
                    print(f'Middle Name: {rows[1]}')
                    print(f'Last Name: {rows[2]}')
                    print(f'Age: {rows[3]}')
                    print(f'Sex: {rows[4]}')
                    print(f'Address: {rows[5]}')
                    print(f'Email: {rows[6]}')
                    print(f'Department: {rows[7]}')
            else:
                print("Don't have any record.")

            input("\nPress any key to CONTINUE: ")

        except mysql.connector.Error as err:
            print(err)
        finally:
            self.cursor.close()
            Employee_management()


    def edit_employee(self):
        os.system('cls')
        print("==== EDIT EMPLOYEE RECORD ====")
        print()

        try:
            while True:
                employee_id = int(input("Enter Employee ID: "))

                self.cursor.execute(f'''select * from employee where employee_id = {employee_id}''')
                crs = self.cursor.fetchone()

                if crs is not None:

                    print("---------------------------------------------------")
                    print(f'ENTER THE NEW EMPLOYEE INFORMATION WITH THE ID OF {employee_id}')
                    print("---------------------------------------------------")
                    first = input("\nEnter First Name: ").title()
                    middle = input("Enter Middle Name: ").title()
                    last = input("Enter Last Name: ").title()
                    age = int(input("Enter the Age: "))
                    sex = int(input("Enter Sex [1. Male   2. Female]: "))
                    address = input("Enter Address: ")
                    email = input("Enter Email: ").lower()
                    print("1. Finance")
                    print("2. Marketing")
                    print("3. Information Technology")
                    print("4. Accounting")
                    print("5. Production/Operation Department")
                    dept = int(input("Enter Department: "))

                    self.cursor.execute(f''' update employee set FirstName = '{first}', 
                    MiddleName = '{middle}', 
                    LastName = '{last}', 
                    Age ={age}, 
                    Sex_id = {sex}, 
                    Address = '{address}', 
                    Email = '{email}', 
                    Department_id = {dept} 
                    Where employee_id = {employee_id};''')
                    self.conn.commit()
                    os.system('cls')
                    print()
                    print('CHANGES SAVE')
                    print()

                else:
                    print(f"No Employee Exists With an ID of {employee_id}")

                edit_more = input("\nDo you want to edit more [y/n]: ")

                if edit_more == 'y':
                    self.edit_employee()
                elif edit_more == 'n':
                    break

        except mysql.connector.Error as err:
            print(err)
        else:
            self.cursor.close()
            self.conn.close()
            Employee_management()

    def delete_employee(self):
        os.system('cls')
        print("==== DELETE EMPLOYEE RECORD ====")
        print()
        try:
            while True:
                e_id = int(input("Enter Employee ID: "))
                query = f'''Delete from employee Where employee_id = {e_id}'''
                self.cursor.execute(query)

                self.conn.commit()

                print("\nRECORD DELETED")

                delete_more = input("Do you want to delete more [y/n]: ")
                if delete_more == 'y':
                    self.delete_employee()
                elif delete_more == 'n':
                    break

        except mysql.connector.Error as err:
            print(err)
        else:
            self.cursor.close()
            self.conn.close()
            Employee_management()


if __name__ == '__main__':
    Employee_management()



