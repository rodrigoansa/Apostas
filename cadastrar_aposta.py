from PyQt5 import  uic,QtWidgets

def funcao_principal():
    time1 = cadastro.lineEdit.text()
    time2 = cadastro.lineEdit_2.text()
    time3 = cadastro.lineEdit_3.text()
    time4 = cadastro.lineEdit_4.text()    
    time5 = cadastro.lineEdit_5.text()    
    time6 = cadastro.lineEdit_6.text()    
    time7 = cadastro.lineEdit_7.text()
    time8 = cadastro.lineEdit_8.text()
    lucro = cadastro.lineEdit_9.text()

             
    if cadastro.checkBox_1.isChecked() == True:
        print('Time 1: ',time1, check)
    if cadastro.checkBox_2.isChecked() == True:
        print('Time 2: ',time2, check_1)
    if cadastro.checkBox_3.isChecked() == True:
        print('Time 3: ',time3, check_2)
    if cadastro.checkBox_4.isChecked() == True:
        print('Time 4: ',time4, check_3)
    if cadastro.checkBox_5.isChecked() == True:
        print('Time 5: ',time5, check_4)
    if cadastro.checkBox_6.isChecked() == True:
        print('Time 6: ',time6, check_5)
    if cadastro.checkBox_7.isChecked() == True:
        print('Time 7: ',time7, check_6)
    if cadastro.checkBox_8.isChecked() == True:
        print('Time 8: ',time8, check_7)
        
    print('Lucro: R$', lucro)
    print(check)

mercado = ['','Casa', 'Empate', 'Fora', '+2,5']

      
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

check = cadastro.comboBox.addItems(mercado)
check_1 = cadastro.comboBox_1.addItems(mercado)
check_2 = cadastro.comboBox_2.addItems(mercado)
check_3 = cadastro.comboBox_3.addItems(mercado)
check_4 = cadastro.comboBox_4.addItems(mercado)
check_5 = cadastro.comboBox_5.addItems(mercado)
check_6 = cadastro.comboBox_6.addItems(mercado)
check_7 = cadastro.comboBox_7.addItems(mercado)


cadastro.show()
app.exec()