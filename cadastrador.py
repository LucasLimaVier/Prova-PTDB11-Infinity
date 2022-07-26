# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrador.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 379)
        MainWindow.setMinimumSize(QtCore.QSize(576, 379))
        MainWindow.setMaximumSize(QtCore.QSize(576, 379))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(60, 20, 451, 61))
        self.lbl_titulo.setAutoFillBackground(False)
        self.lbl_titulo.setStyleSheet("font: 75 20pt \"Arial\";")
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.btn_visul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_visul.setGeometry(QtCore.QRect(130, 90, 111, 31))
        self.btn_visul.setObjectName("btn_visul")
        self.btn_admin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_admin.setGeometry(QtCore.QRect(320, 90, 111, 31))
        self.btn_admin.setObjectName("btn_admin")
        self.lbl_modoAtual = QtWidgets.QLabel(self.centralwidget)
        self.lbl_modoAtual.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.lbl_modoAtual.setObjectName("lbl_modoAtual")
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setGeometry(QtCore.QRect(90, 130, 71, 16))
        self.lbl_status.setObjectName("lbl_status")
        self.lbl_nome = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome.setGeometry(QtCore.QRect(20, 160, 81, 21))
        self.lbl_nome.setStyleSheet("font: 75 14pt \"Arial\";")
        self.lbl_nome.setObjectName("lbl_nome")
        self.lbl_senha = QtWidgets.QLabel(self.centralwidget)
        self.lbl_senha.setGeometry(QtCore.QRect(20, 190, 61, 21))
        self.lbl_senha.setStyleSheet("font: 75 14pt \"Arial\";")
        self.lbl_senha.setObjectName("lbl_senha")
        self.lbl_email = QtWidgets.QLabel(self.centralwidget)
        self.lbl_email.setGeometry(QtCore.QRect(20, 220, 61, 21))
        self.lbl_email.setStyleSheet("font: 75 14pt \"Arial\";")
        self.lbl_email.setObjectName("lbl_email")
        self.txt_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome.setGeometry(QtCore.QRect(80, 160, 281, 20))
        self.txt_nome.setObjectName("txt_nome")
        self.txt_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_senha.setGeometry(QtCore.QRect(80, 190, 281, 20))
        self.txt_senha.setObjectName("txt_senha")
        self.txt_email = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_email.setGeometry(QtCore.QRect(80, 220, 281, 20))
        self.txt_email.setObjectName("txt_email")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 160, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 190, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 220, 101, 16))
        self.label_3.setObjectName("label_3")
        self.qtab_usuarios = QtWidgets.QTableWidget(self.centralwidget)
        self.qtab_usuarios.setGeometry(QtCore.QRect(20, 260, 401, 111))
        self.qtab_usuarios.setObjectName("qtab_usuarios")
        self.qtab_usuarios.setColumnCount(5)
        self.qtab_usuarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.qtab_usuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtab_usuarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtab_usuarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtab_usuarios.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.qtab_usuarios.setHorizontalHeaderItem(4, item)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(480, 190, 75, 23))
        self.btn_add.setObjectName("btn_add")
        self.btn_editar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editar.setGeometry(QtCore.QRect(480, 220, 75, 23))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_remover = QtWidgets.QPushButton(self.centralwidget)
        self.btn_remover.setGeometry(QtCore.QRect(480, 250, 75, 23))
        self.btn_remover.setObjectName("btn_remover")
        self.txt_id = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_id.setGeometry(QtCore.QRect(460, 320, 61, 21))
        self.txt_id.setObjectName("txt_id")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 300, 47, 13))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_titulo.setText(_translate("MainWindow", "CADASTRADOR DE USUÁRIOS"))
        self.btn_visul.setText(_translate("MainWindow", "Modo de visualização"))
        self.btn_admin.setText(_translate("MainWindow", "Modo administrador"))
        self.lbl_modoAtual.setText(_translate("MainWindow", "MODO ATUAL:"))
        self.lbl_status.setText(_translate("MainWindow", "Visualização"))
        self.lbl_nome.setText(_translate("MainWindow", "Nome:"))
        self.lbl_senha.setText(_translate("MainWindow", "Senha:"))
        self.lbl_email.setText(_translate("MainWindow", "Email:"))
        self.label.setText(_translate("MainWindow", "(max 50 caracteres)"))
        self.label_2.setText(_translate("MainWindow", "(max 20 caracteres)"))
        self.label_3.setText(_translate("MainWindow", "(max 100 caracteres)"))
        item = self.qtab_usuarios.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.qtab_usuarios.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Senha"))
        item = self.qtab_usuarios.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.qtab_usuarios.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Criacao"))
        item = self.qtab_usuarios.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ID"))
        self.btn_add.setText(_translate("MainWindow", "Adicionar"))
        self.btn_editar.setText(_translate("MainWindow", "Editar"))
        self.btn_remover.setText(_translate("MainWindow", "Remover"))
        self.label_4.setText(_translate("MainWindow", "ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
