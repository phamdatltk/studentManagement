
try:
    x = int(input("Nhập một số nguyên: "))
   #  result = 100 / x
   #  print("Kết quả là:", result)
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên.")
except ZeroDivisionError:
    print("Lỗi: Bạn không thể chia một số cho 0.")
except Exception as e:
    print("Lỗi không xác định:", str(e))
finally:
    print("Chương trình đã kết thúc.")