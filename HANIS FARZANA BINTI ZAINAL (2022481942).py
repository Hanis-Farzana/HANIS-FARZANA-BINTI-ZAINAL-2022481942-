import tkinter as tk 
from tkinter import messagebox 
import mysql.connector 
 
# Connect to your MySQL database 
mydb = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="", 
    database="concert" 
) 
 
# Create a cursor object to execute SQL queries 
mycursor = mydb.cursor() 
 
# Function to handle the database saving 
def calculate_total_cost(): 
    num_tickets = int(num_tickets_var.get()) 
    ticket_price = 50
    total_price = num_tickets * ticket_price 
    total_price_var.set(total_price)
    output_label.config(text=f"Total Cost: RM{total_price}") 

def collect_data(): 
    global num_tickets 
    accepted = accept_var.get() 
 
    if accepted == "accepted": 
        buyer_name = buyername.get() 
        gender_value = gender.get() 
        phone_value = phone.get() 
        email_value = email.get() 
        password_value = password.get() 
        payment_method_value = payment_method_var.get() 
        num_tickets = num_tickets_var.get() 
        total_price_value = total_price_var.get()
 
        if buyer_name and email_value and password_value: 
 
            # Inserting data into "users" table 
            sql = "INSERT INTO users (buyer_name, buyer_gender, buyer_phone, buyer_email, buyer_password, buyer_payment_method, num_tickets, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
            values = (buyer_name, gender_value, phone_value, email_value, password_value, payment_method_value, num_tickets, total_price_value) 
            mycursor.execute(sql, values) 
            mydb.commit() 
 
            # To print back the output 
            output_label.config(text=f"THANK YOU FOR YOUR PURCHASE!") 
            output_label.grid(row=15, column=3)
        else: 
            # Display a warning if required fields are empty 
            messagebox.showwarning(title="Error", message="Name, Email, and Password are required fields.") 
    else: 
        messagebox.showwarning(title="Error", message="Please accept the terms and conditions.") 
 
# Create a window 
root = tk.Tk() 
root.geometry("400x600") 
root.title("CONCERT TICKET PURCHASE SYSTEM") 
 
# Background color 
root.configure(bg="#E6E6FA") 
 
label = tk.Label(root, text="FATE CONCERT IN KL \n RM50 per person", bg="#E6E6FA", font=('Bakso Sapi', 13)) 
label.grid(row=0, column=3) 
 
name_label = tk.Label(root, text="Name*", bg="#F5F5DC") 
name_label.grid(row=1, column=2) 
 
gender_label = tk.Label(root, text="Gender", bg="#F5F5DC") 
gender_label.grid(row=2, column=2) 
 
phone_label = tk.Label(root, text="Phone number", bg="#F5F5DC") 
phone_label.grid(row=3, column=2) 
 
email_label = tk.Label(root, text="Email address*", bg="#F5F5DC") 
email_label.grid(row=4, column=2) 
 
password_label = tk.Label(root, text="Password*", bg="#F5F5DC") 
password_label.grid(row=5, column=2) 
 
payment_method_label = tk.Label(root, text="Payment method", bg="#F5F5DC") 
payment_method_label.grid(row=6, column=2) 
 
# Data entry 
buyername = tk.StringVar() 
buyername_entry = tk.Entry(root, textvariable=buyername) 
buyername_entry.grid(row=1, column=3) 
 
gender = tk.StringVar() 
gender_entry = tk.Entry(root, textvariable=gender) 
gender_entry.grid(row=2, column=3) 
 
phone = tk.StringVar() 
phone_entry = tk.Entry(root, textvariable=phone) 
phone_entry.grid(row=3, column=3) 
 
email = tk.StringVar() 
email_entry = tk.Entry(root, textvariable=email) 
email_entry.grid(row=4, column=3) 
 
password = tk.StringVar() 
password_entry = tk.Entry(root, textvariable=password) 
password_entry.grid(row=5, column=3) 
 
num_tickets_var = tk.StringVar() 
num_tickets_var.set("Select your ticket")  # Default value before your selection 
num_tickets_dropdown = tk.OptionMenu(root, num_tickets_var, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10") 
num_tickets_dropdown.grid(row=8, column=3) 
 
payment_method_var = tk.StringVar() 
payment_method_var.set("Select Payment Method")  # Default value before your selection 
payment_method_dropdown = tk.OptionMenu(root, payment_method_var, "Online Banking", "Credit/Debit Card", "E-Wallet") 
payment_method_dropdown.grid(row=6, column=3) 
 
total_price_var = tk.StringVar()

accept_var = tk.StringVar() 
 
# Creating check button 
check_button = tk.Checkbutton(text="I accept the terms and conditions", variable=accept_var, onvalue="accepted") 
check_button.grid(row=13, column=3) 
 
# Submit button 
submit_button = tk.Button(root, text="Save", command=collect_data) 
submit_button.grid(row=14, column=3) 
calculate_button = tk.Button(root, text="Calculate", command=calculate_total_cost) 
calculate_button.grid(row=9, column=3) 
 
#output 
output_label = tk.Label(root, text="") 
output_label.grid(row=10, column=3) 
 
 
root.mainloop()