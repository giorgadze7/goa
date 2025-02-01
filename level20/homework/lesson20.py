# დღე 20

# 1) if და else ის გამოყენებით შეამოწმეთ არის თუ არა რიცხვი ლუწი
# 2) if და else ის გამოყენებით დაწერეთ არის თუ არა მომხმარებელი სრულს წლოვანი (18 წლის) თუ არა
# 3) if elif და else არგუმენტების გამოყენებით დაუცერეთ მომხმარებელს ქულა ასე:
# თუ მიიღო 90 ან ზემოთ დაუწერე A
# თუ მიიღო 80 დან 90მდე ქულა დაუწერე B
# თუ მიიღ0 70დან 80მდე ქულა, დაუწერე C

#1

num = 8

if num % 2 == 0:
   print("ლუში")
else:
   print("კენტი")

#2
age = int(input("tell me ur age: "))
if age < 18:
    print("u r not of legal age")
else:
    print("u r an adult")

#3



mark = int(input("tell me your mark: "))
if mark >= 90:
   print("A")
elif mark >= 80:
   print("B")
else:
   print("C")

