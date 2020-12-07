import tkinter as tk
from tkinter import *
from tkinter.messagebox import *

from sympy import symbols
import scipy.integrate as integrate
from scipy.integrate import simps
import numpy as np
import matplotlib.pyplot as plt
import sympy

from numpy import linspace
from sympy import lambdify

import matplotlib.pyplot as mpl

raiz = tk.Tk() 
raiz.title("Caso No.3: viga simplemente apoyada con fuerza puntual F genérica") #Cambiar el nombre de la ventana 
raiz.geometry("820x680") #Configurar
raiz.config(bg="#856ff8") #Cambiar color de fondo
imagen=tk.PhotoImage(file="caso_no3.png")
fondo=tk.Label(raiz,image=imagen).place(x=260, y=20) # Posición de la imagen
raiz.resizable(0,0) # No permite maximizar la ventana o ajustar el tamaño de la ventana    

lbl = tk.Label(raiz, font=("Comic", 12), text="¿Cuál es la longitud de la viga en metros?")
lbl.grid(column=71, row=72)
lbl.place(relx = 0.50, rely = 0.40, anchor = 'center') 

lbla = tk.Label(raiz, font=("Comic", 12), text="¿Cuál es la longitud (a) sobre la viga en metros (Véase la figura)?")
lbla.grid(column=71, row=72)
lbla.place(relx = 0.50, rely = 0.50, anchor = 'center')

lblb = tk.Label(raiz, font=("Comic", 12), text="El valor de la longitud (b) sobre la viga en metros (Véase la figura) es:")
lblb.grid(column=71, row=72)
lblb.place(relx = 0.50, rely = 0.60, anchor = 'center') 

txt_long = tk.Entry(raiz, width=10, font=("Comic", 12))
txt_long.grid(column=1, row=0)
txt_long.place(relx = 0.34, rely = 0.45, anchor = 'center')

txt_long_a = tk.Entry(raiz, width=10, font=("Comic", 12))
txt_long_a.grid(column=1, row=0)
txt_long_a.place(relx = 0.34, rely = 0.55, anchor = 'center')

lbl_2 = tk.Label(raiz, font=("Comic", 12), text="¿Cuál es el valor de la fuerza en kN?")
lbl_2.grid(column=71, row=72)
lbl_2.place(relx = 0.48, rely = 0.70, anchor = 'center') 

txt_fuerza = tk.Entry(raiz, width=10, font=("Comic", 12))
txt_fuerza.grid(column=1, row=0)
txt_fuerza.place(relx = 0.34, rely = 0.75, anchor = 'center')

lbl_3 = tk.Label(raiz, font=("Comic", 12), text="¿Cuál es el valor del producto E*I?")
lbl_3.grid(column=71, row=72)
lbl_3.place(relx = 0.48, rely = 0.80, anchor = 'center') 

txt_EI = tk.Entry(raiz, width=10, font=("Comic", 12))
txt_EI.grid(column=1, row=0)
txt_EI.place(relx = 0.34, rely = 0.85, anchor = 'center')

lon = StringVar()

def mostrar_longitud():
    longitud = float(txt_long.get())
    lon.set(longitud)

lon_a = StringVar()

def mostrar_longitud_a():
    longitud_a = float(txt_long_a.get())
    lon_a.set(longitud_a)

val_long_b = StringVar()

def mostrar_longitud_b():
    longitud = float(txt_long.get())
    longitud_a = float(txt_long_a.get())
    long_b = longitud - longitud_a
    val_long_b.set(long_b) 

val_fuerza = StringVar()

def mostrar_fuerza():
    fuerza = float(txt_fuerza.get())
    val_fuerza.set(fuerza) 

val_EI = StringVar()

def mostrar_EI():
    EI = float(txt_EI.get())
    val_EI.set(EI) 

val_reac_a = StringVar()

def calcula_reaccion_a():
    longitud = float(txt_long.get())
    longitud_a = float(txt_long_a.get())
    long_b = longitud - longitud_a
    fuerza = float(txt_fuerza.get())
    reac_a = (fuerza*long_b)/longitud
    val_reac_a.set(reac_a)

val_reac_b = StringVar()

def calcula_reaccion_b():
    longitud = float(txt_long.get())
    longitud_a = float(txt_long_a.get())
    fuerza = float(txt_fuerza.get())
    reac_b = (fuerza*longitud_a)/longitud
    val_reac_b.set(reac_b)

