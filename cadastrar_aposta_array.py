from PyQt5 import  uic,QtWidgets

mercado = ['','Casa', 'Empate', 'Fora', '+2,5']

def funcao_principal():
    for i in range(len(checkBoxes)):
        if(checkBoxes[i].isChecked()):
            print(f'Time {i+1}: {timesTexts[i].text()} - {comboBoxes[i].currentText()}')

    print('Lucro: R$', lucro.text())
    
def configCadastro(cadastro):
    cadastro.pushButton.clicked.connect(funcao_principal)
    cadastro.comboBox.addItems(mercado)
    cadastro.comboBox_1.addItems(mercado)
    cadastro.comboBox_2.addItems(mercado)
    cadastro.comboBox_3.addItems(mercado)
    cadastro.comboBox_4.addItems(mercado)
    cadastro.comboBox_5.addItems(mercado)
    cadastro.comboBox_6.addItems(mercado)
    cadastro.comboBox_7.addItems(mercado)

app = QtWidgets.QApplication([])

cadastro = uic.loadUi("Cadastro.ui")
configCadastro(cadastro)

lucro = cadastro.lineEdit_9

timesTexts = [
    cadastro.lineEdit,
    cadastro.lineEdit_2,
    cadastro.lineEdit_3,
    cadastro.lineEdit_4,
    cadastro.lineEdit_5,
    cadastro.lineEdit_6,
    cadastro.lineEdit_7,
    cadastro.lineEdit_8,
]

comboBoxes = [
    cadastro.comboBox,
    cadastro.comboBox_1,
    cadastro.comboBox_2,
    cadastro.comboBox_3,
    cadastro.comboBox_4,
    cadastro.comboBox_5,
    cadastro.comboBox_6,
    cadastro.comboBox_7,
]

checkBoxes = [
    cadastro.checkBox_1,
    cadastro.checkBox_2,
    cadastro.checkBox_3,
    cadastro.checkBox_4,
    cadastro.checkBox_5,
    cadastro.checkBox_6,
    cadastro.checkBox_7,
    cadastro.checkBox_8,
]

cadastro.show()
app.exec()