from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
from tkinter import messagebox as mb
import os
import stepic
# print(f"📁 Программа работает в папке: {os.getcwd()}")
# print(f"📁 Файлы будут сохраняться сюда: {os.path.abspath('.')}")

# # ф-я для рисования на холсте
#
#
# def draw(event):
#     x, y = event.x, event.y
#     canvas.create_oval(x, y, x + 15, y + 15, fill= pen_color, outline= pen_color)
#
# def change_color(event, color):
#     global pen_color
#     pen_color = color
# pen_color = 'black'
#
# window = Tk()
# window.title ('Рисование на холсте')
#
# canvas = Canvas (window, width= 600, height= 400)
# canvas.pack()
# canvas.bind('<B1-Motion>', draw)
#
# red_label = Label(window, text="", bg='red',width= 8, height= 2)
# red_label.pack(side= LEFT)
# red_label.bind('<Button-1>',lambda event: change_color(event, 'red'))
#
# blue_label = Label(window, text="", bg='blue',width= 8, height= 2)
# blue_label.pack(side= LEFT)
# blue_label.bind('<Button-1>',lambda event: change_color(event, 'blue'))
#
# green_label = Label(window, text="", bg='green',width= 8, height= 2)
# green_label.pack(side= LEFT)
# green_label.bind('<Button-1>',lambda event: change_color(event, 'green'))
# window.mainloop()
def encode_text():
    image_path = file_path.get()
    text = text_to_encode.get()
    output_path = 'encoded_image.png'

    if not image_path or not text:
        mb.showwarning('Внимание', 'Выберите изображение и введите текст!')
        return

    if not os.path.exists(image_path):
        mb.showerror('Ошибка', f'Файл не найден!')
        return

    try:
        img = Image.open(image_path)

        # ✅ Кодируем в UTF-8
        encoded = stepic.encode(img, text.encode('utf-8'))
        encoded.save(output_path)

        full_path = os.path.abspath(output_path)
        file_path.set(full_path)

        mb.showinfo('Успех', f'✅ Текст зашифрован!\nФайл: {output_path}')
    except Exception as e:
        mb.showerror('Ошибка', f'Ошибка шифрования:\n{str(e)}')


def decode_text():
    image_path = file_path.get()

    if not image_path:
        mb.showwarning('Внимание', 'Выберите изображение!')
        return

    if not os.path.exists(image_path):
        mb.showerror('Ошибка', f'Файл не найден!')
        return

    try:
        img = Image.open(image_path)
        result = stepic.decode(img)

        # print("=" * 50)
        # print(f"ТИП: {type(result)}")
        # print(f"ЗНАЧЕНИЕ: {result}")
        # print("=" * 50)
        #
        # # ✅ УНИВЕРСАЛЬНОЕ ДЕКОДИРОВАНИЕ
        # text = None

        if isinstance(result, bytes):
            # Если это байты
            for encoding in ['utf-8', 'cp1251', 'koi8-r', 'cp866', 'latin1']:
                try:
                    text = result.decode(encoding)
                    print(f"✅ Декодировано с {encoding}")
                    break
                except:
                    continue
            if text is None:
                text = str(result)
        else:
            # Если это строка
            text = str(result)
            #Проверяем, не испорчена ли кодировка
            if 'Ð' in text or 'Ã' in text or 'â' in text:
                try:
                    # Перекодируем из cp1251 в utf-8
                    text = text.encode('latin1').decode('utf-8')
                    print("✅ Перекодировано из cp1251 в utf-8")
                except:
                    try:
                        text = text.encode('utf-8').decode('cp1251')
                        print("✅ Перекодировано из utf-8 в cp1251")
                    except:
                        pass

        print(f"РЕЗУЛЬТАТ: {text}")
        print("=" * 50)

        if text and text.strip():
            mb.showinfo('Результат', f'📄 {text}')
        else:
            mb.showwarning('Внимание', 'В изображении нет скрытого текста!')

    except Exception as e:
        mb.showerror('Ошибка', f'Ошибка расшифровки:\n{str(e)}')


def open_file():
    file = fd.askopenfilename(
        title='Выберите изображение',
        filetypes=[('Image files', '*.png *.jpg *.jpeg *.bmp *.gif')]
    )
    if file:
        file_path.set(file)


win = Tk()
win.title('Шифровка/Дешифровка в изображении')
win.geometry ('500x250')

# Путь к файлу
file_path = StringVar()
Label(win, text='Путь к изображению:').pack(pady=5)
Entry(win, textvariable=file_path, width= 50).pack(pady=5)
Button(win, text='Выбрать файл', command=open_file).pack(pady=5)

# Текст для шифрования
text_to_encode = StringVar()
Label (win, text='Текст для шифрования:').pack(pady=5)
Entry (win, textvariable= text_to_encode, width= 50).pack(pady=5)

# Кнопки для шифрования и дешифрования
Button (win, text='Зашифровать текст', command= encode_text, bg='Lightgreen').pack(pady=5)
Button (win, text='Расшифровать текст', command= decode_text, bg='Lightblue').pack(pady=5)

Label (win, text='Посде шифрования путь автоматически обновится', fg='gray').pack(pady=2)
win.mainloop()





