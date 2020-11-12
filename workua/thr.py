


# class Connection:
#     def request(self):
#         print('REQUEST')
#
#     def open(self):
#         print('OPEN')
#
#     def close(self):
#         print('CLOSE')
#
#     def __enter__(self):
#         self.open()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.close()
#
# with Connection() as c:
#     c.request()

# class Student:
#     def __init__(self, first_name, age):
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         pass
#
# st = Student('Dima', 28)
# st.__dict__['last_name'] = 'Kaminskyi'
# print(st.__dict__)
# print(st.last_name)


class Int(int):
    pass

a = Int(5)
print(a.__dict__)
