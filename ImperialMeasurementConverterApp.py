# This still needs a bit of tidying up but it does actually work!
# pip install tkinter
import tkinter as tk
from tkinter import *
import tkinter.messagebox
# import data_file as df


class Unit:
    def __init__(self, name, base, B, In, F, Y, C, Fu, M):
        self.name = name
        self.base = base
        self.B = B
        self.In = In
        self.F = F
        self.Y = Y
        self.C = C
        self.Fu = Fu
        self.M = M

    def get_base_value(self):
        return self.base

    def get_B_value(self):
        return self.B

    def get_inches_value(self):
        return self.In

    def get_F_value(self):
        return self.F
    
    def get_Y_value(self):
        return self.Y

    def get_C_value(self):
        return self.C

    def get_Fu_value(self):
        return self.Fu

    def get_M_value(self):
        return self.M


B = Unit("Barleycorn", 1, 1, 3, 36, 108, 2376, 23760, 190080)
In = Unit("Inch", 3, 3, 1, 12, 36, 792, 7920, 63360)
F = Unit("Foot", 36, 36, 12, 1, 3, 22, 220, 5280)
Y = Unit("Yard", 108, 108, 36, 3, 1, 22, 220, 1760)
C = Unit("Chain", 2376, 2376, 108, 66, 22, 1, 10, 80)
Fu = Unit("Furlong", 23760, 23760, 63360, 660, 220, 10, 1, 8)
M = Unit("Mile", 190080, 190080, 63360, 5280, 1760, 80, 8, 1)


# Store units in a dictionary for easy access
units = {
    "Barleycorn": B,
    "Inch": In,
    "Foot": F,
    "Yard": Y,
    "Chain": C,
    "Furlong": Fu,
    "Mile": M
}


root = tk.Tk()

root.title("Imperial Measurements Converter: Baines Services")

Tops = Frame(root, bg = '#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=0)

headlabel = tk.Label(Tops, font=('lato black', 19, 'bold'), text='Imperial Measurements Converter: Baines Services',
                    bg='#e6e5e5', fg='black')
headlabel.grid(row=1, column=0, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)

variable1.set("Input Measurement")
variable2.set("Output Measurement")
# Function To For Real Time Currency Conversion


def RealTimeConverter():
    # Get user input for the unit
    selected_unit_name = variable1.get()
    selected_output_name = variable2.get()
    
    # Check if the selected unit is valid
    if selected_unit_name in units:
        selected_unit = units[selected_unit_name]
        
        # Get the amount to convert
        amount = float(Amount1_field.get())
        
        # Calculate the result (amount * base value of the selected unit)
        result = amount * selected_unit.get_base_value()
        
#        print(f"\nThe result for amount of barleycorns in {amount} of {selected_unit_name} is: {result}")
    
    
#    selected_output_name = input("\nSelect a unit from the list: ").capitalize()
    if selected_output_name in units:
        output_unit = units[selected_output_name]

        if selected_output_name != 'Barleycorn':
            new_result = result / output_unit.get_B_value()
        elif selected_output_name != 'Inch':
            new_result = result / output_unit.get_inches_value()
        elif selected_output_name != "Foot":
            new_result = result / output_unit.get_F_value()
        elif selected_output_name != "Yard":
            new_result = result / output_unit.get_Y_value()
        elif selected_output_name != "Chain":
            new_result = result / output_unit.get_C_value()
        elif selected_output_name != "Furlong":
            new_result = result / output_unit.get_Fu_value()
        elif selected_output_name != "Mile":
            new_result = result / output_unit.get_M_value()
    
        Amount2_field.insert(0, str(new_result))
    
    else:
        print("Invalid unit selected. Please try again.")


#clearing all the data entered by the user
def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)


unit_list = ["Barleycorn", "Inch", "Foot", "Yard", "Chain", "Furlong", "Mile"] 

root.configure(background='#e6e5e5')
root.geometry("700x400")

Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#e6e5e5", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

selected_unit_name = tk.OptionMenu(root, variable1, *unit_list)
selected_output_name = tk.OptionMenu(root, variable2, *unit_list)

selected_unit_name.grid(row=3, column=0, ipadx=45, sticky=E)
selected_output_name.grid(row=4, column=0, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=RealTimeConverter)
Label_9.grid(row=6, column=0)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)


root.mainloop()
