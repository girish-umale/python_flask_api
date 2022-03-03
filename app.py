from employee import Employee, dummy_emps
from configuration import app
from flask import request
import json

emps = dummy_emps()


@app.route('/')
@app.route('/api/v1/emp', methods=['GET'])
def get_emp_list():
    empjsonlist = []
    for emp in emps:
        empdict = emp.__dict__
        empjsonlist.append(empdict)
    return json.dumps(empjsonlist)


@app.route("/api/v1/add_emp", methods=['POST'])
def add_new_emps():
    req_json = request.get_json()
    emp = Employee(eid=req_json.get("emp_id"), enm=req_json.get("emp_name"), eag=req_json.get("emp_age"),
             esal=req_json.get("emp_salary"), erole=req_json.get("emp_role"))
    emps.append(emp)
    return json.dumps({"Success" : "Employee successfully added..!"})


if __name__ == '__main__':
    app.run(debug=True)
