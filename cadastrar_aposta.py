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
        
    if time1 != (' '):
        print('Time 1: ',time1)
    elif time2 != (' '):
        print('Time 2: ',time2)
    elif time3 != (' '):
        print('Time 3: ',time3)
    elif time4 != (' '):
        print('Time 4: ',time4)
    elif time5 != (' '):
        print('Time 5: ',time5)
    elif time6 != (' '):
        print('Time 6: ', time6)
    elif time7 != (' '):
        print('Time 7: ',time7)
    elif time8 != (' '):
        print('Time 8: ', time8)
    else:
        print('Lucro: ', lucro)
    
    
       
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()