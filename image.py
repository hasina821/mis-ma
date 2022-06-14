from tkinter import *
from PIL import ImageTk,Image

root = Tk() 
root.title("Learn image")


mon_image = ImageTk.PhotoImage(Image.open('image1.jpg'))
mon_image2 = ImageTk.PhotoImage(Image.open('image2.jpg'))
mon_image3 = ImageTk.PhotoImage(Image.open('image3.jpg'))
mon_image4 = ImageTk.PhotoImage(Image.open('image4.jpg'))

mon_label =  Label(image=mon_image)

mon_label.grid(column=0,row=0,columnspan=3)

image_list = [mon_image,mon_image2,mon_image3,mon_image4]


def Back(image_number):
     global mon_label
     global btn_back
     global btn_next

     mon_label.grid_forget()
     mon_label = Label(root,image=image_list[image_number-1])
     mon_label.grid(column=0,row=0,columnspan=3)
     btn_back=Button(root,padx=80,pady=10,text="<<",command=lambda:Back(image_number-1))
     btn_next=Button(root,padx=80,pady=10,text=">>",command=lambda:Next(image_number+1))

     if image_number==1:
          btn_back=Button(root,padx=80,pady=10,text=">>",state=DISABLED)
          btn_back.grid(column=0,row=1)



def Next(image_number):
     global mon_label
     global btn_back
     global btn_next
     mon_label.grid_forget()
     mon_label = Label(root,image=image_list[image_number-1])
     mon_label.grid(column=0,row=0,columnspan=3)
     btn_back=Button(root,padx=80,pady=10,text="<<",command=lambda:Back(image_number-1))
     btn_back.grid(column=0,row=1)
     btn_next=Button(root,padx=80,pady=10,text=">>",command=lambda:Next(image_number+1))

     if image_number==4:
          btn_next=Button(root,padx=80,pady=10,text=">>",state=DISABLED)
     btn_next.grid(column=2,row=1)


btn_back=Button(root,padx=80,pady=10,text="<<",command=Back,state=DISABLED)
btn_back.grid(column=0,row=1)
btn_next=Button(root,padx=80,pady=10,text=">>",command=lambda:Next(2))
btn_next.grid(column=2,row=1)

btn_quitter = Button(root,text="Quitter",command=root.quit,bg="red",fg="white")
btn_quitter.grid(column=1,row=1)

root.mainloop()
