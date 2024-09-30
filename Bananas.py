import tkinter as tk
from PIL import Image, ImageTk
import random
import configparser
import os


def load_config():
    config = configparser.ConfigParser()
    config_file = './config.ini'


    if not os.path.exists(config_file):

        config['Config'] = {'Bananas': '1'}  
        with open(config_file, 'w') as configfile:
            config.write(configfile)


    config.read(config_file)
    return int(config['Config'].get('Bananas', 1))  


class BananaPet:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True) 
        self.root.config(bg='white', highlightthickness=0)  
        self.root.wm_attributes("-transparentcolor", "white") 
        self.root.wm_attributes("-topmost", True)  


        self.root.geometry("100x100")


        self.banana_image = Image.open("banana.png")  
        self.banana_image = self.banana_image.resize((100, 100), Image.ANTIALIAS)
        self.banana_photo = ImageTk.PhotoImage(self.banana_image)


        self.banana_label = tk.Label(self.root, image=self.banana_photo, bg="white")
        self.banana_label.pack()

   
        self.x = random.randint(0, self.root.winfo_screenwidth() - 100)
        self.y = random.randint(0, self.root.winfo_screenheight() - 100)


        self.dx = random.uniform(-7, 7)
        self.dy = random.uniform(-7, 7)


        self.move_banana()


    def move_banana(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()


        self.x += self.dx
        self.y += self.dy


        if self.x <= 0 or self.x >= screen_width - 100:
            self.dx = -self.dx  
        if self.y <= 0 or self.y >= screen_height - 100:
            self.dy = -self.dy  


        self.root.geometry(f"100x100+{int(self.x)}+{int(self.y)}")


        self.root.after(20, self.move_banana)


if __name__ == "__main__":

    banana_count = load_config()


    root = tk.Tk()
    root.withdraw()  


    for _ in range(banana_count):
        new_window = tk.Toplevel(root) 
        BananaPet(new_window)  

    root.mainloop()
