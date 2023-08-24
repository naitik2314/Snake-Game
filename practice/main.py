class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print(f"Animal with {self.num_eyes} eyes can breathe")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.species = "Fish"

    def breathe(self):
        super().breathe()
        print(f"{self.species} can breathe under water")

    def swim(self):
        print(f"{self.species} with {self.num_eyes} eyes can swim through the water")

nemo = Fish()
nemo.swim()
nemo.breathe()