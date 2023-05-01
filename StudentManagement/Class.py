class Class:
   
   class_id = 1000
   
   def __init__(self, name, student_list = []):
      self.id = Class.class_id
      self.name = name
      self.student_list = student_list
      Class.class_id += 1
   
   def getId(self):
      return self.id
   
   def getName(self):
      return self.name
   
   def getStudentList(self):
      return self.student_list
   
   def setName(self, name):
      self.name = name
   
   def addStudent(self, student):
      self.student_list.append(student)
   
   def deleteStudent(self, student):
      self.student_list.remove(student)