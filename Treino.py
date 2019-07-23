class Client:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Pet(Client):
    def __init__(self, nome, idade, nome_pet, idade_pet, raca_pet):
        super().__init__(nome, idade)
        self.nome_pet = nome_pet
        self.idade_pet = idade_pet
        self.raca_pet = raca_pet

cliente = Client('Lion Thunder,', '22 anos')
pet = Pet( 'nome' ,'idade',' Kiara', '4 anos','dalmata')

print('O {} ' 'é dono do(a) {} de {} da raça {}' .format(cliente.nome, pet.nome_pet, pet.idade_pet, pet.raca_pet))