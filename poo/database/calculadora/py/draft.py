class Calculadora:
    def __init__(self, batteryMax: int= 100):
        self.display: float = 0.0
        self.battery: int = 0
        self.batteryMax = batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def show(self):
        print(self)
    
    def recarregar(self, increment: int):
        self.battery += increment
        if self.battery >= self.batteryMax:
         print("fail: limite de carga atingido")
        else:
             self.battery = self.batteryMax

    def soma(self, a: float, b: float):
        if self.battery > 0:
            self.display = a + b
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")
    
    def divisão(self, num: int, den: int):
        if den == 0:
            print("fail: divisao por zero")
        elif self.battery > 0:
            self.display = num/den
            self.battery -= 1
        else:
            print("fail: bateria insuficiente")
    
def main():
    cal = Calculadora()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] line.split(" ")
        if args[0] == "end":
            break
        elif intargs[0] == "init":
            display = args[1]
            battery = int(args[2])
            cal = Calculadora(display, battery)
        elif args[0] == "sum":
            a = int(args[1])
            b = int(args[2])
            print(cal.soma(a, b))
        elif args[0] == "charge":
            increment = int(args[1])
            cal.recarregar(increment)
        elif args[0] == "show":
            print(cal)
        else:
            print(f"fail: comando invalido")
