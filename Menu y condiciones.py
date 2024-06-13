import funciones_pasajes as FP
import csv
asiento_1=[]
asiento_2=[]
asiento_3=[]
asiento_4=[]
asiento_5=[]
asiento_6=[]
asiento_7=[]
asiento_8=[]
asiento_9=[]
asiento_10=[]
asiento_11=[]
asiento_12=[]
asiento_13=[]
asiento_14=[]
asiento_15=[]
asiento_16=[]
asiento_17=[]
asiento_18=[]
asiento_19=[]
asiento_20=[]
asiento_21=[]
asiento_22=[]
asiento_23=[]
asiento_24=[]
asiento_25=[]
asiento_26=[]
asiento_27=[]
asiento_28=[]
asiento_29=[]
asiento_30=[]
asiento_31=[]
asiento_32=[]
asiento_33=[]
asiento_34=[]
asiento_35=[]
asiento_36=[]
asiento_37=[]
asiento_38=[]
asiento_39=[]
asiento_40=[]
asiento_41=[]
asiento_42=[]
matriz=[
    [1,2,3],[4,5,6],
    [7,8,9],[10,11,12],
    [13,14,15],[16,17,18],
    [19,20,21],[22,23,24],
    [25,26,27],[28,29,30],
    [31,32,33],[34,35,36],
    [37,38,39],[40,41,42]
]
while True:
    try:
        print("Menu de usuario")
        print("===============")
        print("1. Ver asientos disponibles")
        print("2. Comprar asiento")
        print("3. Anular vuelo")
        print("4. Modificar datos de pasajero")
        print("5. Salir")
        opcion1=int(input("Ingrese opción: "))
        if opcion1 == 1:
            print(matriz[0][0],"",matriz[0][1],"",matriz[0][2],"         ",matriz[1][0],"",matriz[1][1],"",matriz[1][2])
            print(matriz[2][0],"",matriz[2][1],"",matriz[2][2],"         ",matriz[3][0],matriz[3][1],matriz[3][2])
            print(matriz[4][0],matriz[4][1], matriz[4][2],"        ",matriz[5][0],matriz[5][1],matriz[5][2])
            print(matriz[6][0],matriz[6][1], matriz[6][2],"        ",matriz[7][0],matriz[7][1],matriz[7][2])
            print(matriz[8][0],matriz[8][1], matriz[8][2],"        ",matriz[9][0],matriz[9][1],matriz[9][2])
            print("==========================")
            print(matriz[10][0],matriz[10][1], matriz[10][2],"        ",matriz[11][0],matriz[11][1],matriz[11][2])
            print(matriz[12][0],matriz[12][1], matriz[12][2],"        ",matriz[13][0],matriz[13][1],matriz[13][2])
        else:
            if opcion1 == 2:
                FP.comprar_asiento(matriz,asiento_1,asiento_2,asiento_3,asiento_4,asiento_5,asiento_6,asiento_7,asiento_8,asiento_9,asiento_10,asiento_11,asiento_12,asiento_13,asiento_14,asiento_15,asiento_16,asiento_17,asiento_18,asiento_19,asiento_20,asiento_21,asiento_22,asiento_23,asiento_24,asiento_25,asiento_26,asiento_27,asiento_28,asiento_29,asiento_30,asiento_31,asiento_32,asiento_33,asiento_34,asiento_35,asiento_36,asiento_37,asiento_38,asiento_39,asiento_40,asiento_41,asiento_42)
            else:
                if opcion1 == 3:
                    FP.anular_asiento(matriz,asiento_1,asiento_2,asiento_3,asiento_4,asiento_5,asiento_6,asiento_7,asiento_8,asiento_9,asiento_10,asiento_11,asiento_12,asiento_13,asiento_14,asiento_15,asiento_16,asiento_17,asiento_18,asiento_19,asiento_20,asiento_21,asiento_22,asiento_23,asiento_24,asiento_25,asiento_26,asiento_27,asiento_28,asiento_29,asiento_30,asiento_31,asiento_32,asiento_33,asiento_34,asiento_35,asiento_36,asiento_37,asiento_38,asiento_39,asiento_40,asiento_41,asiento_42)
                else:
                    if opcion1==4:
                        FP.cambiar_datos_usuario(asiento_1,asiento_2,asiento_3,asiento_4,asiento_5,asiento_6,asiento_7,asiento_8,asiento_9,asiento_10,asiento_11,asiento_12,asiento_13,asiento_14,asiento_15,asiento_16,asiento_17,asiento_18,asiento_19,asiento_20,asiento_21,asiento_22,asiento_23,asiento_24,asiento_25,asiento_26,asiento_27,asiento_28,asiento_29,asiento_30,asiento_31,asiento_32,asiento_33,asiento_34,asiento_35,asiento_36,asiento_37,asiento_38,asiento_39,asiento_40,asiento_41,asiento_42)
                    else:
                        if opcion1==5:
                            archivo=open("Datos_pasajeros.csv","w")
                            with open("Datos_pasajeros.csv","w",newline=""):
                                escritor=csv.writer(archivo)
                                escritor.writerow(["Nombre","Rut","Telefono","Banco"])
                                escritor.writerows([
                                    [asiento_1],
                                    [asiento_2],
                                    [asiento_3],
                                    [asiento_4],
                                    [asiento_5],
                                    [asiento_6],
                                    [asiento_7],
                                    [asiento_8],
                                    [asiento_9],
                                    [asiento_10],
                                    [asiento_11],
                                    [asiento_12],
                                    [asiento_13],
                                    [asiento_14],
                                    [asiento_15],
                                    [asiento_16],
                                    [asiento_17],
                                    [asiento_18],
                                    [asiento_19],
                                    [asiento_20],
                                    [asiento_21],
                                    [asiento_22],
                                    [asiento_23],
                                    [asiento_24],
                                    [asiento_25],
                                    [asiento_26],
                                    [asiento_27],
                                    [asiento_28],
                                    [asiento_29],
                                    [asiento_30],
                                    [asiento_31],
                                    [asiento_32],
                                    [asiento_33],
                                    [asiento_34],
                                    [asiento_35],
                                    [asiento_36],
                                    [asiento_37],
                                    [asiento_38],
                                    [asiento_39],
                                    [asiento_40],
                                    [asiento_41],
                                    [asiento_42]
                                ])
                                break              
    except ValueError:
        print("Ingrese dato válido")