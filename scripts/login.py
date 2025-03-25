import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox

tamañoContrasela = 6


# metodo para buscar la contraseña en la base de datos en excel
def buscar_o_agregar():
    input_password = entry_password.get().strip()

    if len(input_password) != tamañoContrasela:
        messagebox.showerror("Error", f"La contraseña debe tener exactamente 6 caracteres.")
        return

    home_dir = os.path.expanduser("~")
    downloads_dir = os.path.join(home_dir, "Descargas", "contraseñasBD")

    files = [f for f in os.listdir(downloads_dir) if f.endswith('.xlsx') and not f.startswith('~$')]
    if not files:
        messagebox.showerror("Error", "No se encontró ningún archivo Excel en la carpeta contraseñasBD.")
        return

    latest_file = max([os.path.join(downloads_dir, f) for f in files], key=os.path.getctime)

    df = pd.read_excel(latest_file)


    found = False
    index_found = -1
    for index, row in df.iterrows():
        if row['Password'] == input_password:
            found = True
            index_found = index
            break

    if found:
        messagebox.showinfo("Contraseña Encontrada", f"La contraseña fue encontrada en el índice: {index_found}")
    else:
        new_row = pd.DataFrame({"Password": [input_password]})
        df = pd.concat([df, new_row], ignore_index=True)
        try:
            df.to_excel(latest_file, index=False)
            messagebox.showinfo("Contraseña Agregada",
                                "La contraseña no fue encontrada y se agregó a la base de datos.")
        except PermissionError:
            messagebox.showerror("Error",
                                 f"No se pudo guardar el archivo: {latest_file}. Asegúrate de que no está en uso.")


root = tk.Tk()
root.title("Gestión de Contraseñas")
root.geometry("400x250")
label_password = tk.Label(root, text="Introduce la contraseña:", font=("Arial", 12))
label_password.pack(pady=10)
entry_password = tk.Entry(root, font=("Arial", 12), width=30)
entry_password.pack(pady=5)
label_longitud = tk.Label(root, text=f"Nota: La contraseña debe tener exactamente 6 caracteres.",
font=("Arial", 10), fg="gray")
label_longitud.pack(pady=5)
btn_buscar_agregar = tk.Button(root, text="Buscar o Agregar", font=("Arial", 12), command=buscar_o_agregar)
btn_buscar_agregar.pack(pady=20)
root.mainloop()




