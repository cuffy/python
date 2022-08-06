from animal import Animal


class Dog(Animal):
    def __init__(self, gender):
        super(Dog, self).__init__("Dog", gender)

    def do(self):
        return "I'm walking..."

    def speak(self):
        return "Guau!"
