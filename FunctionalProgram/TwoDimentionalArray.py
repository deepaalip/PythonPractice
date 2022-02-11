def createArray(rows,cols):
  arr = [[i for i in range(cols)] for j in range(rows)]
  print(arr)
rows = int(input('Enter M number of rows: '))
cols = int(input('Enter N number of cols: '))
createArray(rows, cols)
