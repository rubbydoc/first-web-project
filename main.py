from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk

root = Tk()
root.title("RETAIL-BILLING SYSTEM")
root.geometry('1250x750')

# variables
our_product = {"beer": "83", 
"coke" : "20", 
"juice": "25", 
"soda": "23",
"apple":"25", 
"orange":"15", 
"pineapple":"10", 
"banana":"5",
"kangkong":"20", 
"ampalaya":"30", 
"sayote":"15", 
"squash":"25",
"chicken":"100", 
"pork":"250", 
"choriso":"40", 
"hotdog":"25",
"lipstick":"50", 
"face powder":"25", 
"foundation":"250", 
"eye liner":"15",
"sardines":"21", 
"beef loaf":"25", 
"corned beef":"30", 
"ham":"40"
               
               }



# functions
def cart():
    billArea.configure(state="normal")
    entered_product = products.get()
    entered_quantity = qtyEntry.get()
    price = our_product[entered_product]
    total = int(price) * int(entered_quantity)
    product = our_product.keys()
    if entered_quantity.isdigit():
        if entered_product in product:
            bill_text = "{}\t\t{}\t\t{}\t\t{}\n".format(entered_product, entered_quantity, price, total)
            billArea.insert('insert', bill_text)
    else:
        messagebox.showerror("Oops!", "Invalid Quantity")


def get_product(Event):
    drinks = ["beer", "coke", "juice", "soda"]
    fruits = ["apple", "orange", "pineapple", "banana"]
    vegetables = ["kangkong", "ampalaya", "sayote", "squash"]
    meat = ["chicken", "pork", "choriso", 'hotdog']
    cosmetics = ["lipstick", 'face powder', "foundation", "eye liner"]
    canned_goods = ["sardines", "beef loaf", "corned beef", "ham"]

    list_of_product.configure(state='readonly')
    list_of_product.set('')

    pro = []
    selected_category = categories.get()
    if selected_category == 'drinks':
       pro.extend(drinks)
       
    elif selected_category == 'fruits':
        pro.extend(fruits)
    elif selected_category == 'vegetables':
        pro.extend(vegetables)
    elif selected_category == 'meat':
        pro.extend(meat)
    elif selected_category == 'cosmetics':
        pro.extend(cosmetics)
    elif selected_category == 'canned goods':
        pro.extend(canned_goods)

    list_of_product.configure(values=pro)
    list_of_product.bind("<<ComboboxSelected>>", show_qty)

def show_qty(Event):
    qtyEntry.configure(state="normal")


def clear():
    qtyEntry.delete(0, END)
    list_of_categories.configure(state="normal")
    list_of_product.configure(state="normal")
    list_of_categories.delete(0, END)
    list_of_product.delete(0, END)
    qtyEntry.configure(state="disabled")
    list_of_product.configure(state="disabled")
    list_of_categories.configure(state="readonly")

    




Label(root, text="BILLING SYSTEM").grid(row=0, column=0)

Label(root, text="Quantity").place(relx=0.01, rely=0.14)
qtyEntry = Entry(root, state='disabled')
qtyEntry.place(relx=0.08, rely=0.14, width=185)
cartBtn = Button(root, text="Add to Cart", command=cart)
cartBtn.place(relx=0.01, rely=0.30)
clearBtn = Button(root, text="Clear", command=clear)
clearBtn.place(relx=0.10, rely=0.30)
billArea = scrolledtext.ScrolledText(root, width=53, height=10, state="disabled")
billArea.place(relx=0.25, rely=0.09)
Label(root, text="Product").place(relx=0.25, rely=0.05)
Label(root, text="Quantity").place(relx=0.33, rely=0.05)
Label(root, text="Price").place(relx=0.43, rely=0.05)
Label(root, text="Total").place(relx=0.52, rely=0.05)

ttk.Label(root, text="Product").place(relx=0.01, rely=0.10)

products = StringVar()
list_of_product = ttk.Combobox(root, width=27, textvariable=products, state='disabled')

list_of_product.place(relx=0.08, rely=0.10)


ttk.Label(root, text="Category").place(relx=0.01, rely=0.06)

categories = StringVar()
list_of_categories = ttk.Combobox(root, width=27, textvariable=categories, state='readonly', values=( '',
       'drinks',
       'fruits',
       'vegetables',
       'meat',
       'cosmetics',
       'canned goods'))
list_of_categories.place(relx=0.08, rely=0.06)
list_of_categories.current(0)
list_of_categories.bind("<<ComboboxSelected>>", get_product)

root.mainloop()
