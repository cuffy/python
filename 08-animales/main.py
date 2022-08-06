import dog
import duck

duck = duck.Duck("male")

dog = dog.Dog("female")

print(duck.animal, dog.animal)
print(duck.be(), dog.be())
print(duck.speak(), dog.speak())
print(duck.do(), dog.do())
print(duck.gender, dog.gender)
