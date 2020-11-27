class Bus():
  def __init__(self,capacity):
    self.capacity = capacity
    self.passengers = []
  
  def addPassenger(self,passenger_name):
    if not self.vacant_seats():
      return False 
    self.passengers.append(passenger_name)
    return True

  def vacant_seats(self):
    return self.capacity - len(self.passengers)
    
Jasper_1 = Bus(3)

family = ["Carl","Jhen","Father","Masha"]
for person in family:
  if Jasper_1.addPassenger(person):
    print(f"{person} is now onboard")
  else:
    print(f"There is no more seat for {person}")
