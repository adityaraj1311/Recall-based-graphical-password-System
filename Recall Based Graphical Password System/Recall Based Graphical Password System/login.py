import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
from PIL import ImageTk

root = Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
#setting tkinter window size
root.geometry("%dx%d" % (width, height))

bg = ImageTk.PhotoImage(file="images/frnt.jpg")


my_canvas = Canvas(root, width=800, height=800)
my_canvas.pack(fill=BOTH, expand=True)
#my_canvas.create_image(0, 0, image=bg, anchor="nw")
my_canvas.create_text(700, 85, text="Recall Based Authentication System", fill="black", font=("times new roman", 65))


mnf=Frame(root,highlightbackground="blue", highlightthickness=2,bg="lightblue")
mnf.place(x=700,y=200,width=500,height=400)

title = Label(mnf, text="Level Two", font=("times new roman", 20, "bold"),
                      fg="Black",bg="lightblue").place(x=80, y=10)
title2 = Label(mnf, text="(Select atleat 3 Images)", font=("times new roman", 10, "bold"),
                      fg="Black",bg="lightblue").place(x=240, y=20)
mnf2=Frame(root,highlightbackground="green", highlightthickness=2,bg="lightblue")
mnf2.place(x=300,y=400,width=400,height=200)

mnf3=Frame(root,highlightbackground="green"
                                    "", highlightthickness=2,bg="lightblue")
mnf3.place(x=300,y=200,width=400,height=200)
#backend starts here


def validate():
    if password== "" or impassword=="" or mail=="" or fname=="":

        messagebox.showerror("Error", "All Fields are required", parent=root)

    else:
        try:
            conn = sqlite3.connect('base.db')
            # create acursor instance
            curr = conn.cursor()
            curr.execute("select * from record where email = ? and colors = ? and img=?",
                         (txt_mail.get(), password,impassword))
            row = curr.fetchone()

            print(row)
            if row == None:
                messagebox.showerror("Error", "Invalid USERNAME and Password", parent=root)
                mnf3.config(highlightbackground="red")
            else:
                messagebox.showinfo("success", "welcome", parent=root)





            conn.commit()
            conn.close()

            reset()



        except Exception as esw:
            messagebox.showerror("Error", f"Error due to:{str(esw)}", parent=root)
def result():
    print(impassword)
password=""
impassword=""
def get_button(t):
    global password
    password+=str(t)
    return

def get_buttons(i):
    global impassword
    impassword+=str(i)
    return

#reset color password to =""
def resetc():
    global password
    if len(password) >= 1:
        password = ""
        show_message()
    else:
        if len(password) == 0:
            show_messagee()


    return
def show_messagee():
    label = Label(root, text="Please select colors", font=("times new roman", 15, "bold"),
                  background="lightblue",
                  foreground="red")
    label.place(x=530, y=560)
    label.after(3000, label.destroy)
def show_message():
    label = Label(root, text="Reset Successfully",font=("times new roman", 15, "bold"),
                     background="lightblue",
                     foreground="red")
    label.place(x=530,y=560)
    label.after(3000, label.destroy)
def show_message2():
    label = Label(root, text="Reset Successfully",font=("times new roman", 15, "bold"),
                     background="lightblue",
                     foreground="red")
    label.place(x=985,y=560)
    label.after(3000, label.destroy)
def show_message3():
    label = Label(root, text="please select images",font=("times new roman", 15, "bold"),
                     background="lightblue",
                     foreground="red")
    label.place(x=985,y=560)
    label.after(3000, label.destroy)
#reset image password to=""
def reseti():
    global impassword
    # print(impassword)
    if len(impassword) >= 1:
        impassword = ""
        show_message2()

    else:
        if len(impassword) == 0:
            show_message3()
    return


    return
def reset():
    global password
    global impassword
    password=""
    impassword=""
    txt_fname.delete(0,END)
    txt_mail.delete(0,END)

    return



