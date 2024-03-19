#Un consultorio medioc requiere llevar un registro de la asistencia dde personas en las diferentes especialidades 
#odontologia,ginecologia,consulta general,maternidad,infancia

import os

odontolgia=0
ginecologia=0
consultageneral=0
maternidad=0
infancia = 0
controlbln=True

def fnt_pantalla():
    os.system('cls')
def fnt_selector(op):
    
    global odontolgia
    global ginecologia
    global consultageneral
    global maternidad
    global infancia

    if(op==1):
        odontolgia += 1
    if (op==2):
        ginecologia += 1
    if (op==3):
        consultageneral+= 1
    if (op==4):
        maternidad += 1
    if (op==5):
        infancia += 1
    

def fnt_reporte():
    
    print('Asistencia de Odontologia------------------>',odontolgia)
    print('Asistencia de Ginecologia------------------>',ginecologia)
    print('Asistencia de Consulta General------------->',consultageneral)
    print('Asistencia de Maternidad------------------->',maternidad)
    print('Asistencia de Infancia--------------------->',infancia)
    input('Enter para continuar')
controlbln=True
while controlbln == True:
    fnt_pantalla()
    
    op=int(input('''Seleccione la especialidad a la que desea acceder:\n1. Odontología.\n2. Ginecología.\n3. Consulta General.\n4.Maternidad\n5.Infancia\n6.Reporte\n7.Salir------------>'''))
    
 
    
    
        
    if op==7:
        controlbln=False
         
           
    elif op==1:
        
        fnt_selector(op)
    elif op==2:
        
        fnt_selector(op)
    elif op==3:
        
        fnt_selector(op)
    elif op==4:
        
        fnt_selector(op)
    elif op==5:
        
        fnt_selector(op)
    elif op==6:
        fnt_reporte()
        
    
    

    
           
        
