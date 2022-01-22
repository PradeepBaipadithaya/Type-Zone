from tkinter import *
from turtle import width
from PIL import Image, ImageTk
from matplotlib.pyplot import text
from tkinter import messagebox

root = Tk()
root.title("Type Zone")
root.geometry("900x630")
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
        
        time_count_label.config(text=f"0{minutes} : {seconds}")
        seconds-=1
        if seconds == 0:
            minutes-=1
            seconds =60
        if seconds==0 and minutes ==0:
            messagebox.showinfo("Completed","Done")
        time_count_label.after(1000,counter)

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
        seconds = 59


    

    body_frame.destroy()
    footer_frame.destroy()
    # time_left_label = Label(title_frame,text="Time Left",bg="black", fg ="white",font="Ubuntu 20 bold")   
    # time_left_label.grid(row =0,column=3,padx=30)
    time_count_label = Label(title_frame,text="",bg="#3C3F41", fg ="white",font="Ubuntu 20 bold",width=7)   
    time_count_label.grid(row =0,column=4,sticky=E,padx=500)
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
title_frame = Frame(root, width=900,height=100,bg="#4B4B4B",borderwidth=0, highlightthickness=0)
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
body_frame = Frame(root, width=900,height=400,bg="#3C3F41",borderwidth=0, highlightthickness=0)
body_frame.grid(row=1, column=0)
body_text_frame = Frame(body_frame,bg="#3C3F41",width=900,height=150)
body_text_frame.grid(row=0, column=0,sticky=W)
body_text_label =Label(body_text_frame,text="Hi there!",font=("Lobster 25 "), bg="#3C3F41",fg ="white")
body_text_label.grid(row=0,column =0,ipadx=20,sticky=W)
body_text_label =Label(body_text_frame,text="Ready to break your old milestone, give it your best shot.",font=("Lobster 15 "), bg="#3C3F41",fg ="white")
body_text_label.grid(row=1,column =0,ipadx=30)


inner_body_frame =Frame(body_frame,bg="#45494A",width=900,height=327)
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
footer_frame =Frame(root,bg="#3C3F41",width=900,height=150)
type_button =Button(footer_frame,text ="Type", font=("Lobster 20 bold"), bg="#45494A",fg ="#F9F2FA",highlightthickness=2,cursor="hand2",command=type)
type_button.grid(row=0,column=0,padx=700,pady=30)
footer_frame.grid(row=2,column=0)
footer_frame.grid_propagate(0)

body_frame.grid_propagate(0)


root.mainloop()