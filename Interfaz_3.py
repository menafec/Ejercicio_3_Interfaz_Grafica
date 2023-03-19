from tkinter import *
from tkinter import ttk
import tkinter as ttk

raiz = Tk()
raiz.geometry("1050x500")
raiz.config(background="gray6")

MainFrame = ttk.Frame(raiz, background="turquoise4")
MainFrame.grid(column=0, row=0, sticky=(W))
Frameinicio = ttk.Frame(raiz, background="gray6")
Frameinicio.grid(column=0, row=1, sticky=(W))
Izquierda = ttk.Frame(Frameinicio, background="gray6")
Izquierda.grid(column=0, row=0, sticky=(W))
IzquierdaArriba = ttk.Frame(Izquierda, background="gray6")
IzquierdaArriba.grid(column=0, row=0, padx=50, sticky=(W))
IzquierdaAbajo = ttk.Frame(Izquierda, background="gray6")
IzquierdaAbajo.grid(column=0, row=1, padx=50, sticky=(W))
FirstFrame = ttk.Frame(IzquierdaArriba, background="gray20")
FirstFrame.grid(column=0, row=0, padx=10 ,pady=5, sticky=(W,N))
SecondFrame = ttk.Frame(IzquierdaArriba, background="gray20")
SecondFrame.grid(column=1, row=0,pady=5, sticky=(W,N)) 
ThirdFrame = ttk.Frame(IzquierdaAbajo, background="gray20")
ThirdFrame.grid(column=0, row=0, padx=8 ,sticky=(W,N))
FourthFrame = ttk.Frame(IzquierdaAbajo, background="gray20")
FourthFrame.grid(column=1, row=0,sticky=(W,N))
Right = ttk.Frame(Frameinicio, background="gray6")
Right.grid(column=0, row=0, padx = 600 , pady=5, sticky=(W,N))
FifthFrame = ttk.Frame(Right, background="gray20")
FifthFrame.grid(column=0,row=0,sticky=(W))

ttk.Label(MainFrame, background="turquoise4",text="SPAI 4.0", foreground="white", font=("arial",12,"bold"), anchor="w",width=300).grid(column=1,row=0,sticky=(W))
ttk.Label(FirstFrame, background="gray20", foreground="cyan4", font=("arial",10), text="Indicadores Digitales").grid(column=0, row=0, padx=4, pady=2, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="Linea 1: ").grid(column=0, row=1, padx=4, pady= 8, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="Linea 2: ").grid(column=0, row=2, padx=4, pady= 8, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="Linea 3: ").grid(column=0, row=3, padx=4, pady= 8,sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="Gabinete: Abierto").grid(column=0, row=4, padx=4,  pady= 8, sticky=(W,N),columnspan=1)
ttk.Label(FirstFrame, background="gray20", foreground="white", text="Alarma: ").grid(column=0, row=5, padx=4, pady= 8, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="Alarma 2: ").grid(column=0, row=6, padx=4, pady= 8, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="On").grid(column=1, row=1, padx=4, pady= 8, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="On").grid(column=1, row=2, padx=4, pady= 8, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="On").grid(column=1, row=3, padx=4, pady= 8, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="On").grid(column=1, row=5, padx=4, pady= 8, sticky=(W,N))
ttk.Label(FirstFrame, background="gray20", foreground="white", text="Off").grid(column=1, row=6, padx=4, pady= 8, sticky=(W,N))
ttk.Label(SecondFrame, background="gray20", foreground="cyan4", font=("arial",10), text="Temperaturas:").grid(column=0, row=0, sticky=(W, N))
ttk.Label(SecondFrame, background="gray20", foreground="white", text="Temperatura 1:").grid(column=0, row=1, padx=50, pady=20, sticky=(W))
ttk.Label(SecondFrame, background="gray20", foreground="white", text="Temperatura 2:").grid(column=1, row=1, padx=30, pady=20, sticky=(W))
ttk.Label(SecondFrame, background="gray20", foreground="white", text="Temp. Agua: 58°C", anchor="center").grid(column=0, row=3, pady=8, columnspan=2)
ttk.Label(SecondFrame, background="gray20", foreground="white", text="Temp. Ambiente: 32°C", anchor="center").grid(column=0, row=4, pady=8, columnspan=2)
ttk.Label(ThirdFrame, background="gray20", foreground="white", text="Velocidad bomba:", width=35, anchor="w").grid(column=0, row=0, padx=20, pady=20, sticky=(W), columnspan=1)
ttk.Label(FourthFrame, background="gray20", foreground="cyan4", font=("arial",12), text="  Nivel del tanque: ",width=25, anchor="w").grid(column=0, row=0, sticky=(W), pady=2, padx=3)
ttk.Label(FifthFrame, background="gray20", foreground="cyan4", font=("arial",12), text="Produccion: ").grid(column=0, row=0, sticky=(W))
ttk.Label(FifthFrame, background="gray20", foreground="white", text="Piezas producidas: 50").grid(column=0, row=2, columnspan=2, pady=10)
ttk.Label(FifthFrame, background="gray20", foreground="white", text="Piezas defectuosas: 12").grid(column=0, row=3, columnspan=2, pady=5)


