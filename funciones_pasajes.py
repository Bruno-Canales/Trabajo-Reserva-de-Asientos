def comprar_asiento(matriz,asiento_1,asiento_2,asiento_3,asiento_4,asiento_5,asiento_6,asiento_7,asiento_8,asiento_9,asiento_10,asiento_11,asiento_12,asiento_13,asiento_14,asiento_15,asiento_16,asiento_17,asiento_18,asiento_19,asiento_20,asiento_21,asiento_22,asiento_23,asiento_24,asiento_25,asiento_26,asiento_27,asiento_28,asiento_29,asiento_30,asiento_31,asiento_32,asiento_33,asiento_34,asiento_35,asiento_36,asiento_37,asiento_38,asiento_39,asiento_40,asiento_41,asiento_42):
    try:
        valor_pasaje_normal=78900
        valor_pasaje_vip=240000
        nombre=str(input("Ingrese su nombre: "))
        cerrar_while=False
        while True:
            if cerrar_while==True:
                break
            print("Ingrese rut con digito verificador")
            rut=input("Ingrese su rut: ")
            for i in rut:
                if i == "-":
                    print("Rut válido")
                    cerrar_while=True
                    break
            if cerrar_while==False:
                print("Ingrese rut valido")
        while True:
            print("Ingrese número de telefono de 9 digitos")
            telefono=input("Ingrese su telefono: ")
            if len(telefono) == 9:
                print("Numero válido")
                break
            else:
                print("Ingrese un numero válido")
        banco=input("Ingresar nombre de banco (Si es bancoDuoc se aplica 15% de descuento): ")
        if banco=="bancoDuoc":
            descuento_normal=valor_pasaje_normal*0.15
            descuento_vip=valor_pasaje_vip*0.15
            valor_pasaje_normal=valor_pasaje_normal-descuento_normal
            valor_pasaje_vip=valor_pasaje_vip-descuento_vip
            print("El descuento se ha aplicado")
        while True:
            try:
                print(matriz[0][0],"",matriz[0][1],"",matriz[0][2],"         ",matriz[1][0],"",matriz[1][1],"",matriz[1][2])
                print(matriz[2][0],"",matriz[2][1],"",matriz[2][2],"         ",matriz[3][0],matriz[3][1],matriz[3][2])
                print(matriz[4][0],matriz[4][1], matriz[4][2],"        ",matriz[5][0],matriz[5][1],matriz[5][2])
                print(matriz[6][0],matriz[6][1], matriz[6][2],"        ",matriz[7][0],matriz[7][1],matriz[7][2])
                print(matriz[8][0],matriz[8][1], matriz[8][2],"        ",matriz[9][0],matriz[9][1],matriz[9][2])
                print("==========================")
                print(matriz[10][0],matriz[10][1], matriz[10][2],"        ",matriz[11][0],matriz[11][1],matriz[11][2])
                print(matriz[12][0],matriz[12][1], matriz[12][2],"        ",matriz[13][0],matriz[13][1],matriz[13][2])
                while True:
                    asiento=int(input("Ingrese el asiento que desea comprar o x para volver al menú: "))
                    if asiento<31 and asiento>=1:
                        print("El valor de su pasaje es de $",valor_pasaje_normal)
                        break
                    elif asiento<43 and asiento>30:
                        print("El valor de su pasaje es de $", valor_pasaje_vip)
                        break
                    else:
                        print("Ingrese un asiento válido")
                aceptar_asiento=input("¿Acepta la compra de su asiento (si/no)?: ")
                if aceptar_asiento.lower()=="si":
                    if asiento==1:
                        asiento_1.append(nombre)
                        asiento_1.append(rut)
                        asiento_1.append(telefono)
                        asiento_1.append(banco)
                        matriz[0][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==2:
                        asiento_2.append(nombre)
                        asiento_2.append(rut)
                        asiento_2.append(telefono)
                        asiento_2.append(banco)
                        matriz[0][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==3:
                        asiento_3.append(nombre)
                        asiento_3.append(rut)
                        asiento_3.append(telefono)
                        asiento_3.append(banco)
                        matriz[0][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==4:
                        asiento_4.append(nombre)
                        asiento_4.append(rut)
                        asiento_4.append(telefono)
                        asiento_4.append(banco)
                        matriz[1][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==5:
                        asiento_5.append(nombre)
                        asiento_5.append(rut)
                        asiento_5.append(telefono)
                        asiento_5.append(banco)
                        matriz[1][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==6:
                        asiento_6.append(nombre)
                        asiento_6.append(rut)
                        asiento_6.append(telefono)
                        asiento_6.append(banco)
                        matriz[1][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==7:
                        asiento_7.append(nombre)
                        asiento_7.append(rut)
                        asiento_7.append(telefono)
                        asiento_7.append(banco)
                        matriz[2][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==8:
                        asiento_8.append(nombre)
                        asiento_8.append(rut)
                        asiento_8.append(telefono)
                        asiento_8.append(banco)
                        matriz[2][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==9:
                        asiento_9.append(nombre)
                        asiento_9.append(rut)
                        asiento_9.append(telefono)
                        asiento_9.append(banco)
                        matriz[2][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==10:
                        asiento_10.append(nombre)
                        asiento_10.append(rut)
                        asiento_10.append(telefono)
                        asiento_10.append(banco)
                        matriz[3][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==11:
                        asiento_11.append(nombre)
                        asiento_11.append(rut)
                        asiento_11.append(telefono)
                        asiento_11.append(banco)
                        matriz[3][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==12:
                        asiento_12.append(nombre)
                        asiento_12.append(rut)
                        asiento_12.append(telefono)
                        asiento_12.append(banco)
                        matriz[3][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==13:
                        asiento_13.append(nombre)
                        asiento_13.append(rut)
                        asiento_13.append(telefono)
                        asiento_13.append(banco)
                        matriz[4][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==14:
                        asiento_14.append(nombre)
                        asiento_14.append(rut)
                        asiento_14.append(telefono)
                        asiento_14.append(banco)
                        matriz[4][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==15:
                        asiento_15.append(nombre)
                        asiento_15.append(rut)
                        asiento_15.append(telefono)
                        asiento_15.append(banco)
                        matriz[4][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==16:
                        asiento_16.append(nombre)
                        asiento_16.append(rut)
                        asiento_16.append(telefono)
                        asiento_16.append(banco)
                        matriz[5][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==17:
                        asiento_17.append(nombre)
                        asiento_17.append(rut)
                        asiento_17.append(telefono)
                        asiento_17.append(banco)
                        matriz[5][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==18:
                        asiento_18.append(nombre)
                        asiento_18.append(rut)
                        asiento_18.append(telefono)
                        asiento_18.append(banco)
                        matriz[5][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==19:
                        asiento_19.append(nombre)
                        asiento_19.append(rut)
                        asiento_19.append(telefono)
                        asiento_19.append(banco)
                        matriz[6][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==20:
                        asiento_20.append(nombre)
                        asiento_20.append(rut)
                        asiento_20.append(telefono)
                        asiento_20.append(banco)
                        matriz[6][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==21:
                        asiento_21.append(nombre)
                        asiento_21.append(rut)
                        asiento_21.append(telefono)
                        asiento_21.append(banco)
                        matriz[6][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==22:
                        asiento_22.append(nombre)
                        asiento_22.append(rut)
                        asiento_22.append(telefono)
                        asiento_22.append(banco)
                        matriz[7][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==23:
                        asiento_23.append(nombre)
                        asiento_23.append(rut)
                        asiento_23.append(telefono)
                        asiento_23.append(banco)
                        matriz[7][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==24:
                        asiento_24.append(nombre)
                        asiento_24.append(rut)
                        asiento_24.append(telefono)
                        asiento_24.append(banco)
                        matriz[7][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==25:
                        asiento_25.append(nombre)
                        asiento_25.append(rut)
                        asiento_25.append(telefono)
                        asiento_25.append(banco)
                        matriz[8][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==26:
                        asiento_26.append(nombre)
                        asiento_26.append(rut)
                        asiento_26.append(telefono)
                        asiento_26.append(banco)
                        matriz[8][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==27:
                        asiento_27.append(nombre)
                        asiento_27.append(rut)
                        asiento_27.append(telefono)
                        asiento_27.append(banco)
                        matriz[8][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==28:
                        asiento_28.append(nombre)
                        asiento_28.append(rut)
                        asiento_28.append(telefono)
                        asiento_28.append(banco)
                        matriz[9][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==29:
                        asiento_29.append(nombre)
                        asiento_29.append(rut)
                        asiento_29.append(telefono)
                        asiento_29.append(banco)
                        matriz[9][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==30:
                        asiento_30.append(nombre)
                        asiento_30.append(rut)
                        asiento_30.append(telefono)
                        asiento_30.append(banco)
                        matriz[9][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==31:
                        asiento_31.append(nombre)
                        asiento_31.append(rut)
                        asiento_31.append(telefono)
                        asiento_31.append(banco)
                        matriz[10][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==32:
                        asiento_32.append(nombre)
                        asiento_32.append(rut)
                        asiento_32.append(telefono)
                        asiento_32.append(banco)
                        matriz[10][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==33:
                        asiento_33.append(nombre)
                        asiento_33.append(rut)
                        asiento_33.append(telefono)
                        asiento_33.append(banco)
                        matriz[10][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==34:
                        asiento_34.append(nombre)
                        asiento_34.append(rut)
                        asiento_34.append(telefono)
                        asiento_34.append(banco)
                        matriz[11][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==35:
                        asiento_35.append(nombre)
                        asiento_35.append(rut)
                        asiento_35.append(telefono)
                        asiento_35.append(banco)
                        matriz[11][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==36:
                        asiento_36.append(nombre)
                        asiento_36.append(rut)
                        asiento_36.append(telefono)
                        asiento_36.append(banco)
                        matriz[11][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==37:
                        asiento_37.append(nombre)
                        asiento_37.append(rut)
                        asiento_37.append(telefono)
                        asiento_37.append(banco)
                        matriz[12][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==38:
                        asiento_38.append(nombre)
                        asiento_38.append(rut)
                        asiento_38.append(telefono)
                        asiento_38.append(banco)
                        matriz[12][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==39:
                        asiento_39.append(nombre)
                        asiento_39.append(rut)
                        asiento_39.append(telefono)
                        asiento_39.append(banco)
                        matriz[12][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==40:
                        asiento_40.append(nombre)
                        asiento_40.append(rut)
                        asiento_40.append(telefono)
                        asiento_40.append(banco)
                        matriz[13][0]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==41:
                        asiento_41.append(nombre)
                        asiento_41.append(rut)
                        asiento_41.append(telefono)
                        asiento_41.append(banco)
                        matriz[13][1]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    elif asiento==42:
                        asiento_42.append(nombre)
                        asiento_42.append(rut)
                        asiento_42.append(telefono)
                        asiento_42.append(banco)
                        matriz[13][2]="x"
                        print("Se ha completado la compra del pasaje")
                        break
                    else:
                        print("Ingrese un asiento válido")
                else:
                    print("Se ha cancelado la compra del pasaje")
                    break
            except ValueError:
                break
        
    except ValueError:
        print("ingrese dato valido")
def anular_asiento(matriz,asiento_1,asiento_2,asiento_3,asiento_4,asiento_5,asiento_6,asiento_7,asiento_8,asiento_9,asiento_10,asiento_11,asiento_12,asiento_13,asiento_14,asiento_15,asiento_16,asiento_17,asiento_18,asiento_19,asiento_20,asiento_21,asiento_22,asiento_23,asiento_24,asiento_25,asiento_26,asiento_27,asiento_28,asiento_29,asiento_30,asiento_31,asiento_32,asiento_33,asiento_34,asiento_35,asiento_36,asiento_37,asiento_38,asiento_39,asiento_40,asiento_41,asiento_42):
    while True:
        try:
            asiento_anular=int(input("Ingrese su numero de asiento o x para volver al menú: "))
            rut_anular=input("Ingrese su rut: ")
        except ValueError:
            break
        if asiento_anular==1:
            for i in asiento_1:
                if (i)==rut_anular:
                    asiento_1=[]
                    matriz[0][0]=1
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==2:
            for i in asiento_2:
                if(i)==rut_anular:
                    asiento_2=[]
                    matriz[0][1]=2
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==3:
            for i in asiento_3:
                if (i)==rut_anular:
                    asiento_3=[]
                    matriz[0][2]=3
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==4:
            for i in asiento_4:
                if(i)==rut_anular:
                    asiento_4=[]
                    matriz[1][0]=4
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==5:
            for i in asiento_5:
                if(i)==rut_anular:
                    asiento_5=[]
                    matriz[1][1]=5
                    print("El pasaje se ha anulado correctamente")  
            break  
        elif asiento_anular==6:
            for i in asiento_6:
                if(i)==rut_anular:
                    asiento_6=[]
                    matriz[1][2]=6
                    print("El pasaje se ha anulado correctamente")
            break  
        elif asiento_anular==7:
            for i in asiento_7:
                if(i)==rut_anular:
                    asiento_7=[]
                    matriz[2][0]=7 
                    print("El pasaje se ha anulado correctamente")
            break                          
        elif asiento_anular==8:
            for i in asiento_8:
                if(i)==rut_anular:
                    asiento_8=[]
                    matriz[2][1]=8
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==9:
            for i in asiento_9:
                if(i)==rut_anular:
                    asiento_9=[]
                    matriz[2][2]=9 
                    print("El pasaje se ha anulado correctamente")
            break           
        elif asiento_anular==10:
            for i in asiento_10:
                if(i)==rut_anular:
                    asiento_10=[]
                    matriz[3][0]=10
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==11:
            for i in asiento_11:
                if(i)==rut_anular:
                    asiento_11=[]
                    matriz[3][1]=11
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==12:
            for i in asiento_12:
                if(i)==rut_anular:
                    asiento_12=[]
                    matriz[3][2]=12
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==13:
            for i in asiento_13:
                if(i)==rut_anular:
                    asiento_13=[]
                    matriz[4][0]=13
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==14:
            for i in asiento_14:
                if(i)==rut_anular:
                    asiento_14=[]
                    matriz[4][1]=14
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==15:
            for i in asiento_15:
                if(i)==rut_anular:
                    asiento_15=[]
                    matriz[4][2]=15
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==16:
            for i in asiento_16:
                if(i)==rut_anular:
                    asiento_16=[]
                    matriz[5][0]=16
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==17:
            for i in asiento_17:
                if(i)==rut_anular:
                    asiento_17=[]
                    matriz[5][1]=17
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==18:
            for i in asiento_18:
                if(i)==rut_anular:
                    asiento_18=[]
                    matriz[5][2]=18
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==19:
            for i in asiento_19:
                if(i)==rut_anular:
                    asiento_19=[]
                    matriz[6][0]=19
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==20:
            for i in asiento_20:
                if(i)==rut_anular:
                    asiento_20=[]
                    matriz[6][1]=20
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==21:
            for i in asiento_21:
                if(i)==rut_anular:
                    asiento_21=[]
                    matriz[6][2]=21
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==4:
            for i in asiento_22:
                if(i)==rut_anular:
                    asiento_22=[]
                    matriz[7][0]=22
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==23:
            for i in asiento_23:
                if(i)==rut_anular:
                    asiento_23=[]
                    matriz[7][1]=23
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==24:
            for i in asiento_24:
                if(i)==rut_anular:
                    asiento_24=[]
                    matriz[7][2]=24
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==25:
            for i in asiento_25:
                if(i)==rut_anular:
                    asiento_25=[]
                    matriz[8][0]=25
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==26:
            for i in asiento_26:
                if(i)==rut_anular:
                    asiento_26=[]
                    matriz[8][1]=26
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==27:
            for i in asiento_27:
                if(i)==rut_anular:
                    asiento_27=[]
                    matriz[8][2]=27
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==28:
            for i in asiento_28:
                if(i)==rut_anular:
                    asiento_28=[]
                    matriz[9][0]=28
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==29:
            for i in asiento_29:
                if(i)==rut_anular:
                    asiento_29=[]
                    matriz[9][1]=29
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==30:
            for i in asiento_30:
                if(i)==rut_anular:
                    asiento_30=[]
                    matriz[9][2]=30
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==31:
            for i in asiento_31:
                if(i)==rut_anular:
                    asiento_31=[]
                    matriz[10][0]=31
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==32:
            for i in asiento_32:
                if(i)==rut_anular:
                    asiento_32=[]
                    matriz[10][1]=32
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==33:
            for i in asiento_33:
                if(i)==rut_anular:
                    asiento_33=[]
                    matriz[10][2]=33
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==34:
            for i in asiento_34:
                if(i)==rut_anular:
                    asiento_34=[]
                    matriz[11][0]=34
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==35:
            for i in asiento_35:
                if(i)==rut_anular:
                    asiento_35=[]
                    matriz[11][1]=35
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==36:
            for i in asiento_36:
                if(i)==rut_anular:
                    asiento_36=[]
                    matriz[11][2]=36
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==37:
            for i in asiento_37:
                if(i)==rut_anular:
                    asiento_37=[]
                    matriz[12][0]=37
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==38:
            for i in asiento_38:
                if(i)==rut_anular:
                    asiento_38=[]
                    matriz[12][1]=38
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==39:
            for i in asiento_39:
                if(i)==rut_anular:
                    asiento_39=[]
                    matriz[12][2]=39
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==40:
            for i in asiento_40:
                if(i)==rut_anular:
                    asiento_40=[]
                    matriz[13][0]=40
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==41:
            for i in asiento_41:
                if(i)==rut_anular:
                    asiento_41=[]
                    matriz[13][1]=41
                    print("El pasaje se ha anulado correctamente")
            break
        elif asiento_anular==42:
            for i in asiento_42:
                if(i)==rut_anular:
                    asiento_42=[]
                    matriz[13][2]=42
                    print("El pasaje se ha anulado correctamente")
            break
        else:
            print("El rut o asiento no coinciden")
def cambiar_datos_usuario(asiento_1,asiento_2,asiento_3,asiento_4,asiento_5,asiento_6,asiento_7,asiento_8,asiento_9,asiento_10,asiento_11,asiento_12,asiento_13,asiento_14,asiento_15,asiento_16,asiento_17,asiento_18,asiento_19,asiento_20,asiento_21,asiento_22,asiento_23,asiento_24,asiento_25,asiento_26,asiento_27,asiento_28,asiento_29,asiento_30,asiento_31,asiento_32,asiento_33,asiento_34,asiento_35,asiento_36,asiento_37,asiento_38,asiento_39,asiento_40,asiento_41,asiento_42):
    while True:
        try:
            asiento_cambiar=int(input("Ingrese su numero de asiento o x para volver al menú: "))
            rut_cambiar=input("Ingrese su rut: ")
            if asiento_cambiar==1:
                for i in asiento_1:
                    if (i)==rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_1[0]= nombre
                        asiento_1[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar==2:
                for i in asiento_2:
                    if(i)==rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_2[0]= nombre
                        asiento_2[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 3:
                for i in asiento_3:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_3[0]= nombre
                        asiento_3[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 4:
                for i in asiento_4:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_4[0]= nombre
                        asiento_4[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 5:
                for i in asiento_5:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_5[0]= nombre
                        asiento_5[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 6:
                for i in asiento_6:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_6[0]= nombre
                        asiento_6[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 7:
                for i in asiento_7:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_7[0]= nombre
                        asiento_7[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 8:
                for i in asiento_8:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_8[0]= nombre
                        asiento_8[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 9:
                for i in asiento_9:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_9[0]= nombre
                        asiento_9[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 10:
                for i in asiento_10:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_10[0]= nombre
                        asiento_10[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 11:
                for i in asiento_11:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_11[0]= nombre
                        asiento_11[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 12:
                for i in asiento_12:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_12[0]= nombre
                        asiento_12[2]= telefono 
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 13:
                for i in asiento_13:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_13[0]= nombre
                        asiento_13[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 14:
                for i in asiento_14:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_14[0]= nombre
                        asiento_14[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 15:
                for i in asiento_15:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_15[0]= nombre
                        asiento_15[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 16:
                for i in asiento_16:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_16[0]= nombre
                        asiento_16[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 17:
                for i in asiento_17:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_17[0]= nombre
                        asiento_17[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 18:
                for i in asiento_18:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_18[0]= nombre
                        asiento_18[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 19:
                for i in asiento_19:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_19[0]= nombre
                        asiento_19[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 20:
                for i in asiento_20:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_20[0]= nombre
                        asiento_20[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 21:
                for i in asiento_21:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_21[0]= nombre
                        asiento_21[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 22:
                for i in asiento_22:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_22[0]= nombre
                        asiento_22[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 23:
                for i in asiento_23:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_23[0]= nombre
                        asiento_23[2]= telefono 
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 24:
                for i in asiento_24:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_24[0]= nombre
                        asiento_24[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 20:
                for i in asiento_25:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_25[0]= nombre
                        asiento_25[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 26:
                for i in asiento_26:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_26[0]= nombre
                        asiento_26[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 27:
                for i in asiento_27:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_27[0]= nombre
                        asiento_27[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 28:
                for i in asiento_28:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_28[0]= nombre
                        asiento_28[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 29:
                for i in asiento_29:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_29[0]= nombre
                        asiento_29[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 30:
                for i in asiento_30:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_30[0]= nombre
                        asiento_30[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 31:
                for i in asiento_31:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_31[0]= nombre
                        asiento_31[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 32:
                for i in asiento_32:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_32[0]= nombre
                        asiento_32[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 33:
                for i in asiento_33:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_33[0]= nombre
                        asiento_33[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 34:
                for i in asiento_34:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_34[0]= nombre
                        asiento_34[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 35:
                for i in asiento_35:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_35[0]= nombre
                        asiento_35[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 36:
                for i in asiento_36:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_36[0]= nombre
                        asiento_36[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 37:
                for i in asiento_37:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_37[0]= nombre
                        asiento_37[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 38:
                for i in asiento_38:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_38[0]= nombre
                        asiento_38[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 39:
                for i in asiento_39:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_39[0]= nombre
                        asiento_39[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 40:
                for i in asiento_40:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_40[0]= nombre
                        asiento_40[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 41:
                for i in asiento_41:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_41[0]= nombre
                        asiento_41[2]= telefono
                        print("Datos cambiados exitosamente")
            elif asiento_cambiar == 42:
                for i in asiento_42:
                    if (i) == rut_cambiar:
                        nombre=input("Ingrese su cambio de nombre: ")
                        telefono=input("Ingrese su cambio de telefono: ")
                        asiento_42[0]= nombre
                        asiento_42[2]= telefono
                        print("Datos cambiados exitosamente")
            else:
                print("Asiento inválido")
        except:
            break