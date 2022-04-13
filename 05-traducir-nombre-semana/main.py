
def get_translate_catalan(english_day):
    catalan = None
    dict_week = {"monday": "Dilluns",
                 "tuesday": "Dimarts",
                 "wednesday": "Dimecres",
                 "thursday": "Dijous",
                 "friday": "Divendres",
                 "saturday": "Dissabte",
                 "sunday": "Diumenge"}
    if english_day is not None:
        if english_day.lower() in dict_week:
            catalan = dict_week[english_day.lower()]
        else:
            raise TypeError
    return catalan

try:
    print(get_translate_catalan(None))
except TypeError:
    print("El texto no es un día de la semana.")

try:
    print(get_translate_catalan("monday"))
except TypeError:
    print("El texto no es un día de la semana.")

try:
    print(get_translate_catalan("Python"))
except TypeError:
    print("El texto no es un día de la semana.")

try:
    print(get_translate_catalan("Sunday"))
except TypeError:
    print("El texto no es un día de la semana.")
