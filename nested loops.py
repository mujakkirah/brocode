# nested loop = A loop within another loop ( outer , inner )
#                                    outer loop:
#                                      inner loop: 

rows = int(input("Enter the # of rows: "))
colums = int(input("Enter the # of colums: "))
symbol = input("Enter a symbol to use: ")


for x in range(rows):
  for y in range (colums):
     print(symbol, end= "")
     print()


#for x in range(3):
#  for y in range (1, 10):
#     print(y, end= " ")
#     print()

#for x in range (1, 10):
#    print(x, end ="")