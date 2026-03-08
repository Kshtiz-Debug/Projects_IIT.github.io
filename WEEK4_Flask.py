import csv

from flask import Flask
from flask import request
from flask import render_template
import pandas as pd
import matplotlib.pyplot as plt

app=Flask(__name__)
@app.route("/", methods=["GET", "POST"])


def Assignment():
    flag=0
    if request.method=="GET":
        return render_template("index.html")
    else:
        id=request.form.get("ID")
        id_v=request.form.get("id_value")
        file = open("data (1).csv")

        reader = csv.DictReader(file, skipinitialspace=True)
        if id=="student_id":
            flag=1
            student_list = []
            total_marks = 0
            for row in reader:
                if row["Student id"]==id_v:
                    student_list.append(row)
                    total_marks=total_marks+int(row["Marks"])
            if flag!=1:
                return render_template("error.html")
            return render_template("student.html",students=student_list,total=total_marks)
        elif id=="course_id":
            marks_list=[]
            avg_marks=0
            max_marks=0
            count=0
            for row in reader:
                if row["Course id"]==id_v:
                    avg_marks=avg_marks+int(row["Marks"])
                    marks_list.append(int(row["Marks"]))
                    count=count+1

                    if max_marks<int(row["Marks"]):
                        max_marks=int(row["Marks"])

            if count!=0:
                avg_marks=avg_marks//count
            else:
                return render_template("error.html")
            return render_template("course.html",avg=avg_marks,max=max_marks)




if __name__=='__main__':
    app.debug=True
    app.run()