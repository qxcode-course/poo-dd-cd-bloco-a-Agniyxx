class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0
    
    def ageBy(self, increment: int): #envelhecer
        self.age += increment
        if self.age >= 4:
            print (f"warning: {self.species} morreu")

    def makeSound(self) :
        if self.sound == "0":
            return ("---")
        if self.sound == "1":
            return self.sound 
        if self.sound == "2":
            return self.sound 
        if self.sound == "3":
            return self.sound
        if self.sound == "4":
            return "RIP"

    def __str__(self) -> str:
        return f"Species:{self.species}, Age:{self.age}, Sound:{self.makeSound()}"

def main():
    animal = Animal("","")
    while True:
        try:
            line: str = input()
        except EOFError:
            break
        args: list[str] = line.split(" ")  
        if args[0] == "$end":
            break
        if args[0] == "$init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        if args[0] == "$show":
            print(animal)
        elif args[0] == "$grow":
            increment = int(args[1])
            animal.ageBy(increment)
        else:
            print("fail: comando desconhecido")

main()