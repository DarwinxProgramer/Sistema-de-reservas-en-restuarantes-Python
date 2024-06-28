# Form implementation generated from reading ui file 'VentanaPrincipal.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ventanaPrincipal(object):
    def setupUi(self, ventanaPrincipal):
        ventanaPrincipal.setObjectName("ventanaPrincipal")
        ventanaPrincipal.resize(1130, 715)
        self.centralwidget = QtWidgets.QWidget(parent=ventanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lblFondo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblFondo.setGeometry(QtCore.QRect(0, 0, 1141, 711))
        self.lblFondo.setText("")
        self.lblFondo.setPixmap(QtGui.QPixmap("Vista/Imagenes/pexels-pixabay-262978.jpg"))
        self.lblFondo.setScaledContents(True)
        self.lblFondo.setObjectName("lblFondo")
        self.lblTitulo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(620, 30, 451, 71))
        self.lblTitulo.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(64, 182, 200, 0)")
        self.lblTitulo.setObjectName("lblTitulo")
        self.btnRegresar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(1010, 570, 81, 61))
        self.btnRegresar.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.btnRegresar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Vista/Imagenes/atras.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnRegresar.setIcon(icon)
        self.btnRegresar.setIconSize(QtCore.QSize(50, 50))
        self.btnRegresar.setObjectName("btnRegresar")
        ventanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=ventanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        self.menuReservar = QtWidgets.QMenu(parent=self.menubar)
        self.menuReservar.setObjectName("menuReservar")
        self.menuAcerca_de = QtWidgets.QMenu(parent=self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        self.menuVer = QtWidgets.QMenu(parent=self.menubar)
        self.menuVer.setObjectName("menuVer")
        self.menuAdministrar = QtWidgets.QMenu(parent=self.menubar)
        self.menuAdministrar.setObjectName("menuAdministrar")
        ventanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=ventanaPrincipal)
        self.statusbar.setObjectName("statusbar")
        ventanaPrincipal.setStatusBar(self.statusbar)
        self.actionMesa = QtGui.QAction(parent=ventanaPrincipal)
        self.actionMesa.setObjectName("actionMesa")
        self.actionSalir = QtGui.QAction(parent=ventanaPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.actionInformacion = QtGui.QAction(parent=ventanaPrincipal)
        self.actionInformacion.setObjectName("actionInformacion")
        self.actionVerReservaciones = QtGui.QAction(parent=ventanaPrincipal)
        self.actionVerReservaciones.setObjectName("actionVerReservaciones")
        self.actionEmpleados = QtGui.QAction(parent=ventanaPrincipal)
        self.actionEmpleados.setObjectName("actionEmpleados")
        self.actionCarta = QtGui.QAction(parent=ventanaPrincipal)
        self.actionCarta.setObjectName("actionCarta")
        self.actionMesas = QtGui.QAction(parent=ventanaPrincipal)
        self.actionMesas.setObjectName("actionMesas")
        self.actionHorarios = QtGui.QAction(parent=ventanaPrincipal)
        self.actionHorarios.setObjectName("actionHorarios")
        self.actionReportes = QtGui.QAction(parent=ventanaPrincipal)
        self.actionReportes.setObjectName("actionReportes")
        self.menuReservar.addAction(self.actionMesa)
        self.menuReservar.addSeparator()
        self.menuAcerca_de.addAction(self.actionInformacion)
        self.menuAcerca_de.addSeparator()
        self.menuVer.addAction(self.actionVerReservaciones)
        self.menuVer.addSeparator()
        self.menuVer.addAction(self.actionReportes)
        self.menuVer.addSeparator()
        self.menuAdministrar.addAction(self.actionEmpleados)
        self.menuAdministrar.addSeparator()
        self.menuAdministrar.addAction(self.actionCarta)
        self.menuAdministrar.addSeparator()
        self.menuAdministrar.addAction(self.actionMesas)
        self.menuAdministrar.addSeparator()
        self.menubar.addAction(self.menuReservar.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAdministrar.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(ventanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(ventanaPrincipal)

    def retranslateUi(self, ventanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        ventanaPrincipal.setWindowTitle(_translate("ventanaPrincipal", "::Bienvenido "))
        self.lblTitulo.setText(_translate("ventanaPrincipal", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#e0fcff;\">Sistema de Reservas de Restaurantes</span></p></body></html>"))
        self.menuReservar.setTitle(_translate("ventanaPrincipal", "Reservar"))
        self.menuAcerca_de.setTitle(_translate("ventanaPrincipal", "Acerca de"))
        self.menuVer.setTitle(_translate("ventanaPrincipal", "Ver Reservaciones"))
        self.menuAdministrar.setTitle(_translate("ventanaPrincipal", "Administrar"))
        self.actionMesa.setText(_translate("ventanaPrincipal", "Mesa"))
        self.actionSalir.setText(_translate("ventanaPrincipal", "Salir"))
        self.actionInformacion.setText(_translate("ventanaPrincipal", "Informacion"))
        self.actionVerReservaciones.setText(_translate("ventanaPrincipal", "Lista Reservas"))
        self.actionEmpleados.setText(_translate("ventanaPrincipal", "Empleados"))
        self.actionCarta.setText(_translate("ventanaPrincipal", "Cartas"))
        self.actionMesas.setText(_translate("ventanaPrincipal", "Mesas"))
        self.actionHorarios.setText(_translate("ventanaPrincipal", "Horarios"))
        self.actionReportes.setText(_translate("ventanaPrincipal", "Reportes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_ventanaPrincipal()
    ui.setupUi(ventanaPrincipal)
    ventanaPrincipal.show()
    sys.exit(app.exec())
