##create a class and object with custom example


class laptoporder:

    def get_data(self):
        self.item =input("enter the item name:")
        self.price =int(input("enter the price:"))
        self.quantity =int(input("enter the quantity:"))

    def total_cost(self):
        total =self.price * self.quantity
        print("total cost for",self.item,"is RS",total)

order1 = laptoporder()
order1.get_data()
order1.total_cost()

#o/p
##enter the item name:lenovo
##enter the price:35000
##enter the quantity:4
##total cost for lenovo is RS 140000