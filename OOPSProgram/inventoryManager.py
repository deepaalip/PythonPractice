import json
import os
class main:
    def read():   
      print(os.getcwd())
      print(os.path.abspath('inventoryData.json'))
base_dir = 'c:/Users/DELL/Documents/PythonBridgelabz/OOPSProgram/inventoryData.json'
with open(base_dir,'r') as f:
 data = json.load(f)
 value = dict()
 for inventory_Data in data['rice']:
     price_per_kg = inventory_Data['price_per_kg']
     weight = inventory_Data['weight']
     print(price_per_kg*weight)
     print(inventory_Data)
 for inventory_Data in data['wheats']:
    price_per_kg = inventory_Data['price_per_kg']
    weight = inventory_Data['weight']
    print(price_per_kg*weight)
    print(inventory_Data)
 for inventory_Data in data['pulses']:
    price_per_kg = inventory_Data['price_per_kg']
    weight = inventory_Data['weight']
    print(price_per_kg*weight)      
    print(inventory_Data) 
    
 if __name__ == "_main_":
    printData = main() 
    printData.read()   