"""
Program: employee_class.py
Author: Ihsanullah Anwary
Last date modified: 12/11/2020
This is program is an example employee management system which allows the user to choose one for option from the list of
the selection.This program allows the user to save, find and delete the employee's id, first name, last name, deportment, job tiltle
salary and date hired to a file named employee_data.txt as dictionary.
"""

import os.path
import pickle
from tkinter.ttk import Label

try:
    import Tkinter as tk
except:
    import tkinter as tk
""" try exception GUI"""

class Employee:
    """ class employee"""

    def __init__(self, first_name, last_name, ID_number, dept, job_title, Salary, Hired_date):  # constructor
        self.root = tk.Tk()
        self.quit = None
        self.__first_name = first_name
        self.__last_name = last_name
        self.__ID_number = ID_number
        self.__department = dept
        self.__job_title = job_title
        self.__salary = Salary
        self.__date = Hired_date
        # getters and setters

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    def set_department(self, dept):
        self.__department = dept

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def set_salary(self, Salary):
        self.__salary = Salary

    def set_date(self, Hired_date):
        self.__date = Hired_date

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_ID_number(self):
        return self.__ID_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def get_salary(self):
        return self.__salary

    def get_date(self):
        return self.__date


class Welcome():
    """ Class welcome"""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Welcome to employee management')
        self.root.geometry('500x50')
        self.label = tk.Label(self.root, text="Click OK to start the program")
        self.label.pack()
        button = tk.Button(self.root, text='OK', command=self.start)

        button.pack()
        self.root.mainloop()

    def start(self):
        self.root.destroy()


welcome = Welcome()


def add_employee():
    """Function add_employee"""

    global id_number, choice
    """global Variables"""
    if os.path.exists("employee_data.txt"):  # file name
        # If the file exist which contains a dictionary of employee records.
        f = open('employee_data.txt', 'rb')
        emp_dct = pickle.load(f)
        f.close()
    # if the file does not exist
    else:
        """ Creating employee and adding to dictionary"""
        first_employee = Employee('Moke', 'John', 1, 'Accounting',
                                  'Manager', '4000', '01-04-2019')
        # initializing dictionary
        emp_dct = {first_employee.get_ID_number(): first_employee.get_first_name() + ' '
                                                   + first_employee.get_last_name() + ' ' +
                                                   first_employee.get_department() + ' ' + first_employee.get_job_title() + ' ' + first_employee.get_salary() + ' ' + first_employee.get_date()}
    # using while loop to continue the program as per users' choice.

    choice_qiut = 'y'
    while choice_qiut.upper() == 'Y':
        # This gives choices to the user
        print('Enter any of the following choices: ')
        print('Add a new employee to the dictionary: enter 1')
        print('Find an employee in the dictionary by ID number: enter 2')
        print('Change an existing employee\'s first name,last name,department or job title: enter 3')
        print('Delete an employee from a dictionary: enter 4')
        print('Quit the program: enter 5')
        choice = input('Enter your choice: ')
        if int(choice) == 2:
            id_number = input('Enter the ID of the employee: ')

            if int(id_number) in emp_dct.keys():
                print(emp_dct[int(id_number)])
                # If id_number entered by the use does not exist.
            else:
                print('Employee id not found!')
        else:
            if int(choice) == 1:
                id_number = input('Enter ID of the employee: ')
                # If id_number entered by the use exists
                if int(id_number) in emp_dct.keys():
                    print('Employee already exist')
                    # If id_number entered by the use does not exist, then add
                else:
                    first_name_ = input('Enter first name of the employee: ')
                    last_name_ = input('Enter last name of the employee: ')
                    dept = input('Enter department of the employee: ')
                    job = input('Enter job title of the employee: ')
                    salary_ = input(' enter salary of employee: ')
                    date_ = input(' enter date hired employee: ')
                    name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
                    salary__characters = set("1234567890-")
                    if not (name_characters.issuperset(first_name_ ) and name_characters.issuperset(last_name_)):
                        raise ValueError
                    if salary_ and not salary__characters.issuperset(salary_):
                        raise ValueError

                    new_employee = Employee(first_name_, last_name_, int(id_number),
                                            dept, job, salary_, date_)
                    for id_number in range(100):
                        """ for loop allows user to add 100 employees"""
                        id_number = +1
                    emp_dct[
                        new_employee.get_ID_number()] = 'name:' + new_employee.get_first_name() + '' + new_employee.get_last_name() + '   ' + 'Departament:' + new_employee.get_department() + '  ' + 'Job:' + new_employee.get_job_title() + '  ' + 'Salary: $' + new_employee.get_salary() + '  ' + 'Date hired:' + new_employee.get_date()
                    print('Employee added to file')
            else:
                if int(choice) == 3:
                    """ User choice to modify the user information"""
                    id_number = input('Enter ID of the employee: ')
                    # If id_number entered by the use exists,then modify the record
                    if int(id_number) in emp_dct.keys():
                        first_name_ = input('Enter first name of the employee: ')
                        last_name_ = input('Enter last name of the employee: ')
                        dept = input('Enter department of the employee: ')
                        job = input('Enter job title of the employee: ')
                        salary_ = input(' enter salary of employee: ')
                        date_ = input(' enter date hired employee: ')
                        e4 = Employee(first_name_, last_name_, int(id_number),
                                      dept, job, salary_, date_)

                        emp_dct[
                            e4.get_ID_number()] = e4.get_first_name() + ' ' + e4.get_last_name() + ' ' + e4.get_department() + e4.get_job_title() + ' ' + e4.get_salary() + ' ' + e4.get_date()
                        print('Employee data modified!')
                    # If id_number entered by the use does not exist, not modified
                    else:
                        print('Employee not found!')

                else:
                    if int(choice) == 4:
                        id_number = input('Enter ID of the employee: ')
                # Using  pop() method to delete
                # It returns default message, if the item not found
                print('Deleted: ', emp_dct.pop(int(id_number), 'Employee not found!'))

                # ends the program
            if int(choice) != 5:
                print('Invalid Choice!')
            else:
                print('OK Bye!')
                break

        choice_qiut = input('Continue? enter y for yes: ')
        # Write the dictionary into the file
    f = open('employee_data.txt', 'wb')
    pickle.dump(emp_dct, f)
    f.close()


add_employee()
""""Calling the function"""
