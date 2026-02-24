class Carrier:
        def __init__(self,carrier_id,name):
            self.name = name
            self.carrier_id = carrier_id
            pass

class Truck:
        def __init__(self,truck_id,capacity):
            self.truck_id = truck_id
            self.capacity = capacity
            self.available = True
            self.current_load = 0
            pass


