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
        print('Time 1: ',time1, box)
    if cadastro.checkBox_2.isChecked() == True:
        print('Time 2: ',time2, box_1)
    if cadastro.checkBox_3.isChecked() == True:
        print('Time 3: ',time3, box_2)
    if cadastro.checkBox_4.isChecked() == True:
        print('Time 4: ',time4, box_3)
    if cadastro.checkBox_5.isChecked() == True:
        print('Time 5: ',time5, box_4)
    if cadastro.checkBox_6.isChecked() == True:
        print('Time 6: ',time6, box_5)
    if cadastro.checkBox_7.isChecked() == True:
        print('Time 7: ',time7, box_6)
    if cadastro.checkBox_8.isChecked() == True:
        print('Time 8: ',time8, box_7)
        
    print('Lucro: R$', lucro)
    

mercado = ['','Casa', 'Empate', 'Fora', '+2,5']

      
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

box = cadastro.comboBox.addItems(mercado)
box_1 = cadastro.comboBox_1.addItems(mercado)
box_2 = cadastro.comboBox_2.addItems(mercado)
box_3 = cadastro.comboBox_3.addItems(mercado)
box_4 = cadastro.comboBox_4.addItems(mercado)
box_5 = cadastro.comboBox_5.addItems(mercado)
box_6 = cadastro.comboBox_6.addItems(mercado)
box_7 = cadastro.comboBox_7.addItems(mercado)


cadastro.show()
app.exec()