fname = Label(mnf3, text="First Name:", font=("times new roman", 15, "bold"), bg="lightblue",
                      fg="black").place(x=10, y=40)
fname=StringVar()
txt_fname=Entry(mnf3,textvariable=fname,font=("times new roman",15),bg="lightgray")
txt_fname.place(x=130,y=40,width=250)
#lastname
mail = Label(mnf3, text="Email:", font=("times new roman", 15, "bold"), bg="lightblue",
              fg="black").place(x=10, y=100)
mail=StringVar()
txt_mail = Entry(mnf3,textvariable=mail, font=("times new roman", 15), bg="lightgray")
txt_mail.place(x=130, y=100, width=250)


title = Label(mnf2, text="Level One", font=("times new roman", 20, "bold"),
                      fg="black",bg="lightblue").place(x=40, y=10)
title2 = Label(mnf2, text="(Select atleast 3 Colors)", font=("times new roman", 10, "bold"),
                      fg="black",bg="lightblue").place(x=200, y=20)

red = Button(mnf2,bg="red",padx=5,height=2,width=10, bd=0,cursor="hand2",command=lambda t= "red": get_button(t)).place(x=10,y=60)
green = Button(mnf2,bg="green",padx=5,height=2,width=10, bd=0,cursor="hand2",command=lambda t= "green": get_button(t)).place(x=105,y=60)
blue = Button(mnf2,bg="blue",padx=5,height=2,width=10, bd=0,cursor="hand2",command=lambda t= "blue": get_button(t)).place(x=200,y=60)
yellow = Button(mnf2,bg="yellow",padx=5,height=2,width=10, bd=0,cursor="hand2",command=lambda t= "yellow": get_button(t)).place(x=300,y=60)

brown2 = Button(mnf2,bg="brown2",padx=5,height=2,width=10, bd=0,cursor="hand2",command=lambda t= "brown2": get_button(t)).place(x=10,y=100)
burlywood = Button(mnf2,bg="burlywood",padx=5,height=2,width=10, bd=0,cursor="hand2",command=lambda t= "burly": get_button(t)).place(x=105,y=100)

dblue = Button(mnf2,bg="dark blue",padx=5,height=2,width=10, bd=0,cursor="hand2",command=lambda t= "dblue": get_button(t)).place(x=200,y=100)
black = Button(mnf2,bg="black",padx=5,height=2,width=10, bd=0,cursor="hand2",command=lambda t= "black": get_button(t)).place(x=300,y=100)
rst = Button(mnf2,bg="lightgreen",fg="Black",text="Reset",padx=5,height=2,width=8, bd=2,cursor="hand2",command=resetc).place(x=150,y=150)



container = Frame(mnf,highlightbackground="red", highlightthickness=2)
container.place(x=50,y=50)
canvas = Canvas(container)
scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame =Frame(canvas)
rsti = Button(mnf,bg="lightgreen",fg="Black",text="Reset",padx=5,height=2,width=8, bd=2,cursor="hand2",command=reseti).place(x=200,y=350)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

image = Image.open("images/ch.png")
resize_image = image.resize((100, 80))
left2 = ImageTk.PhotoImage(resize_image)

#Let us create a label for button event
img_label= Label(image=left2)
#Let us create a dummy button and pass the image
button= Button(scrollable_frame, image=left2,command=lambda i= "man": get_buttons(i),height=100,width=80,
borderwidth=0)
button.grid(row=0,column=0)

#mango


image2 = Image.open("images/man.jpg")
resize_image2 = image2.resize((100, 80))
left22 = ImageTk.PhotoImage(resize_image2)

#Let us create a label for button event
img_label2= Label(image=left22)
#Let us create a dummy button and pass the image
button2= Button(scrollable_frame, image=left22,command=lambda i= "mgo": get_buttons(i),height=100,width=80,
borderwidth=0)
button2.grid(row=0,column=1,padx=10)
#bheem
image3 = Image.open("images/bheem.jpg")
resize_image3 = image3.resize((100, 80))
left3 = ImageTk.PhotoImage(resize_image3)

