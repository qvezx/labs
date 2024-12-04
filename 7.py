employes = {}


class Employee:
  def __init__(self, name, idd):
    self.name = name
    self.idd = idd

  def get_info(self):
    return f"имя: {self.name}, идентификационный номер: {self.idd}"


class Manager(Employee):
  def __init__(self, name, idd, department = ''):
    super().__init__(name, idd)
    self.department = department

  def manage_project(self):
    return f"отдел: {self.department}"


class Technician(Employee):
  def __init__(self, name, idd, specialization = ''):
    super().__init__(name, idd)
    self.specialization = specialization

  def perform_maintenance(self):
    return f"специализация: {self.specialization}"


class TechManager(Manager, Technician):
  def __init__(self, idd, name, department, specialization):
    Manager.__init__(self, idd, name, department)
    Technician.__init__(self, idd, name, specialization)

  def manage_project(self):
    return super().manage_project()
  
  def perform_maintenance(self):
    return super().perform_maintenance()
  
  def add_employee(self, NameOfEmployee, AgeOfEmployee):
    self.NameOfEmployee = NameOfEmployee
    self.AgeOfEmployee = AgeOfEmployee
    employes.update({NameOfEmployee : AgeOfEmployee})

  def get_team_info(self):
    return f"сотрудники: {employes}"
  
b = Manager("njdjfs", "731784871", "fjsjk")
c = Technician("fndanjfajs", "1784781", "fndsjj")

a = TechManager("fjksfsjk", "2y81749", "fshdfhsdshfd", "sfdnjsjnjnsf")

a.add_employee("fsjdfkhsg", "21312")
a.add_employee("sjjsfj", "12")
a.add_employee("fjfsjfsj", "5")
a.add_employee("iewqiriqri", "88")

print(a.perform_maintenance())
print(a.manage_project())
print(b.manage_project())
print(c.perform_maintenance())


print(a.get_team_info())
