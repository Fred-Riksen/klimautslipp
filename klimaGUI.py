from utslipp import*
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def oppdater_graf(valg):
    global klimadata, graf_overskrift
    klimadata = []
    graf_overskrift = ""
    if valg == "Klimagasser":
        klimadata = klimagasser
        graf_overskrift = "Klimagasser"
    elif valg == "Karbondioksid":
        klimadata = karbondioksid
        graf_overskrift = "Karbondioksid"
    elif valg == "Metan":
        klimadata = metan
        graf_overskrift = "Metan"
    else:
        klimadata = []
        graf_overskrift = ""
    
    if klimadata:
        plt.clf()
        plt.plot(aarstall[s], klimadata[s])
        plt.xlabel("Årstall")
        plt.ylabel("1000 tonn")
        plt.title(graf_overskrift)
        plt.show()
        

# GUI
root = tk.Tk()
root.title("Klimadata")
root.geometry("400x300")

# Nedtrekksmeny
valg_var = tk.StringVar(root)
valg_var.set("Klimagasser")
valg_meny = tk.OptionMenu(root, valg_var, "Klimagasser", "Karbondioksid", "Metan", command=oppdater_graf)
valg_meny.pack(pady=10)

# Nedtrekksmeny for årstall
aarstall_var = tk.StringVar(root)
aarstall_var.set("")
aarstall_meny = tk.OptionMenu(root, aarstall_var, *aarstall, command=lambda x: oppdater_graf(valg_var.get(), int(aarstall_var.get())))
aarstall_meny.pack(pady=10)


# Startgraf
klimadata = klimagasser
graf_overskrift = "Klimagasser"

fig = plt.figure()
plt.plot(aarstall[s], klimadata[s])
plt.xlabel("Årstall")
plt.ylabel("1000 tonn")
plt.title(graf_overskrift)
plt.show()

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()
canvas.draw()
plot_widget.pack()


root.mainloop()
