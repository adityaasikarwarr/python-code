# format specifiers = {value : flags } format a value based on what flags are inserted
# :f for floating point numbers
# :.nf for n floating point numbers
# :n for integers
# :<n for left alignment
# :>n for right alignment
# :^n for center alignment
# :+n for sign
# :n for padding
price1 = 5000
price2 = 23.865346
price3 = 4000
print(f"the price 1 is {price1 : .2f} dollars")
print(f"the price 2 is {price2 : .2f} dollars")
print(f"the price 3 is {price3 : .2f} dollars")