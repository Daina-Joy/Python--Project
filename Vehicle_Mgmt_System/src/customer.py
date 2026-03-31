class Customer_Panel:
     def __init__(self,customers,vehicles,cursor,conn):
          self.vehicles=vehicles
          self.customers=customers
          self.cursor=cursor
          self.conn=conn
          
     def register(self,cid,name,phone):
          self.customers[cid]={
               "id":cid,
               "name":name,
               "phone":phone,
               "rented_status":0,
               "rented_vehicle" :None
          }
          self.cursor.execute("INSERT INTO customers (cid,name,phone) VALUES  (?,?,?)",(cid,name,phone))
          print(f"--------------------Customer:{name} was successfully added----------------------")
          print("***********************************************************************")
     def show_available_vehicles(self):
        print("----------------------------Displaying vehicle details:-------------------------")
        self.cursor.execute("SELECT vid, rent, brand FROM vehicles WHERE available = 1")
        rows = self.cursor.fetchall()

        if not rows:
         print("---------No vehicles available------ ")
        else:
          for row in rows:
            print(f"Vehicle: {row[0]}, Rent: {row[1]}, Brand: {row[2]} Available")

        print("***********************************************************************")

     def rent_a_vehicle(self,cid,vid):
          self.cursor.execute("SELECT * FROM customers WHERE cid = ?", (cid,))
          customer = self.cursor.fetchone()
          if not customer:
            print("Customer not found, please register ")
            return
          # Check vehicle exists
          self.cursor.execute("SELECT available,model,brand FROM vehicles WHERE vid = ?", (vid,))
          vehicle = self.cursor.fetchone()
          print(f"vehicle available:{vehicle}")
          if not vehicle:
           print("Vehicle does not exist ")
           return
          if vehicle[0] == 0:
             print("Vehicle already rented ")
             return
          self.cursor.execute("UPDATE vehicles SET available = 0 WHERE vid = ?", (vid,))
          
          self.cursor.execute(
           "INSERT INTO rentals (cid, vid, rent_date, status) VALUES (?, ?, date('now'), 'RENTED')",
          (cid, vid)
          )

          self.conn.commit()

         
          print(f"----------{ customer[1]}  rented {vehicle[1]} ({vehicle[2]})")
          print("***********************************************************************")

     def  return_a_vehicle(self,cid):
            self.cursor.execute("SELECT * FROM customers WHERE cid = ?", (cid,))
            customer =self.cursor.fetchone()
            if not customer:
               print("Customer not found !!!!")
               return
            self.cursor.execute("SELECT vid FROM rentals WHERE cid = ? AND status = 'RENTED'",(cid,))
            result = self.cursor.fetchone()
          #   print("++++++++++++++Fetch all customer++++++")
          #   self.cursor.execute("select cid from rentals")
          #   customer1=self.cursor.fetchall()
          #   print(f"customer vehicle:{customer1}")
            if   not result :
                print(f"No vehicle is rented by this customer {cid}")
                return
            rented_vid = result[0]
            self.cursor.execute("UPDATE vehicles SET available = 1 WHERE vid = ?",(rented_vid,))
            self.cursor.execute("UPDATE rentals SET return_date = date('now'), status = 'RETURNED' WHERE cid = ? AND vid = ? AND status = 'RENTED'",
                               (cid, rented_vid,))

            self.conn.commit()
            print(f"----------------{customer[1]} returned {rented_vid}------------------")
            print("***********************************************************************")
           

# customer = Customer_Panel(customers,vehicles)
# customer.register("c01","dfr","345464")
# customer.show_available_vehicles()
# customer.rent_a_vehicle()