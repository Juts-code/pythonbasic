List = []
n = 0

Number = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    List.append(value)

print("\nPositive Numbers in this List are : ")
while(n < Number):
    if(List[n] >= 0):
        print(List[n], end = '   ')
    n = n + 1
