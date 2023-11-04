import serial
import tkinter as tk
from tkinter import filedialog

def send_file():
    # Ottieni i parametri della porta seriale dalla GUI
    port = port_entry.get()
    
    baudrate_str = baudrate_entry.get()
    if not baudrate_str:
        result_label.config(text="Inserire un valore di Baud Rate valido")
        return
    
    try:
        baudrate = int(baudrate_str)
    except ValueError:
        result_label.config(text="Baud Rate deve essere un numero intero valido")
        return
    
    stopbits = stopbits_var.get()
    parity = parity_var.get()
    
    ser = serial.Serial(port, baudrate=baudrate, stopbits=stopbits, parity=parity)

    # Apri una finestra di dialogo per selezionare un file da caricare
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                ser.write(file_content.encode())
                result_label.config(text=f'Dati inviati via seriale: {file_content}')
        except Exception as e:
            result_label.config(text=f'Errore durante il caricamento e l\'invio dei dati via seriale: {str(e)}')
        finally:
            ser.close()

# Creazione della finestra principale
window = tk.Tk()
window.title("Invio dati via seriale")

# Creazione dei widget per l'interfaccia utente
port_label = tk.Label(window, text="Porta Seriale:")
port_label.pack()
port_entry = tk.Entry(window)
port_entry.pack()

baudrate_label = tk.Label(window, text="Baud Rate:")
baudrate_label.pack()
baudrate_entry = tk.Entry(window)
baudrate_entry.pack()

stopbits_label = tk.Label(window, text="Bit di Stop:")
stopbits_label.pack()
stopbits_var = tk.StringVar()
stopbits_var.set('1')
stopbits_menu = tk.OptionMenu(window, stopbits_var, '1', '1.5', '2')
stopbits_menu.pack()

parity_label = tk.Label(window, text="Parità:")
parity_label.pack()
parity_var = tk.StringVar()
parity_var.set('N')
parity_menu = tk.OptionMenu(window, parity_var, 'N', 'E', 'O', 'M', 'S')
parity_menu.pack()

select_file_button = tk.Button(window, text="Seleziona File", command=send_file)
select_file_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Avvia l'applicazione
window.mainloop()
