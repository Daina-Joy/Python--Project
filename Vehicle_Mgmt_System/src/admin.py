class AdminPanel:
    def __init__(self,vehicles,cursor):
        self.vehicles=vehicles
        self.cursor = cursor
       
    def add_new_vehicle(self,vehicle_id,vehicle_model,rent,vehicle_color,vehicle_brand):
        self.vehicles[vehicle_id] = {
            "id":vehicle_id,
            "rent":rent,
            "model":vehicle_model,
            "color":vehicle_color,
            "brand":vehicle_brand,
            "available":True
        }
        self.cursor.execute("INSERT INTO vehicles (vid, model, rent, color,brand,available) VALUES (?, ?, ?, ?, ?, ?)",
                       (vehicle_id, vehicle_model,rent,vehicle_color,vehicle_brand,1))
        print(f"Vehicle:{vehicle_id}  was addded succesfully")
        print("***********************************************************************")
        
    def display_all_vehicles(self):
      #print(self.vehicles)
      self.cursor.execute("SELECT * FROM vehicles")
      rows=self.cursor.fetchall()
      if not rows:
         print("No vehicles available ")
      for row in rows:    
        print(row)   
         #print(f"{key}: {value['brand']} costs:{value['rent']} per day,Available:{value['available']}")
      print("***********************************************************************")
vehicles = {}
#admin=AdminPanel(vehicles)
#admin.add_new_vehicle("V01","bike",2500,"red","RE350")
#admin.display_all_vehicles()