# # group = ['uds', 2, 2, 0, 'eur', 3, 4, 0]
# # n = 4
# #
# # res = [group[i:i + n] for i in range(0, len(group), n)]
# # print(res)
#
# from time import sleep
#
# CACHE = {}
#
#
# def foo(a, b, c):
#     key = f'{__name__}:foo:{a}_{b}_{c}'
#     print(key)
#     if key in CACHE:
#         return CACHE[key]
#     else:
#         result = a + b + c
#         sleep(result)
#         CACHE[key] = result
#         return result
#
# def bar(a, b, c):
#     key = f'{__name__}:bar:{a}_{b}_{c}'
#     print(key)
#     if key in CACHE:
#         return CACHE[key]
#     else:
#         result = a * b * c
#         sleep(result)
#         CACHE[key] = result
#         return result
#
#
# print(foo(4, 2, 2))
# print(bar(4, 2, 2))

# class Discount:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __getattr__(self, item: str):
#         print('__getattr__')
#         print(item)
#         if item.startswith('greater_than_'):
#             amount = int(item.split('_')[-1])
#             return self.amount > amount
#         raise AttributeError
#
#
# d1 = Discount(20)
# d2 = Discount(52)
#
# print(d1.greater_than_49)
# print(d2.greater_than_32)

# class Discount:
#     def __init__(self, amount):
#         self.__amount = amount
#
#     # def get_amount(self):
#     #     return self.__amount
#     #
#     # def set_amount(self, value):
#     #     if isinstance(value, int):
#     #         self.__amount = value
#     #     else:
#     #         raise ValueError(str(value))
#
#     @property
#     def amount(self):
#         print('getter')
#         return self.__amount
#
#     @amount.setter
#     def amount(self, value):
#         print('setter')
#         self.__amount = value
#
#     def get_discount(self):
#         return 0.5 * self.__amount
#
# d1 = Discount(20)
# print(d1.amount)
# d1.amount = 50

# print(d1.get_amount())
# d1.set_amount('not integer')
# d1.set_amount(50)
# print(d1.get_discount())


# class Price:
#     def __init__(self, amount):
#         self.__amount = amount
#
# class Discount:
#     def __init__(self, amount):
#         self.__amount = Price(amount)
#
# d1 = Discount(20)


value = 'Dima'
SECRET_KEY = 3
print(value)

def get_session_key(val):
    return ''.join(chr(ord(char) + SECRET_KEY) for char in val)

def decode_session_key(val):
    return ''.join(chr(ord(char) - SECRET_KEY) for char in val)

session_key = get_session_key(value)
print(session_key)
original_value = decode_session_key(session_key)
print(original_value)




