#lepine client
from typing import Any
import customtkinter as ctk
import tkinter as tk
import fileinput
import build_exe
import os
 
#force the dark theme
ctk.set_appearance_mode("dark") 
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")    

#set the width and height of the window 
appWidth, appHeight = 800, 600
 
# App Class
class App(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.title("Lepine Client")
        self.geometry(f"{appWidth}x{appHeight}")
 
        # label of the exe file name
        self.nameLabel = ctk.CTkLabel(self,
                                      text="Name of ouput file")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                         placeholder_text="superh4x0rT00L.exe")
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # ip Label
        self.ipLabel = ctk.CTkLabel(self,
                                     text="IP")
        self.ipLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # IP Entry Field
        self.ipEntry = ctk.CTkEntry(self,
                            placeholder_text="ipadress:port")
        self.ipEntry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Build", command=self.build)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
        
        self.generateStartServerButton = ctk.CTkButton(self,
                                         text="Start Server", command=self.startserv)
        self.generateStartServerButton.grid(row=5, column=0,
                                        columnspan=1,
                                        padx=20, pady=20,
                                        sticky="ew")
        
    def build(self):
        hotecomplet = self.ipEntry.get().split(":")
        print(hotecomplet)
        # path of client script
        path = 'lepine_client.py'

        # findin
        new = "client = CLIENT("+'"'+hotecomplet[0]+'"'+","+hotecomplet[1]+")"

        # open the file and make a .bak
        with fileinput.FileInput(path, inplace=True, backup='.bak') as fichier:    
            for line, ligne in enumerate(fichier, start=1):
                if line == 610:
                    # write new content
                    print(new)
                else:
                    #do not edit
                    print(ligne, end='')
            print("host class created")
        name = self.nameEntry.get()
        if self.nameEntry.get() == "":
            name = self.nameEntry._placeholder_text
        build_exe.build(str(name))
        
    def startserv(self):
        os.system('python lepine_server.py')


 
if __name__ == "__main__":
    app = App()
    app.mainloop()