from math import ceil, floor, pi

def get_perimeter(r):
    return 2 * pi * r

def get_area(r):
    return pi * r**2

def get_volume(r):
    return 4/3 * pi * r**3

radius = [4, 22.3]

for i in radius:
    p = get_perimeter(i)
    a = get_area(i)
    v = get_volume(i)

    print("El perímetro es", p, round(p, 3))
    print("-- ceil="+str(ceil(p)), "floor="+str(floor(p)))
    print("El área es", a, round(a, 3))
    print("-- ceil="+str(ceil(a)), "floor="+str(floor(a)))
    print("El volumen es", v, round(v, 3))
    print("-- ceil="+str(ceil(v)), "floor="+str(floor(v)))
    print()
