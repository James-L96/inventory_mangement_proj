import random 
class InventoryItem:
    def __init__(self,inventory_id,name):
        self.inventory = inventory_id
        self.name = name
        self.quantity = 100
        pass

class Warehouse:
    def __init__(self,warehouse_id,name,capacity):
        self.warehouse_id = warehouse_id
        self.name = name
        self.capacity = capacity
        Space = True
        pass


class InventoryManager:
    pass