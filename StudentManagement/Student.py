class Student:
   
   student_id = 20230000
   
   def __init__(self, name):
      self.id = Student.student_id;
      self.name = name;
      Student.student_id += 1
   
   def getId(self):
      return self.id
   
   def getName(self):
      return self.name
   
   
   