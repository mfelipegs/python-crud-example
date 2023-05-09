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

def atualizar():
    id = txt_codigo.get()
    name = txt_nome.get()
    phone = txt_telefone.get()
    if name == "" or phone == "":
        MessageBox.showinfo("ALERT", "Digite todos os campos para realizar alteração")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="Exemplo")
        cursor = conectar.cursor()
        cursor.execute("UPDATE teste SET nome= '"+ txt_nome.get() + "', telefone='"+ txt_telefone.get() + "' WHERE codigo = '" + txt_codigo.get() + "'")
        cursor.execute("commit")
        MessageBox.showinfo("Status", "Successfully Updated")
        conectar.close()

def Select():
    if(txt_codigo.get() == ""):
        MessageBox.showinfo("ALERT", "Por Favor, digite o código")
    else:
        conectar = mysql.connect(host="localhost", user="root", password="", database="Exemplo")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM teste WHERE codigo= '" + txt_codigo.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            txt_nome.insert(0, row[1])
            txt_telefone.insert(0, row[2])

        conectar.close()

btn_salvar = Button(tela, text="Salvar", command=salvar, font=("Arial 12")).place(x=100,y=190)     
btn_excluir = Button(tela, text="Apagar", command=excluir, font=("Arial 12")).place(x=200,y=190)        
btn_update = Button(tela, text="Update", command=atualizar, font=("Arial 12")).place(x=320,y=190)
btn_consultar = Button(tela, text="Consultador", command=Select, font=("Arial 12")).place(x=200,y=240)
tela.mainloop()