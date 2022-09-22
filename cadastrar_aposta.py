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
    print('Time 2: ',time2)
    if not time2:
        print('Lucro: ', lucro)
    else:
        print('Time 3: ',time3)
    if not time3:
        print('Lucro: ', lucro)
    else:
        print('Time 4: ',time4)
    if not time4:
        print('Lucro: ', lucro)
    else:
        print('Time 5: ',time5)
    if not time5:
        print('Lucro: ', lucro)
    else:
        print('Time 6: ',time6)
    if not time6:
        print('Lucro: ', lucro)
    else:
        print('Time 7: ',time7)
    if not time7:
        print('Lucro: ', lucro)
    else:
        print('Time 8: ',time8)
    if not time8:
        print('Lucro: ', lucro)
    
    
       
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()