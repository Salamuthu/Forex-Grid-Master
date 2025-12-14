import tkinter as tk
import MetaTrader5 as mt5
from classes import Bot
from threading import Thread

root = tk.Tk()
root.title('Forex Grid Master')
root.geometry('300x780')
root.resizable(False, False)



COLORS = {
    'bg': '#1e1e1e',        # Dark Grey Background
    'fg': '#e0e0e0',        # Off-white text
    'entry_bg': '#2d2d2d',  # Lighter Grey for inputs
    'entry_fg': '#ffffff',  # White text for inputs
    'accent': '#007acc',    # Professional Blue
    'accent_hover': '#005f9e',
    'btn_text': '#ffffff'
}

FONTS = {
    'main': ('Segoe UI', 9),
    'bold': ('Segoe UI', 9, 'bold'),
    'header': ('Segoe UI', 10, 'bold')
}

root.configure(bg=COLORS['bg'])


try:
    icon = tk.PhotoImage(file='logo (1).png')
    root.iconphoto(False, icon)
except Exception:
    pass


lbl_style = {'bg': COLORS['bg'], 'fg': COLORS['fg'], 'font': FONTS['main'], 'anchor': 'w'}
entry_style = {
    'bg': COLORS['entry_bg'],
    'fg': COLORS['entry_fg'],
    'insertbackground': 'white',
    'relief': 'flat',
    'highlightthickness': 1,
    'highlightbackground': '#3e3e3e',
    'highlightcolor': COLORS['accent']
}
btn_style = {
    'bg': COLORS['accent'],
    'fg': COLORS['btn_text'],
    'font': FONTS['bold'],
    'relief': 'flat',
    'activebackground': COLORS['accent_hover'],
    'activeforeground': '#ffffff',
    'cursor': 'hand2'
}
grid_pad = {'padx': 6, 'pady': 4, 'sticky': 'ew'}


tk.Label(root, text="--- FOREX GRID MASTER ---", bg=COLORS['bg'], fg=COLORS['accent'], font=FONTS['header']).grid(row=0, column=0, columnspan=2, pady=(5, 5))

lbl_login = tk.Label(root, text='Login ID', **lbl_style)
lbl_password = tk.Label(root, text='Password', **lbl_style)
lbl_server = tk.Label(root, text='Server', **lbl_style)

txtb_login = tk.Entry(root, **entry_style)
txtb_password = tk.Entry(root, show="•", **entry_style)
txtb_server = tk.Entry(root, **entry_style)

def login():
    try:
        login_id = int(txtb_login.get())
        password = str(txtb_password.get())
        server = str(txtb_server.get())
        mt5.initialize(login=login_id, password=password, server=server)
    except ValueError:
        pass

btn_login = tk.Button(root, text='CONNECT', **btn_style, command=login)


lbl_login.grid(row=1, column=0, **grid_pad)
txtb_login.grid(row=1, column=1, **grid_pad)

lbl_password.grid(row=2, column=0, **grid_pad)
txtb_password.grid(row=2, column=1, **grid_pad)

lbl_server.grid(row=3, column=0, **grid_pad)
txtb_server.grid(row=3, column=1, **grid_pad)

btn_login.grid(row=4, column=1, columnspan=2, padx=2, pady=2, sticky='ew')



# BOT 1 SECTION

tk.Label(root, text="BOT 1 CONFIG ", bg=COLORS['bg'], fg=COLORS['accent'], font=FONTS['header']).grid(row=5, column=0, columnspan=2, pady=(2, 2), sticky='w', padx=10)

lbl_symbol_b1 = tk.Label(root, text='Symbol', **lbl_style)
lbl_volume_b1 = tk.Label(root, text='Volume', **lbl_style)
lbl_tp_b1 = tk.Label(root, text='Take Profit', **lbl_style)
lbl_no_of_levels_b1 = tk.Label(root, text='Levels', **lbl_style)
lbl_no_of_cycles_b1 = tk.Label(root, text='Cycles', **lbl_style)

txtb_symbol_b1 = tk.Entry(root, **entry_style)
txtb_volume_b1 = tk.Entry(root, **entry_style)
txtb_tp_b1 = tk.Entry(root, **entry_style)
txtb_levels_b1 = tk.Entry(root, **entry_style)
txtb_cycles_b1 = tk.Entry(root, **entry_style)

def run_b1():
    symbol = str(txtb_symbol_b1.get())
    volume = float(txtb_volume_b1.get())
    tp = float(txtb_tp_b1.get())
    levels = int(txtb_levels_b1.get())
    cycles = int(txtb_cycles_b1.get())

    bot = Bot(symbol, volume, tp, levels, cycles)
    thread = Thread(target=bot.run)
    thread.start()

btn_run_b1 = tk.Button(root, text='START BOT 1', **btn_style, command=run_b1)

# Grid Layout (Bot 1)
lbl_symbol_b1.grid(row=6, column=0, **grid_pad)
txtb_symbol_b1.grid(row=6, column=1, **grid_pad)

lbl_volume_b1.grid(row=7, column=0, **grid_pad)
txtb_volume_b1.grid(row=7, column=1, **grid_pad)

lbl_tp_b1.grid(row=8, column=0, **grid_pad)
txtb_tp_b1.grid(row=8, column=1, **grid_pad)

