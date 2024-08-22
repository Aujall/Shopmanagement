import tkinter as tk
from tkinter import ttk, messagebox

# Simulate a simple database using dictionaries
products = {}
sales = []
returns = []
purchases = []
purchase_returns = []

# Define colors for better aesthetics
PRIMARY_COLOR = '#6200EA'
SECONDARY_COLOR = '#BB86FC'
BACKGROUND_COLOR = '#F5F5F5'
TEXT_COLOR = '#333333'

# Function to check login credentials
def check_login():
    user_id = entry_id.get()
    password = entry_password.get()
    
    # Correct credentials (can be expanded with a real database)
    correct_id = "admin"
    correct_password = "password"
    
    if user_id == correct_id and password == correct_password:
        messagebox.showinfo("Login Success", "Welcome to the Shop Management System")
        login_window.destroy()  # Close the login window
        load_main_app()  # Load the main application
    else:
        messagebox.showerror("Login Failed", "Invalid User ID or Password")

# Function to load the dashboard
def load_dashboard(content_frame):
    clear_frame(content_frame)
    
    label_dashboard = tk.Label(content_frame, text="Dashboard", font=("Helvetica", 24, 'bold'), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_dashboard.pack(pady=20)

def load_dashboard(content_frame):
    clear_frame(content_frame)
    
    # Add a label for the title
    label_dashboard = tk.Label(content_frame, text="Dashboard", font=("Helvetica", 24, 'bold'), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_dashboard.pack(pady=20)
    
    # Load and display the PNG image
    try:
        # Ensure the image file is in the same directory as your script
        dashboard_image = tk.PhotoImage(file="PNG1.png")
        image_label = tk.Label(content_frame, image=dashboard_image, bg=BACKGROUND_COLOR)
        image_label.image = dashboard_image  # Keep a reference to avoid garbage collection
        image_label.pack(pady=20)
    except tk.TclError:
        # If the image fails to load, show an error message
        messagebox.showerror("Image Error", "Failed to load dashboard image. Make sure 'dashboard_image.png' is in the script directory.")


# Function to manage products
def load_product_management(content_frame):
    clear_frame(content_frame)

    label_product = tk.Label(content_frame, text="Product Management", font=("Helvetica", 24, 'bold'), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_product.pack(pady=20)

    tk.Label(content_frame, text="Product Name:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    product_name_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    product_name_entry.pack(pady=5)

    tk.Label(content_frame, text="Product Price:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    product_price_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    product_price_entry.pack(pady=5)

    tk.Label(content_frame, text="Stock Quantity:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    product_stock_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    product_stock_entry.pack(pady=5)

    def add_product():
        name = product_name_entry.get()
        try:
            price = float(product_price_entry.get())
            stock = int(product_stock_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Price and Stock must be numeric.")
            return
        if name:
            products[name] = {"price": price, "stock": stock}
            messagebox.showinfo("Product Added", f"Product {name} added successfully!")
        else:
            messagebox.showerror("Input Error", "Product Name cannot be empty.")

    add_product_button = tk.Button(content_frame, text="Add Product", font=("Helvetica", 14, 'bold'), command=add_product,
                                    bg=PRIMARY_COLOR, fg='white', relief='raised', bd=2)
    add_product_button.pack(pady=20)

# Function to manage sales
def load_sales_management(content_frame):
    clear_frame(content_frame)

    label_sales = tk.Label(content_frame, text="Sales Management", font=("Helvetica", 24, 'bold'), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_sales.pack(pady=20)

    tk.Label(content_frame, text="Product Name:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    product_name_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    product_name_entry.pack(pady=5)

    tk.Label(content_frame, text="Quantity:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    quantity_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    quantity_entry.pack(pady=5)

    def process_sale():
        name = product_name_entry.get()
        try:
            quantity = int(quantity_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be a number.")
            return
        if name in products and products[name]['stock'] >= quantity:
            total_price = products[name]['price'] * quantity
            products[name]['stock'] -= quantity
            sales.append({"type": "Sale", "name": name, "quantity": quantity, "total": total_price})
            messagebox.showinfo("Sale Processed", f"Sale processed for {name}. Total: ₹ {total_price}")
        else:
            messagebox.showerror("Sale Error", "Product not available or insufficient stock.")

    process_sale_button = tk.Button(content_frame, text="Process Sale", font=("Helvetica", 14, 'bold'),
                                     command=process_sale, bg=PRIMARY_COLOR, fg='white', relief='raised', bd=2)
    process_sale_button.pack(pady=20)

# Function to manage returns
def load_return_management(content_frame):
    clear_frame(content_frame)

    label_return = tk.Label(content_frame, text="Returns Management", font=("Helvetica", 24, 'bold'), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_return.pack(pady=20)

    tk.Label(content_frame, text="Product Name:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    product_name_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    product_name_entry.pack(pady=5)

    tk.Label(content_frame, text="Quantity:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    quantity_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    quantity_entry.pack(pady=5)

    def process_return():
        name = product_name_entry.get()
        try:
            quantity = int(quantity_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be a number.")
            return
        if name in products:
            products[name]['stock'] += quantity
            returns.append({"type": "Return", "name": name, "quantity": quantity})
            messagebox.showinfo("Return Processed", f"Return processed for {name}.")
        else:
            messagebox.showerror("Return Error", "Product not found.")

    process_return_button = tk.Button(content_frame, text="Process Return", font=("Helvetica", 14, 'bold'),
                                       command=process_return, bg=PRIMARY_COLOR, fg='white', relief='raised', bd=2)
    process_return_button.pack(pady=20)

# Function to manage purchases
def load_purchase_management(content_frame):
    clear_frame(content_frame)

    label_purchase = tk.Label(content_frame, text="Purchase Management", font=("Helvetica", 24, 'bold'), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_purchase.pack(pady=20)

    tk.Label(content_frame, text="Product Name:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    product_name_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    product_name_entry.pack(pady=5)

    tk.Label(content_frame, text="Quantity:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    quantity_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    quantity_entry.pack(pady=5)

    def process_purchase():
        name = product_name_entry.get()
        try:
            quantity = int(quantity_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be a number.")
            return
        if name in products:
            products[name]['stock'] += quantity
            total_cost = products[name]['price'] * quantity
            purchases.append({"type": "Purchase", "name": name, "quantity": quantity, "total_cost": total_cost})
            messagebox.showinfo("Purchase Processed", f"Purchase processed for {name}. Total Cost: ₹ {total_cost}")
        else:
            messagebox.showerror("Purchase Error", "Product not found.")

    process_purchase_button = tk.Button(content_frame, text="Process Purchase", font=("Helvetica", 14, 'bold'),
                                         command=process_purchase, bg=PRIMARY_COLOR, fg='white', relief='raised', bd=2)
    process_purchase_button.pack(pady=20)

# Function to manage purchase returns
def load_purchase_return_management(content_frame):
    clear_frame(content_frame)

    label_purchase_return = tk.Label(content_frame, text="Purchase Return Management", font=("Helvetica", 24, 'bold'),
                                      bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_purchase_return.pack(pady=20)

    tk.Label(content_frame, text="Product Name:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    product_name_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    product_name_entry.pack(pady=5)

    tk.Label(content_frame, text="Quantity:", font=("Helvetica", 14), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=5)
    quantity_entry = tk.Entry(content_frame, font=("Helvetica", 14))
    quantity_entry.pack(pady=5)

    def process_purchase_return():
        name = product_name_entry.get()
        try:
            quantity = int(quantity_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be a number.")
            return
        if name in products:
            products[name]['stock'] -= quantity
            total_refund = products[name]['price'] * quantity
            purchase_returns.append({"type": "Purchase Return", "name": name, "quantity": quantity, "total_refund": total_refund})
            messagebox.showinfo("Purchase Return Processed", f"Purchase return processed for {name}. Total Refund: ₹ {total_refund}")
        else:
            messagebox.showerror("Purchase Return Error", "Product not found.")

    process_purchase_return_button = tk.Button(content_frame, text="Process Purchase Return",
                                                font=("Helvetica", 14, 'bold'), command=process_purchase_return, bg=PRIMARY_COLOR, 
                                                fg='white', relief='raised', bd=2)
    process_purchase_return_button.pack(pady=20)

# Function to manage stock
def load_stock_management(content_frame):
    clear_frame(content_frame)

    label_stock = tk.Label(content_frame, text="Stock Management", font=("Helvetica", 24, 'bold'), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_stock.pack(pady=20)

    # Display stock information
    stock_text = tk.Text(content_frame, width=60, height=20, font=("Helvetica", 14))
    stock_text.pack(pady=20)
    
    for product, details in products.items():
        stock_text.insert(tk.END, f"Product: {product}\nPrice: ₹ {details['price']}\nStock: {details['stock']}\n\n")

# Function to manage transaction history
def load_transaction_history(content_frame):
    clear_frame(content_frame)

    label_history = tk.Label(content_frame, text="Transaction History", font=("Helvetica", 24, 'bold'), bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
    label_history.pack(pady=20)

    history_text = tk.Text(content_frame, width=80, height=20, font=("Helvetica", 14))
    history_text.pack(pady=20)

    for transaction in sales + returns + purchases + purchase_returns:
        history_text.insert(tk.END, f"Type: {transaction['type']}\n")
        history_text.insert(tk.END, f"Product Name: {transaction['name']}\n")
        history_text.insert(tk.END, f"Quantity: {transaction.get('quantity', 'N/A')}\n")
        history_text.insert(tk.END, f"Total: {transaction.get('total', 'N/A')}\n")
        history_text.insert(tk.END, f"Total Cost: {transaction.get('total_cost', 'N/A')}\n")
        history_text.insert(tk.END, f"Total Refund: {transaction.get('total_refund', 'N/A')}\n")
        history_text.insert(tk.END, "-"*50 + "\n")

# Function to clear the content frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Function to load the main application
def load_main_app():
    global main_window
    main_window = tk.Tk()
    main_window.title("Store Management System")
    main_window.geometry("1200x800")
    main_window.configure(bg=BACKGROUND_COLOR)
    
    sidebar = tk.Frame(main_window, width=200, bg=PRIMARY_COLOR, height=800, relief='raised', bd=2)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)
    
    content_frame = tk.Frame(main_window, bg=BACKGROUND_COLOR)
    content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    tk.Label(sidebar, text="Shop Management System", font=("Helvetica", 20, 'bold'), bg=PRIMARY_COLOR, fg='white').pack(pady=20)
    
    buttons = [
        ("Dashboard", load_dashboard),
        ("Product Management", load_product_management),
        ("Sales Management", load_sales_management),
        ("Return Management", load_return_management),
        ("Purchase Management", load_purchase_management),
        ("Purchase Return Management", load_purchase_return_management),
        ("Stock Management", load_stock_management),
        ("Transaction History", load_transaction_history),
    ]
    
    for text, command in buttons:
        button = tk.Button(sidebar, text=text, font=("Helvetica", 16, 'bold'), command=lambda cmd=command: cmd(content_frame), bg=SECONDARY_COLOR, fg='white', relief='raised', bd=2)
        button.pack(pady=10, fill=tk.X, padx=10)
    
    main_window.mainloop()

# Function to open login window
def open_login():
    global login_window
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x250")
    login_window.configure(bg=BACKGROUND_COLOR)
    
    tk.Label(login_window, text="User ID", font=("Helvetica", 16), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=10)
    global entry_id
    entry_id = tk.Entry(login_window, font=("Helvetica", 16))
    entry_id.pack(pady=10)
    
    tk.Label(login_window, text="Password", font=("Helvetica", 16), bg=BACKGROUND_COLOR, fg=TEXT_COLOR).pack(pady=10)
    global entry_password
    entry_password = tk.Entry(login_window, show="*", font=("Helvetica", 16))
    entry_password.pack(pady=10)
    
    tk.Button(login_window, text="Login", font=("Helvetica", 16, 'bold'), command=check_login, bg=PRIMARY_COLOR, fg='white',
               relief='raised', bd=2).pack(pady=20)
    
    login_window.mainloop()

open_login()
 