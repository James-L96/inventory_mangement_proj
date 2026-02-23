# Logistics project
#Inventory management system that allows admin to add, remove, and update a virtual warehouse
# Lightweight inventory management system for tracking warehouse items across locations, quantities, types and companies.\n
# Command line based and later web based usage.
#Tech and industrial projects to be tracked.
"""
Key fields: location_warehouse, quantity, type, and company

location_warehouse: Three buildings(A, B,and C). Will each warehouse have its own set quantity?Yes

quantity:Tied to each set warehouse location.

type: items to be held will be either technical or industrial.

Will be tied to company item is being set too.

Create file for both inventory which will hold the above key fields.
"""

"""Create a file to hold shippers and the carrier they are under.
Fedex,RXO,DHL, and N&M.
"""

"""
Entirely optional but do I have a mapping module called plotly I could used to place the warehouses on the map.
"""

"""
RULES:
1.Quantity can be 0 which should signify item is out of stock. However items cannot be shipped when at 0.
2.A shipment is only valid if inventory exists, quantity is positive, and a carrier is available.
3.Though items can be sent to one or more locations, the ids must be unique per item.

NON-GOALS (for now):
- No user authentication
- No real-time tracking
- No external APIs


"""




# Focus on clarity, validation rules, and future scalability over features