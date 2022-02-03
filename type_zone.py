from cProfile import label
from random import random
from textwrap import wrap
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from click import wrap_text
from matplotlib.pyplot import text
from tkinter import messagebox
import random
from tkinter import ttk

root = Tk()
root.title("Type Zone")
root.geometry("999x720")
root.minsize(900, 630)
root.maxsize(1000,800)
# root.iconbitmap()
min =[1,2,3]
level = ["Easy","Medium","Hard"]
i=0
j=0

def type():
    global seconds
    global minutes
    
    def counter():
        global seconds
        global minutes
        number_of_word=0
        i=0
        
        time_count_label.config(text=f"0{minutes} : {seconds}")
        if seconds==0 and minutes ==0:
            entered_text = text_widget.get(1.0,END)
            print(len(entered_text))
            print(entered_text)
            label_text_frame.destroy()
            text_frame.destroy()
            result_frame = Frame(t_body_frame,bg="#3C3F41",width=900,height=400)
            result_frame.grid(row=2, column=0,sticky=W,ipadx=22,padx=(30,30),pady=20)
            result_frame.grid_propagate(0)
            result_label_frame = Frame(result_frame, bg="#3C3F41",width=900,height=50)
            label_text =Label(result_label_frame,text="Result",font=("Lobster 25 "), bg="#3C3F41",fg ="white")
            label_text.grid(row=0,column=0,sticky=W)
            result_label_frame.grid(row=0, column=0,sticky=W)
            result_frame_1 = Frame(result_frame, bg="#45494A",width=870,height=300)
            result_frame_1.grid(row=1,column=0,pady=20,padx=(50,50))
            result_frame_1.grid_propagate(0)
            entered_list =entered_text.split()
            textInLine =0
            j=0
            k=0
            num_line =0
            while i<len(entered_list):
                # print(textInLisne)
                if entered_list[i]==content_list[i]:                   
                    if textInLine<50 and num_line <10:
                        print(num_line)
                        textInLine+=len(entered_list[i])
                        result_label = Label(result_frame_1,text =f"{entered_list[i]}",font=("Lobster 14 "), bg="#45494A",fg="green", justify="center").grid(row=j, column=k,padx=0,pady=0)
                        k+=1
                        num_line+=1
                        number_of_word+=1
                    else:
                        print(num_line)
                        num_line=1
                        textInLine =0
                        j+=1
                        k=0
                        result_label = Label(result_frame_1,text =f"{entered_list[i]}",font=("Lobster 14 "), bg="#45494A",fg="green", justify="center").grid(row=j, column=k,padx=0,pady=0)
                        number_of_word+=1
                        k+=1
                else:
                    if textInLine<50 and num_line<10:
                        textInLine+=len(entered_list[i])
                        result_label = Label(result_frame_1,text =f"{entered_list[i]}",font=("Lobster 14 "), bg="#45494A",fg="red", justify="center").grid(row=j, column=k,padx=0,pady=0)
                        num_line+=1
                        k+=1
                    else:
                        num_line =1
                        textInLine =0
                        j+=1
                        k=0
                        
                        result_label = Label(result_frame_1,text =f"{entered_list[i]}",font=("Lobster 14 "), bg="#45494A",fg="red", justify="center").grid(row=j, column=k,padx=0,pady=0)
                        k+=1
                i+=1    
            global bg_image
            result_window = Toplevel()
            result_window.title("Yay!")
            result_window.geometry("370x450")
            result_window.config(background="#3C3F41")
            bg_image = PhotoImage(file =r"Result_Images//1.png")

            my_canvas = Canvas(result_window,width=370,height=450)
            my_canvas.pack()

            my_canvas.create_image(0,0,image = bg_image,anchor="nw")
            my_canvas.create_text(180,170,text="50",font=("Ubuntu 100 "),fill="#2cfa1f")
            my_canvas.create_text(180,250,text="WPM",font=("Ubuntu 50 bold"),fill="#f1deco")


        if seconds == 0:
            minutes-=1
            seconds =60
        
        time_count_label.after(1000,counter)
        seconds-=1

    global body_frame
    global footer_frame
    global title_frame

    time = 60*(j+1)
    if time ==180:
        minutes = 2
        seconds = 59
    elif time ==120:
        minutes = 1
        seconds = 59
    else :
        minutes = 0
        seconds = 7

    body_frame.destroy()
    footer_frame.destroy()

    r = random.randint(1,10)
    # print(r)
    file = open("Easy/"+f"{r}.txt",encoding="utf8")

    content = file.readline()
    content_list = content.split()
    # print(content_list) 
    time_count_label = Label(title_frame,text="",bg="#3C3F41", fg ="white",font="Ubuntu 20 bold",width=7)   
    time_count_label.grid(row =0,column=4,sticky=E,padx=500)

    t_body_frame = Frame(root, width=1000,height=700,bg="#3C3F41",borderwidth=0, highlightthickness=0)
    t_body_frame.grid(row=1, column=0)
    t_body_frame.grid_propagate(0)
    t_body_text_frame = Frame(t_body_frame,bg="#45494A",width=900,height=150)
    t_body_text_frame.grid(row=0, column=0,sticky=W)
    t_body_text_label =Label(t_body_text_frame,text="Here is your text",font=("Lobster 25 "), bg="#3C3F41",fg ="white")
    t_body_text_label.grid(row=0,column =0,ipadx=20,sticky=W)

    t_inner_body_frame =Frame(t_body_frame,bg="#45494A",width=900,height=250)
    t_inner_body_frame.grid(row=1,column=0,ipadx=30,padx=(20,5))
    # my_label =Label(t_inner_body_frame, text="Hi").pack()
    t_inner_body_text_label =Message(t_inner_body_frame,text=f"{content}",font=("Lobster 15 "), bg="#45494A",fg ="white",width =800)
    t_inner_body_text_label.pack()
    t_inner_body_frame.grid_propagate(0)

    label_text_frame = Frame(t_body_frame,bg="#45494A",width=900,height=150)
    label_text_frame.grid(row=2, column=0,sticky=W)
    label_text =Label(label_text_frame,text="Hurry up! Dont think just write :-)",font=("Lobster 25 "), bg="#3C3F41",fg ="white")
    label_text.grid(row=0,column =0,ipadx=20,sticky=W)

    text_frame = Frame(t_body_frame,bg="#45494A",width=900,height=250)
    text_frame.grid(row=3,column=0,ipadx=30,padx=(20,5),pady=20)
    text_widget = Text(text_frame,fg ="white",bg="#45494A",font=("Lobster 15 "),width=73,height=8)
    text_widget.pack()
    text_frame.grid_propagate(0)
    counter()





