class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0
    
    def ageBy(self, increment: int): #envelhecer
        if self.age >= 4:
            print (f"warning: {self.species} morreu")
            self.age = 4
            return
        self.age += increment
        if self.age>= 4:
            print(f"warning: {self.species} morreu")
            self.age = 4

    def makeSound(self) :
        if self.age == 0:
            return "---"
        elif self.age >= 4:
            return "RIP"
        else:
            return self.sound

    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"

def main():
    animal = Animal("","")
    while True:
            line: str = input()
            print("$" + line)
            args: list[str] = line.split(" ")  
            if args[0] == "end":
                break
            if args[0] == "init":
                if len(args) <3:
                    print("fail: uso incorreto -> init <species> <sound>")
                    continue
                species = args[1]
                sound = args[2]
                animal = Animal(species, sound)
            elif args[0] == "show":
                print(animal)
            elif args[0] == "grow":
                if len(args)<2:
                    print("fail: uso incorreto -> grow <increment>")
                    continue
                increment = int(args[1])
                animal.ageBy(increment)
            elif args[0] == "noise":
                print(animal.makeSound())
            else:
                print("fail: comando desconhecido")

main()