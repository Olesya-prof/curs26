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

# Получает курсы и обновляет таблицу
def get_prices():
    try:
        ids = ','.join(coins.keys()) # получает все id монет из словаря
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true'
        data = requests.get(url, timeout=5).json() # отправляет GET-запрос по URL,ждёт ответа максимум 5 сек

        # Очищаем таблицу
        for row in table.get_children():
            table.delete(row)

        # Заполняем таблицу
        for coin_id, symbol in coins.items() :
            if coin_id in data:
                price = data[coin_id]['usd']
                table.insert('', 'end', values=(
                    coin_id.capitalize(),
                    symbol,
                    f'${price:,.2f}'
                ))

        # Обновляем время , текст на метке
        time_lb.config (text=f'Обновлено: {datetime.now().strftime("%H:%M:%S")}')
        status_lb.config(text='Данные загружены', fg='green')

    except Exception as e:
        time_lb.config(text='Ошибка! Проверьте интернет')
        status_lb(text='Ошибка загрузки', fg='red')

root = tk.Tk()
root.title('Курсы криптовалют')
root.geometry ('450x350')
# Кнопка обновления
btn = tk.Button(root, text='Обновить курсы', command=get_prices, bg='green', fg='white')
btn.pack(pady=10)
# Время обновления
time_lb = tk.Label(root, text='Обновлено: --')
time_lb.pack()

status_lb = tk.Label(root, text='Статус: --', fg='gray')
status_lb.pack(side=tk.BOTTOM , pady=10)
# таблица
table = ttk.Treeview(root,columns=('name', 'symbol', 'price'), show='headings', height=8)
table.heading('name', text='Криптовалюта')
table.heading('symbol', text='Символ')
table.heading('price', text='Цена (USD)')
table.column('name', width=120)
table.column('symbol', width=80)
table.column('price', width=100)
table.pack(pady=10, padx=10)

# Загружаем сразу при запуске
get_prices()

root.mainloop()