def incr_level():
    global i
    global inner_body_frame
    global increment_level
    global decrement_level
    i+=1
    if i ==2:
        lev_label.destroy()
        
        lev_label1 =Label(inner_body_frame,text=f"{level[i]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
        lev_label1.grid(row=0,column =2,ipadx=20)
        incr_level_button =Button(inner_body_frame,image=increment_level, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=incr_level,state =DISABLED)
        incr_level_button.grid(row=0, column=3)
    else:
        lev_label.destroy()
        decr_level_button =Button(inner_body_frame,image=decrement_level, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=decr_level)
        decr_level_button.grid(row=0, column=1)
        lev_label1 =Label(inner_body_frame,text=f"{level[i]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
        lev_label1.grid(row=0,column =2,ipadx=20)
        incr_level_button =Button(inner_body_frame,image=increment_level, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=incr_level)
        incr_level_button.grid(row=0, column=3)
    

def decr_level():
    global i
    global inner_body_frame
    global increment_level
    global decrement_level
    i-=1
    if i ==0:
        lev_label.destroy()
        
        lev_label1 =Label(inner_body_frame,text=f"{level[i]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
        lev_label1.grid(row=0,column =2,ipadx=20)
        decr_level_button =Button(inner_body_frame,image=decrement_level, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=decr_level,state = DISABLED)
        decr_level_button.grid(row=0, column=1)
    else:
        lev_label.destroy()
        decr_level_button =Button(inner_body_frame,image=decrement_level, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=decr_level)
        decr_level_button.grid(row=0, column=1)
        lev_label1 =Label(inner_body_frame,text=f"{level[i]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
        lev_label1.grid(row=0,column =2,ipadx=20)
        incr_level_button =Button(inner_body_frame,image=increment_level, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=incr_level)
        incr_level_button.grid(row=0, column=3)

def incr_min():
    global j
    global inner_body_frame
    global increment
    global decrement
    j+=1
    if j ==2:
        min_label.destroy()
        
        min_label1 =Label(inner_body_frame,text=f"{min[j]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
        min_label1.grid(row=1,column =2,ipadx=20)
        incr_min_button =Button(inner_body_frame,image=increment, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=incr_min,state =DISABLED)
        incr_min_button.grid(row=1, column=3)
    else:
        min_label.destroy()
        decr_min_button =Button(inner_body_frame,image=decrement, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=decr_min)
        decr_min_button.grid(row=1, column=1)
        min_label1 =Label(inner_body_frame,text=f"{min[j]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
        min_label1.grid(row=1,column =2,ipadx=20)
        incr_min_button =Button(inner_body_frame,image=increment, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=incr_min)
        incr_min_button.grid(row=1, column=3)
    

def decr_min():
    global j
    global inner_body_frame
    global increment
    global decrement
    j-=1
    if j ==0:
        min_label.destroy()
        
        min_label1 =Label(inner_body_frame,text=f"{min[j]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
        min_label1.grid(row=1,column =2,ipadx=20)
        decr_min_button =Button(inner_body_frame,image=decrement, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=decr_min,state = DISABLED)
        decr_min_button.grid(row=1, column=1)
    else:
        min_label.destroy()
        decr_min_button =Button(inner_body_frame,image=decrement, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=decr_min)
        decr_min_button.grid(row=1, column=1)
        min_label1 =Label(inner_body_frame,text=f"{min[j]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
        min_label1.grid(row=1,column =2,ipadx=20)
        incr_min_button =Button(inner_body_frame,image=increment, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=incr_min)
        incr_min_button.grid(row=1, column=3)


#Title Frame
title_frame = Frame(root, width=1000,height=100,bg="#4B4B4B",borderwidth=0, highlightthickness=0)
img = ImageTk.PhotoImage(Image.open("Dark_theme_logo.png"))
pic_frame = Frame(title_frame)
pic_label =Label(pic_frame,image=img,borderwidth=0, highlightthickness=0,bg="#4B4B4B")
pic_label.grid(row=0,column=0,ipadx=10,ipady=10)
pic_frame.grid(row=0,column = 0)
text_frame = Frame(title_frame,bg="#4B4B4B")
text_label =Label(text_frame,text="Type Zone",font=("Lobster 20 bold"), bg="#4B4B4B",fg ="white")
text_label.grid(row=0,column =0)
sub_text_label =Label(text_frame,text="  Start typing",font=("Lobster 10"), bg="#4B4B4B",fg ="white")
sub_text_label.grid(row=1,column =0,sticky = W)
text_frame.grid(row=0,column=1)
title_frame.grid(row=0, column=0)
title_frame.grid_propagate(0)

#Body Frame
body_frame = Frame(root, width=1000,height=400,bg="#3C3F41",borderwidth=0, highlightthickness=0)
body_frame.grid(row=1, column=0)
body_text_frame = Frame(body_frame,bg="#3C3F41",width=900,height=150)
body_text_frame.grid(row=0, column=0,sticky=W)
body_text_label =Label(body_text_frame,text="Hi there!",font=("Lobster 25 "), bg="#3C3F41",fg ="white")
body_text_label.grid(row=0,column =0,ipadx=20,sticky=W)
body_text_label =Label(body_text_frame,text="Ready to break your old milestone, give it your best shot.",font=("Lobster 15 "), bg="#3C3F41",fg ="white")
body_text_label.grid(row=1,column =0,ipadx=30)


inner_body_frame =Frame(body_frame,bg="#45494A",width=900,height=350)
level_label =Label(inner_body_frame,text="Choose Level",font=("Lobster 20 "), bg="#45494A",fg ="white")
level_label.grid(row=0,column =0,ipadx=20,ipady=20,sticky=W)

decrement_level = PhotoImage(file = "decrement.png")
decr_level_button =Button(inner_body_frame,image=decrement_level, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=decr_level,state=DISABLED)
decr_level_button.grid(row=0, column=1)

lev_label =Label(inner_body_frame,text=f"{level[i]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
lev_label.grid(row=0,column =2,ipadx=20)

increment_level = PhotoImage(file = "increment.png")
incr_level_button =Button(inner_body_frame,image=increment_level, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=incr_level)
incr_level_button.grid(row=0, column=3)

minute_label =Label(inner_body_frame,text="Choose Minutes",font=("Lobster 20 "), bg="#45494A",fg ="white")
minute_label.grid(row=1,column =0,ipadx=20,sticky=W)


decrement = PhotoImage(file = "decrement.png")
decr_min_button =Button(inner_body_frame,image=decrement, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=decr_min,state=DISABLED)
decr_min_button.grid(row=1, column=1)

min_label =Label(inner_body_frame,text=f"{min[j]}",width=5,font=("Lobster 20 bold"), bg="#3C3F41",fg ="white")
min_label.grid(row=1,column =2,ipadx=20)

increment = PhotoImage(file = "increment.png")
incr_min_button =Button(inner_body_frame,image=increment, bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=incr_min)
incr_min_button.grid(row=1, column=3)

inner_body_frame.grid(row=1,column=0,ipadx=30,padx=20)
inner_body_frame.grid_propagate(0)



#Footer Frame
footer_frame =Frame(root,bg="#3C3F41",width=1000,height=220)
type_button =Button(footer_frame,text ="Type", font=("Lobster 20 bold"), bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=type)
type_button.grid(row=0,column=0,padx=700,pady=30)
footer_frame.grid(row=2,column=0)
footer_frame.grid_propagate(0)

body_frame.grid_propagate(0)


root.mainloop()