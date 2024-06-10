from tkinter import*
import time
import pygame
from pygame import mixer
mixer.init()
root=Tk()
a="/storage/emulated/0/snaptube/download/SnapTube Audio/Unstoppable - Sia (Lyrics   Vietsub) ♫(MP3_160K).mp3"
mixer.music.load(a)
mixer.music.play()
root.config(bg="#e3eaab")
#Hien thi thu ngay thang nam
thu={
   0:"Thứ Hai",
   1:"Thứ Ba",
   2:"Thứ Tư",
   3:"Thứ Năm",
   4:"Thứ Sáu",
   5:"Thứ Bảy",
   6:"Chủ Nhật"
}
#Truy xuat value tu key
wd=thu[time.localtime(time.time()).tm_wday]

ngay=time.localtime(time.time()).tm_mday

thang=time.localtime(time.time()).tm_mon

nam=time.localtime(time.time()).tm_year

text=wd + " " + "," +" " + "Ngày" + " " + str(ngay) + " " +"Tháng" + " " +str(thang) + " " + "Năm" + " "+str(nam)
lbl=Label(root,text=text,font=("Serif",11,"bold"),fg="red",width=35)
lbl.pack(pady=180)


#Hien thi thoi gian hien tai
def clock():
	t=time.strftime("%H:%M:%S  %p",time.localtime())
	lbl_clock.config(text=t)
	lbl_clock.after(1000,clock)

lbl_clock=Label(root,text=" ",fg="green",font=("Serif",20,"bold"))
lbl_clock.place(x=150,y=670)
clock()

lbl_name=Label(root,text="Bé Bi Channel",font=("Serif",19,"bold"),fg="#000000")
lbl_name.place(x=150,y=1200)
root.mainloop()
