import csv
class main:
  def readWrite():   
                 
    with open("/Users/DELL/Documents/PythonBridgelabz/OOPSProgram/data.csv", "r") as csvfile:
     data = csv.reader(csvfile)
     #for row in data:
      #print(row)

    with open('newData.csv','w') as file:
      writer = csv.writer(file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  
      writer.writerows(data)
     
if __name__ == "_main_":
    outputdata = main()
    outputdata.readWrite()