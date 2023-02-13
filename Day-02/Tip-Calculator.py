print("WELCOME TO THE TIP CALCULATOR!")

bill = input("How much is the bill?\n")
tip_percent = input("Tip in percentage? 10%, 12% or 15%\n")
people = input("How many to split the bill?\n")

tip_amount = int(bill) * int(tip_percent) / 100
new_bill = float(bill) + tip_amount
share = new_bill / int(people)

share_2dp = "%.2f" % share

print(f'Each person should pay: ${share_2dp}')


