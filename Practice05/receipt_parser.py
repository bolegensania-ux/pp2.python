"""
Tasks:

Extract all prices from the receipt
Find all product names
Calculate total amount
Extract date and time information
Find payment method
Create a structured output (JSON or formatted text)
"""

with open("Practice05/raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

import re
import json
#all prices from the receipt
prices = re.findall(r'\d[\d\s]*,\d{2}', text)
print(prices)

#all product names from the receipt
product = re.findall(r'\d\.\s*\n(.+)', text)
print(product)

#total amount
total = re.search(r'ИТОГО:\s*\n([\d\s]+,\d{2})', text)
if total:
    total_amount = total.group(1)
    print("Total: ", total_amount)

#time and date information
datetime = re.search(r'Время:\s*(\d{2}.\d{2}.\d{4}\s*\d{2}:\d{2}:\d{2})', text)
if datetime:
    datetime_match = datetime.group(1)
    print("Date and Time is:", datetime_match)

# output the payment method
payment = re.search(r'(Банковская карта)', text)
if payment:
    payment_method = payment.group(1)
    print("Payment method is:", payment_method)

# create structured output using json 
data = {
    "prices" : prices,
    "product_names" : product,
    "total_price" : total_amount,
    "date_time" : datetime_match,
    "payment_method" : payment_method
}
print(json.dumps(data, indent=4))