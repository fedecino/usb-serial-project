import serial
import tkinter as tk
from tkinter import filedialog

ser = None  # Variabile globale per la porta seriale

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        selected_file_path.set(file_path)

def send_file():
    global ser
    if ser is None:
        result_label.config(text="Errore: La porta seriale non è configurata.")
        return

    file_path = selected_file_path.get()
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            ser.write(file_content.encode())
            result_label.config(text=f'Dati inviati via seriale: {file_content}')
    except Exception as e:
        result_label.config(text=f'Errore durante l\'invio dei dati via seriale: {str(e)}')

def configure_serial():
    global ser
    if ser is not None:
        ser.close()
    port = port_entry.get()
    baudrate = int(baudrate_entry.get())
    stopbits = int(stopbits_var.get())
    parity = parity_var.get()
    try:
        ser = serial.Serial(port, baudrate=baudrate, stopbits=stopbits, parity=parity)
    except serial.SerialException as e:
        result_label.config(text=f'Errore durante la configurazione della porta seriale: {str(e)}')

# Creazione della finestra principale
window = tk.Tk()
window.title("Invio dati via seriale")

# Creazione dei widget per l'interfaccia utente
selected_file_path = tk.StringVar()
file_path_label = tk.Label(window, text="File Selezionato:")
file_path_label.pack()
file_path_entry = tk.Entry(window, textvariable=selected_file_path)
file_path_entry.pack()

select_file_button = tk.Button(window, text="Seleziona File", command=open_file_dialog)
select_file_button.pack()

port_label = tk.Label(window, text="Porta COM:")
port_label.pack()
port_entry = tk.Entry(window)
port_entry.pack()

baudrate_label = tk.Label(window, text="Baud Rate:")
baudrate_label.pack()
baudrate_entry = tk.Entry(window)
baudrate_entry.pack()

stopbits_label = tk.Label(window, text="Bit di Stop:")
stopbits_label.pack()
stopbits_var = tk.IntVar()
stopbits_var.set(1)
stopbits_menu = tk.OptionMenu(window, stopbits_var, 1, 1.5, 2)
stopbits_menu.pack()

parity_label = tk.Label(window, text="Parità:")
parity_label.pack()
parity_var = tk.StringVar()
parity_var.set('N')
parity_menu = tk.OptionMenu(window, parity_var, 'N', 'E', 'O', 'M', 'S')
parity_menu.pack()

configure_button = tk.Button(window, text="Configura Porta Seriale", command=configure_serial)
configure_button.pack()

send_file_button = tk.Button(window, text="Invia File via Seriale", command=send_file)
send_file_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Avvia l'applicazione
window.mainloop()
