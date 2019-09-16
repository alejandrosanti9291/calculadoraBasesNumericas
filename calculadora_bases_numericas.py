from tkinter import *
import os

class Calculadora():
    def __init__(self):
        ##variables a utilizar en la interfaz grafica
        self.principal = Tk()
        self.principal.title("Calculadora")
        self.principal.resizable(False,False)   #prohibe la ampliación de la ventana
        self.ancho_boton = 4    #variable para definir ancho de botones
        self.alto_boton = 1     #varible para definir alto de los botones
        self.color_boton = "#A9BCF5"    #variable para definir color de botones
        self.fuente_btn = ('Consolas', '22')    #define fuente de botones
        self.padx_btn = 2
        self.pady_btn = 2
        self.pady_btn = 2
        self.bg_gral = "#EFEFFB"
        self.fuente_selec = ('Consolas', '12')

        #variables a utilizar en la calculadora de bases numericas
        self.hubo_resultado = False
        self.input_text = StringVar()   #variable para almacenar valores ingresados a la pantalla de la calculadora
        self.input_text_bin = StringVar()   #variable para almacenar numeros base 2
        self.input_text_oct = StringVar()   #variable para almacenar numeros base 8
        self.input_text_dec = StringVar()   #variable para almacenar numeros base 10
        self.input_text_hex = StringVar()   #variable para almacenar numero base 16
        self.caracteres_especiales = ['*', '/', '-', '+', '(', ')'] #lista de caracteres especiales (operadores) presnetados en la calculadora
        self.un_caracter_especial = False   #define si el usuario ingreso un caracter especial antes mecionado, o no
        self.hasta_operador = int()         #variable para almacenar la cantidad de digitos ingresados por el usuario hasta un operador matematico (caracter especial)

        self.ventana()                  #funcion donde esta el codigo de la interfaz grafica
        self.principal.mainloop()       #se lanza el ciclo de la interfaz grafica

    def On_Clik_btn(self, bton):
        if self.hubo_resultado:     #verifica si se ha oprimido el boton igual
            self.hasta_operador = 0
            self.limpiar_celdas(True)   #funcion para limpiar todas celdas
            self.hubo_resultado = False
        texto = self.campo_pantalla.get() + str(bton)   #se carga en la variable texto el texto en la variable más el botón ingresado
        if str(bton) in self.caracteres_especiales: #si es un caracter especiale
            self.operacion = self.input_text_dec.get()  ##guarda lo que habia en el campo decimal en un variable operacion, para luego hacer la operacion con la funcion eval
            self.operacion = self.operacion + str(bton) #Se le agrega la tecla orpimida por el usuario a la variable operacion
            self.hasta_operador = len(texto)    #se cuentan los elementos que hay hasta el operador ingresado, para luego hacer un slice y sacar solo el ultimo numero ingresado, para luego hacer la operacion con la funcion eval() todo en base 10
            self.limpiar_celdas()   #funcion que limpia las celdas
            self.input_text.set(texto)  #se coloca el texto en la pantalla principal de la calculadora
            self.un_caracter_especial = True    #almacena True si el usuario ingreso un operador
        else:
            self.input_text.set(texto)      #la funcion set() coloca el valor indicado en el campo grafico
            texto = self.input_text.get()[self.hasta_operador:]     ##solo coje los numeros que hay hasta antes del operador
            self.imprmir_en_celdas(texto)   #coloca en los inputs las conversiones


    def imprmir_en_celdas(self, texto):
        if self.base_numeric.get() == 1:  # osea que la calculadora esta en binarios
            decimal = self.bin_a_dec(texto) #obtiene el valor del campo decimal, ya que es más facil hacer la conversion a otras bases, partiendo con un numero base 10
            self.input_text_bin.set(texto)  #si la calculadora esta en binario, el texto en pantalla es binario y no necesita conversion
            self.input_text_oct.set(self.dec_a_baseN(decimal, 8))   #la funcion dec_a_baseN convierte numeros base 10 a cualquiera que se le indique
            self.input_text_dec.set(decimal)
            self.input_text_hex.set(self.dec_a_baseN(decimal, 16))
        elif self.base_numeric.get() == 2:  # osea que la calculadra esta en octadecimal
            decimal = self.oct_a_dec(texto)
            self.input_text_bin.set(self.dec_a_baseN(decimal, 2))
            self.input_text_oct.set(texto)
            self.input_text_dec.set(decimal)
            self.input_text_hex.set(self.dec_a_baseN(decimal, 16))
        elif self.base_numeric.get() == 3:  # osea que la calculadra esta en decimal
            self.input_text_bin.set(self.dec_a_baseN(texto, 2))
            self.input_text_oct.set(self.dec_a_baseN(texto, 8))
            self.input_text_dec.set(texto)
            self.input_text_hex.set(self.dec_a_baseN(texto, 16))
        elif self.base_numeric.get() == 4:  # osea que la calculadora esta en haxadecimal
            decimal = self.hexa_a_dec(texto)
            self.input_text_bin.set(self.dec_a_baseN(decimal, 2))
            self.input_text_oct.set(self.dec_a_baseN(decimal, 8))
            self.input_text_dec.set(decimal)
            self.input_text_hex.set(texto)


    def bin_a_dec(self, binario):   #funcion que convirte numero base 2 a base 10

        decimal = 0
        numero_de_bits = len(str(binario))
        for n in range(numero_de_bits):
            decimal = decimal + int(str(binario)[-(n + 1)]) * 2 ** n
        return decimal

    def oct_a_dec(self, octal): #funcion que convierte número base 8 a numero base 10

        decimal = 0
        numero_de_valores = len(str(octal))
        for n in range(numero_de_valores):
            decimal = decimal + int(str(octal)[-(n + 1)]) * 8 ** n
        return decimal

    def dec_a_baseN(self, decimal, base):   #funcion que convierte numero base 10 a cualquier base
        conversion = ''
        while int(decimal) // base != 0:
            conversion = str(int(decimal) % base) + conversion
            decimal = int(decimal) // base
        return str(decimal) + conversion

    def hexa_a_dec(self, hexa): #funcion que convirte numero base 16 a base 10

        decimal = 0
        numero_de_valores = len(str(hexa))
        for n in range(numero_de_valores):
            if str(hexa)[-(n + 1)] >='0' and str(hexa)[-(n + 1)] <='9':
                decimal = decimal + int(str(hexa)[-(n + 1)]) * 16 ** n
            elif str(hexa)[-(n + 1)] >='A' and str(hexa)[-(n + 1)] <='F':
                decimal = decimal + (int(str(hexa)[-(n + 1)])-55) * 16 ** n
        return decimal

    def calcular(self): #funcion que realiza el calculo al usuario oprimir el botón =
        try:
            if len(self.operacion) > 0: #si hay un valor en la variable operacion, se le suma el numero base 10 ingresado por el usuario despues del signo de operacion
                self.operacion = self.operacion + self.input_text_dec.get()
                resultado = str(eval(self.operacion))   #realiza la operacion con la funcion eval(). esta función ejecuta el string entregado como una linea de comando
                if self.base_numeric.get() == 1:  #se define en que base se va a colocar en la pantalla principal de la calculadora
                    resultado = self.dec_a_baseN(resultado, 2)
                elif self.base_numeric.get() == 2:
                    resultado = self.dec_a_baseN(resultado, 8)
                elif self.base_numeric.get() == 4:
                    resultado = self.dec_a_baseN(resultado, 16)
                print(resultado)
                self.guardartxt(self.operacion)
                self.input_text.set(resultado)
                self.imprmir_en_celdas(resultado)
                self.operacion = ""
            else:
                self.limpiar_celdas(True)
            self.un_caracter_especial = False
            self.hubo_resultado = True
        except:
            self.limpiar_celdas()
            resultado = "ERROR"
            self.hubo_resultado = True


    def limpiar_celdas(self, todo=True):    ##borra el contenido de los campos graficados
        self.input_text_bin.set("")
        self.input_text_oct.set("")
        self.input_text_dec.set("")
        self.input_text_hex.set("")
        if todo:
            self.input_text.set("")

    def cerrando_p(self):       #funcion para detener el loop de la interfaz grafica y destruye la ventana creada
        self.principal.quit()
        self.principal.destroy()

    def guardartxt(self, operacion):    #funcion para guardar los resulados en un archivo .txt
        file = open("resultados.txt", "w")
        file.write("Operación: %s" % operacion + os.linesep)
        file.write("Reseultados: binario = %s, octadecimal = %s, decimal = %s, hexadecimal = %s" %(str(self.input_text_bin.get()), str(self.input_text_oct.get()), str(self.input_text_dec.get()), str(self.input_text_hex.get())))
        file.close()

    def sele_base(self):    #funcion para habilitar/deshabilitar los botones utilizados en las bases numericas
        self.base_numeric.set(self.base_numeric.get())
        self.botones.destroy()
        self.limpiar_celdas(True)
        if self.base_numeric.get() == 1:
            self.botone("disabled","disabled")
        elif self.base_numeric.get() == 2:
            self.botone("disabled","normal")
        else:
            self.botone("normal","normal")


    def botone(self, estado8a9 ="normal", estado2a7="normal"):  #funcion donde esta el codigo que crea los botones de la calculadora
        self.botones = Frame(self.marco02)
        self.botones.pack(fill=X, expand=True, side=TOP, pady=2)

        # FILA 0 DE BOTONES
        bton_c = Button(self.botones, text="BORRAR", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                        width=9,
                        height=self.alto_boton, command=lambda: self.limpiar_celdas(True)).grid(row=0, column=0,
                                                                                                columnspan=2,
                                                                                         padx=self.padx_btn,
                                                                                         pady=self.pady_btn)

        bton_Iparent = Button(self.botones, text="(", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                              width=self.ancho_boton,
                              height=self.alto_boton, command=lambda: self.On_Clik_btn("(")).grid(row=0, column=2,
                                                                                                  padx=self.padx_btn,
                                                                                                  pady=self.pady_btn)
        bton_Fparent = Button(self.botones, text=")", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                              width=self.ancho_boton,
                              height=self.alto_boton, command=lambda: self.On_Clik_btn(")")).grid(row=0, column=3,
                                                                                                  padx=self.padx_btn,
                                                                                                  pady=self.pady_btn)
        bton_power = Button(self.botones, text="OFF", font=self.fuente_btn, bd=self.pady_btn, bg="#B22222",
                            width=self.ancho_boton,
                            height=self.alto_boton, command=lambda: self.cerrando_p()).grid(row=0, column=4, rowspan=1,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        # FILA 1 DE BOTONES
        bton_7 = Button(self.botones, text="7", font=self.fuente_btn,state =estado2a7, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("7")).grid(row=1, column=0,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_8 = Button(self.botones, text="8", font=self.fuente_btn, state=estado8a9, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("8")).grid(row=1, column=1,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_9 = Button(self.botones, text="9", font=self.fuente_btn,state = estado8a9, bd=self.pady_btn, bg=self.color_boton,
                             width=self.ancho_boton,
                             height=self.alto_boton, command=lambda: self.On_Clik_btn("9")).grid(row=1, column=2,
                                                                                                 padx=self.padx_btn,
                                                                                                 pady=self.pady_btn)
        bton_div = Button(self.botones, text="/", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                          width=self.ancho_boton,
                          height=self.alto_boton, command=lambda: self.On_Clik_btn("/")).grid(row=1, column=3,
                                                                                              padx=self.padx_btn,
                                                                                              pady=self.pady_btn)

        # FILA 2 DE self.botones
        bton_4 = Button(self.botones, text="4",state =estado2a7, font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("4")).grid(row=2, column=0,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_5 = Button(self.botones, text="5",state =estado2a7, font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("5")).grid(row=2, column=1,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_6 = Button(self.botones, text="6",state =estado2a7, font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("6")).grid(row=2, column=2,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_mult = Button(self.botones, text="*", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                           width=self.ancho_boton,
                           height=self.alto_boton, command=lambda: self.On_Clik_btn("*")).grid(row=2, column=3,
                                                                                               padx=self.padx_btn,
                                                                                               pady=self.pady_btn)
        bton_igual = Button(self.botones, text="=", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                            width=self.ancho_boton,
                            height=self.alto_boton, command=lambda: self.calcular()).grid(row=1, column=4,
                                                                                           padx=self.padx_btn,
                                                                                           pady=self.pady_btn,
                                                                                           rowspan=4,
                                                                                           sticky=N + S)
        # FILA 3 DE BOTONES
        bton_1 = Button(self.botones, text="1", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("1")).grid(row=3, column=0,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_2 = Button(self.botones, text="2",state =estado2a7, font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("2")).grid(row=3, column=1,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_3 = Button(self.botones, text="3",state =estado2a7, font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("3")).grid(row=3, column=2,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_men = Button(self.botones, text="-", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                          width=self.ancho_boton,
                          height=self.alto_boton, command=lambda: self.On_Clik_btn("-")).grid(row=3, column=3,
                                                                                              padx=self.padx_btn,
                                                                                              pady=self.pady_btn)
        # FILA 4 DE BOTONES
        bton_0 = Button(self.botones, text="0", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                        width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("0")).grid(row=4, column=0,
                                                                                            padx=self.padx_btn,
                                                                                            pady=self.pady_btn,
                                                                                            columnspan=3,
                                                                                            sticky=W + E)

        bton_sum = Button(self.botones, text="+", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                          width=self.ancho_boton,
                          height=self.alto_boton, command=lambda: self.On_Clik_btn("+")).grid(row=4, column=3,
                                                                                              padx=self.padx_btn,
                                                                                              pady=self.pady_btn)

    def calculadora_bases_numericas(self):  #funcion donde se configura el tamaño de la ventana y contiene los radios y campos de entrada para las conversiones
        self.principal.geometry("420x590")
        # self.marco para la fila 2, columna 0
        self.marco02 = Frame(self.principal, bg="#BDBDBD")
        self.marco02.pack(fill=Y, side=TOP, pady=20, padx=8, ipady=30)

        pantalla = Frame(self.marco02)
        pantalla.pack(fill=X, expand=True, side=TOP)
        self.campo_pantalla = Entry(pantalla, font=('Consolas', 20, 'bold'), width=22, bg="#A9F5A9", bd=20,
                                    insertwidth=4, textvariable=self.input_text, justify="right")  # , state=DISABLED)
        self.campo_pantalla.pack(fill=X, side=TOP, expand=True)

        self.base_numeric  = IntVar()
        self.base_numeric.set(3)
        radios = Frame(self.marco02, bg= "#BDBDBD")
        radios.pack(fill = X, expand = True, side = TOP, pady=1)

        binarios = Radiobutton(radios, text="Binario", variable=self.base_numeric, bg="#BDBDBD", value=1,
                               font=self.fuente_selec,
                               command=lambda: self.sele_base()).grid(row=0, column=0, padx=25,sticky =W)
        input_binarios = Entry(radios, font=self.fuente_selec, width=20,insertwidth=4, textvariable=self.input_text_bin, justify="right").grid(row=0, column=1)
        octaldecimal = Radiobutton(radios, text="Octal decimal", variable=self.base_numeric, bg="#BDBDBD", value=2,
                                   font=self.fuente_selec,
                                   command=lambda: self.sele_base()).grid(row=1, column=0, padx=25,sticky =W)
        input_octaldecimal = Entry(radios, font=self.fuente_selec, width=20,insertwidth=4, textvariable=self.input_text_oct, justify="right").grid(row=1, column=1)

        decimal = Radiobutton(radios, text="Decimal", variable=self.base_numeric, bg="#BDBDBD", value=3,
                              font=self.fuente_selec,
                              command=lambda: self.sele_base()).grid(row=2, column=0, padx=25,sticky =W)
        input_decimal = Entry(radios, font=self.fuente_selec, width=20,insertwidth=4, textvariable=self.input_text_dec, justify="right").grid(row=2, column=1)

        hexadecimal = Radiobutton(radios, text="Hexadecimal", variable=self.base_numeric, bg="#BDBDBD", value=4,
                                  font=self.fuente_selec,
                                  command=lambda: self.sele_base()).grid(row=3, column=0, padx=25,sticky =W)
        input_hexadecimal = Entry(radios, font=self.fuente_selec, width=20,insertwidth=4, textvariable=self.input_text_hex, justify="right").grid(row=3, column=1)


        #coloca en pantalla los botones
        self.botone()


    def ventana(self):
        self.principal.config(bg=self.bg_gral,relief="ridge")
        self.calculadora_bases_numericas()

        self.principal.protocol("WM_DELETE_WINDOW", self.cerrando_p)


def main():
    app = Calculadora()

if __name__ == "__main__":
    main()