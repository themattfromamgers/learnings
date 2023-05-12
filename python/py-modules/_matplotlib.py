import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
# x = [1,2,3,4]
# y = [1,4,9,16]

# plt.plot(x,y, "o--r")
# plt.axis([0,6,0,20])

# plt.title("Grafik")
# plt.xlabel("x label")
# plt.ylabel("y label")

# plt.show()

# 2

# x = np.linspace(0,2,100)

# plt.plot(x, x, label="linear",color="red")
# plt.plot(x, x**2, label="quadratic",color="yellow")
# plt.plot(x, x**3, label="cubic",color="green")

# plt.xlabel("x label")
# plt.ylabel("y label")

# plt.title("simple plot")
# plt.legend()

# plt.show() 

# 3

# x = np.linspace(0,2,100)
# fig,axs =  plt.subplots(3)
# axs[0].plot(x, x, color="red")
# axs[0].set_title("linear")
# axs[1].plot(x, x**2, color="green")
# axs[1].set_title("quadratic")
# axs[2].plot(x, x**3, color="yellow")
# axs[2].set_title("cubic")
# plt.tight_layout()
# plt.show() 

# 4

# x = np.linspace(0,2,100)
# fig,axs =  plt.subplots(2,2)
# fig.suptitle("grafik başlığı")
# axs[0,0].plot(x, x, color="red")
# axs[0,1].plot(x, x**2, color="blue")
# axs[1,0].plot(x, x**3, color="green")
# axs[1,1].plot(x, x**4, color="yellow")
# plt.show() 

# 5


# df = pd.read_csv("lib/nba.csv")
# df = df.drop(["Number"], axis = 1).groupby("Team").mean()
# df.head().plot(subplots=True)
# plt.legend()
# plt.show() 



# BAR
# plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
# plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)
# plt.legend()
# plt.xlabel("Gün")
# plt.ylabel("Mesafe (km)")
# plt.title("Araç Bilgileri")
# plt.show()


# PİE
# goal_types = 'Penaltı','Kaleye Atılan Şut','Serbest Vuruş'
# goals = [12,35,7]
# colors = ['y','r','b']
# plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05), autopct="%1.1f%%")
# plt.show()

# HİSTOGRAM
# yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
# yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
# plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
# plt.xlabel("yaş grupları")
# plt.ylabel("Kişi Sayısı")
# plt.title("Histogram Grafiği")
# plt.show()

# Stack
# yil = [2011,2012,2013,2014,2015]
# oyuncu1 = [8,10,12,7,9]
# oyuncu2 = [7,12,5,15,21]
# oyuncu3 = [18,20,22,25,19]
# plt.plot([],[],color="y",label="oyuncu1")
# plt.plot([],[],color="r",label="oyuncu2")
# plt.plot([],[],color="b",label="oyuncu3")
# plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
# plt.title("Yıllara göre atılan goller")
# plt.xlabel("yil")
# plt.ylabel("Gol Sayısı")
# plt.legend()
# plt.show()


# ---->
""""
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x, y, "o--r")
plt.axis([0,6, 0, 20])
plt.show()
"""

# x= np.linspace(0,2,100)

# plt.plot(x,x, label="linear")
# plt.plot(x,x**2, label="quadratic")
# plt.plot(x,x*3, label="cubic")

# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.legend()

# plt.show()

# ---> 
# x = np.linspace(0,2,100)
# fig, axs = plot.subplots(3)

# axs[0].plot(x,x, color="red")
# axs[0].set_title("linear")

# axs[1].plot(x,x**2, color="green")
# axs[1].set_title("quan")

# axs[2].plot(x,x**3, color="yellow")
# axs[2].set_title("cobuic")

#-,-->

# x = np.linspace(0,2,100)
# fig, axs = plot.subplots(2,2)
# fig.suptitle("grafik baş")

# axs[0, 0].plot(x,x, color="red")
# axs[0, 1].plot(x,x**2, color="blue")
# axs[1, 0].plot(x,x**3, color="green")
# axs[1, 1].plot(x,x**4, color="yellow")
# ---->
# df = pd.read_csv("Lib/nba.csv")
# df=df.drop(["Number"], axis=1).groupby("Team").mean()

# df.plot(subplots=True)
# plot.legend()
# ---->

# plot.show()

# ---->

# x = np.linspace(-10, 9, 20)
# y = x**3
# z = x**2
# figure = plot.figure()

# axes_cube = figure.add_axes([0.1,0.1,0.9,0.98])
# axes_cube.plot(x,y,'b')
# axes_cube.set_xlabel("X Axis")
# axes_cube.set_ylabel("Y Axis")
# axes_cube.set_title("AxisCUBE")

# axes_sq = figure.add_axes([0.15,0.6,0.25,0.25])
# axes_sq.plot(x,y,'b')
# axes_sq.set_xlabel("X Axis")
# axes_sq.set_ylabel("Y Axis")
# axes_sq.set_title("AxisCUBE")
# plot.show()
# ---->

x = np.linspace(-10, 9, 20)
y = x**3
z = x**2


# figure = plot.figure()

# axes = figure.add_axes([0,0,1,1])
# axes.plot(x,z, label="Square")
# axes.plot(x,y, label="Cube")

# axes.legend()
# ---->

# fix, axes = plot.subplots(nrows=2, ncols=1, figsize=(8,8))

# axes[0].plot(x,y)
# axes[0].set_title("Cb")
# axes[0].plot(x,z)
# axes[0].set_title("sq")

# plot.tight_layout()
# fix.savefig("f1.pdf")
# plot.show()

"""
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]

plot.plot([], [], color="y", label="oyuncu1")
plot.plot([], [], color="r", label="oyuncu2")
plot.plot([], [], color="b", label="oyuncu3")

plot.stackplot(yil, oyuncu1, oyuncu2,oyuncu3, colors=["y","r","b"])
plot.title("yıl bilgilerine göre")
plot.xlabel("yil")
plot.ylabel("gol")
plot.legend()
plot.show()
"""
#----->

# goal_tyoes = "Penaltı", "Kaleye Atılan Şut", "Serbest Vuruş"

# goals = [12,35,7]

# colors = ["y", "r", "b"]

# plot.pie(goals, labels=goal_tyoes, colors=colors, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%")

# plot.show()

#----->
# plot.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50,40,70,80,20], label="BMW", width=5)
# plot.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80,20,20,50,60], label="Audi", width=5)

# plot.legend()
# plot.xlabel("Gün")
# plot.ylabel("Mesafe (km)")
# plot.title("Araç Bilgileri")

# plot.show()
#----->

yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plot.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plot.xlabel("yaş grupları")
plot.ylabel("Kişi Sayısı")
plot.title("Histogram Grafiği")


plot.show()

