import tkinter as tk

def create_rounded_label(parent, text, width, height, radius, bg_color, fg_color):
    frame = tk.Frame(parent, background="white")
    frame.pack_propagate(False)
    frame.config(width=width, height=height)

    canvas = tk.Canvas(frame, width=width, height=height, bg="white", highlightthickness=0)
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

root = tk.Tk()
root.geometry("300x200")

rounded_label = create_rounded_label(root, "Etiqueta con bordes redondeados", width=200, height=50, radius=15, bg_color="blue", fg_color="white")
rounded_label.pack(pady=20)

root.mainloop()
