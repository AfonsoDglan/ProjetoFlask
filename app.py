from os import error
from flask import Flask, render_template, redirect, url_for, request, make_response
import pdfkit
import sqlite3
from datetime import datetime
from classes import *
from funcoes import *
from banco import *

#acho que está pegando a mesma vaga pq reinia o site e a lista volta para seu estado inicial.
appFlask = Flask(__name__)

Estacionamento = Vaga()
#startBanco()
dados_comprovante = {}


@appFlask.route('/')
def index():
  dadosSQLveiculo=selectVeiculos()
  return render_template("index.html",carro=len(Estacionamento.vagasCarro),moto=len(Estacionamento.vagasMoto),dadosSQLveiculo=dadosSQLveiculo)

@appFlask.route('/consulta',methods=["POST"])
def consulta():
  cpf = request.form.get("cpf")
  if cpf !=" ":
    dadosSQL=verificarCadastroCliente(cpf)
    if dadosSQL[0][0] != 'f':
      cond="1"
    else:
      cond="2"
    return render_template("cadastro.html",dadosSQL=dadosSQL,cpf=cpf,cond=cond,error="")

@appFlask.route('/comprovante')
def comprovante():
  rend = render_template("comprovante.html",dados=dados_comprovante)
  pdf = pdfkit.from_string(rend, False)
  resp = make_response(pdf)
  resp.headers['Content-Type'] = 'application/pdf'
  resp.headers['Content-Disposition'] = 'attachment; filiname=test.pdf'
  return resp

@appFlask.route('/entrada',methods=["GET","POST"])
def entrada():
  error=[]
  type = request.form.get("type")
  data_e_hora_atuais = datetime.now()
  data_e_hora_format = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
  dados_comprovante["horas"] = data_e_hora_format;
  cpf = request.form.get("cpfcli")
  condi= request.form.get("cond")
  nome = request.form.get("nome")
  phone = request.form.get("phone")
  dados_comprovante["nome"] = nome
  dados_comprovante["fone"] = phone 
  if condi == '1':
    clienteUP=Cliente(nome,cpf,phone)
    updateUser(clienteUP)
    if type == "Moto":
      if len(Estacionamento.vagasMoto) == 0:
        error.append('moto')      
      else:
        placa = request.form.get("placa")
        dados_comprovante["placa"] = placa
        vaga = Estacionamento.EstacionarMoto()
        dados_comprovante["vaga"] = vaga
        print("cpfpro: ",cpf)
        moto = Moto(placa,data_e_hora_atuais,vaga,cpf)
        createMoto(moto)
        error.append('certo')
    elif type == "Carro":
      if len(Estacionamento.vagasCarro) == 0:
        error.append('carro')
      else:
        placa = request.form.get("placa")
        dados_comprovante["placa"] = placa
        vaga = Estacionamento.EstacionarCarro()
        dados_comprovante["vaga"] = vaga
        porte = request.form.get("flexRadioDefault")
        carro = Carro(placa,data_e_hora_atuais,vaga,cpf)
        carro.setPorteCarro(porte)
        createCarro(carro)
        error.append('certo')
    return render_template("cadastro.html",error=error,cpf="",tipoc="")
  else:
    createcliente = Cliente(nome,cpf,phone)
    if cpf != None:
      createUser(createcliente)
      if type == "Moto":
        if len(Estacionamento.vagasMoto) == 0:
          error.append('moto')
        else:
          placa = request.form.get("placa")
          dados_comprovante["placa"] = placa
          vaga = Estacionamento.EstacionarMoto()
          dados_comprovante["vaga"] = vaga
          print("cpfpro: ",cpf)
          moto = Moto(placa,data_e_hora_atuais,vaga,cpf)
          createMoto(moto)
          error.append('certo')
      elif type == "Carro":
        if len(Estacionamento.vagasCarro) == 0:
          error.append('carro')
        else:
          placa = request.form.get("placa")
          dados_comprovante["placa"] = placa
          vaga = Estacionamento.EstacionarCarro()
          dados_comprovante["vaga"] = vaga
          porte = request.form.get("flexRadioDefault")
          carro = Carro(placa,data_e_hora_atuais,vaga,cpf)
          carro.setPorteCarro(porte)
          createCarro(carro)
          error.append('certo')
    return render_template("cadastro.html",error=error)

@appFlask.route('/exitid')
def exitid():
  my_var = request.args.get('my_var', None)
  dados=exitVeiculo(my_var)
  return render_template("saida.html",dados=dados)
# @appFlask.route('/excluir/<int:id>')
# def excluir(id):
#   banco = sqlite3.connect("db_teste.db")
#   cursor = banco.cursor()
#   cursor.execute("DELETE FROM PESSOA WHERE idPessoa=?",(id,))
#   regiPessoas=cursor.execute("SELECT * FROM PESSOA")
#   result=regiPessoas.fetchall()
#   #banco.commit()
#   banco.close()
#   return render_template("index.html",result=result)

@appFlask.route('/saida')
def saida():
    return render_template("saida.html")

@appFlask.route('/teste')
def teste():
    return render_template("comprovante.html")

@appFlask.route('/exit',methods=["POST"])
def exit():
    cpfplaca = request.form.get("cpfplaca")
    dados=exitVeiculo(cpfplaca)
    return render_template("saida.html",dados=dados)

if __name__ == "__main__":
  appFlask.run(debug=True)