def es_bisiesto(year):
    es_bisiesto = False

    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        es_bisiesto = True
    elif year % 4 == 0 and year % 100 != 0:
        es_bisiesto = True
    return es_bisiesto


years = [1600, 1900, 2000, 2016, 1987, 2100]

for y in years:
    print(es_bisiesto(y))
