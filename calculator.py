print('==================')
print('Area Calculator 📐')
print('==================')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

shape = int(input('Which shape:'))


if shape == 1: 
    h = int(input('Height :'))
    b = int(input('Base :'))
    area = (h*b)/2
    print('The area is', area)
elif shape == 2:
    l = int(input('Length :'))
    w = int(input('Width :'))
    area = l * w 
    print('The area is', area)
elif shape == 3: 
    s = int(input('Side :'))
    area = s ** 2
    print('The area is', area)
elif shape == 4:
    pi = 3.14
    r = int(input('Radius :'))
    area = pi * (r ** 2)
    print('The area is', area)
elif shape == 5:
    print('Quit')
else:
    print('Something is wrong!')


