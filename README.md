# Tkinter_interfaces
Interfaces in tkinter for practice and do things about grafics


# Creación de ventana 

Comenzando es necesario importar los módulos correspondientes, los cuales son tkinter (abrebiando con tk) el otro módulo es ttk el cual se encuentra en tkiter  

```
    import tkinter as tk 
    from tkinter import ttk 
```

una vez esten importados los modulos necesarios es crear la ventana principal.
- La primera línea se crea la instancia de Tk donde se crea la ventana principal 
- la segunda linea ejecuta el método mainloop() el cual es el bucle principal del programa.

```
    ventana = tk.Tk()
    ventana.mainloop()

```

creada la ventana con los métodos, es posible configurar las propiedades de la misma con los métodos title() y config(), donde en cualquier método, función o clase de Tk donde se requiera especificar un tamaño, será vía los argumentos:

--> width(ancho)
--> heiht(alto)

```
    ventana.title("Aca la primera muestra")
    ventana.config(width=400, height=300)
```

# Etiquetas 

Para creación de etiquetas sin orientado a objetos.

```
    etiqueta_lectura = ttk.Label(text="Lecutra nativa: ")
    etiqueta_lectura.place(x=20, y=20)
```
# Caja de texto

Para la realización de cajas de texto de manera similar ya que se declara una variable con el método ttk.entry.

```
    caja_lectura = ttk.Entry()
    caja_lectura.place(x=110, y=20, width=130) 
```
# Button 

``` 
    boton_lectura = ttk.Button(text="Calculo")
    boton_lectura.place(x=20, y=60)  
```

# Para cambiar icono de ventana  

La imagen deve de estar en formato .ico
la pagina que encontr de iconos:
https://icon-icons.com/es/


``` 
    ventana.iconbitmap("icon.ico")  
```