#библиотеки
from tkinter import *
import time



#переменные
money = 0
oranges = 0
helper = 0
upgrade_level = 0
upgrade_cost = 0



#окно
okno = Tk()
okno.title('Апельсин?')
okno.geometry("1050x550")
okno["bg"] = "black" 



#defs 
def plant():
    global oranges
    global money
    #прибавка в зависимости от уровня пракачки
    if upgrade_level == 0:
        oranges = oranges + 1
    if upgrade_level == 1:
        oranges = oranges + 5
    if upgrade_level == 2:
        oranges = oranges + 40
    if upgrade_level == 3:
        oranges = oranges + 100
    if upgrade_level == 4:
        oranges = oranges + 400
    if upgrade_level == 5:
        oranges = oranges + 1000
    if upgrade_level == 6:
        oranges = oranges + 4000
    if upgrade_level == 7:
        oranges = oranges + 66666
    if upgrade_level == 8:
        oranges = oranges + 987654
    if upgrade_level == 9:
        oranges = oranges + 9999999
    if upgrade_level == 10:
        oranges = oranges + 100000000
    oranges_text['text'] = "Апельсинчики : " + str(oranges)
    money_text['text'] = "Монет : " + str(money)


def shoping():
    shop = Tk()
    shop.title('Апельсиновый магазин')
    shop.geometry("550x550")
    shop["bg"] = "black"

    #экран магазина
    #продать апельсины
    oranges_remove_to_cash = Button(shop, text="Продать апельсины", background="#03071e", foreground="#ffba08", activeforeground = "#ffba08", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 16, "bold"), width = "14", height = "2", command = sell_oranges)
    oranges_remove_to_cash.pack()
    oranges_remove_to_cash.place(x=10, y=5)


    #купить бустер
    busters_button = Button(shop, text="Прокачки", background="#03071e", foreground="#ffba08", activeforeground = "#ffba08", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 16, "bold"), width = "14", height = "2", command = bye_busters)
    busters_button.pack()
    busters_button.place(x=10, y=115)

    
