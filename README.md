# Tkinter_interfaces
Interfaces in tkinter for practice and do things about grafics


# Declaración de ventana 

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