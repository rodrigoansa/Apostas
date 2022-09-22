from PyQt5 import  uic,QtWidgets

def funcao_principal():
    time1 = cadastro.lineEdit.text()
    time2 = cadastro.lineEdit_2.text()
    if not time2:    
        time3 = cadastro.lineEdit_3.text()
    else:
        lucro = cadastro.lineEdit_9.text()
    if not time3:           
        time4 = cadastro.lineEdit_4.text()
    else:
        lucro = cadastro.lineEdit_9.text()  
    if not time4:              
        time5 = cadastro.lineEdit_5.text()
    else:
        lucro = cadastro.lineEdit_9.text()
    if not time5:               
        time6 = cadastro.lineEdit_6.text()
    else:
        lucro = cadastro.lineEdit_9.text()
    if not time6:                           
        time7 = cadastro.lineEdit_7.text()
    else:
        lucro = cadastro.lineEdit_9.text() 
    if not time7:                             
        time8 = cadastro.lineEdit_8.text()
    else:                             
        lucro = cadastro.lineEdit_9.text()
        
    print('Time 1: ',time1)
    print('Time 2: ',time2)
    print('Time 3: ',time3)
    print('Time 4: ',time4)
    print('Time 5: ',time5)
    print('Time 6: ',time6)
    print('Time 7: ',time7)
    print('Time 8: ',time8)
    print('Lucro: ', lucro) 
    
       
app=QtWidgets.QApplication([])
cadastro=uic.loadUi("Cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()