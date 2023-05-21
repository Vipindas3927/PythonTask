# 'product name': [price, quantity, total_amount]
product = {
    'Product A': [20, 0, 0],
    'Product B': [40, 0, 0],
    'Product C': [50, 0, 0]
}
sub_total = 0
total_product = 0
total_gift_wrap = 0
gift_wrap_fee = 1
shipping_fee = 5
offers = ["flat_10_discount",
        "bulk_5_discount", 
        "bulk_10_discount", 
        "tiered_50_discount", 
        "no offer received"
    ]
max_value = 0
max_value_index = -1

# offer comparison
def offerSelection():
    global max_value, max_value_index, off_list
    off_list = [offerOne(sub_total),
            offerTwo(),
            offerThree(total_product, sub_total),
            offerFour()
        ]
    max_value = max(off_list)
    if max_value != 0:
        max_value_index = off_list.index(max_value)

# 4 offers
offerOne = lambda t :10 if t>200 else 0

def offerTwo():
    off = 0
    for i in product.values():
        if i[1]>10:
            offer = i[2] * 0.05
            if off< offer:
                off = offer
    return off

offerThree = lambda prod, pri: pri*0.1 if prod>20 else 0

def offerFour():
    off = 0
    if total_product > 30:
        for i in product.values():
            if i[1] > 15:
                offer = (i[1] - 15) * i[0] * 0.5
                if off < offer:
                    off = offer
    return off

# bill printing 
def billPrint():
    print("\n______________________________________________\n")
    print("BILL\n----")
    print("Product Name\tProduct Quantity\tPrice")
    for name, item in product.items():
        print(f"{name}\t{item[1]}\t\t\t$ {item[2]}")
    print("______________________________________________")
    print(f"Subtotal:\t\t\t\t$ {sub_total}")
    print("______________________________________________")
    print("Discount Applied:\t", offers[max_value_index])
    print("Discount Amount:\t$", max_value)
    total_shipping_fee = shipping_fee*((total_product//10)+(total_product%10>0))
    print("Shipping Fee:\t\t$", total_shipping_fee)
    total_gift_wrap_fee = total_gift_wrap*gift_wrap_fee
    print("Gift Wrap Fee:\t\t$", total_gift_wrap_fee)
    print("______________________________________________")
    print("TOTAL AMOUNT:\t\t\t\t$",sub_total+total_gift_wrap_fee+total_shipping_fee-max_value)
    print("______________________________________________")

    
# Collecting product qantity from users
print("Enter the product quantity\n--------------------------")
for name, item in product.items():
    item[1] = int(input(f"{name}\t: "))
    if item[1] > 0:
        item[2] = item[1] * item[0]
        sub_total += item[2]
        total_product += item[1]
        gift_wrap = input(f"Do you want to wrap {name} as a gift? (yes/no): ").lower()
        while gift_wrap not in ['yes', 'no']:
            gift_wrap = input("Please select correct option.\nDo you want to wrap {name} as a gift? (yes/no): ").lower()
        if gift_wrap == 'yes':
            total_gift_wrap += item[1]

offerSelection()
billPrint()