def sell_oranges():
    seil_oranges = Tk()
    seil_oranges.title('Рынок апельсинов')
    seil_oranges.geometry("450x900")
    seil_oranges["bg"] = "black"

    #количество имеющихся всех апельсинов
    kurs_oranges = Label(seil_oranges, text="У тебя апельсинов: " + str(oranges), foreground = "white", background = "Black", font = ("Verdana", 12, "bold"))
    kurs_oranges.pack()
    kurs_oranges.place(x=100, y=30)
    
    #продать апельсинчички 100
    orange_seil_100 = Button(seil_oranges, text="Продать 100 апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "19", height = "2", command = oranges_100_to_cash)
    orange_seil_100.pack()
    orange_seil_100.place(x=50, y=75)

    #продать апельсинчички 500
    orange_seil_500 = Button(seil_oranges, text="Продать 500 апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "19", height = "2", command = oranges_500_to_cash)
    orange_seil_500.pack()
    orange_seil_500.place(x=50, y=165)
    
    #продать апельсинчички 1000
    orange_seil_1000 = Button(seil_oranges, text="Продать 1K апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "20", height = "2", command = oranges_1000_to_cash)
    orange_seil_1000.pack()
    orange_seil_1000.place(x=45, y=255)

    #продать все апельсинчички 
    orange_seil_all = Button(seil_oranges, text="Продать 10K апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "21", height = "2", command = oranges_all_to_cash)
    orange_seil_all.pack()
    orange_seil_all.place(x=40, y=345)

    #продать 100K апельсинчички 
    orange_seil_100000 = Button(seil_oranges, text="Продать 100K апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "21", height = "2", command = oranges_100000_to_cash)
    orange_seil_100000.pack()
    orange_seil_100000.place(x=40, y=435)

    #продать 1M апельсинчички 
    orange_seil_1m = Button(seil_oranges, text="Продать 1M апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "21", height = "2", command = oranges_1m_to_cash)
    orange_seil_1m.pack()
    orange_seil_1m.place(x=40, y=525)

    #продать 10M апельсинчички 
    orange_seil_10m = Button(seil_oranges, text="Продать 10M апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "21", height = "2", command = oranges_10m_to_cash)
    orange_seil_10m.pack()
    orange_seil_10m.place(x=40, y=615)

    #продать 100M апельсинчички 
    orange_seil_100m = Button(seil_oranges, text="Продать 100M апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "21", height = "2", command = oranges_100m_to_cash)
    orange_seil_100m.pack()
    orange_seil_100m.place(x=40, y=615)

    #продать 1B апельсинчички 
    orange_seil_1b = Button(seil_oranges, text="Продать 1B апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "21", height = "2", command = oranges_1b_to_cash)
    orange_seil_1b.pack()
    orange_seil_1b.place(x=40, y=705)

    #продать 10B апельсинчички 
    orange_seil_10b = Button(seil_oranges, text="Продать 10B апельсинов", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "21", height = "2", command = oranges_10b_to_cash)
    orange_seil_10b.pack()
    orange_seil_10b.place(x=40, y=795)

    #курс для продажи за один апельсин
    kurs_oranges = Label(seil_oranges, text="Цена за апельсин: 0.1 монет/апельсин", foreground = "white", background = "Black", font = ("Verdana", 12, "bold"))
    kurs_oranges.pack()
    kurs_oranges.place(x=10, y=5)


def oranges_100_to_cash():
    global oranges
    global money
    if oranges > 100 or oranges == 100:
        oranges = oranges - 100
        money = money + 10
    else:
        None

def oranges_500_to_cash():
    global oranges
    global money
    if oranges > 500 or oranges == 500:
        oranges = oranges - 500
        money = money + 50
    else:
        None

def oranges_1000_to_cash():
    global oranges
    global money
    if oranges > 1000 or oranges == 1000:
        oranges = oranges - 1000
        money = money + 100
    else:
        None

def oranges_100000_to_cash():
    global oranges
    global money
    if oranges > 100000 or oranges == 100000:
        oranges = oranges - 100000
        money = money + 10000
    else:
        None

def oranges_1m_to_cash():
    global oranges
    global money
    if oranges > 1000000 or oranges == 1000000:
        oranges = oranges - 1000000
        money = money + 100000
    else:
        None

def oranges_10m_to_cash():
    global oranges
    global money
    if oranges > 10000000 or oranges == 10000000:
        oranges = oranges - 10000000
        money = money + 1000000
    else:
        None

def oranges_100m_to_cash():
    global oranges
    global money
    if oranges > 100000000 or oranges == 100000000:
        oranges = oranges - 100000000
        money = money + 10000000
    else:
        None

def oranges_1b_to_cash():
    global oranges
    global money
    if oranges > 1000000000 or oranges == 1000000000:
        oranges = oranges - 1000000000
        money = money + 100000000
    else:
        None

def oranges_10b_to_cash():
    global oranges
    global money
    if oranges > 10000000000 or oranges == 10000000000:
        oranges = oranges - 10000000000
        money = money + 1000000000
    else:
        None

def oranges_all_to_cash():
    global oranges
    global money
    if oranges > 10000 or oranges == 10000:
        oranges = oranges - 10000
        money = money + 1000
    else:
        None


def bye_busters():
    global upgrade_level
    global upgrade_cost
    busters = Tk()
    busters.title('Прокачки')
    busters.geometry("700x450")
    busters["bg"] = "black"
    
    #апгрейд первого уровня с текстом в комплекте 
    level_up_1 = Button(busters, text="Улучшиться на все деньги, минимум - ", background="#03071e", foreground="#eb5e28", activeforeground = "#ee9b00", activebackground="#03071e",anchor = "w", padx="20", pady="8", bd = 0, font = ("Verdana", 14, "bold"), width = "42", height = "2", command = upgrading)
    level_up_1.pack()
    level_up_1.place(x=40, y=10)
    str(upgrade_cost) + " монет"
    cost_level_up = Label(busters, text=str(upgrade_cost) + " монет", foreground = "#eb5e28", background = "#03071e", font = ("Verdana", 14, "bold"))
    yours_level = Label(busters, text="Ваш уровень: " + str(upgrade_level), foreground = "#f48c06", background = "black", font = ("Verdana", 14, "bold"))
    yours_level.pack()
    yours_level.place(x=240, y=105)
    cost_level_up.pack()
    cost_level_up.place(x=500, y=32)
    #апгрейд левел (не обращай внимания)
    if upgrade_level == 0:
        upgrade_cost = upgrade_cost - upgrade_cost + 15
    if upgrade_level == 1:
        upgrade_cost = upgrade_cost - upgrade_cost + 100
    if upgrade_level == 2:
        upgrade_cost = upgrade_cost - upgrade_cost + 500
    if upgrade_level == 3:
        upgrade_cost = "3K"
    if upgrade_level == 4:
        upgrade_cost = "10K"
    if upgrade_level == 5:
        upgrade_cost = "40K"
    if upgrade_level == 6:
        upgrade_cost = "200K"
    if upgrade_level == 7:
        upgrade_cost = "1.5M"
    if upgrade_level == 8:
        upgrade_cost = "125M"
    if upgrade_level == 9:
        upgrade_cost = "4B"
    if upgrade_level == 10:
        upgrade_cost = "75B"
    if upgrade_level == 11:
        upgrade_cost = "MAX"

    #памятка
    pamatka1_upgrade = Label(busters, text=" 0 уровень - 1 апельсин/клик   \n 1 уровень - 5 апельсин/клик   \n  2 уровень - 40 апельсин/клик  \n   3 уровень - 100 апельсин/клик \n   4 уровень - 400 апельсин/клик \n5 уровень - 1K апельсин/клик\n  6 уровень - 4K апельсин/клик  \n    7 уровень - 66K апельсин/клик  \n     8 уровень - 987K апельсин/клик \n   9 уровень - 9M апельсин/клик   \n      10 уровень - 100M апельсин/клик", foreground = "white", background = "Black", font = ("Verdana", 12, "bold"))
    pamatka1_upgrade.pack()
    pamatka1_upgrade.place(x=170, y=145)
    cost_level_up['text'] = str(upgrade_cost) + " монет"
    
    


def upgrading():
    global money
    global upgrade_level
    if upgrade_level == 0:
        if money > 15 or money == 15:
            money = money - 15
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 1:
        if money > 100 or money == 100:
            money= money - 100
            upgrade_level = upgrade_level + 1
        else:
            None    
    if upgrade_level == 2:
        if money > 500 or money == 500:
            money= money - 500
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 3:
        if money > 3000 or money == 3000:
            money= money - 3000
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 4:
        if money > 10000 or money == 10000:
            money= money - 10000
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 5:
        if money > 40000 or money == 40000:
            money= money - 40000
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 6:
        if money > 200000 or money == 200000:
            money= money - 200000
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 7:
        if money > 1666666 or money == 1666666:
            money= money - 1666666
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 8:
        if money > 123456789 or money == 123456789:
            money= money - 123456789
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 9:
        if money > 3999999999 or money == 3999999999:
            money= money - 3999999999
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 10:
        if money > 75000000000 or money == 75000000000:
            money= money - 75000000000
            upgrade_level = upgrade_level + 1
        else:
            None
    if upgrade_level == 11:
        upgrade_level = upgrade_level - 1
        
    
    


    
#главный экран
#кнопка для майнинга
oranges_mining = Button(text="Апельсины?", background="#f48c06", foreground="#03071e", activeforeground = "#03071e", activebackground="#f48c06", padx="20", pady="8", font = ("Verdana", 16, "bold"), width = "11", height = "2", bd = 3, command = plant)
oranges_mining.pack()
oranges_mining.place(x=392, y=120)


#кнопка для шопа
shop_button = Button(text="Магазинчик", background="#03071e", foreground="#f48c06", activeforeground = "#f48c06", activebackground="#03071e", padx="20", pady="8", font = ("Verdana", 16, "bold"), width = "11", height = "2", bd = 0, command = shoping)
shop_button.pack()
shop_button.place(x=800, y=270)


#инвентарь
inventory = Label(okno, text="Инвентарь:", foreground = "white", background = "Black", font = ("Verdana", 12, "bold"))
inventory.pack()
inventory.place(x=10, y=5)


#кол-во апельсинов
oranges_text = Label(okno, text="Апельсинчики : " + str(oranges), foreground = "white", background = "Black", font = ("Verdana", 12))
oranges_text.pack()
oranges_text.place(x=10, y=35)


#кол-во денежек
money_text = Label(okno, text="Монет : " + str(money), foreground = "white", background = "Black", font = ("Verdana", 12))
money_text.pack()
money_text.place(x=10, y=60)



#work
okno.mainloop()
