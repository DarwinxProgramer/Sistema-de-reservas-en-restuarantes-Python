# Form implementation generated from reading ui file 'VentanaLogin.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaLogin(object):
    def setupUi(self, VentanaLogin):
        VentanaLogin.setObjectName("VentanaLogin")
        VentanaLogin.resize(1128, 530)
        VentanaLogin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(parent=VentanaLogin)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 541))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Vista/Imagenes/Diseno-de-restaurante.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=VentanaLogin)
        self.label_4.setGeometry(QtCore.QRect(860, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtUser = QtWidgets.QLineEdit(parent=VentanaLogin)
        self.txtUser.setGeometry(QtCore.QRect(810, 200, 221, 22))
        self.txtUser.setStyleSheet("border-bottom-color: rgb(0, 0, 0);")
        self.txtUser.setText("")
        self.txtUser.setObjectName("txtUser")
        self.txtContrasena = QtWidgets.QLineEdit(parent=VentanaLogin)
        self.txtContrasena.setGeometry(QtCore.QRect(810, 290, 221, 22))
        self.txtContrasena.setText("")
        self.txtContrasena.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txtContrasena.setObjectName("txtContrasena")
        self.btnIngresar = QtWidgets.QPushButton(parent=VentanaLogin)
        self.btnIngresar.setGeometry(QtCore.QRect(880, 340, 93, 28))
        self.btnIngresar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.btnIngresar.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:5px;")
        self.btnIngresar.setObjectName("btnIngresar")
        self.label_8 = QtWidgets.QLabel(parent=VentanaLogin)
        self.label_8.setGeometry(QtCore.QRect(670, 20, 421, 101))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(parent=VentanaLogin)
        self.label_2.setGeometry(QtCore.QRect(730, 180, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Vista/Imagenes/perfil.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=VentanaLogin)
        self.label_3.setGeometry(QtCore.QRect(730, 260, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Vista/Imagenes/contrasena.png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(VentanaLogin)
        QtCore.QMetaObject.connectSlotsByName(VentanaLogin)

    def retranslateUi(self, VentanaLogin):
        _translate = QtCore.QCoreApplication.translate
        VentanaLogin.setWindowTitle(_translate("VentanaLogin", "Login"))
        self.label_4.setText(_translate("VentanaLogin", "Login"))
        self.btnIngresar.setText(_translate("VentanaLogin", "Ingresar"))
        self.label_8.setText(_translate("VentanaLogin", "<html><head/><body><p align=\"center\">SISTEMA DE GESTION</p><p align=\"center\">DE RESERVAS EN RESTAURANTE</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaLogin = QtWidgets.QWidget()
    ui = Ui_VentanaLogin()
    ui.setupUi(VentanaLogin)
    VentanaLogin.show()
    sys.exit(app.exec())
