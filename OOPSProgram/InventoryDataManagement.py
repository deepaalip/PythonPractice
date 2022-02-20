import json
import os
class main:
 
 def readWrite():
  print(os.getcwd())
  print(os.path.abspath('inventoryData.json'))
base_dir = 'c:/Users/DELL/Documents/PythonBridgelabz/OOPSProgram/inventoryData.json'
with open(base_dir,'r') as f:
    data = json.load(f)           #convert json to python string
    
# for inventory_Data in data['rice']:
#     print(inventory_Data) 
# for inventory_Data in data['wheats']:
#       print(inventory_Data) 
# for inventory_Data in data['pulses']:
#      print(inventory_Data)   


# dic ={
#     "rice": [
# 		{
# 			"price_per_kg": 60,
# 			"name": "basmati",
# 			"weight": 7
# 		}
# 	],
# 	"wheats": [
# 		{
# 			"price_per_kg": 45,
# 			"name": "chakki_fresh",
# 			"weight": 5
# 		}
# 	],
# 	"pulses": [
# 		{
# 			"price_per_kg": 65,
# 			"name": "greens",
# 			"weight": 3
# 		}
# 	]



# }
    
    with open("inventory.json", "w") as outfile:
       json.dump(data, outfile)               #convert python object to json object
       
       
if __name__ == "_main_":
      printData = main()
      printData.readWrite()
      

































