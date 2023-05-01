from Manager import Manager

x = Manager()

print("--------------------------------------------------------------")
print("Xin chào mừng bạn đến với chương trình của tôi: ")

while(True):
   
   print("\n\nDanh sách chức năng:")
   print("1. Tạo lớp học")
   print("2. Xóa lớp học")
   print("3. Hiển thị thông tin các lớp")
   print("4. Thêm sinh viên vào lớp học")
   print("5. Xóa sinh viên trong một lớp")
   print("6. Tìm kiếm theo tên sinh viên")
   print("7. Hiển thị sinh viên trong một lớp")
   print("8. Thoát chương trình")
   try:
      option = int(input("\nVui lòng chọn chức năng: "))
      if option == 1:
         x.create_class()
      if option == 2:
         x.delete_class()
      if option == 3:
         x.display_class()
      if option == 4:
         x.add_student()
      if option == 5:
         x.delete_student()
      if option == 6:
         x.find_student()
      if option == 7:
         x.display_student()
      if option == 8:
         print("Cảm ơn vì đã sử dụng chương trình của chúng tôi!")
         break
      if option < 1 or option > 8:
         print("Giá trị bạn nhập vào không hợp lệ!")
   except ValueError:
      print("Lỗi! Giá trị bạn nhập vào không hợp lệ")