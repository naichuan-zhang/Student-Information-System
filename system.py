# -*- coding:utf-8 -*-

import re
import sys

from os import path

filename = "students.txt"

def main():
    running = True
    while running:
        # show system menu
        menu()
        string = input("Please pick a number: ")
        option_str = re.sub("[^0-9]", "", string)      # replace all the non-digits to empty, only remains number
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option = int(option_str)

            if option == 0:
                print("You have quit the system successfully :)")
                running = False     # quit system

            elif option == 1:
                insert()            # insert student info

            elif option == 2:
                search()            # search for student info

            elif option == 3:
                delete()            # delete student info

            elif option == 4:
                modify()            # modify student info

            elif option == 5:
                sort()              # sort sudent info

            elif option == 6:
                total()              # count total student number

            elif option == 7:
                show()              # show all student info


def menu():
    """
    print and show system menu
    """
    print("""
    -------------------------- Student Information System --------------------------
    |                                                                              |
    |  Welcome to the system!                                                      |
    | =================================== Menu =================================== |
    |                                                                              |
    |   1. Insert a student record                                                 |
    |   2. Search a student record                                                 |
    |   3. Delete a student record                                                 |
    |   4. Modify a student record                                                 |
    |   5. Sort                                                                    |
    |   6. Count student number of the system                                      |
    |   7. Show all students record                                                |
    |   0. Exit the System                                                         |
    |                                                                              |
    --------------------------------------------------------------------------------
    """)


def insert():
    # store student info as a list
    student_list = []
    # if wanna add more
    inserting = True
    while inserting:
        student_id = input("Please enter student ID (i.e. 1001): ")
        # if student id is null or doesn't match, then re-try
        if (not student_id) or (re.match("[0-9]+$", student_id) is None):
            break

        student_name = input("Please enter student name: ")
        if not student_name:
            break

        student_english_score = input("Please enter student English test score: ")
        if (not student_english_score) or (re.match("^(?:100|[1-9]?[0-9])$", student_english_score) is None):
            break

        student_python_score = input("Please enter student Python test score: ")
        if (not student_python_score) or (re.match("^(?:100|[1-9]?[0-9])$", student_python_score) is None):
            break

        # save student data
        student = dict(id=student_id, name=student_name,
                       english=student_english_score, python=student_python_score)
        student_list.append(student)

        add_more = input("Do you want to continue to add more? (y/N)")
        if add_more.lower() == 'y':
            inserting = True
        else:
            inserting = False

        # save student insert data into .txt file
        save(student_list)


def search():
    pass


def delete():
    deleting = True
    while deleting:
        student_id = input("Please enter the student ID you want to delete: ")
        if student_id is not "":
            if path.exists(filename):
                with open(filename, 'r') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []

            ifDel = False
            if student_old:
                with open(filename, 'w') as wfile:
                    d = {}
                    for list in student_old:
                        d = dict(eval(list))
                        if d['id'] == student_id:
                            ifDel = True
                    if ifDel:
                        print("The student with id %s has been deleted" % student_id)
                    else:
                        print("ERROR: student record not found!")
            else:
                print("No any student record exists yet ...")
                break

            mark = input("Continue to delete? (y/N) ")
            if mark.lower() == 'y':
                deleting = True
            else:
                deleting = False


def modify():
    pass


def sort():
    pass


def total():
    pass


def show():
    pass


def save(student_list):
    try:
        file = open(filename, "a")      # append
    except FileNotFoundError as ex:
        file = open(filename, "w")      # if doesn't exit, create new file and open

    for student in student_list:
        file.write(str(student) + "\n")

    file.close()


if __name__ == '__main__':
    main()
