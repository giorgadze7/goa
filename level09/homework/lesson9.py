# day 09:
# @. გააკეთეთ solo learn 
# 1. შექმენით ორი ცვლადი და ეკრანზე გამოიტანეთ მათი შედარება (მაგ. num1 > num2 ან num1 != num2) შედარების ყველა ოპერატორის გამოყენებით:
# <
# >
# >=
# <=
# !=
# ==
# 2. მომხმარებელს შემოატანინეთ ორი ციფრი, შემდეგ ისინი გადააკეთეთ integer ებად და ეკრანზე გამოიტანეთ მათი შედარება (გამოიყენეთ < ; > ; == და !=)
# 3. დაწერეთ ორი მაგალითი შედარების ოპერატორებზე (გამოიყენეთ <= ; >=) და კომენტარებით ახსენით რას აკეტებენ ისინი
# 4.შეასრულეთ საკლასო დავალება 
# 5. კომენტრარებით ახსენით რას ნიშნავს და აკეთებს თითოეული შედარების ოპერატორი, ასევე დააკომენტარეთ საკლასო დავალება 
# 6. გადახედეთ დოკუმენტაციას 
# https://www.w3schools.com/python/gloss_python_comparison_operators.asp


# N1
num1 = 1.5
num2 = 2.3

num1 < num2
num1 > num2
num1 == num2
num1 != num2
num1 >= num2
num1 <= num2

# N2
num3 = int(num1)
num4 = int(num2)

num3 < num4
num3 > num4
num3 == num4
num3 != num4

# N3

# <= ამოწმებს რომ მოცემული მნოშვნელობა არის მეორე მნიშვნელობაზე ნაკლები ან მაქსიმუმ ტოლი ხოლო >= ამოწმებს რომ მოცემული მნიშვნელობა არის ან მეტი ან მინიმუმ ტოლი მეორე მნიშვნელობაზე 

# N4 

int = 10
str = "nika"
float = 5.5




# N5

# < "ნაკლებობა" აფასებს არის თუ არა ოპერატორის მარჯვენა მხარეს მნიშვნელოვა უფრო პატარა ვიდრე მარჯვენა მხარეს
# > "მეტობა" აფასებს არის თუ არა ოპერატორის მარცხენა მხარეს მნიშვნელობა უფრო დიდი ვიდრე მარჯვენა მხარეს
# >= "მეტი ან ტოლი" ამოწმებს რომ მოცემული მნიშვნელობა არის ან მეტი ან მინიმუმ ტოლი მეორე მნიშვნელობაზე
# <= "ნაკლები ან ტოლი" ამოწმებს რომ მოცემული მნიშვნელობა არის მეორე მნიშვნელობაზე ნაკლევი ან მაქსიმუმ ტოლი
# != "არ არის თანაბარი ოპერატორი" აბრუნებს ლოგიკურ მნიშვნელობას: ე.ი true ან false 
# == "ტოლობა" აკეთებს თავისუფალ შედარებას ორ მნიშვნელობას შორის