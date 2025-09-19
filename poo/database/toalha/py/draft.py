class Towel:
    def __init__(self): #construtor
        self.color: str = "" #atributo
        self.size: str = ""
        self.wetness: int = 0
    def __str__(self):
            return f"{self.color}, {self.size}, {self.wetness}"

print("Qual a sua toalha?")
color = input()
towel: Towel = Towel(color, "P")
print (f"Sua toalha é {towel.color}")