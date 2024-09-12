print("solution a")
# solution a

height: float = float(input("Enter height :"))
while True:
    if 0.4 <= height <= 2.5:
        print("Your height  is ok")
        break
    else:
        print("wrong input")
        height: float = float(input("Enter height :"))

print("\n" "solution b")
# solution b

num_1: int = int(input("Enter num1"))
num_2: int = int(input("Enter num2"))

if num_2 > num_1:
    for x in range(num_1, num_2+1):
        print(x, end=" ")
else:
    for x in range(num_2, num_1+1):
        print(x, end=" ")

print("\n" "solution c")
# solution c

counter: int = 0
for x in range(3):
    pai: float = float(input("What is the value of pi?"))
    if pai == 3.14:
        print("correct are you")
        break

if pai != 3.14:
    print(" 3.14 is pie ")

print("\n" "solution d")
# solution d

while True:
    num_1: int = int(input("Enter num1"))
    num_2: int = int(input("Enter num2"))
    num_3: int = int(input("Enter num3"))
    if 60 <= num_3 <= 100 and 10 <= num_2 <= 60 and 0 <= num_1 <= 10 and num_2 == (num_2 + num_3 + num_1) / 3:
        print("Successful")
        break
    else:
        print("Try agin :")

print("\n" "solution Chalnge")
# solution e

bear: int = 10
while bear > 1:
    age: int = int(input("Ennter your age"))
    if age >= 18:
        print(bear, end =" ")
        bear -= 1
