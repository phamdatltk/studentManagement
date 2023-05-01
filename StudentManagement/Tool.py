def classNameExists(name, class_list):
   for cl in class_list:
      if cl.getName() == name:
         return cl
   return -1

def classIdExists(id, class_list):
   for cl in class_list:
      if cl.getId() == id:
         return cl
   return -1

def studentIdExists(id, student_list):
   for st in student_list:
      if st.getId() == id:
         return st
   return -1

def studentNameExists(name, student_list):
   for st in student_list:
      if st.getName() == name:
         return st
   return -1