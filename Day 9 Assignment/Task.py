##assignment 1:
## get product price and quantity and print the total price. implement this code in 4 types of functions based on parameter and return type


#1.no para,no return type

def products():
    product_price = 500
    quantity = 20
    total_price = product_price * quantity
    print('total_price is',total_price)

products()

#2.with para, no return type

def products(product_price,quantity):
    total_price = product_price * quantity
    print('total_price is',total_price)
    
product_price = 1000
quantity = 50
products(product_price,quantity)

#3.with para,with return type

def products(product_price,quantity):
    total_price = product_price * quantity
    return total_price

product_price = 3000
quantity = 40
product_margin = products(product_price,quantity)
print('total_price is',product_margin)


#4.no para,with return type

def products():
    product_price = 5000
    quantity = 60
    total_price = product_price * quantity
    return total_price
product_margin = products()
print('total_price is',product_margin)

