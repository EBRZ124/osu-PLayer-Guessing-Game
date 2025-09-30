import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import random
import answerlogic

osuplayegame = tk.Tk()

player_list = answerlogic.player_list  

image_files = [ # Doesnt recognise jpg (maybe potential fix...?)
    "images/xootynator.png",
    "images/rafis.png",
    "images/flyingtuna.png",
    "images/mrekk.png",
    "images/chicony.png",
    "images/nirux.png",
    "images/btmc.png",
    "images/whitecat.png",
    "images/ninerik.png",
    "images/toesu.png",
    "images/aleph.png",
    "images/lifeline.png",
    "images/spazza.png",
    "images/lemuze.png",
    "images/zylice.png",
    "images/ryuk.png",
    "images/sst3w.png"
]

max_size = 200

player_images = []
for img_file in image_files:
    img = Image.open(img_file)
    if img.width > max_size:
        img = img.resize((max_size, max_size), Image.Resampling.LANCZOS)
    
    tk_img = ImageTk.PhotoImage(img)
    player_images.append(tk_img)

osuplayegame.title("osu! player guessing game")
osuplayegame.geometry("640x580")
osuplayegame.configure( bg="#E6E6E6", cursor="star")

def show_frame(frame):
    frame.tkraise()

container = tk.Frame(osuplayegame, bg="#E6E6E6")
container.pack(fill="both", expand = True)

container.grid_rowconfigure(0, weight = 1)
container.grid_columnconfigure(0, weight = 1)

start_menu=tk.Frame(container, bg="#E6E6E6")
start_menu.grid(row=0, column=0, sticky="nsew")

title_label = tk.Label(start_menu, text = "Welcome to The osu! Player Guessing Game", 
                       font=("Comic Sans MS", 30), fg='black', bg="white", relief="groove")
title_label.pack(pady=20)

play_button = tk.Button(start_menu, text = "Play", font=("Comic Sans MS", 50, ), command=lambda: build_quiz_screen())
play_button.pack(pady=20)

exit_button = tk.Button(start_menu, text = "Quit", font=("Comic Sans MS", 30), fg="#B30000", command=osuplayegame.destroy)
exit_button.pack(pady=20)

mistakenr = tk.IntVar(value=0)

# The game

def build_quiz_screen():
    for widget in osuplayegame.winfo_children():
        widget.destroy()

    index, ans1, ans2, ans3, right_answer = answerlogic.generate_round()

    top_frame = tk.Frame(osuplayegame, bg="#E6E6E6")
    top_frame.pack(pady=10)

    label = tk.Label(top_frame, text="Who is this?", font=("Comic Sans MS", 14), bg="black", fg="white")
    label.pack()
    
    image_label = tk.Label(top_frame, image=player_images[index])
    image_label.pack(pady=10)

    answer_frame = tk.Frame(osuplayegame,  bg="#E6E6E6")
    answer_frame.pack(pady=15)

    def correct():
        build_quiz_screen()

    def wrong():
        mistakenr.set(mistakenr.get() + 1)

    if right_answer == 0:
        opt1_cmd, opt2_cmd, opt3_cmd = correct, wrong, wrong
    elif right_answer == 1:
        opt1_cmd, opt2_cmd, opt3_cmd = wrong, correct, wrong
    else:
        opt1_cmd, opt2_cmd, opt3_cmd = wrong, wrong, correct

    option1 = tk.Button(answer_frame, text=player_list[ans1],
                        font=("Comic Sans MS", 16), fg='black', bg="white", relief="groove",
                        command=opt1_cmd)
    option2 = tk.Button(answer_frame, text=player_list[ans2],
                        font=("Comic Sans MS", 16), fg='black', bg="white", relief="groove",
                        command=opt2_cmd)
    option3 = tk.Button(answer_frame, text=player_list[ans3],
                        font=("Comic Sans MS", 16), fg='black', bg="white", relief="groove",
                        command=opt3_cmd)

    option1.pack(side="left", padx=10)
    option2.pack(side="left", padx=10)
    option3.pack(side="left", padx=10)

    misc_frame = tk.Frame(osuplayegame, bg="#E6E6E6")
    misc_frame.pack(pady=10)

    mistake_counter = tk.Label(misc_frame, textvariable=mistakenr,
                               font=("Comic Sans MS", 13), fg='black', bg="white", relief="groove")
    mistake_counter.pack(side="left", padx=10)

    exit_button = tk.Button(misc_frame, text="Quit", font=("Comic Sans MS", 10),
                            fg="#B30000", command=osuplayegame.destroy)
    exit_button.pack(side="left", padx=10)

show_frame(start_menu)

osuplayegame.mainloop()

