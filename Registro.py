from Datos import *



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
    
        
            
        
            
        
            
            
            
            
            
            
            
            
        
        

    
    
    

