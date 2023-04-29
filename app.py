from tkinter import *
import tkinter.messagebox as MessageBox
#biblioteca para carregar messagebox
import mysql.connector as mysql
#biblioteca externa do mysql

tela = Tk()
tela.geometry("500x300")
tela.title("Exemplo Banco de Dados SQL")

#Campo Codigo
lbl_codigo = Label(tela, text="Codigo", font=("Arial 12"))
lbl_codigo.place(x=50, y=30)

txt_codigo = Entry(tela, font=("Arial 12"))
txt_codigo.place(x=150, y=30)

#Campo Nome
lbl_nome = Label(tela, text="Nome", font=("Arial 12"))
lbl_nome.place(x=50, y=80)

txt_nome = Entry(tela, font=("Arial 12"))
txt_nome.place(x=150, y=80)

#Campo Telefone
lbl_telefone = Label(tela, text="Telefone", font=("Arial 12"))
lbl_telefone.place(x=50, y= 130)

txt_telefone = Entry(tela, font=("Arial 12"))
txt_telefone.place(x=150, y=130)

#Função para salvar os dados
def salvar():
    variavel_codigo = txt_codigo.get();
    variavel_nome = txt_nome.get();
    variavel_telefone = txt_telefone.get();
    #o valor da caixa repassado a variavel

    #estrutura de decisão para verificar a existência de campos em branco
    if variavel_codigo == "" or variavel_nome == "" or variavel_telefone == "":
        MessageBox.showinfo("Erro", "Há campos em branco")
    else:
        #variavel conectar corresponde a configurar a localização e acesso ao
        #banco de dados
        conectar = mysql.connect(host="localhost", user="root", password="",
                                 database = "exemplo_python_crud")
        #variavel cursor executa a coneção
        cursor = conectar.cursor()
        #metodo execute executa a query para enviar a informação ao banco de dados
        cursor.execute("INSERT INTO teste VALUES('" + variavel_codigo + "', '" + variavel_nome + "', '" + variavel_telefone + "')")
        #commit para confirmar o envio da informação ao banco de dados
        cursor.execute("commit")
        MessageBox.showinfo("Mensagem", "Cadastro realizado com sucesso.")
        conectar.close()

btn_salvar = Button(tela, text="Salvar", command="salvar", font=("Arial 12")).place(x=100,y=190)        
tela.mainloop()