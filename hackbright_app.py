import sqlite3
from parser import *

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row

def get_projects_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
Title: %s
Description: %s
Max Grade: %s""" % (row[0], row[1], row[2])

def get_project_grade(student_github, project_title):
    query = """SELECT first_name, last_name, project_title, grade FROM Grades INNER JOIN Students ON student_github = github WHERE student_github = ? AND project_title = ?"""
    DB.execute(query, (student_github, project_title))
    row = DB.fetchone()
    print """\
Student: %s %s
Project: %s
Grade: %s""" % (row[0], row[1], row[2], row[3])

def get_student_grades(student_github):
    query = """SELECT first_name, last_name, project_title, grade FROM Grades INNER JOIN Students ON student_github = github WHERE student_github = ?"""
    DB.execute(query, (student_github,))
    row = DB.fetchone()
    return row
    # while row:
    #     print """\
    #     Student: %s %s
    #     Project: %s
    #     Grade: %s""" % (row[0], row[1], row[2], row[3])
    #     row = DB.fetchone()

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values(?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects values(?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s" % (title)

def assign_grade(student_github, project_title, grade):
    query = """INSERT into Grades values(?, ?, ?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully added grade for %s." % (student_github)

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        parsed_input = parser(input_string)
        
        command = parsed_input[0]
        args = parsed_input[1][:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project": 
            get_projects_by_title(*args)
        elif command == "create_project":
            make_new_project(*args)
        elif command == "project_grade": 
            get_project_grade(*args)
        elif command == "assign_grade":
            assign_grade(*args)
        elif command == "get_grades": 
            get_student_grades(*args)

    CONN.close()

if __name__ == "__main__":
    main()
