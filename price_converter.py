import tkinter as tk

def main():
    numbers = input_box.get("1.0","end-1c").splitlines()
    converter(numbers)
    
def converter(number):
    converted_nums_list = {}
    for i in range(len(number)):
        x,y = number[i].split(".")
        len_y = len(y)

        if len_y <= 6:
            powers_div = 10**(len_y-2)

            if len_y == 1:
                powers_div = 1

            converted_nums = f"{powers_div*float(number[i]):.2f}"
            converted_nums_list[converted_nums] = str(powers_div) #['1.23':1, "12.34":10]; original 1.23, 1.234

    #display results in the Text widgets
    unit_price_box.insert('1.0', "\n".join(converted_nums_list.keys()))
    ##use .insert to add this result to Text widget
    price_break_box.insert('1.0', "\n".join(converted_nums_list.values()))

#set up the window
window = tk.Tk()
window.title("PO Price Converter")

#create an input box
input_box = tk.Text(window, height = 5, width= 30)
input_box.pack()

#create the button to convert
convert_button = tk.Button(window, text = "Convert", command = main)
convert_button.pack()

#create a result box (w/ Unit price)
unit_price_box = tk.Text(window, height = 5, width = 30)
unit_price_box.pack()

#create a result box (w/ Price break)
price_break_box = tk.Text(window, height = 5, width = 30)
price_break_box.pack()


window.mainloop()
          
