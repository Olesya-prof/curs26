import tkinter as tk
from tkinter import ttk
from datetime import datetime
import requests

coins = {
    'bitcoin': 'BTC',
    'ethereum': 'ETH',
    'solana': 'SOL',
    'cardano': 'ADA',
    'ripple': 'XRP',
    'dogecoin': 'DOGE'
}

root = tk.Tk()
root.title('Курсы криптовалют')
root.geometry ('450x350')
# Кнопка обновления
btn = tk.Button(root, text='Обновить курсы')
btn.pack(pady=10)
# Время обновления
time_lb = tk.Label(root, text='Обновлено: --')
time_lb.pack()
# таблица
table = ttk.Treeview(root,columns=('name', 'symbol', 'price'), show='headings', height=8)
table.heading('name', text='Криптовалюта')
table.heading('symbol', text='Символ')
table.heading('price', text='Цена (USD)')
table.column('name', width=120)
table.column('symbol', width=80)
table.column('price', width=100)
table.pack(pady=10, padx=10)

root.mainloop()
