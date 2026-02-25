class Carrier:
        COMPANIES = ['FedEx', 'UPS', 'RXO', 'XPO']
        TRUCKS = ['D1', 'D2', 'D3', 
                'E1', 'E2', 'E3',
                'F1', 'F2', 'F3',
                'G1', 'G2', 'G3',]
        def __init__(self,carrier_id,name,company):
            if company not in Carrier.COMPANIES:
                raise ValueError(f'Invalid carrier company: {company}')
            self.name = name
            self.carrier_id = carrier_id


class Truck:
        def __init__(self,truck_id,capacity, truck):
            if truck not in Carrier.TRUCKS:
                raise ValueError(f'Invalid truck Id.')
            
            self.truck_id = truck_id
            self.capacity = capacity
            self.available = True
            self.current_load = 0



