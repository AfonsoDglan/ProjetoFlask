import sqlite3
from sqlite3.dbapi2 import Cursor


#Conectando o banco...
def connectBanco():
    bancoBD = sqlite3.connect("bancoShowCar.db")
    return bancoBD

#Desconectando o banco
def desconectBnaco(bancoBD):
    bancoBD.close()

#Criando o banco...
def startBanco():
    banco=connectBanco()
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE if not exists CLIENTE
    (
        cpfCliente varchar(11),
        nomeCliente varchar(45),
        phoneCliente varchar(15),
        CONSTRAINT cpfcliente_pkey PRIMARY KEY (cpfCliente)
    );""")
    

    cursor.execute("""
    CREATE TABLE CARRO
    (
        placaCarro varchar(8),
        porteCarro varchar(10),
        horaDataEntrada datatime,
        horaDataSaida datatime,
        numVaga integer,
        cpfProprietario varchar(11),
        CONSTRAINT idCarro_pkey PRIMARY KEY (placaCarro),
        CONSTRAINT cpfcliente_fkey FOREIGN KEY (cpfProprietario) references CLIENTE(cpfCliente)
    );
   
   """)
    
    cursor.execute("""
    CREATE TABLE if not exists MOTO
    (
        placaMoto varchar(8),
        horaDataEntrada datatime,
        horaDataSaida datatime,
        numVaga integer,
        cpfProprietario varchar(11),
        CONSTRAINT idMoto_pkey PRIMARY KEY (placaMoto),
        CONSTRAINT cpfcliente_fkey FOREIGN KEY (cpfProprietario) references CLIENTE(cpfCliente)
    );
    """)
    
    cursor.execute("""
    CREATE TABLE if not exists VAGA
    (
        idVagas integer auto_increment,
        totalVagas integer,
        vagasMotos integer,
        vagasCarros integer,
        vagasAtivas integer,
        CONSTRAINT idvagas_pkey PRIMARY KEY(idVagas)
    );
    """)
    banco.commit()
    return banco




    


    





    


    
