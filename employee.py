class Employee:
    def __init__(self, eid, enm, eag, esal, erole):
        self.empId = eid
        self.empName = enm
        self.empAge = eag
        self.empSalary = esal
        self.empRole = erole

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)


emps = []


def dummy_emps():
    e1 = Employee(101, "Girish", 27, 100000, "SE")
    e2 = Employee(102, "Harish", 30, 90000, "SE")
    emps.append(e1)
    emps.append(e2)
    return emps