lbl_no_of_levels_b1.grid(row=9, column=0, **grid_pad)
txtb_levels_b1.grid(row=9, column=1, **grid_pad)

lbl_no_of_cycles_b1.grid(row=10, column=0, **grid_pad)
txtb_cycles_b1.grid(row=10, column=1, **grid_pad)

btn_run_b1.grid(row=11, column=1, columnspan=2, padx=2, pady=2, sticky='ew')



# BOT 2 SECTION

tk.Label(root, text="BOT 2 CONFIG ", bg=COLORS['bg'], fg=COLORS['accent'], font=FONTS['header']).grid(row=12, column=0, columnspan=2, pady=(2, 2), sticky='w', padx=10)

lbl_symbol_b2 = tk.Label(root, text='Symbol', **lbl_style)
lbl_volume_b2 = tk.Label(root, text='Volume', **lbl_style)
lbl_tp_b2 = tk.Label(root, text='Take Profit', **lbl_style)
lbl_no_of_levels_b2 = tk.Label(root, text='Levels', **lbl_style)
lbl_no_of_cycles_b2 = tk.Label(root, text='Cycles', **lbl_style)

txtb_symbol_b2 = tk.Entry(root, **entry_style)
txtb_volume_b2 = tk.Entry(root, **entry_style)
txtb_tp_b2 = tk.Entry(root, **entry_style)
txtb_levels_b2 = tk.Entry(root, **entry_style)
txtb_cycles_b2 = tk.Entry(root, **entry_style)

def run_b2():
    symbol = str(txtb_symbol_b2.get())
    volume = float(txtb_volume_b2.get())
    tp = float(txtb_tp_b2.get())
    levels = int(txtb_levels_b2.get())
    cycles = int(txtb_cycles_b2.get())

    bot = Bot(symbol, volume, tp, levels, cycles)
    thread = Thread(target=bot.run)
    thread.start()

btn_run_b2 = tk.Button(root, text='START BOT 2', **btn_style, command=run_b2)

# Grid Layout (Bot 2)
lbl_symbol_b2.grid(row=13, column=0, **grid_pad)
txtb_symbol_b2.grid(row=13, column=1, **grid_pad)

lbl_volume_b2.grid(row=14, column=0, **grid_pad)
txtb_volume_b2.grid(row=14, column=1, **grid_pad)

lbl_tp_b2.grid(row=15, column=0, **grid_pad)
txtb_tp_b2.grid(row=15, column=1, **grid_pad)

lbl_no_of_levels_b2.grid(row=16, column=0, **grid_pad)
txtb_levels_b2.grid(row=16, column=1, **grid_pad)

lbl_no_of_cycles_b2.grid(row=17, column=0, **grid_pad)
txtb_cycles_b2.grid(row=17, column=1, **grid_pad)

btn_run_b2.grid(row=18, column=1, columnspan=2, padx=2, pady=2, sticky='ew')



# BOT 3 SECTION

tk.Label(root, text="BOT 3 CONFIG ", bg=COLORS['bg'], fg=COLORS['accent'], font=FONTS['header']).grid(row=19, column=0, columnspan=2, pady=(2, 2), sticky='w', padx=10)

lbl_symbol_b3 = tk.Label(root, text='Symbol', **lbl_style)
lbl_volume_b3 = tk.Label(root, text='Volume', **lbl_style)
lbl_tp_b3 = tk.Label(root, text='Take Profit', **lbl_style)
lbl_no_of_levels_b3 = tk.Label(root, text='Levels', **lbl_style)
lbl_no_of_cycles_b3 = tk.Label(root, text='Cycles', **lbl_style)

txtb_symbol_b3 = tk.Entry(root, **entry_style)
txtb_volume_b3 = tk.Entry(root, **entry_style)
txtb_tp_b3 = tk.Entry(root, **entry_style)
txtb_levels_b3 = tk.Entry(root, **entry_style)
txtb_cycles_b3 = tk.Entry(root, **entry_style)

def run_b3():
    symbol = str(txtb_symbol_b3.get())
    volume = float(txtb_volume_b3.get())
    tp = float(txtb_tp_b3.get())
    levels = int(txtb_levels_b3.get())
    cycles = int(txtb_cycles_b3.get())

    bot = Bot(symbol, volume, tp, levels, cycles)
    thread = Thread(target=bot.run)
    thread.start()

btn_run_b3 = tk.Button(root, text='START BOT 3', **btn_style, command=run_b3)

# Grid Layout (Bot 3)
lbl_symbol_b3.grid(row=20, column=0, **grid_pad)
txtb_symbol_b3.grid(row=20, column=1, **grid_pad)

lbl_volume_b3.grid(row=21, column=0, **grid_pad)
txtb_volume_b3.grid(row=21, column=1, **grid_pad)

lbl_tp_b3.grid(row=22, column=0, **grid_pad)
txtb_tp_b3.grid(row=22, column=1, **grid_pad)

lbl_no_of_levels_b3.grid(row=23, column=0, **grid_pad)
txtb_levels_b3.grid(row=23, column=1, **grid_pad)

lbl_no_of_cycles_b3.grid(row=24, column=0, **grid_pad)
txtb_cycles_b3.grid(row=24, column=1, **grid_pad)

btn_run_b3.grid(row=25, column=1, columnspan=2, padx=2, pady=2, sticky='ew')


root.grid_columnconfigure(1, weight=1)

root.mainloop()