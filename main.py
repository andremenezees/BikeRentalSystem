import datetime


class RentalSystem:
    def __init__(self, invetory=0):
        # Invertario representa a quantidade de bicicletas disponiveis.
        self.inventory = invetory

    def printInvetory(self):
        """Método que tem a função de mostrar as bicicletas disponiveis em stock e retorna o valor"""
        print(f"Estão disponíveis {self.invetory} bicicletas para aluguel.")
        return self.inventory

    def rentBikeOneHour(self, n):
        """Método responsável por alugar a bike por uma hora a um cliente. """

        # Laço para numero de bicicletas soclitadas para aluguel inválido.
        if n <= 0:
            print('Número de bicicletas invalido, o número deve ser positivo.')
            return none

        # Laço para número de bicicletas solicitas para aluguel maior que número de bicicletas disponíveis.
        elif n > self.inventory:
            print(f"Não possível alugar está quantidade pois tem-se apenas {self.inventory} bicicletas no estoque")
            return none

        # Alugando as bicicletas
        else:
            now = datetime.datetime.now()
            print(f"Foram alugadas {n} bicicletas por uma hora as {now.hour} horas do dia {now.day} ")
            print('Cada bicicleta é alugado por 5 dolars a hora.')

            self.inventory = self.inventory - n

    #Modificar
    def rentBikeOneDaily(self, n):
        """Método responsável por alugar a bike por uma hora a um cliente. """

        # Laço para numero de bicicletas soclitadas para aluguel inválido.
        if n <= 0:
            print('Número de bicicletas invalido, o número deve ser positivo.')
            return none

        # Laço para número de bicicletas solicitas para aluguel maior que número de bicicletas disponíveis.
        elif n > self.inventory:
            print(f"Não possível alugar está quantidade pois tem-se apenas {self.inventory} bicicletas no estoque")
            return none

        # Alugando as bicicletas
        else:
            now = datetime.datetime.now()
            print(f"Foram alugadas {n} bicicletas por uma hora as {now.hour} horas do dia {now.day} ")
            print('Cada bicicleta é alugado por 5 dolars a hora.')

            self.inventory = self.inventory - n

    #Modificar
    def rentBikeOneWeak(self, n):
        """Método responsável por alugar a bike por uma hora a um cliente. """

        # Laço para numero de bicicletas soclitadas para aluguel inválido.
        if n <= 0:
            print('Número de bicicletas invalido, o número deve ser positivo.')
            return none

        # Laço para número de bicicletas solicitas para aluguel maior que número de bicicletas disponíveis.
        elif n > self.inventory:
            print(f"Não possível alugar está quantidade pois tem-se apenas {self.inventory} bicicletas no estoque")
            return none

        # Alugando as bicicletas
        else:
            now = datetime.datetime.now()
            print(f"Foram alugadas {n} bicicletas por uma hora as {now.hour} horas do dia {now.day} ")
            print('Cada bicicleta é alugado por 5 dolars a hora.')

            self.inventory = self.inventory - n

    def returnBikes(self, request):
        """
        Parametro request:
        rentalTime = Hora em que as bicicletas foram alugadas.
        rentalBasis = É utilizado para fazer o calculo do pagamento
            (1 para alugueis de uma hora, 2 para alugueis de 1 dia, 3 para alugies de um mes).
        numOfBikes = Numero de bicicletas alugadas nesta hora.

        """

        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        #Se os 3 valores forem True(diferente de 0)
        if rentalTime and rentalBasis and numOfBikes:
            self.inventory = self.inventory + numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            #Calculo para alugueis de uma hora
            if rentalBasis == 1:
            #Transformou o tempo em horas para calcular o preço.
                bill = float(rentalPeriod.seconds / 3600) * 5 * numOfBikes


             #calculo para alugueis de um dia
            elif rentalBasis == 2:
                bill = float(rentalPeriod.days) * 20 * numOfBikes

            #calculo para alugueis de uma semaa
            elif rentalBasis == 3:
                bill = float(rentalPeriod.days / 7) * 60 * numOfBikes

            #Desconto familia
            if 3 <= numOfBikes >= 5:
                print('Será aplicado o desconto de família (30% de desconto)')
                bill = bill * 0.7

            print('Sua bicicleta foi devolvida.')

        else:
            print('Não foi possivel devolver a sua bicicleta, tente novamente.')



