import pymysql.cursors
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QMessageBox
from PyQt5 import QtWidgets
from datetime import datetime
from cadastrador import Ui_MainWindow

class Dao:
    def __init__(self):
        self.conexao = pymysql.connect(host="localhost",
                                       database="administracao",
                                       password="admin@123",
                                       user="root",
                                       cursorclass=pymysql.cursors.DictCursor)

    def ler_cadastrados(self):
        with self.conexao.cursor() as cursor:
            sql = "SELECT * FROM usuarios"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            self.conexao.commit()
            return resultado

    def bd_adicionar(self, nome, senha, email):
        with self.conexao.cursor() as cursor:
            sql = "INSERT INTO usuarios(nome, senha, email, criacao) VALUES(%s, %s, %s, %s)"
            data = datetime.now()
            dataFormatada = data.strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(sql, (nome, senha, email, dataFormatada))
            self.conexao.commit()
    def bd_editar(self, nome, senha, email, ident):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE usuarios SET nome = %s, senha = %s, email = %s WHERE id_usuario = %s"
            cursor.execute(sql, (nome, senha, email, ident))
            self.conexao.commit()

    def bd_remove(self, id_usuario):
        with self.conexao.cursor() as cursor:
            sql = "DELETE FROM usuarios WHERE id_usuario = %s"
            cursor.execute(sql, (id_usuario,))
            self.conexao.commit()


class Janela(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.modoVisualizar()
        self.btn_visul.clicked.connect(self.modoVisualizar)
        self.btn_admin.clicked.connect(self.modoAdmin)
        self.cadastrados()
        self.qtab_usuarios.cellClicked.connect(self.celula_clicada)
        self.btn_add.clicked.connect(self.adicionar)
        self.btn_editar.clicked.connect(self.editar)
        self.txt_id.setEnabled(False)
        self.btn_remover.clicked.connect(self.remover)


    def modoVisualizar(self):
        self.lbl_status.setText("Visualização")
        self.txt_nome.setEnabled(False)
        self.txt_senha.setEnabled(False)
        self.txt_email.setEnabled(False)
        self.btn_add.setEnabled(False)
        self.btn_editar.setEnabled(False)
        self.btn_remover.setEnabled(False)


    def modoAdmin(self):
        self.lbl_status.setText("Administrador")
        self.txt_nome.setEnabled(True)
        self.txt_senha.setEnabled(True)
        self.txt_email.setEnabled(True)
        self.btn_add.setEnabled(True)
        self.btn_editar.setEnabled(True)
        self.btn_remover.setEnabled(True)

    def cadastrados(self):
        bd = Dao()
        listaCadastrados = bd.ler_cadastrados()
        linha = 0
        self.qtab_usuarios.setRowCount(len(listaCadastrados))
        for n in listaCadastrados:
            self.qtab_usuarios.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(n["nome"])))
            self.qtab_usuarios.setItem(linha, 1, QtWidgets.QTableWidgetItem(str(n["senha"])))
            self.qtab_usuarios.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(n["email"])))
            self.qtab_usuarios.setItem(linha, 3, QtWidgets.QTableWidgetItem(str(n["criacao"])))
            self.qtab_usuarios.setItem(linha, 4, QtWidgets.QTableWidgetItem(str(n["id_usuario"])))
            linha += 1

    def celula_clicada(self, row):
        nome = self.qtab_usuarios.item(row, 0).text()
        senha = self.qtab_usuarios.item(row, 1).text()
        email = self.qtab_usuarios.item(row, 2).text()
        identidade = self.qtab_usuarios.item(row, 4).text()

        self.txt_nome.setText(str(nome))
        self.txt_senha.setText(str(senha))
        self.txt_email.setText(str(email))
        self.txt_id.setText(str(identidade))

    def adicionar(self):
        bd = Dao()
        nome = self.txt_nome.text()
        senha = self.txt_senha.text()
        email = self.txt_email.text()
        if nome == "" or senha == "" or email == "":
            QMessageBox.critical(self, "Erro tipo 1", "Dados em branco")
        elif len(nome) > 50 or len(senha) > 20 or len(email) > 100:
            QMessageBox.critical(self, "Erro tipo 2", "Respeite o número de caracteres")
        else:
            bd.bd_adicionar(nome, senha, email)
            QMessageBox.information(self, "Aviso!", "Cadastro Realizado")
            self.cadastrados()

    def editar(self):
        bd = Dao()
        nome = self.txt_nome.text()
        senha = self.txt_senha.text()
        email = self.txt_email.text()
        ident = self.txt_id.text()
        if nome == "" or senha == "" or email == "":
            QMessageBox.critical(self, "Erro tipo 1", "Dados em branco")
        elif len(nome) > 50 or len(senha) > 20 or len(email) > 100:
            QMessageBox.critical(self, "Erro tipo 2", "Respeite o número de caracteres")
        else:
            bd.bd_editar(nome, senha, email, ident)
            QMessageBox.information(self, "Aviso!", "Edição Realizada")
            self.cadastrados()

    def remover(self):
        bd = Dao()
        identidade = str(self.txt_id.text())
        nome = self.txt_nome.text()
        senha = self.txt_senha.text()
        email = self.txt_email.text()
        if nome == "" or senha == "" or email == "":
            QMessageBox.critical(self, "Erro tipo 1", "Dados em branco")
        elif len(nome) > 50 or len(senha) > 20 or len(email) > 100:
            QMessageBox.critical(self, "Erro tipo 2", "Respeite o número de caracteres")
        else:
            bd.bd_remove(identidade)
            QMessageBox.information(self, "Aviso!", "Remoção Realizada")
            self.cadastrados()



app = QApplication([])
window = Janela()
window.show()
app.exec_()