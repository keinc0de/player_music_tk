from tkinter import ttk
import tkinter as tk
from pathlib import Path
from mi_config import MiConfig


class Playlist(tk.Listbox):
    def __init__(self, parent, *args, **kw):
        super(Playlist, self).__init__(master=parent, *args, **kw)
        self._widget_init()

    def _widget_init(self):
        self.ELEMENTOS = []
        self.DC = {}
        self.var_elementos = tk.StringVar(value=self.ELEMENTOS)
        self.recarga_configs()

    def recarga_configs(self):
        cf = self._obten_configs()
        self.config(
            listvariable=self.var_elementos,
            bg=cf.get('bg'),
            fg=cf.get('fg'),
            activestyle='none',
            selectbackground=cf.get('select bg'),
            selectforeground=cf.get('select fg'),
            relief='flat',
            bd=0, borderwidth=0, border=0,
            highlightthickness=0,
            font=(cf.get('font'), cf.get('font size'), "normal"),
        )

    def _obten_configs(self):
        return MiConfig('mi_player.config', header='[[CONFIG]] MI PLAYER')
    
    def asigna_elementos(self, elems:list):
        self.DC = {Path(e).name:Path(e).parent.as_posix() for e in elems}
        self.var_elementos.set(list(self.DC.keys()))


class Ventana(tk.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.geometry("420x300")

        li = [
            "O:/MUSICA/Rodrigo - Cuarteto/rodrigo cut version/01 yerba mala.mp3",
            "O:/MUSICA/Rodrigo - Cuarteto/rodrigo cut version/11 por lo que yo te quiero.mp3"
        ]

        self.wli = Playlist(self)
        self.wli.grid(row=0, column=0, sticky="wens", padx=4)
        self.wli.asigna_elementos(li)
        # self.obten_musicas()
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
            
if __name__=="__main__":
    app = Ventana()
    app.config(bg='gray10')
    app.mainloop()