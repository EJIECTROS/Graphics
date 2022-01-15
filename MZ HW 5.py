import tkinter as tk
import time
import random

colors = ["red", "yellow", "blue", "green"]
start_time = 0
results_list = list()
wrong_clicks = 0
right_clicks = 0


win = tk.Tk()
photo = tk.PhotoImage(file='venv/fun.jpg')# указываем путь для картинки
win.iconphoto(False, photo) #указываем фотку для лого
win.config(bg="#b7e8e6") # задаем задний фон
win.title('графическое приложение')
win.geometry("600x500+700+50") # размер и расположение на экране
win.resizable(True,True) # можем запретить или разрешить расширение или уменьшение окна
win.minsize(100,100)# указваем минимальный размер окна
win.maxsize(500,500)# задаем максимальный размер окна
bottom_frame = tk.Frame(win)
bottom_frame.pack(side="bottom")

label = tk.Label(
        text='''Приложение 
для выявления 
скорости реакции''',
    font=("Arial", 10, 'bold'),
    foreground="white",
    background='black',
    width=15,  # ширина ( сколько символов поместится )
    height=2,  # высота ( сколько символов поместится )
    padx=20,  # (отступы от краев) x - по ширине
    pady=20,  # (отступы от краев) y - по высоте
    anchor="s",  # n-вверху  s-внизу w-слева e- справа ( так же можно комбинировать, на пример sw)
    relief=tk.RAISED,  # обтекание кнопки по краям(четкие границы, по умолчанию идут 2пикселя)
    bd=5,  # ширина обтикания кнопки
    justify=tk.CENTER,
    # Выравнивание текста по центру либо сторонам, применяется в случае использования '''МНОГОСТРОЧНОЙ СТРОКИ'''
)
label_right = tk.Label(bottom_frame,
                       text="Правильные: 0",
                       foreground="green"

                       )

label_wrong = tk.Label(bottom_frame,
                       text="Неправильные: 0",
                       foreground="red"

                       )


def send_info():
    global right_clicks, wrong_clicks
    if label["background"] == "red":
        difference = round(time.time() - start_time, 3)
        result.config(text=f"Время: {difference} сек.")
        right_clicks += 1
        label_right.config(text=f"Правильные: {right_clicks}")
        label.config(background="grey")
    else:
        wrong_clicks += 1
        label_wrong.config(text=f"Неправильные: {wrong_clicks}")
        label.config(background="grey")
        win.update()
        time.sleep(1)


button = tk.Button(
        text="Click here if red",
    font=("Arial", 10, 'bold'),
    foreground="white",
    background='red',
    width=15,  # ширина ( сколько символов поместится )
    height=2,  # высота ( сколько символов поместится )
    padx=20,  # (отступы от краев) x - по ширине
    pady=20,  # (отступы от краев) y - по высоте
    relief=tk.RAISED,  # обтекание кнопки по краям(четкие границы, по умолчанию идут 2пикселя)
    bd=20,  # ширина обтикания кнопки
    justify=tk.CENTER,
    # Выравнивание текста по центру либо сторонам, применяется в случае использования '''МНОГОСТРОЧНОЙ СТРОКИ'''
        command=send_info
)

result = tk.Label(
        text="0.0",
    font=("Arial", 30, 'bold'),
    foreground="red",
    background='white',
    width=15,  # ширина ( сколько символов поместится )
    height=2,  # высота ( сколько символов поместится )
    padx=20,  # (отступы от краев) x - по ширине
    pady=20,  # (отступы от краев) y - по высоте
)

for c in win.children:
    win.children[c].pack()

label_wrong.pack(side="left")
label_right.pack(side="right")


def timer_update():
    global start_time
    label.config(background=colors[random.randint(0, 3)])
    if label["background"] == "red":
        start_time = time.time()

    win.after(random.randint(500, 2500), timer_update)


win.after(random.randint(500, 2500), timer_update)

win.mainloop()
