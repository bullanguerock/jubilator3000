import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog
import time
from datetime import date

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(685, 522)
        self.boxfondos = QtWidgets.QComboBox(Dialog)
        self.boxfondos.setGeometry(QtCore.QRect(320, 370, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.boxfondos.setFont(font)
        self.boxfondos.setObjectName("boxfondos")
        self.boxfondos.addItem("")
        self.boxfondos.addItem("")
        self.boxfondos.addItem("")
        self.boxfondos.addItem("")
        self.boxfondos.addItem("")
        self.simular = QtWidgets.QPushButton(Dialog)
        self.simular.setGeometry(QtCore.QRect(60, 440, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        self.simular.setFont(font)
        self.simular.setObjectName("simular")
        self.boxafp = QtWidgets.QComboBox(Dialog)
        self.boxafp.setGeometry(QtCore.QRect(320, 330, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.boxafp.setFont(font)
        self.boxafp.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.boxafp.setObjectName("boxafp")
        self.boxafp.addItem("")
        self.boxafp.addItem("")
        self.boxafp.addItem("")
        self.boxafp.addItem("")
        self.boxafp.addItem("")
        self.boxafp.addItem("")
        self.sueldouf = QtWidgets.QLineEdit(Dialog)
        self.sueldouf.setGeometry(QtCore.QRect(320, 130, 133, 16))
        self.sueldouf.setObjectName("sueldouf")
        self.sexo = QtWidgets.QComboBox(Dialog)
        self.sexo.setGeometry(QtCore.QRect(320, 30, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.sexo.setFont(font)
        self.sexo.setObjectName("sexo")
        self.sexo.addItem("")
        self.sexo.addItem("")
        self.sueldos = QtWidgets.QLineEdit(Dialog)
        self.sueldos.setGeometry(QtCore.QRect(320, 110, 133, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.sueldos.setFont(font)
        self.sueldos.setObjectName("sueldos")
        self.fechanacimiento = QtWidgets.QDateEdit(Dialog)
        self.fechanacimiento.setGeometry(QtCore.QRect(320, 70, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.fechanacimiento.setFont(font)
        self.fechanacimiento.setObjectName("fechanacimiento")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(460, 110, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(460, 130, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.saldocartola = QtWidgets.QLineEdit(Dialog)
        self.saldocartola.setGeometry(QtCore.QRect(320, 180, 132, 16))
        self.saldocartola.setObjectName("saldocartola")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(460, 180, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(400, 450, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 450, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.apvfinal = QtWidgets.QLabel(Dialog)
        self.apvfinal.setGeometry(QtCore.QRect(420, 450, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(11)
        self.apvfinal.setFont(font)
        self.apvfinal.setText("")
        self.apvfinal.setObjectName("apvfinal")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(460, 220, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.sueldoapv = QtWidgets.QLineEdit(Dialog)
        self.sueldoapv.setGeometry(QtCore.QRect(320, 220, 132, 16))
        self.sueldoapv.setObjectName("sueldoapv")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(460, 270, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.apvmensual = QtWidgets.QLineEdit(Dialog)
        self.apvmensual.setGeometry(QtCore.QRect(320, 270, 132, 16))
        self.apvmensual.setObjectName("apvmensual")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(460, 410, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.sueldouf_5 = QtWidgets.QLineEdit(Dialog)
        self.sueldouf_5.setGeometry(QtCore.QRect(320, 410, 132, 16))
        self.sueldouf_5.setObjectName("sueldouf_5")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 281, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labela = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.labela.setFont(font)
        self.labela.setObjectName("labela")
        self.gridLayout.addWidget(self.labela, 8, 0, 1, 1)
        self.apva = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.apva.setFont(font)
        self.apva.setObjectName("apva")
        self.gridLayout.addWidget(self.apva, 5, 0, 1, 1)
        self.apv = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.apv.setFont(font)
        self.apv.setObjectName("apv")
        self.gridLayout.addWidget(self.apv, 6, 0, 1, 1)
        self.labelf_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.labelf_2.setFont(font)
        self.labelf_2.setObjectName("labelf_2")
        self.gridLayout.addWidget(self.labelf_2, 10, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.labela_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.labela_2.setFont(font)
        self.labela_2.setObjectName("labela_2")
        self.gridLayout.addWidget(self.labela_2, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.labela_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.labela_3.setFont(font)
        self.labela_3.setObjectName("labela_3")
        self.gridLayout.addWidget(self.labela_3, 3, 0, 1, 1)
        self.labelf = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Dotum")
        font.setPointSize(10)
        self.labelf.setFont(font)
        self.labelf.setObjectName("labelf")
        self.gridLayout.addWidget(self.labelf, 9, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(190, 480, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(350, 480, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.jubilacionapvfinal = QtWidgets.QLabel(Dialog)
        self.jubilacionapvfinal.setGeometry(QtCore.QRect(380, 480, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(11)
        self.jubilacionapvfinal.setFont(font)
        self.jubilacionapvfinal.setText("")
        self.jubilacionapvfinal.setObjectName("jubilacionapvfinal")
        self.layoutWidget.raise_()
        self.boxfondos.raise_()
        self.boxafp.raise_()
        self.simular.raise_()
        self.sueldouf.raise_()
        self.sexo.raise_()
        self.sueldos.raise_()
        self.fechanacimiento.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.saldocartola.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_3.raise_()
        self.apvfinal.raise_()
        self.label_9.raise_()
        self.sueldoapv.raise_()
        self.label_10.raise_()
        self.apvmensual.raise_()
        self.label_11.raise_()
        self.sueldouf_5.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.jubilacionapvfinal.raise_()
        self.labela.setBuddy(self.boxafp)
        self.labelf_2.setBuddy(self.boxfondos)
        self.labelf.setBuddy(self.boxfondos)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RS Estimar monto APV"))
        self.boxfondos.setItemText(0, _translate("Dialog", "A"))
        self.boxfondos.setItemText(1, _translate("Dialog", "B"))
        self.boxfondos.setItemText(2, _translate("Dialog", "C"))
        self.boxfondos.setItemText(3, _translate("Dialog", "D"))
        self.boxfondos.setItemText(4, _translate("Dialog", "E"))
        self.simular.setText(_translate("Dialog", "Simular"))
        self.boxafp.setItemText(0, _translate("Dialog", "AFP Capital"))
        self.boxafp.setItemText(1, _translate("Dialog", "AFP Cuprum"))
        self.boxafp.setItemText(2, _translate("Dialog", "AFP Habitat"))
        self.boxafp.setItemText(3, _translate("Dialog", "AFP Modelo"))
        self.boxafp.setItemText(4, _translate("Dialog", "AFP Planvital"))
        self.boxafp.setItemText(5, _translate("Dialog", "AFP Provida"))
        self.sexo.setItemText(0, _translate("Dialog", "Hombre"))
        self.sexo.setItemText(1, _translate("Dialog", "Mujer"))
        self.fechanacimiento.setDisplayFormat(_translate("Dialog", "MM-yyyy"))
        self.label_5.setText(_translate("Dialog", "($)"))
        self.label_6.setText(_translate("Dialog", "(UF)"))
        self.label_7.setText(_translate("Dialog", "($)"))
        self.label_8.setText(_translate("Dialog", "($)"))
        self.label_3.setText(_translate("Dialog", "Usted, deberá adicionar mes a mes  :"))
        self.label_9.setText(_translate("Dialog", "($)"))
        self.label_10.setText(_translate("Dialog", "($)"))
        self.label_11.setText(_translate("Dialog", "($)"))
        self.labela.setText(_translate("Dialog", "7.          AFP"))
        self.apva.setText(_translate("Dialog", "5.          Saldo cuenta APV"))
        self.apv.setText(_translate("Dialog", "6.          APV mensual"))
        self.labelf_2.setText(_translate("Dialog", "9.         Jubilacion esperada"))
        self.label.setText(_translate("Dialog", "1.          Sexo (H o M)"))
        self.labela_2.setText(_translate("Dialog", "4.          Saldo Cartola"))
        self.label_4.setText(_translate("Dialog", "2.          Mes y año de nacimiento"))
        self.labela_3.setText(_translate("Dialog", "3.          Remuneración mensual"))
        self.labelf.setText(_translate("Dialog", "8.          Fondo"))
        self.label_12.setText(_translate("Dialog", "Jubilación + APV adicional :"))
        self.label_13.setText(_translate("Dialog", "($)"))
        self.sueldouf.setText('0')
        self.sueldos.setText('0')
        
        self.simular.clicked.connect(self.getJubilacion)

    def getJubilacion(self):
        s = self.sexo.currentText()
        ano = self.fechanacimiento.date().year()
        mes = self.fechanacimiento.date().month()
        hoy = date.today()
        m = hoy.month
        y = hoy.year
        anoactual = int(y)
        mesactual = int(m)
        
        aa = int(self.saldocartola.displayText()) # saldo cartola
        je = int(self.sueldouf_5.displayText())
        afp = self.boxafp.currentText()
        fondo = self.boxfondos.currentText()
        tabla = [[1.44,2.06,2.35,2.12,1.74,2.4],[1.44,2.15,2.29,1.94,1.59,1.9],[1.27,2.47,2.82,2.54,2.17,2.55],[0.77,2.22,2.64,2.3,2.18,2.29],[1.16,1.53,1.65,1.62,1.38,1.97],[1.45,1.83,1.94,1.57,1.22,1.63]]
        uf = int(self.sueldouf.displayText())
        5
        if uf != 0:
            rm = uf*27208
        else:
            rm = int(self.sueldos.displayText())
        
        if afp == 'AFP Capital':
            com = tabla[0][0]
            if fondo == 'A':
                rent = tabla[0][1]
            elif fondo == 'B':
                rent = tabla[0][2]
            elif fondo == 'C':
                rent = tabla[0][3]
            elif fondo == 'D':
                rent = tabla[0][4]
            else:
                rent = tabla[0][5]
        elif afp == 'AFP Cuprum':
            com = tabla[1][0]
            if fondo == 'A':
                rent = tabla[1][1]
            elif fondo == 'B':
                rent = tabla[1][2]
            elif fondo == 'C':
                rent = tabla[1][3]
            elif fondo == 'D':
                rent = tabla[1][4]
            else:
                rent = tabla[1][5]
    
        elif afp == 'AFP Habitat':
            com = tabla[2][0]
            if fondo == 'A':
                rent = tabla[2][1]
            elif fondo == 'B':
                rent = tabla[2][2]
            elif fondo == 'C':
                rent = tabla[2][3]
            elif fondo == 'D':
                rent = tabla[2][4]
            else:
                rent = tabla[2][5]
        elif afp == 'AFP Modelo':
            com = tabla[3][0]
            if fondo == 'A':
                rent = tabla[3][1]
            elif fondo == 'B':
                rent = tabla[3][2]
            elif fondo == 'C':
                rent = tabla[3][3]
            elif fondo == 'D':
                rent = tabla[3][4]
            else:
                rent = tabla[3][5]
        
        elif afp == 'AFP Planvital' :
            com = tabla[4][0]
            if fondo == 'A':
                rent = tabla[4][1]
            elif fondo == 'B':
                rent = tabla[4][2]
            elif fondo == 'C':
                rent = tabla[4][3]
            elif fondo == 'D':
                rent = tabla[4][4]
            else:
                rent = tabla[4][5]
        else:
            com = tabla[5][0]
            if fondo == 'A':
                rent = tabla[5][1]
            elif fondo == 'B':
                rent = tabla[5][2]
            elif fondo == 'C':
                rent = tabla[5][3]
            elif fondo == 'D':
                rent = tabla[5][4]
            else:
                rent = tabla[5][5]
        if (mes <= mesactual):
            e = anoactual - ano
        else:
            e = anoactual - ano - 1  # e = edad

        if s == 'Hombre':        #  Calcula Años restantes para Jubilar según sexo
            ar = 65 - e           # ar =  Años para jubilar
            av = float(85.4 - 65)
        else:
            ar = 60 - e

            av = float(90.5 - 60)
        # ahorro total
        at = (((rm*12*ar)*0.1)+aa)
        atr = float(at * rent)
        p = int((atr/av)/12)
        apva = int(self.sueldoapv.displayText())
        apv = int(self.apvmensual.displayText())



        #calculo APV
        #ahorro apv * rentabilidad
        aapv = ((apv*12*ar)+apva)*rent
        print(int(aapv))
        caapv = (aapv *(1-com))
        #print(caapv)
        papv = ((caapv/av)/12.00)
        #print(papv)
        tapv = p + papv
        print('Pension total con APV', int(tapv))
        jj=str(int(tapv))

        rest = je-p
        apvj = (((((rest*12*av)/ 2.4)*1.005)/12)/ar)
        #print(apvj)
        print('Para tener una jubilacion esperada de: ', je, ', debes ahorrar mensualmente, ', apvj,' pesos.')

        o = str(int(apvj))

        self.apvfinal.setText(o)  # Imprime resultado en la Interfaz
        self.jubilacionapvfinal.setText(jj)

        
        
        
       
        

        


        
        
     
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
