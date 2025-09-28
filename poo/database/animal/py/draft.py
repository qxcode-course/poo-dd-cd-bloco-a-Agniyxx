class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0
    
    def ageBy(self, increment: int): #envelhecer
        self.age += increment
        if self.age >= 4:
            print("warning: {species} morreu")

    def makeSound(self) :
        if self.sound == "0":
            return ("")
        if self.sound == "1":
            return ("")
        if self.sound == "2":
            return ("")
        if self.sound == "3":
            return ("")
        if self.sound == "4":
            return "RIP"
        return 0

    def __str__(self) -> str:
        return f"Species:{self.species}, Age:{self.sound}, Sound:{self.age}"

def main():
    animal = Animal("","")
    while True:
        line: str = input()
        args: str = line.split(" ")
        
        if args[0] == "$end":
            break
        elif args[0] == "$new":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args[0] == "$show":
            print(animal)
main()