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
    radio = cadastro.radioButton.isChecked()
    
        
    print('Time 1: ',time1)
    if cadastro.radioButton.isChecked() == True:
        print('Lucro: ', lucro)
    else:
        print('Time 2: ',time2)
    if cadastro.radioButton.isChecked() == True:
        print('Lucro: ', lucro)
    else:
        print('Time 3: ',time3)
    if cadastro.radioButton.isChecked() == True:
        print('Lucro: ', lucro)
    else:
        print('Time 4: ',time4)
    if cadastro.radioButton.isChecked() == True:
        print('Lucro: ', lucro)
    else:
        print('Time 5: ',time5)
    if cadastro.radioButton.isChecked() == True:
        print('Lucro: ', lucro)
    else:
        print('Time 6: ',time6)
    if cadastro.radioButton.isChecked() == True:
        print('Lucro: ', lucro)
    else:
        print('Time 7: ',time7)
    if cadastro.radioButton.isChecked() == True:
        print('Lucro: ', lucro)
    else:
        print('Time 8: ',time8)
    if cadastro.radioButton.isChecked() == True:
        print('Lucro: ', lucro)
                
    
       
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)
cadastro.radioButton.isChecked()

cadastro.show()
app.exec()