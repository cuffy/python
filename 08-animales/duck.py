from animal import Animal


class Duck(Animal):
    def __init__(self, gender):
        self.gender = gender
        super(Duck, self).__init__("Duck", gender)

    def do(self):
        return "I'm flying..."

    def speak(self):
        return "cuak!"
