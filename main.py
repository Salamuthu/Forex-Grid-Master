import tkinter as tk
from threading import Thread
import MetaTrader5 as mt5
from classes import Bot

# --- STYLE CONFIGURATION ---
COLORS = {
    'bg_main': '#121212',  # Deep Black
    'bg_card': '#1E1E1E',  # Card Background
    'text_main': '#E0E0E0',  # White-ish text
    'text_dim': '#757575',  # Placeholder text
    'input_bg': '#252525',  # Input field background
    'input_fg': '#FFFFFF',
    'accent_blue': '#2196F3',  # Bot 1
    'accent_orange': '#FF9800',  # Bot 2
    'accent_purple': '#9C27B0',  # Bot 3
    'success': '#4CAF50',  # Connect Button
}

FONTS = {
    'header': ('Segoe UI', 9, 'bold'),
    'input': ('Consolas', 9),
    'btn': ('Segoe UI', 8, 'bold')
}


# --- HELPER CLASS FOR STYLISH INPUTS ---
class CompactEntry(tk.Frame):
    def __init__(self, parent, placeholder, is_password=False):
        super().__init__(parent, bg=COLORS['input_bg'], padx=5, pady=3)
        self.entry = tk.Entry(
            self, bg=COLORS['input_bg'], fg=COLORS['input_fg'],
            font=FONTS['input'], relief='flat', insertbackground='white',
            show="•" if is_password else ""
        )
        self.entry.pack(fill='both')

        self.placeholder = placeholder
        if placeholder:
            self.entry.insert(0, placeholder)
            self.entry.config(fg=COLORS['text_dim'])
            self.entry.bind("<FocusIn>", self._clear_placeholder)
            self.entry.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, tk.END)
            self.entry.config(fg=COLORS['input_fg'])

    def _add_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg=COLORS['text_dim'])

    def get(self):
        val = self.entry.get()
        return val if val != self.placeholder else ""


# --- MAIN APP ---
root = tk.Tk()
root.title('Forex Grid Master')
root.geometry('290x700')  # Compact size
root.configure(bg=COLORS['bg_main'])
root.resizable(False, False)

try:
    icon = tk.PhotoImage(file='logo (1).png')
    root.iconphoto(False, icon)
except Exception:
    pass

# Container to hold everything neatly
main_container = tk.Frame(root, bg=COLORS['bg_main'], padx=10, pady=10)
main_container.pack(fill='both', expand=True)

# --- LOGIN SECTION ---
lbl_login_header = tk.Label(main_container, text="TERMINAL ACCESS", bg=COLORS['bg_main'], fg=COLORS['text_dim'],
                            font=FONTS['header'])
lbl_login_header.pack(anchor='w', pady=(0, 5))

fr_auth = tk.Frame(main_container, bg=COLORS['bg_card'], padx=10, pady=10)
fr_auth.pack(fill='x', pady=(0, 15))

txtb_login = CompactEntry(fr_auth, "Login ID")
txtb_login.pack(fill='x', pady=2)

txtb_password = CompactEntry(fr_auth, "Password", is_password=True)
txtb_password.pack(fill='x', pady=2)

txtb_server = CompactEntry(fr_auth, "Server")
txtb_server.pack(fill='x', pady=(2, 8))


def login():
    try:
        login_id = int(txtb_login.get())
        password = str(txtb_password.get())
        server = str(txtb_server.get())
        if mt5.initialize(login=login_id, password=password, server=server):
            print("Connected")
        else:
            print("Failed")
    except ValueError:
        pass


btn_login = tk.Button(fr_auth, text='CONNECT', bg=COLORS['success'], fg='white', font=FONTS['btn'], relief='flat',
                      command=login)
btn_login.pack(fill='x')

# --- BOT 1 SECTION ---
fr_b1 = tk.Frame(main_container, bg=COLORS['bg_card'])
fr_b1.pack(fill='x', pady=(0, 10))

# Color strip
tk.Frame(fr_b1, bg=COLORS['accent_blue'], width=3).pack(side='left', fill='y')

# Content
content_b1 = tk.Frame(fr_b1, bg=COLORS['bg_card'], padx=10, pady=8)
content_b1.pack(side='left', fill='both', expand=True)

tk.Label(content_b1, text="Bot 1", bg=COLORS['bg_card'], fg=COLORS['accent_blue'], font=FONTS['header']).pack(
    anchor='w', pady=(0, 5))

grid_b1 = tk.Frame(content_b1, bg=COLORS['bg_card'])
grid_b1.pack(fill='x')

txtb_symbol_b1 = CompactEntry(grid_b1, "Symbol")
txtb_symbol_b1.grid(row=0, column=0, padx=(0, 2), pady=2, sticky='ew')

txtb_volume_b1 = CompactEntry(grid_b1, "Vol (0.01)")
txtb_volume_b1.grid(row=0, column=1, padx=(2, 0), pady=2, sticky='ew')

txtb_tp_b1 = CompactEntry(grid_b1, "TP")
txtb_tp_b1.grid(row=1, column=0, padx=(0, 2), pady=2, sticky='ew')

txtb_levels_b1 = CompactEntry(grid_b1, "Levels")
txtb_levels_b1.grid(row=1, column=1, padx=(2, 0), pady=2, sticky='ew')

txtb_cycles_b1 = CompactEntry(grid_b1, "Cycles")
txtb_cycles_b1.grid(row=2, column=0, columnspan=2, pady=(2, 5), sticky='ew')

grid_b1.columnconfigure(0, weight=1)
grid_b1.columnconfigure(1, weight=1)