cortante_v_ac = StringVar()

def calcula_cortante_v_ac():                                                                                                               
    longitud = float(txt_long.get())
    longitud_a = float(txt_long_a.get())
    long_b = longitud - longitud_a
    fuerza = float(txt_fuerza.get())
    cortantes_v_ac = (fuerza*long_b)/longitud
    cortante_v_ac.set(cortantes_v_ac)

cortante_v_cb = StringVar()   

def calcula_cortante_v_cb():
    longitud = float(txt_long.get())
    longitud_a = float(txt_long_a.get())
    fuerza = float(txt_fuerza.get())
    cortantes_v_cb = -(fuerza*longitud_a)/longitud
    cortante_v_cb.set(cortantes_v_cb)

def grafica_cortantes():
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    
    longitud = float(txt_long.get())
    fuerza = float(txt_fuerza.get())
    longitud_a = float(txt_long_a.get())
    long_b = longitud - longitud_a
    
    cortantes_v_ac = (fuerza*long_b)/longitud
    cortantes_v_cb = -(fuerza*longitud_a)/longitud 
  
    fig, ax = plt.subplots()
    
    x = np.linspace(0, longitud)
    y = np.piecewise(x, [(x <= longitud_a) & (x >= 0), (x <= longitud) & (x >= longitud_a)], [cortantes_v_ac, cortantes_v_cb])

    big_size = 28
    plt.rc('font', size=big_size)
    plt.rc('axes', titlesize=big_size) 
    plt.plot(x, y, linewidth = 8)
    plt.grid(True)
    plt.title("Gráfica de Esfuerzo Vs longitud")
    plt.xlabel("Longitud [m]")
    plt.ylabel("Esfuerzo [kN]")
    plt.show()

flectores_M_ac = StringVar()   

def calcula_mom_flectores_M_ac():                                                                                                               
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    longitud_a = float(txt_long_a.get())
    long_b = longitud - longitud_a
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    flector_M_ac = (fuerza*long_b*x)/longitud
    flectores_M_ac.set(flector_M_ac)

flectores_M_cb = StringVar()   

def calcula_mom_flectores_M_cb():                                                                                                               
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    longitud_a = float(txt_long_a.get())
    long_b = longitud - longitud_a
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    flector_M_cb = ((fuerza*longitud_a)/(longitud))*(longitud - x)
    flectores_M_cb.set(flector_M_cb)

def grafica_flectores():
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    longitud_a = float(txt_long_a.get())
    long_b = longitud - longitud_a
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)

    fig, ax = plt.subplots()
    
    x = np.linspace(0, longitud)
    y = np.piecewise(x, [(x <= longitud_a) & (x >= 0), (x <= longitud) & (x >= longitud_a)], [lambda x: (fuerza*long_b*x)/longitud, lambda x: ((fuerza*longitud_a)/(longitud))*(longitud - x)]) 
    
    big_size = 28
    plt.rc('font', size=big_size)
    plt.rc('axes', titlesize=big_size) 
    plt.plot(x, y, linewidth = 8)
    plt.grid(True)
    plt.title("Momento de flexion Vs longitud")
    plt.xlabel("Longitud [m]")
    plt.ylabel("Momento [KN*m]")
    plt.show()

giros_a = StringVar()   

def calcula_giros_a():
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    EI = float(txt_EI.get())
    giro = (7*fuerza*longitud**3)/(64*EI)
    giros_a.set(giro)

giros_b = StringVar() 

def calcula_giros_b():
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    EI = float(txt_EI.get())
    giro = -(fuerza*longitud**3)/(45*EI)
    giros_b.set(giro)

giros_c = StringVar() 

def calcula_giros_c():
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    EI = float(txt_EI.get())
    giro = -(fuerza*longitud**3)/(45*EI)
    giros_b.set(giro)

deformaciones_ac = StringVar()   

def calcula_deformaciones_ac():                                                                                                               
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    EI = float(txt_EI.get())
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    deformacion = ((fuerza*longitud**3*x)/(360*EI))*(7 - ((10*x**2)/(longitud**2)) + ((3*x**4)/(longitud**4)))
    deformaciones.set(deformacion)

deformaciones_cb = StringVar()   

def calcula_deformaciones_cb():                                                                                                               
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    EI = float(txt_EI.get())
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    deformacion = ((fuerza*longitud**3*x)/(360*EI))*(7 - ((10*x**2)/(longitud**2)) + ((3*x**4)/(longitud**4)))
    deformaciones.set(deformacion)

