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
                        6. Nitritos
                        7.Metales
                        8. Fosfatos
                        9.Salir
                        """)
    print(Menu_Variables)
    Cantidad_Variables = int(input("Inrese la cantidad de Variables"))
    for i in range(Cantidad_Variables):
        ingreso_Variables = int(input('Ingrese el numero de Variable Por ejemplo 1 Para DBO:  '))
        if ingreso_Variables == 1:
            if Residual[Codigo_Muestra].get("DB0",None) ==None:
                Residual[Codigo_Muestra]["DB0"]={}
                guardar_datos(Ruta_JSON_Resultados_Residual,Residual)
            else:
                print("Variable ya Registrada No puede sobre escribri")
                continue
            
                
                
            
       
            
            
            
            
            
        
        
        
    
        
    
        

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
    
        
            
        
            
        
            
            
            
            
            
            
            
            
        
        

    
    
    

