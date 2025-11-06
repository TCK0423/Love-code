import tkinter as tk
import random as rd
import time
import math

Msg_choice = [
    "我很想你",
    "想念是一種很玄的東西",
    "希望你一切都好",
    "有好好照顧自己嗎?",
    "要天天開心",
    "記得多喝水",
    "保持微笑",
    "你是被愛的",
    "你是我今生最美的遇見",
    "願你被這世界溫柔以待",
]
color_choice = [
    {'bg': "#ffc9c9", 'text': "#000000"},
    {'bg': "#FAF89C", 'text': "#000000"},
    {'bg': "#81F78D", 'text': "#000000"},
    {'bg': "#9ED2FF", 'text': "#000000"},
    {'bg': "#C380FF", 'text': "#000000"},
]

def heart_generate():
    window = tk.Tk()
    window.withdraw()
    Sc_W = window.winfo_screenwidth()
    Sc_H = window.winfo_screenheight()
    Center_X = Sc_W // 2
    Center_Y = Sc_H // 2
    num = 200
    scale = 25
    all_small_window_generate = []
    all_delay = []
    print("計算並生成視窗")
    for i in range(num):
        t = 2 * math.pi * i / num
        x_count = scale * 16 * (math.sin(t) ** 3)
        y_count = -scale * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        #電腦向下為正y軸
        end_x = Center_X + x_count
        end_y = Center_Y + y_count
        chosen_color = rd.choice(color_choice)
        chosen_Msg = rd.choice(Msg_choice)
        bg_c = chosen_color['bg']
        text_c = chosen_color['text']
        small_window = tk.Toplevel(window)
        small_window.overrideredirect(True)
        small_window.configure(bg=bg_c)
        small_window.geometry(f"200x100+{int(end_x)}+{int(end_y)}")
        small_window.attributes("-topmost", True)
        lb = tk.Label(
            small_window,
            text = chosen_Msg,
            bg = bg_c,
            fg = text_c,
            font = ("Arial", 12)
        )   
        lb.pack(
            expand=True,
            fill='both'
        )
        window.update()
        time.sleep(0.03)
        all_small_window_generate.append(small_window)
    print("生成完畢，開始消失")
    for small_window in all_small_window_generate:
        small_window.after(rd.randint(4000, 12000), small_window.destroy)
    def try_destroy():
        for small_window in all_small_window_generate:
            if small_window.winfo_exists():
                print("嘗試執行window.destroy")
                window.after(1000, try_destroy)
                return
            #偵測到還有視窗，重複請求try_destroy，又偵測到還有視窗，繼續重複請求，直到無視窗存在
        print("觸發結束主視窗")
        window.destroy()
    window.after(1000, try_destroy)
    window.mainloop()
    print("結束")
heart_generate()