def run_b1():
    try:
        symbol = str(txtb_symbol_b1.get())
        volume = float(txtb_volume_b1.get())
        tp = float(txtb_tp_b1.get())
        levels = int(txtb_levels_b1.get())
        cycles = int(txtb_cycles_b1.get())
        bot = Bot(symbol, volume, tp, levels, cycles)
        Thread(target=bot.run).start()
    except ValueError:
        print("Check Bot 1 Inputs")


btn_run_b1 = tk.Button(content_b1, text='START BOT 1', bg=COLORS['accent_blue'], fg='white', font=FONTS['btn'],
                       relief='flat', command=run_b1)
btn_run_b1.pack(fill='x')

# --- BOT 2 SECTION ---
fr_b2 = tk.Frame(main_container, bg=COLORS['bg_card'])
fr_b2.pack(fill='x', pady=(0, 10))

tk.Frame(fr_b2, bg=COLORS['accent_orange'], width=3).pack(side='left', fill='y')

content_b2 = tk.Frame(fr_b2, bg=COLORS['bg_card'], padx=10, pady=8)
content_b2.pack(side='left', fill='both', expand=True)

tk.Label(content_b2, text="Bot 2", bg=COLORS['bg_card'], fg=COLORS['accent_orange'], font=FONTS['header']).pack(
    anchor='w', pady=(0, 5))

grid_b2 = tk.Frame(content_b2, bg=COLORS['bg_card'])
grid_b2.pack(fill='x')

txtb_symbol_b2 = CompactEntry(grid_b2, "Symbol")
txtb_symbol_b2.grid(row=0, column=0, padx=(0, 2), pady=2, sticky='ew')

txtb_volume_b2 = CompactEntry(grid_b2, "Vol (0.01)")
txtb_volume_b2.grid(row=0, column=1, padx=(2, 0), pady=2, sticky='ew')

txtb_tp_b2 = CompactEntry(grid_b2, "TP")
txtb_tp_b2.grid(row=1, column=0, padx=(0, 2), pady=2, sticky='ew')

txtb_levels_b2 = CompactEntry(grid_b2, "Levels")
txtb_levels_b2.grid(row=1, column=1, padx=(2, 0), pady=2, sticky='ew')

txtb_cycles_b2 = CompactEntry(grid_b2, "Cycles")
txtb_cycles_b2.grid(row=2, column=0, columnspan=2, pady=(2, 5), sticky='ew')

grid_b2.columnconfigure(0, weight=1)
grid_b2.columnconfigure(1, weight=1)


def run_b2():
    try:
        symbol = str(txtb_symbol_b2.get())
        volume = float(txtb_volume_b2.get())
        tp = float(txtb_tp_b2.get())
        levels = int(txtb_levels_b2.get())
        cycles = int(txtb_cycles_b2.get())
        bot = Bot(symbol, volume, tp, levels, cycles)
        Thread(target=bot.run).start()
    except ValueError:
        print("Check Bot 2 Inputs")


btn_run_b2 = tk.Button(content_b2, text='START BOT 2', bg=COLORS['accent_orange'], fg='white', font=FONTS['btn'],
                       relief='flat', command=run_b2)
btn_run_b2.pack(fill='x')

# --- BOT 3 SECTION ---
fr_b3 = tk.Frame(main_container, bg=COLORS['bg_card'])
fr_b3.pack(fill='x', pady=(0, 10))

tk.Frame(fr_b3, bg=COLORS['accent_purple'], width=3).pack(side='left', fill='y')

content_b3 = tk.Frame(fr_b3, bg=COLORS['bg_card'], padx=10, pady=8)
content_b3.pack(side='left', fill='both', expand=True)

tk.Label(content_b3, text="Bot 3", bg=COLORS['bg_card'], fg=COLORS['accent_purple'],
         font=FONTS['header']).pack(anchor='w', pady=(0, 5))

grid_b3 = tk.Frame(content_b3, bg=COLORS['bg_card'])
grid_b3.pack(fill='x')

txtb_symbol_b3 = CompactEntry(grid_b3, "Symbol")
txtb_symbol_b3.grid(row=0, column=0, padx=(0, 2), pady=2, sticky='ew')

txtb_volume_b3 = CompactEntry(grid_b3, "Vol (0.01)")
txtb_volume_b3.grid(row=0, column=1, padx=(2, 0), pady=2, sticky='ew')

txtb_tp_b3 = CompactEntry(grid_b3, "TP")
txtb_tp_b3.grid(row=1, column=0, padx=(0, 2), pady=2, sticky='ew')

txtb_levels_b3 = CompactEntry(grid_b3, "Levels")
txtb_levels_b3.grid(row=1, column=1, padx=(2, 0), pady=2, sticky='ew')

txtb_cycles_b3 = CompactEntry(grid_b3, "Cycles")
txtb_cycles_b3.grid(row=2, column=0, columnspan=2, pady=(2, 5), sticky='ew')

grid_b3.columnconfigure(0, weight=1)
grid_b3.columnconfigure(1, weight=1)


def run_b3():
    try:
        symbol = str(txtb_symbol_b3.get())
        volume = float(txtb_volume_b3.get())
        tp = float(txtb_tp_b3.get())
        levels = int(txtb_levels_b3.get())
        cycles = int(txtb_cycles_b3.get())
        bot = Bot(symbol, volume, tp, levels, cycles)
        Thread(target=bot.run).start()
    except ValueError:
        print("Check Bot 3 Inputs")


btn_run_b3 = tk.Button(content_b3, text='START BOT 3', bg=COLORS['accent_purple'], fg='white', font=FONTS['btn'],
                       relief='flat', command=run_b3)
btn_run_b3.pack(fill='x')

root.mainloop()