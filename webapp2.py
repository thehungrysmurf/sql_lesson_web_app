from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    row2 = hackbright_app.get_student_grades(student_github)

    html = render_template("student_info.html", first_name = row[0], 
        last_name = row[1], github = row[2], projects = row2)
    return html

@app.route("/projects")
def get_project_info():
    hackbright_app.connect_to_db()
    student_project = request.args.get("project_title")
    # student_github = request.args.get("github")
    row = hackbright_app.get_project_grade(student_project)
    html = render_template("student_projects.html", student = row, project_title = student_project)
    return html

@app.route("/add_new_student")
def add_new_student():
    return render_template("add_new_student.html")

@app.route("/create_student_record")
def create_student_record():
    hackbright_app.connect_to_db()
    student_first = request.args.get("first_name")
    student_last = request.args.get("last_name")
    student_github = request.args.get("student_github")
 
    hackbright_app.make_new_student(student_first, student_last, student_github)

    html = render_template("added_successfully.html")
    return html

@app.route("/add_new_project")
def add_new_project():
    return render_template("add_new_project.html")

@app.route("/create_project_record")
def create_project_record():
    hackbright_app.connect_to_db()
    project_title = request.args.get("title")
    project_description = request.args.get("description")
    project_maxgrade = request.args.get("max_grade")
 
    hackbright_app.make_new_project(project_title, project_description, project_maxgrade)

    html = render_template("added_successfully.html")
    return html

@app.route("/assign_student_grade")
def assign_student_grade():
    return render_template("assign_student_grade.html")

@app.route("/assign_grade")
def assign_grade():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    project = request.args.get("project_title")
    student_grade = request.args.get("grade")

    hackbright_app.assign_grade(student_github, project, student_grade)

    html = render_template("added_successfully.html")
    return html

if __name__ == "__main__":
    app.run(debug=True)