def grafica_deformaciones():
    fuerza = float(txt_fuerza.get())
    longitud = float(txt_long.get())
    EI = float(txt_EI.get())
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)

    fig, ax = plt.subplots()
    
    x = np.linspace(0, longitud)
    y = np.piecewise(x,[(x <= longitud) & (x >= 0)],[lambda x: ((fuerza*longitud**3*x)/(360*EI))*(7 - ((10*x**2)/(longitud**2)) + ((3*x**4)/(longitud**4)))]) 
    
    big_size = 28
    plt.rc('font', size=big_size)
    plt.rc('axes', titlesize=big_size) 
    plt.plot(x, y, linewidth = 8)
    plt.grid(True)
    plt.title("Gráfica de deformación Vs longitud")
    plt.xlabel("Longitud [m]")
    plt.ylabel("Deformación [m]")
    plt.show()


text_long = tk.Entry(raiz, justify="center", textvariable=lon, state="disabled").place(x=440, y=300)
text_long_a = tk.Entry(raiz, justify="center", textvariable=lon_a, state="disabled").place(x=440, y=368)
text_long_b = tk.Entry(raiz, justify="center", textvariable=val_long_b, state="disabled").place(x=440, y=435)
text_fuerza = tk.Entry(raiz, justify="center", textvariable=val_fuerza, state="disabled").place(x=440, y=500)
text_EI = tk.Entry(raiz, justify="center", textvariable=val_EI, state="disabled").place(x=440, y=572)

boton_long = tk.Button(raiz, text="Aceptar", command=mostrar_longitud).place(x=350, y=292)
boton_long_a = tk.Button(raiz, text="Aceptar", command=mostrar_longitud_a).place(x=350, y=360)
boton_long_b = tk.Button(raiz, text="Calcular", command=mostrar_longitud_b).place(x=350, y=428)
boton_fuerza = tk.Button(raiz, text="Aceptar", command=mostrar_fuerza).place(x=350, y=495)
boton_EI = tk.Button(raiz, text="Aceptar", command=mostrar_EI).place(x=350, y=566)

