# for row in range(1, 5):
#     print("*")
#     for row in range(1, 0, -5):
#         print("*")


# Total number of rows = 5
#  Number of spaces for a row 4 space and 1 stars
#  Number spaces for 2nd row is 3 spaces and 2 stars     
#  Number spaces for 3nd row is 2 spaces and 3 stars     

# Total no of rows - Row number

# 5 - 3 = 2

# Num of stars = row number


# rows = int(input("Enter the no of rows: "))
# columns = int(input("Enter the no of columns: "))
# symbol = input("Enter a symbol to use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()    

print("*")

for i in range(5):
    print("*", end="")
    for j in range(i +1):
        print("*", end="") 
    print()       
  
