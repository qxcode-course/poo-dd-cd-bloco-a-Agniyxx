class Carro:
    def __init__ (self, gasMax: int = 100, passMax: int = 2):
        self.passageiros: int = 0
        self.quilometros: int = 0
        self.gas: int = 0
        self.passMax: int = passMax
        self.gasMax: int = gasMax

    def __str__(self) -> str:
        return f"pass: {self.passageiros}, gas: {self.gas}, km: {self.quilometros}"
    
    def show(self):
        print (self)

    def enter(self):
        if self.passageiros >= self.passMax:
            print("fail: limite de pessoas atingido")
        else:
             self.passageiros += 1
    
    def leave(self):
        if self.passageiros <= 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.passageiros -= 1

    def abastecer(self, qtd: int):
        self.gas += qtd
        if self.gas >= self.gasMax:
            self.gas = self.gasMax
        
    def drive(self, distancia: int):
        if self.passageiros == 0:
            print("fail: nao ha ninguem no carro")
            return
        if self.gas == 0:
            print("fail: tanque vazio")
            return
        if distancia > self.gas:
            kmPercorridos = self.gas
            self.quilometros += kmPercorridos
            self.gas = 0
            print(f"fail: tanque vazio apos andar {kmPercorridos} km")
        else:
            self.gas -= distancia
            self.quilometros += distancia

        
def main():
    carro = Carro()
    while True:
        line: (str) = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            carro.show()
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            qtd = int(args[1])
            carro.abastecer(qtd)
        elif args[0] == "drive":
            distance = int(args[1])
            carro.drive(distance)
        else:
            print("fail: comando desconhecido")

main()