#Let us create a label for button event
img_label3= Label(image=left3)
#Let us create a dummy button and pass the image
button3= Button(scrollable_frame, image=left3,command=lambda i= "bhm": get_buttons(i),height=100,width=80,
borderwidth=0)
button3.grid(row=0,column=2)
#apple
image4 = Image.open("images/apple.jpg")
resize_image4 = image4.resize((100, 80))
left4 = ImageTk.PhotoImage(resize_image4)

#Let us create a label for button event
img_label4= Label(image=left4)
button4= Button(scrollable_frame ,image=left4,command=lambda i= "appy": get_buttons(i),height=100,width=80,
borderwidth=0)
button4.grid(row=0,column=3,padx=10)

#tom
image5 = Image.open("images/tom.jpg")
resize_image5 = image5.resize((100, 80))
left5 = ImageTk.PhotoImage(resize_image5)

#Let us create a label for button event
img_label5= Label(image=left5)

button5= Button(scrollable_frame, image=left5,command=lambda i= "tom": get_buttons(i),height=100,width=80,
borderwidth=0)
button5.grid(row=1,column=0)

#yrose
image6 = Image.open("images/yrose.jpg")
resize_image6 = image6.resize((100, 80))
left6 = ImageTk.PhotoImage(resize_image6)

#Let us create a label for button event
img_label6= Label(image=left6)

button6= Button(scrollable_frame, image=left6,command=lambda i= "yros": get_buttons(i),height=100,width=80,
borderwidth=0)
button6.grid(row=1,column=1,padx=0,pady=0)

#wolf
image7 = Image.open("images/wolf.jpg")
resize_image7 = image7.resize((100, 80))
left7 = ImageTk.PhotoImage(resize_image7)

#Let us create a label for button event
img_label7= Label(image=left7)

button7= Button(scrollable_frame, image=left7,command=lambda i= "wlf": get_buttons(i),height=100,width=80,
borderwidth=0)
button7.grid(row=1,column=2,padx=0,pady=0)

#monkey
image8 = Image.open("images/monkey.jpg")
resize_image8 = image8.resize((100, 80))
left8 = ImageTk.PhotoImage(resize_image8)

#Let us create a label for button event
img_label8= Label(image=left8)

button8= Button(scrollable_frame, image=left8,command=lambda i= "monk": get_buttons(i),height=100,width=80,
borderwidth=0)
button8.grid(row=1,column=3,padx=10,pady=0)
#orange
image9 = Image.open("images/orange.jpg")
resize_image9 = image9.resize((100, 80))
left9 = ImageTk.PhotoImage(resize_image9)

#Let us create a label for button event
img_label9= Label(image=left9)
button9= Button(scrollable_frame, image=left9,command=lambda i= "orng": get_buttons(i),height=100,width=80,
borderwidth=0)
button9.grid(row=2,column=0)
#turtle
#orange
image10 = Image.open("images/turtle.jpg")
resize_image10 = image10.resize((100, 80))
left10 = ImageTk.PhotoImage(resize_image10)

#Let us create a label for button event
img_label10= Label(image=left10)
button10= Button(scrollable_frame, image=left10,command=lambda i= "trtle": get_buttons(i),height=100,width=80,
borderwidth=0)
button10.grid(row=2,column=1)

#rrsoe
#orange
image11 = Image.open("images/rrose.jpg")
resize_image11 = image11.resize((100, 80))
left11 = ImageTk.PhotoImage(resize_image11)

#Let us create a label for button event
img_label11= Label(image=left11)
button11= Button(scrollable_frame, image=left11,command=lambda i= "rrse": get_buttons(i),height=100,width=80,
borderwidth=0)
button11.grid(row=2,column=2)
#parrot
image12 = Image.open("images/parrot.jpg")
resize_image12 = image12.resize((100, 80))
left12 = ImageTk.PhotoImage(resize_image12)

