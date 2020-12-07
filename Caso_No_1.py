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

raiz = tk.Tk() 
raiz.title("Caso No.1: viga simplemente apoyada con carga distribuida rectangular") #Cambiar el nombre de la ventana 
raiz.geometry("820x680") #Configurar
raiz.config(bg="#856ff8") #Cambiar color de fondo
imagen=tk.PhotoImage(file="foto_1.png")
fondo=tk.Label(raiz,image=imagen).place(x=220, y=20) # Posición de la imagen
raiz.resizable(0,0) # No permite maximizar la ventana o ajustar el tamaño de la ventana    

lbl = tk.Label(raiz, font=("Comic", 12), text="¿Cuál es la longitud de la viga en metros?")
lbl.grid(column=71, row=72)
lbl.place(relx = 0.48, rely = 0.40, anchor = 'center') 

txt_long = tk.Entry(raiz, width=10, font=("Comic", 12))
txt_long.grid(column=1, row=0)
txt_long.place(relx = 0.34, rely = 0.45, anchor = 'center')

lbl_2 = tk.Label(raiz, font=("Comic", 12), text="¿Cuál es el valor de la carga en kN/m?")
lbl_2.grid(column=71, row=72)
lbl_2.place(relx = 0.48, rely = 0.50, anchor = 'center') 

txt_carga = tk.Entry(raiz, width=10, font=("Comic", 12))
txt_carga.grid(column=1, row=0)
txt_carga.place(relx = 0.34, rely = 0.55, anchor = 'center')

lbl_3 = tk.Label(raiz, font=("Comic", 12), text="¿Cuál es el valor del producto E*I?")
lbl_3.grid(column=71, row=72)
lbl_3.place(relx = 0.48, rely = 0.60, anchor = 'center') 

txt_EI = tk.Entry(raiz, width=10, font=("Comic", 12))
txt_EI.grid(column=1, row=0)
txt_EI.place(relx = 0.34, rely = 0.65, anchor = 'center')

lon = StringVar()

def mostrar_longitud():
    longitud = float(txt_long.get())
    lon.set(longitud) 

val_carga = StringVar()

def mostrar_carga():
    carga = float(txt_carga.get())
    val_carga.set(carga) 

val_EI = StringVar()

def mostrar_EI():
    EI = float(txt_EI.get())
    val_EI.set(EI) 

val_centroide = StringVar()

def calcula_centroide():
    cen = float(txt_long.get())/2
    val_centroide.set(cen)

val_carga_puntual = StringVar()

def calcula_carga_puntualizada():
    carga = float(txt_carga.get())
    longitud = float(txt_long.get())
    carga_puntual = carga*longitud    
    val_carga_puntual.set(carga_puntual)

reacciones = StringVar()

def calcula_reacciones():                                                                                                               
    carga = float(txt_carga.get())
    longitud = float(txt_long.get())
    reaccion = carga*longitud/2
    reacciones.set(reaccion)

cortantes = StringVar()   

def calcula_cortantes():
    carga = float(txt_carga.get())
    longitud = float(txt_long.get())
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    cortante = carga*((longitud/2) - x) 
    cortantes.set(cortante)

def grafica_cortantes():
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    carga = float(txt_carga.get())
    longitud = float(txt_long.get())
    cortante = carga*((longitud/2) - x) 
    cortantes.set(cortante)

    fig, ax = plt.subplots()

    
    x = np.linspace(0, longitud)
    y = np.piecewise(x,[(x <= longitud) & (x >= 0)],[lambda x: carga*((longitud/2) - x)]) 
    
    big_size = 28
    plt.rc('font', size=big_size)
    plt.rc('axes', titlesize=big_size) 
    plt.plot(x, y, linewidth = 8)
    plt.grid(True)
    plt.title("Gráfica de Esfuerzo Vs longitud")
    plt.xlabel("Longitud [m]")
    plt.ylabel("Esfuerzo [kN]")
    plt.show()

flectores = StringVar()   

def calcula_mom_flectores():                                                                                                               
    carga = float(txt_carga.get())
    longitud = float(txt_long.get())
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    flector = ((carga*x)/2)*(longitud - x)
    flectores.set(flector)

def grafica_flectores():
    carga = float(txt_carga.get())
    longitud = float(txt_long.get())
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    flector = ((carga*x)/2)*(longitud - x)
    flectores.set(flector)

    fig, ax = plt.subplots()
    
    x = np.linspace(0, longitud)
    y = np.piecewise(x,[(x <= longitud) & (x >= 0)],[lambda x: ((carga*x)/2)*(longitud - x)]) 
    
    big_size = 28
    plt.rc('font', size=big_size)
    plt.rc('axes', titlesize=big_size) 
    plt.plot(x, y, linewidth = 8)
    plt.grid(True)
    plt.title("Momento de flexion Vs longitud")
    plt.xlabel("Longitud [m]")
    plt.ylabel("Momento [KN*m]")
    plt.show()

deformaciones = StringVar()   

def calcula_deformaciones():                                                                                                               
    carga = float(txt_carga.get())
    longitud = float(txt_long.get())
    EI = float(txt_EI.get())
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    deformacion = ((carga*x)/(24*EI))*(x**3 - (2*longitud*x**2) + longitud**3)
    deformaciones.set(deformacion)

