print("Welcome to the tip calculator! ")
Bill = input ("What is the total Bill? $")
Tip = input("How much tip would you like to give? 10, 12, or 15? ")
People = input ("How many people to Split the bill ")

# print(type(Bill))

percentageTip = int(Tip)/100
New_Bill = float(Bill)
New_people = int(People)

each_Payment = ( (New_Bill * percentageTip)+ New_Bill) / New_people

print(f"Each person Should Pay : {each_Payment}")