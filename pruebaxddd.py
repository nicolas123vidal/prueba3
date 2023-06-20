import numpy as np 
op1=0
patente=0 
marca=0
fRegistro=0
precio=0
caracteres=1 
vehiculo=0
autosComprar=np.ones((8,4),dtype=object) 

for f in range (8): 
    for c in range (4): 
        autos=autos+1 
        autosComprar[f,c]=autos 



while op1 !=4: 
    print("MENU")  
    print("1.grabar") 
    print("2.buscar") 
    print("3.imprimir certificados") 
    print("4.salir")  
    op1=int(input("ingrese opcion deseada: ")) 

    if op1==1: 
       nom=str(input("ingrese nombre y apellido"))
       
       tipo=str(input("tipo de veiculo"))  

       patente==str(input("patente de vehiculo")) 
        
       precio=int(input("ingrese precio del auto"))  
       
       marca==str(input("marca de vehiculo")) 
        
       for caracteres in range (int(marca)): 
            if caracteres>2 and caracteres<15: 
                break 
       else:  
          print("debe ser mayor a 2 y menor que 15")  
    if op1==2: 
        print(patente) 
        filaAuto=int(input("elija la fila"))  
        filaAuto=filaAuto-1
        columnAuto=int(input("elija columna")) 
        columnAuto=columnAuto-1
        autosComprar[filaAuto,columnAuto]="X"  
        print("auto comprado")  
    if op1==3: 
       multas=int(input("valor de la multa"))  
       cantMulti=int(input("ingrese cantidad de multas"))
       
       if multas>=1500 and multas<=3500: 
           result=multas*cantMulti 
           print("usted en multas debe",)
            
       else: 
           print("debe de ser entre 1500 y 3500")   

       emiCont=int(input("valor del gasto de emicion de contaminantes: ")) 
       emi=int(input("ingrese cantidad de multas"))  

       if emiCont>=1500 and emiCont<=3500: 
          result2=emiCont*emi 
          print("usted en emicion de contaminantes debe",result2)  
          print("su patente es ",patente) 
          print("su tipo de vehiculo es ",tipo)  
          print("su precio es ",precio)

       else: 
            print("debe de ser entre 1500 y 3500")   
    if op1==4: 
        print("adios señor ",nom)



        

        




            
       