def grafica_deformaciones():
    carga = float(txt_carga.get())
    longitud = float(txt_long.get())
    EI = float(txt_EI.get())
    x, y = symbols('x y')
    sympy.init_printing(use_unicode=True)
    deformacion = ((carga*x)/(24*EI))*(x**3 - (2*longitud*x**2) + longitud**3)
    deformaciones.set(deformacion)

    fig, ax = plt.subplots()
    
    x = np.linspace(0, longitud)
    y = np.piecewise(x,[(x <= longitud) & (x >= 0)],[lambda x: ((carga*x)/(24*EI))*(x**3 - (2*longitud*x**2) + longitud**3)]) 
    
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
text_carga = tk.Entry(raiz, justify="center", textvariable=val_carga, state="disabled").place(x=440, y=368)
text_EI = tk.Entry(raiz, justify="center", textvariable=val_EI, state="disabled").place(x=440, y=437)

boton_long = tk.Button(raiz, text="Aceptar", command=mostrar_longitud).place(x=350, y=292)
boton_carga = tk.Button(raiz, text="Aceptar", command=mostrar_carga).place(x=350, y=360)
boton_EI = tk.Button(raiz, text="Aceptar", command=mostrar_EI).place(x=350, y=428)

def ventana_calcular():
    		
    newWindow = tk.Toplevel(raiz)

    newWindow.title("Solución: Ventana de resultados") #Cambiar el nombre de la ventana 
    newWindow.geometry("820x680") #Configurar
    newWindow.config(bg="#567ff9") #Cambiar color de fondo
    newWindow.resizable(0,0) # No permite maximizar la ventana o ajustar el tamaño de la ventana 

    lbl_n1 = tk.Label(newWindow, font=("Comic", 12), text="El valor del centroide en x en m, es:")
    lbl_n1.grid(column=71, row=0)
    lbl_n1.place(relx = 0.48, rely = 0.04, anchor = 'center')  
    text_centroide = tk.Entry(newWindow, justify="center", textvariable=val_centroide, state="disabled").place(x=350, y=54)
    boton_centroide_cal = tk.Button(newWindow, text="Calcular", command=calcula_centroide).place(x=260, y=50)

    lbl_n2 = tk.Label(newWindow, font=("Comic", 12), text="La carga puntualizada en kN, es:")
    lbl_n2.grid(column=71, row=0)
    lbl_n2.place(relx = 0.48, rely = 0.15, anchor = 'center')  
    text_carga_puntual = tk.Entry(newWindow, justify="center", textvariable=val_carga_puntual, state="disabled").place(x=350, y=129)
    boton_carga_puntual = tk.Button(newWindow, text="Calcular", command=calcula_carga_puntualizada).place(x=260, y=125)

    lbl_n3 = tk.Label(newWindow, font=("Comic", 12), text="La reacción en kN de R_A=R_b, es:") 
    lbl_n3.grid(column=71, row=0)
    lbl_n3.place(relx = 0.48, rely = 0.26, anchor = 'center')
    text_reacciones = tk.Entry(newWindow, justify="center", textvariable=reacciones, state="disabled").place(x=350, y=205)
    boton_reacciones = tk.Button(newWindow, text="Calcular", command=calcula_reacciones).place(x=260, y=200)
 
    lbl_n4 = tk.Label(newWindow, font=("Comic", 12), text="La función de los cortantes V_AB en kN, es:") 
    lbl_n4.grid(column=71, row=0)
    lbl_n4.place(relx = 0.48, rely = 0.37, anchor = 'center')
    text_cortantes = tk.Entry(newWindow, justify="center", textvariable=cortantes, state="disabled").place(x=350, y=280)
    boton_cortantes = tk.Button(newWindow, text="Calcular", command=calcula_cortantes).place(x=260, y=275)
    boton_cortantes_grafica = tk.Button(newWindow, text="Graficar", command=grafica_cortantes).place(x=530, y=275)
	
    lbl_n5 = tk.Label(newWindow, font=("Comic", 12), text="La función de los flectores M_AB en kN*m, es:") 
    lbl_n5.grid(column=71, row=0)
    lbl_n5.place(relx = 0.48, rely = 0.48, anchor = 'center')
    text_flectores = tk.Entry(newWindow, justify="center", textvariable=flectores, state="disabled").place(x=350, y=356)
    boton_flectores = tk.Button(newWindow, text="Calcular", command=calcula_mom_flectores).place(x=260, y=350)
    boton_flectores_grafica = tk.Button(newWindow, text="Graficar", command=grafica_flectores).place(x=530, y=350)

    lbl_n6 = tk.Label(newWindow, font=("Comic", 12), text="La función de las deformaciones y_AB en m, es:") 	
    lbl_n6.grid(column=71, row=0)
    lbl_n6.place(relx = 0.48, rely = 0.59, anchor = 'center')
    text_deformaciones = tk.Entry(newWindow, justify="center", textvariable=deformaciones, state="disabled").place(x=350, y=434)
    boton_deformaciones = tk.Button(newWindow, text="Calcular", command=calcula_deformaciones).place(x=260, y=428)
    boton_deformaciones_grafica = tk.Button(newWindow, text="Graficar", command=grafica_deformaciones).place(x=530, y=428)    


button_calcular = tk.Button(raiz, text="Calcular",command=ventana_calcular, height = 2, width = 5, font=("Comic", 14)).place(x=335, y=480)

raiz.mainloop()
