def add_and_compare(a, b, c):
    while a <= b:
          print(a, '<', b)
          a = a + c
    print(a, '>', b)


x = int(input('Input a:'))
y = int(input('Input b:'))
z = int(input('Input c:'))
add_and_compare(x, y, z)