def ventana_calcular():
    		
    newWindow = tk.Toplevel(raiz)

    newWindow.title("Solución: Ventana de resultados") #Cambiar el nombre de la ventana 
    newWindow.geometry("820x680") #Configurar
    newWindow.config(bg="#567ff9") #Cambiar color de fondo
    newWindow.resizable(0,0) # No permite maximizar la ventana o ajustar el tamaño de la ventana 

    lbl_n1 = tk.Label(newWindow, font=("Comic", 12), text="El valor de la reacción de A R_A en kN, es:")
    lbl_n1.grid(column=71, row=0)
    lbl_n1.place(relx = 0.48, rely = 0.04, anchor = 'center')  
    text_reaccion_a = tk.Entry(newWindow, justify="center", textvariable=val_reac_a, state="disabled").place(x=350, y=54)
    boton_reaccion_a = tk.Button(newWindow, text="Calcular", command=calcula_reaccion_a).place(x=260, y=50)

    lbl_n2 = tk.Label(newWindow, font=("Comic", 12), text="El valor de la reacción de B R_B en kN, es:")
    lbl_n2.grid(column=71, row=0)
    lbl_n2.place(relx = 0.48, rely = 0.15, anchor = 'center')  
    text_reaccion_b = tk.Entry(newWindow, justify="center", textvariable=val_reac_b, state="disabled").place(x=350, y=129)
    boton_reaccion_b = tk.Button(newWindow, text="Calcular", command=calcula_reaccion_b).place(x=260, y=125)

    lbl_n3 = tk.Label(newWindow, font=("Comic", 12), text="EL cortante V_AC en kN,  es:") 
    lbl_n3.grid(column=71, row=0)
    lbl_n3.place(relx = 0.48, rely = 0.26, anchor = 'center')
    text_cortante_v_ac = tk.Entry(newWindow, justify="center", textvariable=cortante_v_ac, state="disabled").place(x=350, y=205)
    boton_cortante_v_ac = tk.Button(newWindow, text="Calcular", command=calcula_cortante_v_ac).place(x=260, y=200)
 
    lbl_n4 = tk.Label(newWindow, font=("Comic", 12), text="El valor del cortante V_CB en kN, es:") 
    lbl_n4.grid(column=71, row=0)
    lbl_n4.place(relx = 0.48, rely = 0.37, anchor = 'center')
    text_cortante_v_cb = tk.Entry(newWindow, justify="center", textvariable=cortante_v_cb, state="disabled").place(x=350, y=280)
    boton_cortante_v_cb = tk.Button(newWindow, text="Calcular", command=calcula_cortante_v_cb).place(x=260, y=275)
    boton_cortantes_grafica = tk.Button(newWindow, text="Graficar", command=grafica_cortantes).place(x=530, y=275)
	
    lbl_n5 = tk.Label(newWindow, font=("Comic", 12), text="La función de los flectores M_AC y M_CB en kN*m, es:") 
    lbl_n5.grid(column=71, row=0)
    lbl_n5.place(relx = 0.48, rely = 0.48, anchor = 'center')
    text_flectores_M_AC = tk.Entry(newWindow, justify="center", textvariable=flectores_M_ac, state="disabled").place(x=200, y=356)
    boton_flectores_M_AC = tk.Button(newWindow, text="Calcular M_AC", command=calcula_mom_flectores_M_ac).place(x=80, y=350)
    text_flectores_M_CB = tk.Entry(newWindow, justify="center", textvariable=flectores_M_cb, state="disabled").place(x=505, y=356)
    boton_flectores_M_CB = tk.Button(newWindow, text="Calcular M_CB", command=calcula_mom_flectores_M_cb).place(x=380, y=350)
    boton_flectores_grafica = tk.Button(newWindow, text="Graficar", command=grafica_flectores).place(x=680, y=350)

    lbl_n6 = tk.Label(newWindow, font=("Comic", 12), text="La función de las deformaciones y_AC y y_CB en m, es:") 	
    lbl_n6.grid(column=71, row=0)
    lbl_n6.place(relx = 0.48, rely = 0.59, anchor = 'center')
    boton_deformaciones_y_AC = tk.Button(newWindow, text="Calcular y_AC", command=calcula_deformaciones_ac).place(x=80, y=428)
    text_deformaciones_y_AC = tk.Entry(newWindow, justify="center", textvariable=deformaciones_ac, state="disabled").place(x=200, y=436)
    boton_deformaciones_y_CB = tk.Button(newWindow, text="Calcular y_CB", command=calcula_deformaciones_cb).place(x=380, y=428)
    text_deformaciones_y_CB = tk.Entry(newWindow, justify="center", textvariable=deformaciones_cb, state="disabled").place(x=505, y=434)
    boton_deformaciones_grafica = tk.Button(newWindow, text="Graficar", command=grafica_deformaciones).place(x=680, y=428)

    lbl_n7 = tk.Label(newWindow, font=("Comic", 12), text="La función de los giros φ_A, es:") 	
    lbl_n7.grid(column=71, row=0)
    lbl_n7.place(relx = 0.28, rely = 0.71, anchor = 'center')    
    text_giros_a = tk.Entry(newWindow, justify="center", textvariable=giros_a, state="disabled").place(x=200, y=510)
    boton_giros_a = tk.Button(newWindow, text="Calcular φ_A", command=calcula_giros_a).place(x=80, y=505)

    lbl_n8 = tk.Label(newWindow, font=("Comic", 12), text="La función de los giros φ_B, es:") 	
    lbl_n8.grid(column=71, row=0)
    lbl_n8.place(relx = 0.62, rely = 0.71, anchor = 'center')    
    text_giros_b = tk.Entry(newWindow, justify="center", textvariable=giros_b, state="disabled").place(x=505, y=510)
    boton_giros_b = tk.Button(newWindow, text="Calcular φ_B", command=calcula_giros_b).place(x=380, y=502)

    lbl_n9 = tk.Label(newWindow, font=("Comic", 12), text="La función de los giros φ_C, es:") 	
    lbl_n9.grid(column=71, row=0)
    lbl_n9.place(relx = 0.47, rely = 0.82, anchor = 'center')    
    text_giros_C = tk.Entry(newWindow, justify="center", textvariable=giros_b, state="disabled").place(x=370, y=586)
    boton_giros_C = tk.Button(newWindow, text="Calcular φ_C", command=calcula_giros_b).place(x=250, y=580)

button_calcular = tk.Button(raiz, text="Calcular",command=ventana_calcular, height = 2, width = 5, font=("Comic", 14)).place(x=346, y=615)

raiz.mainloop()
