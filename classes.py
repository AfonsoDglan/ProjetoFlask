class Veiculo():
    data_hora_saida = ''
    def __init__(self,placa,data_hora_entrada,numVaga,cpfPro) -> None:
        self.placa = placa
        self.data_hora_entrada = data_hora_entrada
        self.numVaga = numVaga
        self.cpfProprietario = cpfPro

    def saidaVeiculo(self,saida):
        self.data_hora_saida = saida

    def registrarPagamento():
        pass

    def imprimirTicket():
        pass

    
class Moto(Veiculo):
    def __init__(self,placa,data_hora_entrada,numVaga,cpfPro) -> None:
        super().__init__(placa,data_hora_entrada,numVaga,cpfPro)

class Carro(Veiculo):
    porteCarro = ''
    def __init__(self,placa,data_hora_entrada,numVaga,cpfPro) -> None:
        super().__init__(placa,data_hora_entrada,numVaga,cpfPro)
    
    def setPorteCarro(self,porte):
        self.porteCarro = porte

class Cliente():
    def __init__(self,Nome,cpf,phone) -> None:
        self.nome = Nome
        self.cpf = cpf
        self.phone = phone

class Vaga():
    vagasMoto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
    vagasCarro = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    #vagasCarro=[]
    totalVagas = ''
    vagasAtivas = ''
    idVaga = ''

    def vagasDisponiveis():
        pass

    def EstacionarMoto(self):
        numero = self.vagasMoto.pop()
        return int(numero)
    
    def EstacionarCarro(self):
        numero = self.vagasCarro.pop()
        return int(numero)

