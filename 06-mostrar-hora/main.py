import datetime
from time import sleep
from os import system

LIMIT = 50

index = 0

while index < LIMIT:
    system("cls")
    index += 1
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    sleep(1)
