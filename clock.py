from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("600x450")
clock_image = ImageTk.PhotoImage(Image.open ("clock.jpg"))

india_label = Label(root,text="India")
india_label.place(relx=0.225, rely=0.05, anchor= CENTER)

india_clock=Label(root)
india_clock["image"]=clock_image
india_clock.place(relx=0.225, rely=0.35, anchor= CENTER)

india_time = Label(root)
india_time.place(relx=0.225,rely=0.7, anchor = CENTER)

UK_label = Label(root,text="UK")
UK_label.place(relx=0.775, rely=0.05, anchor= CENTER)

UK_clock=Label(root)
UK_clock["image"]=clock_image
UK_clock.place(relx=0.775, rely=0.35, anchor= CENTER)

UK_time = Label(root)
UK_time.place(relx=0.775,rely=0.7, anchor = CENTER)

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftiime("%H:%M:%S")
        india_time["text"]="Time :"+ current_time
        india_time.after(200,self.times)
   
        


    
class UK():
    def times(self):
        home=pytz.timezone('UK/BST')
        local_time=datetime.now(home)
        current_time=local_time.strftiime("%H:%M:%S")
        UK_time["text"]="Time :"+ current_time
        UK_time.after(200,self.times)
        
obj_india=India()
obj_uk=UK()
india_btn=Button(root,text="Show Time", command=obj_india.times)
india_btn.place(relx=0.2, rely=0.8, anchor= CENTER)
uk_btn=Button(root,text="Show Time", command=obj_uk.times)
uk_btn.place(relx=0.7, rely=0.8, anchor= CENTER)

   

root.mainloop()