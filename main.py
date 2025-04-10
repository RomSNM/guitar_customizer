from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class GuitarRequest:
    def __init__(self, model, frets, pickups, color, bridge):
        self.model = model
        self.frets = frets
        self.pickups = pickups
        self.color = color
        self.bridge = bridge
        self.cost = 0

    def calculate_cost(self):
        cost_model = {"Stratocaster": 500, "Telecaster": 450, "Les Paul": 700}
        cost_frets = {"22": 100, "24": 150}
        cost_pickups = {"Single": 200, "Humbucker": 300}
        cost_color = {"Black": 50, "White": 50, "Red": 60, "Burst": 100}
        cost_bridge = {"Tuneomatic": 100, "Floyd": 200}

        try:
            self.cost += cost_model[self.model]
            self.cost += cost_frets[self.frets]
            self.cost += cost_pickups[self.pickups]
            self.cost += cost_color[self.color]
            self.cost += cost_bridge[self.bridge]
        except KeyError as e:
            messagebox.showerror("Invalid Input", f"Invalid option selected: {e}")
            return None

        return self.cost

# --------------------------- GRAPHICAL INTERFACE ------------------------------------

window = Tk()
window.title('Custom Guitar Request')
window.config(padx=20, pady=20)

THEME_COLOR = "#375362"

canvas = Canvas(height=250, width=250)
logo_img = PhotoImage(file='C:\\Users\\Desktop\\Documents\\Códigos\\custom_logo.png')
canvas.create_image(150, 100, image=logo_img)
canvas.grid(column=1, row=0)
canvas.create_text(120, 230, width=280, text='Choose your specifications', fill=THEME_COLOR, font=('Arial', 10, 'italic'))

# Labels
Label(text='Model').grid(row=1, column=0)
Label(text='Frets').grid(row=2, column=0)
Label(text='Pickups').grid(row=3, column=0)
Label(text='Color').grid(row=4, column=0)
Label(text='Bridge').grid(row=5, column=0)

# Comboboxes
model_combo = ttk.Combobox(values=["Stratocaster", "Telecaster", "Les Paul"], width=27)
model_combo.grid(row=1, column=1, columnspan=2)
model_combo.set("Stratocaster")

frets_combo = ttk.Combobox(values=["22", "24"], width=27)
frets_combo.grid(row=2, column=1, columnspan=2)
frets_combo.set("22")

pickups_combo = ttk.Combobox(values=["Single", "Humbucker"], width=27)
pickups_combo.grid(row=3, column=1, columnspan=2)
pickups_combo.set("Single")

color_combo = ttk.Combobox(values=["Black", "White", "Red", "Burst"], width=27)
color_combo.grid(row=4, column=1, columnspan=2)
color_combo.set("Black")

bridge_combo = ttk.Combobox(values=["Tuneomatic", "Floyd"], width=27)
bridge_combo.grid(row=5, column=1, columnspan=2)
bridge_combo.set("Tuneomatic")

# Action
def sum_cost():
    model = model_combo.get()
    frets = frets_combo.get()
    pickups = pickups_combo.get()
    color = color_combo.get()
    bridge = bridge_combo.get()

    request = GuitarRequest(model, frets, pickups, color, bridge)
    cost_total = request.calculate_cost()

    if cost_total is not None:
        resultado_label.config(text=f"Total cost: R$ {cost_total}")

sum_button = Button(text='Calculate Cost', command=sum_cost)
sum_button.grid(row=6, column=1)

resultado_label = Label(text="Total cost: R$ 0")
resultado_label.grid(row=7, column=1)

window.mainloop()