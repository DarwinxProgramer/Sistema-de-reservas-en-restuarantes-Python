# Form implementation generated from reading ui file 'VentanaListarReservas.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1124, 576)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btnRegresar = QtWidgets.QPushButton(parent=Form)
        self.btnRegresar.setGeometry(QtCore.QRect(1020, 470, 81, 61))
        self.btnRegresar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Vista/Imagenes/atras.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnRegresar.setIcon(icon)
        self.btnRegresar.setIconSize(QtCore.QSize(50, 50))
        self.btnRegresar.setObjectName("btnRegresar")
        self.btnver = QtWidgets.QPushButton(parent=Form)
        self.btnver.setGeometry(QtCore.QRect(320, 80, 81, 21))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Vista/Imagenes/buscar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnver.setIcon(icon1)
        self.btnver.setObjectName("btnver")
        self.tablareservas = QtWidgets.QTableWidget(parent=Form)
        self.tablareservas.setGeometry(QtCore.QRect(320, 120, 400, 250))
        self.tablareservas.setObjectName("tablareservas")
        self.tablareservas.setColumnCount(4)
        self.tablareservas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablareservas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablareservas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablareservas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablareservas.setHorizontalHeaderItem(3, item)
        self.lblTitulo = QtWidgets.QLabel(parent=Form)
        self.lblTitulo.setGeometry(QtCore.QRect(470, 20, 201, 31))
        self.lblTitulo.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(64, 182, 200, 0)")
        self.lblTitulo.setObjectName("lblTitulo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnver.setText(_translate("Form", "Ver"))
        item = self.tablareservas.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Numero"))
        item = self.tablareservas.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mesa"))
        item = self.tablareservas.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Fecha"))
        item = self.tablareservas.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Hora"))
        self.lblTitulo.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Reservas</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
