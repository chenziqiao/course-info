# this code will generate random data for the 'orders' table
# of the PVFC database


# this part prints aa date in the correct way, for testing purposes:
order_day = 3
order_month = "Sep"
order_year = "2014"
order_date = str(order_day) + "-" + order_month + "-" + order_year
#print(order_date)



#here's the first acceptable order number
ordernum = 1011

#here's the list of acceptable products
prods = [1,2,3,4,5,6,7,8]

#here's the list of acceptable customers
custs = list(range(1,16)) # this produces a list of values from 1 to 15



import random  # needed to generate randome numbers

f = open("output.sql","w") # opens a file to write our generated SQL

for i in range(10):
    # now create a new order
    ordernum = ordernum + 1
    order_day = random.randint(1,28)  # so we don't end up with "31-Feb" or the like
    order_month = random.choice(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
    order_year = "2014"
    order_date = str(order_day) + "-" + order_month + "-" + order_year
    sql = "{\n\"ordernum\": " + \
          str(ordernum) + ",\"orderdate\": \"" + \
          order_date + "\", \"customer\": " + \
	  str(random.choice(custs)) + ",\n\"items\":[" 
    f.write(sql)

    #now create a random number of items in each order
    num_items = random.randint(1,4)
    for j in range(num_items):
        sql = "{\"product\":" + \
              str(random.choice(prods)) + ", \"quantity\": " + \
	      str(random.randint(1,10)) + "},"
        f.write(sql)

    f.write("]\n}\n")

# note: a bug here is that the same item might be added to the order twice, 
# violating the primary key of the 'order_lines' table. there are a few ways
# you might fix this.  i leave it as a challenge to the reader.



f.close()