#Let us create a label for button event
img_label12= Label(image=left12)
button12= Button(scrollable_frame, image=left12,command=lambda i= "prt": get_buttons(i),height=100,width=80,
borderwidth=0)
button12.grid(row=2,column=3)
#tank

image13 = Image.open("images/tank.jfif")
resize_image13 = image13.resize((100, 80))
left13 = ImageTk.PhotoImage(resize_image13)

#Let us create a label for button event
img_label13= Label(image=left13)
button13= Button(scrollable_frame, image=left13,command=lambda i= "tnk": get_buttons(i),height=100,width=80,
borderwidth=0)
button13.grid(row=3,column=0)
#ship
image14 = Image.open("images/ship.jpg")
resize_image14 = image14.resize((100, 80))
left14 = ImageTk.PhotoImage(resize_image14)

#Let us create a label for button event
img_label14= Label(image=left14)
button14= Button(scrollable_frame, image=left14,command=lambda i= "shp": get_buttons(i),height=100,width=80,
borderwidth=0)
button14.grid(row=3,column=1)
#jet
image15 = Image.open("images/jet.jpg")
resize_image15 = image15.resize((100, 80))
left15 = ImageTk.PhotoImage(resize_image15)

#Let us create a label for button event
img_label15= Label(image=left15)
button15= Button(scrollable_frame, image=left15,command=lambda i= "jet": get_buttons(i),height=100,width=80,
borderwidth=0)
button15.grid(row=3,column=2)

#sub
image16 = Image.open("images/sub.jpg")
resize_image16 = image16.resize((100, 80))
left16 = ImageTk.PhotoImage(resize_image16)

#Let us create a label for button event
img_label16= Label(image=left16)
button16= Button(scrollable_frame, image=left16,command=lambda i= "sub": get_buttons(i),height=100,width=80,
borderwidth=0)
button16.grid(row=3,column=3)

#car
image17 = Image.open("images/car.jpg")
resize_image17 = image17.resize((100, 80))
left17 = ImageTk.PhotoImage(resize_image17)

#Let us create a label for button event
img_label17= Label(image=left17)
button17= Button(scrollable_frame, image=left17,command=lambda i= "car": get_buttons(i),height=100,width=80,
borderwidth=0)
button17.grid(row=4,column=0)
#auto
image18 = Image.open("images/auto.jpg")
resize_image18 = image18.resize((100, 80))
left18 = ImageTk.PhotoImage(resize_image18)

#Let us create a label for button event
img_label18= Label(image=left18)
button18= Button(scrollable_frame, image=left18,command=lambda i= "ato": get_buttons(i),height=100,width=80,
borderwidth=0)
button18.grid(row=4,column=1)
#bike
image19 = Image.open("images/bike.jpg")
resize_image19 = image19.resize((100, 80))
left19 = ImageTk.PhotoImage(resize_image19)

#Let us create a label for button event
img_label19= Label(image=left19)
button19= Button(scrollable_frame, image=left19,command=lambda i= "bike": get_buttons(i),height=100,width=80,
borderwidth=0)
button19.grid(row=4,column=2)

#cycle
image20 = Image.open("images/cycle.jpg")
resize_image20 = image20.resize((100, 80))
left20 = ImageTk.PhotoImage(resize_image20)

#Let us create a label for button event
img_label20= Label(image=left20)
button20= Button(scrollable_frame, image=left20,command=lambda i= "cycle": get_buttons(i),height=100,width=80,
borderwidth=0)
button20.grid(row=4,column=3)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
#button

imagel = Image.open("images/kpr.png")
resize_imagel = imagel.resize((300, 70))
left3l = ImageTk.PhotoImage(resize_imagel)

#Let us create a label for button event
img_labell= Label(image=left3l)
#Let us create a dummy button and pass the image
button2l= Button(root, image=left3l,command=validate,
borderwidth=0)
button2l.place(x=600,y=650)

root.mainloop()
