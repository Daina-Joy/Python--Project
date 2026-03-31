# #register_User
# display_AvailableVehicles
# rent_Vehicle
# return_Vehicle

# showVehicles
# addVehicle

from src.admin import AdminPanel
from src.customer import Customer_Panel

import sqlite3   
conn = sqlite3.connect("rental.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles (
    vid TEXT PRIMARY KEY ,
    model TEXT,
    rent REAL,
    color TEXT,
    brand Text,
    available INTEGER
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
    cid TEXT PRIMARY KEY,
    name TEXT,
    phone TEXT
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS rentals (
    rid INTEGER PRIMARY KEY AUTOINCREMENT,
    cid TEXT,
    vid TEXT,
    rent_date TEXT,
    return_date TEXT,
    status TEXT,
    
    FOREIGN KEY (cid) REFERENCES customers(cid),
    FOREIGN KEY (vid) REFERENCES vehicles(vid)

)""")
conn.commit()

def main():
    print("**********************************************")
    print("     Welcome to Krish Rentals")
    print("**********************************************")
    print("\n")
    vehicles = {}
    admin=AdminPanel(vehicles,cursor)
    customers={}


    customer = Customer_Panel(customers,vehicles,cursor,conn)
    
    
    while True:
        print("Enter your choice:")    
        print("1.Admin Panel")   
        print("2.Customer Panel")   
        print("3.Exit()")
        user_input=int(input("Enter the choice:1/2/3:"))
        if user_input == 3:
         print("Thank you for using Krish Rentals")
         break
        elif user_input ==1:
            print("+++++++++++++Welcome to the Admin Panel++++++++++")
            while True:
             print("Enter your choice:")    
             print("1.Add new vehicle")   
             print("2.View Avaliable vehicle")   
             print("3.Exit()")
             admin_choice=int(input("Enter your choice 1/2/3:"))
             if(admin_choice == 1):
              print("Adding New vehicle")
              vehicle_id=input("Enter Vehicle Id:")
              vehicle_model = input("Enter Vehicle model:")
              rent = input("Enter Vehicle rent:")
              vehicle_color = input("Enter Vehicle Color:")
              vehicle_brand = input("Enter Vehicle Brand:")
              
              admin.add_new_vehicle(vehicle_id,vehicle_model,rent,vehicle_color,vehicle_brand)
             elif(admin_choice == 2):
              print("View vehicle option selected")
              admin.display_all_vehicles()
             elif(admin_choice == 3):
              print("*****************Exiting the Admin Panel********************")
              break
             else:
              print("--------------------------Invalid choice please try again!!!--------------------------")

        elif user_input == 2:
            print("+++++++++++++ Welcome to the Customer Panel++++++++++")
            while True:
             print("Enter your choice:")    
             print("1.Register yourself")   
             print("2.Display Avaliable vehicles")   
             print("3.Rent a vehicle")
             print("4.Return a vehicle")
             print("5.Exit()")
             customer_choice=int(input("Enter your choice 1/2/3/4/5:"))
             if(customer_choice == 1):
              cid=input("Enter your id:")
              name=input("Enter your name:")
              phone=input("enter your phone number:")
              customer.register(cid,name,phone)
             elif(customer_choice == 2):
              customer.show_available_vehicles()   
             elif(customer_choice == 3):
              cid = input("Enter your customer id:")
              vid = input("Enter vehicle id to rent:")
              customer.rent_a_vehicle(cid,vid)
             elif(customer_choice == 4):
              cid = input("Enter Customer ID: ")
              customer.return_a_vehicle(cid)
             elif(customer_choice == 5):
              print("**********Exiting the Customer Panel***********")
              break
             else:
              print("--------------------------Invalid choice please try again!!!-------")
           
        else:
           print("--------------------------Invalid Entry !!! please use 1/2/3-------------------")
main()
conn.close()
