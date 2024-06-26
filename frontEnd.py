import tkinter as tk
from tkinter import ttk
from proyecto1 import Producto, Proceso, Tarea, Nodo, Cola, Lista, LineaProduccion

class App:
    def __init__(self, root):
        self.frame_color = '#3C6373' #verde
        self.text_color_1 = '#FFFFFF' #blanco
        self.text_color_2 = '#000000' #negro 88C9F2
        self.proceso_color = '#88C9F2' #celeste
        self.tarea_color = '#2B96D9' #azul
        self.button_color_1 = '#F2C791' # cafe
        self.button_color_2 = '#3C6373' # verde frame
        self.button_border_color_1 = '#F2C791' # cafe

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure("Custom.TButton", borderwidth=5, bordercolor=self.button_border_color_1, background=self.button_color_2, foreground=self.text_color_1)
        self.style.configure("Custom2.TButton", borderwidth=5, bordercolor=self.button_border_color_1, background=self.button_color_1, foreground=self.text_color_2)
        # self.style.configure('Custom.TLabel', background='red')
        self.style.map('Custom.TButton', background=[
            ('disabled', self.button_color_1),
            ('active', self.button_color_1)])


        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg=self.frame_color)

        self.frame1 = tk.Frame(self.root, bg=self.frame_color)
        self.frame2 = tk.Frame(self.root, bg=self.frame_color)
        self.frame3 = tk.Frame(self.root, bg=self.frame_color)
        self.frame4 = tk.Frame(self.root, bg=self.frame_color)

        self.data = {"screen1": "Data from Screen 1",
                     "screen2": "Data from Screen 2",
                     "screen3": "Data from Screen 3",
                     "screen4": "Data from Screen 4"}

        self.setup_screen(self.frame1, "Screen 1", self.data["screen1"], 1)
        self.setup_screen(self.frame2, "Screen 2", self.data["screen2"], 2)
        self.setup_screen(self.frame3, "Screen 3", self.data["screen3"], 3)
        self.setup_screen(self.frame4, "Screen 4", self.data["screen4"], 4)

        self.show_frame(self.frame1)

        self.linea_produccion = LineaProduccion()  # Instancia de la línea de producción
        self.setup_linea_produccion()  # Configura la línea de producción con datos iniciales
        self.update_frame_with_production_data(self.frame1)  # Actualiza el Frame 1 con datos de la línea de producción

    def setup_linea_produccion(self):
        # Aquí puedes configurar tu línea de producción con procesos, tareas y productos iniciales
        p1 = Proceso("Proceso 1")
        self.linea_produccion.insertarProceso(p1)
        p2 = Proceso("Proceso 2")
        self.linea_produccion.insertarProceso(p2)
        p3 = Proceso("Proceso 3")
        self.linea_produccion.insertarProceso(p3)
        t1 = Tarea("Pintar", 1)
        p1.agregarACola(t1)
        pr1 = Producto("Figura")
        t1.agregarACola(pr1)

    # def update_frame_with_production_data(self, frame):
    #     # Limpia el frame antes de actualizarlo
    #     for widget in frame.winfo_children():
    #         widget.destroy()

    #     label = tk.Label(frame, text="Datos de la Línea de Producción", font=("Helvetica", 24), bg=self.frame_color, fg=self.text_color_1)
    #     label.pack(pady=10)

    #     # Agrega la información de la línea de producción al frame
    #     info = self.linea_produccion.Mostrar_Info()
    #     data_label = tk.Label(frame, text=f"Procesos: {info[0]}, Tareas: {info[1]}, Productos: {info[2]}", font=("Helvetica", 16), bg=self.frame_color, fg=self.text_color_1)
    #     data_label.pack(pady=10)

    #     # Agrega botones para navegar entre pantallas
    #     buttons_frame = tk.Frame(frame, bg=self.frame_color)
    #     buttons_frame.pack(pady=10)
    #     for i in range(1, 5):
    #         button = ttk.Button(buttons_frame, text=f"Go to Screen {i}",
    #                            command=lambda i=i: self.switch_frame(i), style="Custom.TButton")
    #         button.pack(side=tk.LEFT, padx=5)

    def create_rounded_label(self, parent, parentBgColor ,text, width, height, radius, bg_color, fg_color):
        frame = tk.Frame(parent, background=parentBgColor)
        frame.pack_propagate(False)
        frame.config(width=width, height=height)

        canvas = tk.Canvas(frame, width=width, height=height, bg=parentBgColor, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Dibuja un rectángulo redondeado
        canvas.create_oval((0, 0, radius * 2, radius * 2), fill=bg_color, outline=bg_color)
        canvas.create_oval((width - radius * 2, 0, width, radius * 2), fill=bg_color, outline=bg_color)
        canvas.create_oval((0, height - radius * 2, radius * 2, height), fill=bg_color, outline=bg_color)
        canvas.create_oval((width - radius * 2, height - radius * 2, width, height), fill=bg_color, outline=bg_color)
        canvas.create_rectangle((radius, 0, width - radius, height), fill=bg_color, outline=bg_color)
        canvas.create_rectangle((0, radius, width, height - radius), fill=bg_color, outline=bg_color)

        # Etiqueta con el texto
        label = tk.Label(frame, text=text, bg=bg_color, fg=fg_color)
        label.place(relx=0.5, rely=0.5, anchor="center")

        return frame

    def update_frame_with_production_data(self, frame):
        # Limpia el frame antes de actualizarlo
        for widget in frame.winfo_children():
            widget.destroy()

        # Agrega botones para navegar entre pantallas
        buttons_frame = tk.Frame(frame, bg=self.frame_color)
        buttons_frame.pack(pady=10)
        for i in range(1, 5):
            button = ttk.Button(buttons_frame, text=f"Go to Screen {i}",
                                command=lambda i=i: self.switch_frame(i), style="Custom.TButton")
            button.pack(side=tk.LEFT, padx=5)
        button = ttk.Button(buttons_frame, text=f"Reload",
                            command=lambda i=i: self.one_step_cycle(), style="Custom.TButton")
        button.pack(side=tk.LEFT, padx=5)

        # Agrega la información de la línea de producción al frame
        label = tk.Label(frame, text="Simulador LimProg", font=("Helvetica", 24), bg=self.frame_color, fg=self.text_color_1)
        label.pack(pady=10)

        # Crear columnas para cada proceso
        procesos_frame = tk.Frame(frame, bg=self.frame_color)
        procesos_frame.pack(pady=10)

        nodo_proceso = self.linea_produccion.lProce.primero
        while nodo_proceso:
            proceso = nodo_proceso.valor
            proceso_frame = tk.Frame(procesos_frame, bg=self.frame_color, borderwidth=2, relief="solid")
            proceso_frame.pack(side=tk.LEFT, padx=10, fill=tk.Y)

            proceso_label = self.create_rounded_label(proceso_frame, self.frame_color, proceso.nombre, width=150, height=30, radius=10, bg_color=self.proceso_color, fg_color=self.text_color_2)
            proceso_label.pack(pady=5)

            nodo_tarea = proceso.cola.primero
            while nodo_tarea:
                tarea = nodo_tarea.valor

                tarea_frame = tk.Frame(proceso_frame, bg=self.frame_color, borderwidth=1, relief="solid")
                tarea_frame.pack(pady=2, fill=tk.X)

                tarea_label = tk.Label(tarea_frame, text=f"{tarea.nombre} - Producto en tarea: {tarea.productoEnProceso}", font=("Helvetica", 14), bg=self.frame_color, fg=self.text_color_1)
                tarea_label.pack(pady=2)

                nodo_producto = tarea.cola.primero
                while nodo_producto:
                    producto = nodo_producto.valor
                    producto_label = tk.Label(tarea_frame, text=f"Producto: {producto.nombre} - Tiempo: {producto.tiempoEntarea}", font=("Helvetica", 12), bg=self.frame_color, fg=self.text_color_1)
                    producto_label.pack(pady=1)
                    nodo_producto = nodo_producto.siguiente

                nodo_tarea = nodo_tarea.siguiente

            nodo_proceso = nodo_proceso.siguiente



    def setup_screen(self, frame, title, data, screen_number):
        frame.grid(row=0, column=0, sticky="nsew")

        label = tk.Label(frame, text=title, font=("Helvetica", 24), bg=self.frame_color, fg=self.text_color_1)
        label.pack(pady=10)

        data_label = tk.Label(frame, text=data, font=("Helvetica", 16), bg=self.frame_color, fg=self.text_color_1)
        data_label.pack(pady=10)

        buttons_frame = tk.Frame(frame)
        buttons_frame.pack(pady=10)

        for i in range(1, 5):
            if i != screen_number:
                button = ttk.Button(buttons_frame, text=f"Go to Screen {i}",
                                   command=lambda i=i: self.switch_frame(i), style="Custom2.TButton")
                button.pack(side=tk.LEFT, padx=5)

    def one_step_cycle(self):
        self.update_frame_with_production_data(self.frame1)

    def switch_frame(self, screen_number):
        if screen_number == 1:
            self.show_frame(self.frame1)
        elif screen_number == 2:
            self.show_frame(self.frame2)
        elif screen_number == 3:
            self.show_frame(self.frame3)
        elif screen_number == 4:
            self.show_frame(self.frame4)

    def show_frame(self, frame):
        frame.tkraise()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
