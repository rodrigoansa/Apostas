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
        
    print('Time 1: ',time1)
    
    if time2 != (' '):
        print('Time 2: ',time2)
    else:
        print('Lucro: ', lucro)
    if time3 != (' '):
        print('Time 3: ',time3)
    else:
        print('Lucro: ', lucro)
    if time4 != (' '):
        print('Time 4: ',time4)
    else:
        print('Lucro: ', lucro)
    if time5 != (' '):
        print('Time 5: ',time5)
    else:
        print('Lucro: ', lucro)
    if time6 != (' '):
        print('Time 6: ', time6)
    else:
        print('Lucro: ', lucro)
    if time7 != (' '):
        print('Time 7: ',time7)
    else:
        print('Lucro: ', lucro)
    if time8 != (' '):
        print('Time 8: ', time8)
    else:
        print('Lucro: ', lucro)

    
    
       
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()