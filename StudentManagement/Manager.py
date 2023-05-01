from Class import Class
from Student import Student
from Tool import *

class Manager:
   
   def __init__(self, class_list=[]):
      self.class_list = class_list
   
   
   # 1: Tạo lớp sinh viên
   def create_class(self):
      class_name = input("Nhập tên lớp cần tạo: ")
      cl = classNameExists(class_name, self.class_list)
      if cl == -1:
         class_x = Class(class_name)
         self.class_list.append(class_x)
         print(f"Thêm thành công lớp {class_name}!")
      else: 
         print(f"Lớp {class_name} đã tồn tại")
      
   # 2: Xóa một lớp
   def delete_class(self):
      class_name = input("Nhập tên lớp cần xóa: ")
      cl = classNameExists(class_name, self.class_list)
      if cl != -1:
         self.class_list.remove(cl)
         print(f"Xóa thành công lớp {class_name}!")
      else:
         print("Không tìm thấy lớp cần xóa!")
      
   # 3: Hiển thị một lớp   
   def display_class(self):
      print("\nDanh sách các lớp: ")
      table_format = "| {:<5} | {:<20} | {:<10} |"
      separator_format = "+{:=<6}+{:=<22}+{:=<12}+"

      # In đầu bảng
      print(separator_format.format('', '', ''))
      print(table_format.format('ID', 'Name', 'Amount'))
      print(separator_format.format('', '', '', '', ''))

      # In thông tin sinh viên
      for cl in self.class_list:
         print(table_format.format(str(cl.getId()), cl.getName(), str(len(cl.getStudentList()))))

      # In cuối bảng
      print(separator_format.format('', '', '', '', ''))
   
   # 4: Thêm sinh viên vào một lớp
   def add_student(self):
      while(True):
         class_id = int(input("Nhập mã lớp cần thêm sinh viên: "))
         cl = classIdExists(class_id, self.class_list)   
         if cl == -1:
            print(f"Mã lớp {class_id} bạn nhập không tồn tại!")
         else:
            break    
      student_name = input("Nhập tên sinh viên: ")
      st = studentNameExists(student_name, cl.getStudentList())
      if st == -1:
         student_x = Student(student_name)
         cl.getStudentList().append(student_x)
         print(f"Thêm sinh viên {student_name} vào lớp {cl.getName()} có mã lớp {cl.getId()} thành công !")
      else:
         print(f"Sinh viên {student_name} đã có tên trong lớp này!")
         
   # 5: Xóa sinh viên trong một lớp
   def delete_student(self):
      while(True):
         class_id = int(input("Nhập mã lớp cần xóa sinh viên: "))
         cl = classIdExists(class_id, self.class_list)   
         if cl == -1:
            print(f"Mã lớp {class_id} bạn nhập không tồn tại!")
         else:
            break    
      student_name = input("Nhập tên sinh viên: ")
      st = studentNameExists(student_name, cl.getStudentList())
      if st == -1:
         print(f"Sinh viên {student_name} không tồn tại trong lớp này")
      else:
         cl.getStudentList().remove(st)
         print(f"Sinh viên {student_name} được xóa thành công khỏi lớp {cl.getName()}")

   
   # 6: Tìm kiếm theo tên sinh viên
   def find_student(self):
      student_name = input("Nhập tên sinh viên cần tìm: ")
      
      print("\nSinh viên tìm được: ")
      table_format = "| {:<5} | {:<20} | {:<10} |"
      separator_format = "+{:=<6}+{:=<22}+{:=<12}+"

      # In đầu bảng
      print(separator_format.format('', '', ''))
      print(table_format.format('ID', 'Name', 'Class_ID'))
      print(separator_format.format('', '', ''))

      # In thông tin sinh viên
      for cl in self.class_list:
         st = studentNameExists(student_name, cl.getStudentList())
         if st != -1:
            print(table_format.format(st.getId(), st.getName(), cl.getId()))

      
      # In cuối bảng
      print(separator_format.format('', '', '', '', ''))
         
   # 7: Hiển thị sinh viên trong một lớp      
   def display_student(self):
      while(True):
         class_id = int(input("Nhập mã lớp cần xem: "))
         cl = classIdExists(class_id, self.class_list)   
         if cl == -1:
            print(f"Mã lớp {class_id} bạn nhập không tồn tại!")
         else:
            break
         
      print(f"\nDanh sác sinh viên trong lớp {cl.getName()}: ")
      table_format = "| {:<5} | {:<20} |"
      separator_format = "+{:=<6}+{:=<22}+"

      # In đầu bảng
      print(separator_format.format('', ''))
      print(table_format.format('ID', 'Name'))
      print(separator_format.format('', ''))

      # In thông tin sinh viên
      for st in cl.getStudentList():
         print(table_format.format(str(st.getId()), st.getName()))

      # In cuối bảng
      print(separator_format.format('', ''))

