# group = ['uds', 2, 2, 0, 'eur', 3, 4, 0]
# n = 4
#
# res = [group[i:i + n] for i in range(0, len(group), n)]
# print(res)

from time import sleep

CACHE = {}


def foo(a, b, c):
    key = f'{__name__}:foo:{a}_{b}_{c}'
    print(key)
    if key in CACHE:
        return CACHE[key]
    else:
        result = a + b + c
        sleep(result)
        CACHE[key] = result
        return result

def bar(a, b, c):
    key = f'{__name__}:bar:{a}_{b}_{c}'
    print(key)
    if key in CACHE:
        return CACHE[key]
    else:
        result = a * b * c
        sleep(result)
        CACHE[key] = result
        return result


print(foo(4, 2, 2))
print(bar(4, 2, 2))
