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

send_file_button = tk.Button(window, text="Invia File via Seriale", command=send_file)
send_file_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Configurazione della porta seriale (inserisci i tuoi parametri)
port = "COM1"  # Inserisci il nome della porta seriale corretta
baudrate = 9600  # Inserisci il baud rate corretto
try:
    ser = serial.Serial(port, baudrate=baudrate)
except serial.SerialException as e:
    result_label.config(text=f'Errore durante la configurazione della porta seriale: {str(e)}')

# Avvia l'applicazione
window.mainloop()
