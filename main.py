import datetime


class BikeRental:
    def __init__(self, inventory=0):
        # Invertario representa a quantidade de bicicletas disponiveis.
        self.inventory = inventory

    def displaystock(self):
        """Método que tem a função de mostrar as bicicletas disponiveis em stock e retorna o valor"""
        print(f"Estão disponíveis {self.inventory} bicicletas para aluguel.")
        return self.inventory

    def rentBikeOnHourlyBasis(self, n):
        """Método responsável por alugar a bike por uma hora a um cliente. """

        # Laço para numero de bicicletas soclitadas para aluguel inválido.
        if n <= 0:
            print('Número de bicicletas invalido, o número deve ser positivo.')
            return None

        # Laço para número de bicicletas solicitas para aluguel maior que número de bicicletas disponíveis.
        elif n > self.inventory:
            print(f"Não possível alugar está quantidade pois tem-se apenas {self.inventory} bicicletas no estoque")
            return None

        # Alugando as bicicletas
        else:
            now = datetime.datetime.now()
            print(f"Foram alugadas {n} bicicletas por uma hora as {now.hour} horas do dia {now.day} ")
            print('Cada bicicleta é alugado por 5 dolars a hora.')

            self.inventory = self.inventory - n
            return now

    def rentBikeOnDailyBasis(self, n):
        """Método responsável por alugar a bike po um dia a um cliente. """

        # Laço para numero de bicicletas soclitadas para aluguel inválido.
        if n <= 0:
            print('Número de bicicletas invalido, o número deve ser positivo.')
            return None

        # Laço para número de bicicletas solicitas para aluguel maior que número de bicicletas disponíveis.
        elif n > self.inventory:
            print(f"Não possível alugar está quantidade pois tem-se apenas {self.inventory} bicicletas no estoque")
            return None

        # Alugando as bicicletas
        else:
            now = datetime.datetime.now()
            print(f"Foram alugadas {n} bicicletas por um dia as {now.hour} horas do dia {now.day} ")
            print('Cada bicicleta é alugado por 20 dolars a hora.')

            self.inventory = self.inventory - n
            return now

    # Modificar
    def rentBikeOnWeeklyBasis(self, n):
        """Método responsável por alugar a bike por uma semana a um cliente. """

        # Laço para numero de bicicletas soclitadas para aluguel inválido.
        if n <= 0:
            print('Número de bicicletas invalido, o número deve ser positivo.')
            return None

        # Laço para número de bicicletas solicitas para aluguel maior que número de bicicletas disponíveis.
        elif n > self.inventory:
            print(f"Não possível alugar está quantidade pois tem-se apenas {self.inventory} bicicletas no estoque")
            return None

        # Alugando as bicicletas
        else:
            now = datetime.datetime.now()
            print(f"Foram alugadas {n} bicicletas por um dia as {now.hour} horas do dia {now.day} ")
            print('Cada bicicleta é alugado por 60 dolars a hora.')

            self.inventory = self.inventory - n
            return now

    def returnBike(self, request):
        """
        Parametro request:
        rentalTime = Hora em que as bicicletas foram alugadas.
        rentalBasis = É utilizado para fazer o calculo do pagamento
            (1 para alugueis de uma hora, 2 para alugueis de 1 dia, 3 para alugies de um mes).
        numOfBikes = Numero de bicicletas alugadas nesta hora.

        """

        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        # Se os 3 valores forem True(diferente de 0)
        if rentalTime and rentalBasis and numOfBikes:
            self.inventory = self.inventory + numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # Calculo para alugueis de uma hora
            if rentalBasis == 1:
                # Transformou o tempo em horas para calcular o preço.
                bill = float(rentalPeriod.seconds / 3600) * 5 * numOfBikes


            # calculo para alugueis de um dia
            elif rentalBasis == 2:
                bill = float(rentalPeriod.days) * 20 * numOfBikes

            # calculo para alugueis de uma semaa
            elif rentalBasis == 3:
                bill = float(rentalPeriod.days / 7) * 60 * numOfBikes

            # Desconto familia
            if 3 <= numOfBikes <= 5:
                print('Será aplicado o desconto de família (30% de desconto)')
                bill = bill * 0.7

            print('Sua bicicleta foi devolvida.')
            return bill

        else:
            print('Não foi possivel devolver a sua bicicleta, tente novamente.')
            return None


class Customer:
    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """

        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """

        bikes = input("How many bikes would you like to rent?")

        # implement logic for invalid input
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0

