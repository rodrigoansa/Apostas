from PyQt5 import  uic,QtWidgets

def funcao_principal():
    time1 = cadastro.lineEdit.text()
    time2 = cadastro.lineEdit_2.text()
    if time2 != (' '):    
        time3 = cadastro.lineEdit_3.text()
    else:
        time4 = cadastro.lineEdit_4.text() 
    if time3 != (' '):           
        time4 = cadastro.lineEdit_4.text()  
    if time4 != (' '):              
        time5 = cadastro.lineEdit_5.text()
    if time5 != (' '):               
        time6 = cadastro.lineEdit_6.text()
    if time6 != (' '):                           
        time7 = cadastro.lineEdit_7.text() 
    if time7 != (' '):                             
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
    print('Lucro: ', lucro)

    
    
       
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()