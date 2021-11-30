from flask.scaffold import F
from banco import *
from classes import Cliente
from flask import render_template


def verificarCadastroCliente(cpf):
    banco=connectBanco()
    cursor = banco.cursor()
    cursor.execute(f"""
    SELECT * FROM CLIENTE WHERE cpfCliente='{cpf}'
    """)
    dados=cursor.fetchall()
    if dados:
        banco.commit()
        banco.close()
        return dados
    else:
        banco.commit()
        banco.close()
        return "f"

def createUser(cliente):
    banco=connectBanco()
    cursor = banco.cursor()
    cursor.execute(f"""
    INSERT INTO CLIENTE(cpfCliente,nomeCliente,phoneCliente) VALUES ({cliente.cpf},'{cliente.nome}',{cliente.phone})
    """)
    banco.commit()
    banco.close()

def createMoto(moto):
    banco=connectBanco()
    cursor = banco.cursor()
    cursor.execute(f"""
    INSERT INTO MOTO(placaMoto,horaDataEntrada,horaDataSaida,numVaga,cpfProprietario) VALUES ('{moto.placa}','{moto.data_hora_entrada}','0000-00-00 00:00:00',{moto.numVaga},{moto.cpfProprietario})
    """)
    banco.commit()
    banco.close()

def createCarro(carro):
    banco=connectBanco()
    cursor = banco.cursor()
    cursor.execute(f"""
    INSERT INTO CARRO(placaCarro,porteCarro,horaDataEntrada,horaDataSaida,numVaga,cpfProprietario) VALUES ('{carro.placa}','{carro.porteCarro}','{carro.data_hora_entrada}','0000-00-00 00:00:00',{carro.numVaga},{carro.cpfProprietario})
    """)
    banco.commit()
    banco.close()

def updateUser(cliente):
    banco=connectBanco()
    cursor = banco.cursor()
    cursor.execute(f"""
    UPDATE CLIENTE SET nomeCliente='{cliente.nome}', phoneCliente={cliente.phone} WHERE cpfCliente={cliente.cpf}""")
    banco.commit()
    banco.close()
    
def selectVeiculos():
    banco=connectBanco()
    cursor = banco.cursor()
    cursor.execute(f"""
    SELECT c.placacarro, c.numvaga,c.horaDataEntrada, cli.nomecliente  FROM CARRO as c
INNER JOIN CLIENTE as cli on c.cpfProprietario=cli.cpfcliente WHERE c.numVaga!=0 UNION
SELECT m.placamoto, m.numVaga,m.horaDataEntrada, clim.nomecliente  from MOTO as m
INNER JOIN CLIENTE as clim on m.cpfProprietario=clim.cpfCliente WHERE m.numVaga!=0;
    """)
    dadosVeiculos=cursor.fetchall()
    banco.commit()
    banco.close()
    return dadosVeiculos

def exitVeiculo(placacpf):
  banco=connectBanco()
  cursor = banco.cursor()
  cursor.execute(f"""
  SELECT c.placacarro, c.numvaga,c.horaDataEntrada, cli.nomecliente  FROM CARRO as c
INNER JOIN CLIENTE as cli on c.cpfProprietario=cli.cpfcliente WHERE c.numVaga!=0  AND c.cpfProprietario='{placacpf}' OR c.placaCarro='{placacpf}' UNION
SELECT m.placamoto, m.numVaga,m.horaDataEntrada, clim.nomecliente  from MOTO as m
INNER JOIN CLIENTE as clim on m.cpfProprietario=clim.cpfCliente WHERE m.numVaga!=0 AND m.cpfProprietario='{placacpf}' OR m.placaMoto='{placacpf}';
  """)
  dadosconsulta=cursor.fetchall()
  banco.commit()
  banco.close()
  return dadosconsulta