LineMenu = PhotoImage(file="LineMenu.png")
MenuDrawer= ttk.Label(MainFrame, background="turquoise4")
MenuDrawer.grid(column=0, row=0, padx=5, sticky=(W,N))
MenuDrawer['image'] = LineMenu
Verde = PhotoImage(file="GreenCircle.png")
GreenCircle1= ttk.Label(FirstFrame, background="gray20")
GreenCircle2= ttk.Label(FirstFrame, background="gray20")
GreenCircle3= ttk.Label(FirstFrame, background="gray20")
GreenCircle4= ttk.Label(FirstFrame, background="gray20")
GreenCircle1.grid(column=2, row=1, pady=2, sticky=(W))
GreenCircle2.grid(column=2, row=2, pady=2, sticky=(W))
GreenCircle3.grid(column=2, row=3, pady=2, sticky=(W))
GreenCircle4.grid(column=2, row=6, pady=2, sticky=(W))
GreenCircle1['image'] = Verde
GreenCircle2['image'] = Verde
GreenCircle3['image'] = Verde
GreenCircle4['image'] = Verde
Rojo = PhotoImage(file="RedCircle.png")
RedCircle1= ttk.Label(FirstFrame, background="gray20")
RedCircle2= ttk.Label(FirstFrame, background="gray20")
RedCircle1.grid(column=2, row=4, pady=2, sticky=(W))
RedCircle2.grid(column=2, row=5, pady=2, sticky=(W))
RedCircle1['image'] = Rojo
RedCircle2['image'] = Rojo
GrafVerde = PhotoImage(file="GraficaVerde.png")
GraficaVerde= ttk.Label(SecondFrame, background="gray20")
GraficaVerde.grid(column=0, row=2, padx=28, sticky=(W,N))
GraficaVerde['image'] = GrafVerde
GrafAmarilla = PhotoImage(file="GraficaAmarilla.png")
GraficaAmarilla= ttk.Label(SecondFrame, background="gray20")
GraficaAmarilla.grid(column=1, row=2, sticky=(W,N))
GraficaAmarilla['image'] = GrafAmarilla
GrafNaranja = PhotoImage(file="GraficaNaranja.png")
GraficaNaranja= ttk.Label(ThirdFrame, background="gray20")
GraficaNaranja.grid(column=0, row=1, sticky=(W,N), columnspan=1, padx=10)
GraficaNaranja['image'] = GrafNaranja
GrafAzul = PhotoImage(file="GraficaAzul.png")
GraficaAzul= ttk.Label(FourthFrame, background="gray20")
GraficaAzul.grid(column=0, row=1, sticky=(W,N), columnspan=1, padx=10)
GraficaAzul['image'] = GrafAzul
Diagrama = PhotoImage(file="DiagramaGrafica.png")
GraficaDG= ttk.Label(FifthFrame, background="gray20")
GraficaDG.grid(column=0, row=1, sticky=(W,N), columnspan=1, padx=10, pady=10)
GraficaDG['image'] = Diagrama

raiz.mainloop()