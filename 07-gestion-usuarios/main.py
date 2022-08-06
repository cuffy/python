import json

import uuid

from os import mkdir
from os.path import exists


def show_menu():
    print("=====[ MENU ]=====")
    print("   1. Crear")
    print("   2. Consultar")
    print("   3. Eliminar")
    print()
    print("   4. Salir")


def ask_info_user():
    name = input("Introduce el nombre: ")
    while True:
        try:
            age = int(input("Introduce la edad: "))
            break
        except:
            print("La edad no es correcta.")
    return {"id": uuid.uuid1().__str__(), "name": name, "age": age}


def save_row(user):
    if not exists("./data"):
        mkdir("./data")

    with open("data/user.list", "a") as f:
        f.write(json.dumps(user)+"\n")


def query_users():
    users = []
    with open("data/user.list") as f:
        for u in f.readlines():
            users.append(json.loads(u.replace("\n", "")))
    return users


def delete_user(id, users):
    for i in range(len(users)):
        u = users[i]
        if u["id"] == id:
            del users[i]
            break
    return users


def save_list(users):
    with open("data/user.list", "w") as f:
        for u in users:
            f.write(json.dumps(u)+"\n")
    return True





while True:
    show_menu()
    option = int(input("Que operación quieres realizar: "))
    if option == 1:
        user = ask_info_user()
        print(user)
        save_row(user)

    elif option == 2:
        print(query_users())

    elif option == 3:
        print(query_users())
        id_delete = input("Introduce el id a eliminar ")
        users = delete_user(id_delete, query_users())
        save_list(users)
    elif option == 4:
        break
