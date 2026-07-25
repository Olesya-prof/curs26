import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

# словарь кодов валют и их полныых названий
currencies = {
    'EUR': 'Евро',
    'JPY': 'Японская йена',
    'GBP': 'Британский фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'

}

def update_b_lb(event):
    code = b_combobox.get()
    name = currencies[code]
    b_lb.config(text=name)


def update_t_lb(event):
    code = t_combobox.get()
    name = currencies[code]
    t_lb.config(text=name)


def update_b1_lb():
    code = b1_combobox.get()
    name = currencies[code]
    b1_lb.config(text=name)



def exchange():
    target_code = t_combobox.get()
    base_code = b_combobox.get()
    base1_code = b1_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{base_code}")
            response.raise_for_status()
            data = response.json()

            base_name = currencies.get(base_code, base_code)
            target_name = currencies.get(target_code,target_code)

            if target_code in data['rates']:
                rate = data['rates'][target_code ]

                message = (
                    f"Курс обмена к {target_name} ({target_code}):\n\n"
                    f"{base_code}({base_name}) = {rate:.2f}{target_code}\n\n"
                )
                mb.showinfo("Курс обмена", message)

            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите код валюты")

win = Tk()
win.title('Курс обмена валюты')
win.geometry ('360x400')

lb =ttk.Label(win, text='Первая базовая валюта')
lb.pack(padx=10, pady=10)

b_combobox = ttk.Combobox(values=list(currencies.keys()))
b_combobox.pack(padx=10, pady=5)
b_combobox.bind("<<ComboboxSelected>>", update_b_lb)

b_lb = ttk.Label(win, text="Выберите валюту")
b_lb.pack(padx=10, pady=10)

lb = Label(win, text="Вторая базовая валюта")
lb.pack(padx=10, pady=5)

b1_combobox = ttk.Combobox(values=list(currencies.keys()))
b1_combobox.pack(padx=10, pady=5)
b1_combobox.bind("<<ComboboxSelected>>", update_b1_lb)

b1_lb = ttk.Label(win, text="Выберите валюту")
b1_lb.pack(padx=10, pady=10)

lb = Label(win, text="Целевая валюта")
lb.pack(padx=10, pady=5)

t_combobox = ttk.Combobox(values=list(currencies.keys()))
t_combobox.pack(padx=10, pady=5)
t_combobox.bind("<<ComboboxSelected>>", update_t_lb)

t_lb = ttk.Label(win, text="Выберите валюту")
t_lb.pack(padx=10, pady=10)



bt = ttk.Button(win, text="Получить курс обмена", command=exchange)
bt.pack(padx=10, pady=10)

win.mainloop()