import tkinter
import tkinter.ttk

MILES_TO_KM_CONVERT_FACTOR = 1.60934


def calculate():
    miles = float(entry_miles.get())
    km = round(miles * MILES_TO_KM_CONVERT_FACTOR)
    label_result["text"] = str(km)


root = tkinter.Tk()
# root.config(text="Miles for Kilometers Converter")

root.title("Miles to Kilometer Conversion")
root.minsize(height=100, width=300)

frm = tkinter.ttk.Frame(root, padding=10)
frm.grid()

label_miles = tkinter.ttk.Label(frm, text="Miles")
label_miles.grid(column=2, row=0, pady=5)

style = tkinter.ttk.Style(root)
style.configure("My.TEntry", padding=(5, 1, 1, 1))
# padding = (padx left, pady up,padx right,pady down)


entry_miles = tkinter.ttk.Entry(frm, width=30, style="My.TEntry")
entry_miles.grid(column=1, row=0, padx=5, pady=5)

label_equal = tkinter.ttk.Label(frm, text="is equal:")
label_equal.grid(column=0, row=1, pady=5)

label_result = tkinter.ttk.Label(frm, width=30, text="result")
label_result.grid(column=1, row=1, padx=(10, 10), pady=5)
label_result.configure(anchor="center")

label_kilometers = tkinter.ttk.Label(frm, text="Kilometers")
label_kilometers.grid(column=2, row=1, pady=5)

button = tkinter.ttk.Button(frm, text="Calculate", command=calculate)
button.grid(column=1, row=2, pady=5)
root.mainloop()
