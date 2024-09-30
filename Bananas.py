import tkinter as tk
from PIL import Image, ImageTk
import random
import configparser
import os

# Funktion zum Laden der Konfiguration aus config.ini oder zum Erstellen einer Standarddatei
def load_config():
    config = configparser.ConfigParser()
    config_file = './config.ini'

    # Überprüfen, ob die Datei existiert
    if not os.path.exists(config_file):
        # Erstelle eine Standard-config.ini Datei mit 1 Banane
        config['Config'] = {'Bananas': '1'}  # Standardmäßig 1 Banane
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        print("config.ini erstellt mit Standardwert: 1 Banane.")

    # Konfiguration lesen
    config.read(config_file)
    return int(config['Config'].get('Bananas', 1))  # Standardwert 1 Banane, falls nicht definiert

# Klasse für jede einzelne Banane
class BananaPet:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # Entfernt die Titelleiste des Fensters
        self.root.config(bg='white', highlightthickness=0)  # Hintergrundfarbe weiß, ohne Rand
        self.root.wm_attributes("-transparentcolor", "white")  # Transparenter Hintergrund
        self.root.wm_attributes("-topmost", True)  # Fenster immer im Vordergrund

        # Fenstergröße festlegen
        self.root.geometry("100x100")

        # Bild der Banane laden
        self.banana_image = Image.open("banana.png")  # Stelle sicher, dass du ein Bild hast
        self.banana_image = self.banana_image.resize((100, 100), Image.ANTIALIAS)
        self.banana_photo = ImageTk.PhotoImage(self.banana_image)

        # Label für die Banane
        self.banana_label = tk.Label(self.root, image=self.banana_photo, bg="white")
        self.banana_label.pack()

        # Startposition der Banane
        self.x = random.randint(0, self.root.winfo_screenwidth() - 100)
        self.y = random.randint(0, self.root.winfo_screenheight() - 100)

        # Geschwindigkeit und Bewegungsrichtung initialisieren
        self.dx = random.uniform(-7, 7)
        self.dy = random.uniform(-7, 7)

        # Starte die Bewegung
        self.move_banana()

    # Funktion zur Bewegung der Banane
    def move_banana(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Aktualisiere Position basierend auf Geschwindigkeit
        self.x += self.dx
        self.y += self.dy

        # Kollisionsabfrage für den Rand des Bildschirms
        if self.x <= 0 or self.x >= screen_width - 100:
            self.dx = -self.dx  # Richtungswechsel bei Kollision mit der Seite
        if self.y <= 0 or self.y >= screen_height - 100:
            self.dy = -self.dy  # Richtungswechsel bei Kollision oben/unten

        # Fenster an die neue Position bewegen
        self.root.geometry(f"100x100+{int(self.x)}+{int(self.y)}")

        # Nach einer kurzen Verzögerung die Bewegung wiederholen
        self.root.after(20, self.move_banana)

# Hauptprogramm
if __name__ == "__main__":
    # Konfiguration laden oder erstellen
    banana_count = load_config()

    # Haupt-Tkinter-Fenster (root) initialisieren
    root = tk.Tk()
    root.withdraw()  # Verstecke das Hauptfenster

    # Mehrere Bananen erzeugen basierend auf der Anzahl in der config.ini
    for _ in range(banana_count):
        new_window = tk.Toplevel(root)  # Neues Fenster für jede Banane
        BananaPet(new_window)  # Jede Banane bekommt ihr eigenes Fenster

    root.mainloop()
