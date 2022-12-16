import math

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start, end + 1):
   root = math.isqrt(num)
   if root ** 2 == num:
       print(num)
