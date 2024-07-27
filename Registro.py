from Datos import *


def ingreso_Muestra():
    cargar_datos(Ruta_JSON_Resultados_Residual,Residual)
    print("Recuerde que el codigo de muestrra no puede tener infop ligada al cliente")
    Codigo_Muestra = (input("Ingrese el Codigo de muestra"))
    Residual[Codigo_Muestra]={}
    guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
    return

def ingreso_Variables():
    cargar_datos(Ruta_JSON_Resultados_Residual,Residual)
    Codigo_Muestra = (input("Ingrese el Codigo de muestra"))
    if Codigo_Muestra not in Residual:
        print("Codigo de Variable no Registrado")
        return
    print("Cada muestra tiene X cantidad de Variables indique cunatas Variables va ingresar")
    Menu_Variables = ("""
                        1. DBO
                        2. DQO 
                        3. Solidos
                        4. Nitrogeno Kendal
                        5. Nitratos
                        6. Fosfatos
                        7. Metales
                        8. Nitritos
                        9. Salir
                        """)
    print(Menu_Variables)
    while True:
        ingreso_Variables = int(input('Ingrese el numero de Variable Por ejemplo 1 Para DBO:  '))
        if ingreso_Variables == 1:
            if Residual[Codigo_Muestra].get("DB0",None) ==None:
                Residual[Codigo_Muestra]["DB0"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("*"*20)
                print("Variable ya Registrada No puede sobre escribri")
                print("*"*20)
                continue
        if ingreso_Variables == 2:
            if Residual[Codigo_Muestra].get("DQ0",None) ==None:
                Residual[Codigo_Muestra]["DQ0"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("*"*20)
                print("Variable ya Registrada No puede sobre escribri")
                print("*"*20)
                continue
        if ingreso_Variables == 3:
            if Residual[Codigo_Muestra].get("Solidos",None) ==None:
                Residual[Codigo_Muestra]["Solidos"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("*"*20)
                print("Variable ya Registrada No puede sobre escribri")
                print("*"*20)
                continue
        if ingreso_Variables == 4:
            if Residual[Codigo_Muestra].get("Nitrogeno Kendal",None) ==None:
                Residual[Codigo_Muestra]["Nitrogeno Kendal"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("*"*20)
                print("Variable ya Registrada No puede sobre escribri")
                print("*"*20)
                continue
        if ingreso_Variables == 5:
            if Residual[Codigo_Muestra].get("Nitratos",None) ==None:
                Residual[Codigo_Muestra]["Nitratos"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("*"*20)
                print("Variable ya Registrada No puede sobre escribri")
                print("*"*20)
                continue
        if ingreso_Variables == 6:
            if Residual[Codigo_Muestra].get("Metales",None) ==None:
                Residual[Codigo_Muestra]["Metales"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("*"*20)
                print("Variable ya Registrada No puede sobre escribri")
                print("*"*20)
                continue
        if ingreso_Variables == 7:
            if Residual[Codigo_Muestra].get("Fosfatos",None) ==None:
                Residual[Codigo_Muestra]["Fosfatos"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("*"*20)
                print("Variable ya Registrada No puede sobre escribri")
                print("*"*20)
                continue
        if ingreso_Variables == 8:
            if Residual[Codigo_Muestra].get("Nitritos",None) ==None:
                Residual[Codigo_Muestra]["Nitritos"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("*"*20)
                print("Variable ya Registrada No puede sobre escribri")
                print("*"*20)
                continue
        if ingreso_Variables == 9:
            break
                
            
                
                
            
       
            
            
            
            
            
        
        
        
    
        
    
        

ingreso_Variables()
    





def Reporte_Residual():
    cargar_datos(Ruta_JSON_Resultados_Residual,Residual)
    
    Id_Muestra = input("Ingrese el Id de la muestra:   ")
    Resultados_Articulo_8={}
    Resultados_Articulo_8["pH"] = input ("ingrese el pH:  ")
    Resultados_Articulo_8["Demanda_DBO"] = input (" Concentracion de DBO:   ")
    Resultados_Articulo_8[ "Demanda_DQO"] = input ("Concentracion de DQO:   ")
    Resultados_Articulo_8["Solidos_Suspendidos_Totlaes" ]= input ("Concentracion de solidos suspendidos totales:  ")
    Resultados_Articulo_8["Solidos_Sedimentables"] = input("Concentracion de solidos Sedimentables:   ")
    Resultados_Articulo_8["grases_aceites"]= input("Concentracion de Solidos totales:   ")
    Residual[Id_Muestra]= Resultados_Articulo_8
    guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
    
    
    
    

    
    
    
    
    
    

def Reportes():
    Pregunta_Reportes = (input(""""
                1- Reporte de Agua Residual
                2- Reporte para picsinas
                3- Reporte de Agua potable
                4-Reporte libre por variables
                """))
    


    
    
 
def Resgistro_Resultados ():
    cargar_datos(Ruta_JSON_Resultados,Resultados )
    Pregunta_1 = (input(""""
                1- Desea Generar un Nuevo Reporte 
                2- Salir a Menu Principal
                """))
    if Pregunta_1 == 2:
        return
    if Pregunta_1 ==1:
        Reportes()
        
        
    
    
    
    
    
    
    
    guardar_datos(Ruta_JSON_Resultados,Resultados )
    
        
            
        
            
        
            
            
            
            
            
            
            
            
        
        

    
    
    

