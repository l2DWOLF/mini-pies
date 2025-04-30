from random import shuffle

def get_nums_arr():
    lst = []
    while True:
        num = input("Enter a Number: \n(Enter [done] when finished).")
        if num == "done":
            break
        if(num.isdigit()):
            lst.append(int(num))    
        print(lst)
    return lst

ul = [400,200,1000,300,1200,100,500,800,1100,600,900]
count = 0

user_list = get_nums_arr()
if(len(user_list) > 0):
    ul = user_list

# Bubble 
for i in range(len(ul) -1):
    flag = False
    for i in range(len(ul) - 1):
        if(ul[i] > ul[i+1]):
            ul[i], ul[i+1] = ul[i+1], ul[i]
            flag = True
        print(f"Rounds: {count} || Length: {len(ul)}\n{ul}")
        count += 1
    if not flag:
        break
print(f"Bubble Result: {ul}")

# List.sort() & sorted(List)
shuffle(ul)
print(f"Shuffled: {ul}")
ul.sort()
print(f"Sort: {ul}")
shuffle(ul)
print(f"Shuffled: {ul}")
print(f"Sorted: {sorted(ul)}")

def mult_table():
    mult_dim = []
    for row in range(1, 11):
        table_row = []
        for col in range(1, 11):
            table_row.append(row * col)
        mult_dim.append(table_row)
    return mult_dim
dim_arr = mult_table()

print(dim_arr[2][5])
for dimension in dim_arr:
    print(dimension, sep="\t")

def suminmax(*args):
    sum = 0
    min = 99999999999
    max = 0
    for arg in args:
        sum += arg
        if max < arg:
            max = arg
        if(min > arg):
            min = arg
    avg = sum / len(args)
    print(f"sum: {sum}, min: {min}, max: {max}, avg: {avg}")
suminmax(1,2,3,4,5,6)

stringer = input("enter phrase:\n")
stringer_set = set(stringer) # list > set
stringer_set.add("T")
stringer_set.update({"P", "#"}) # update() add multiple arguements.
stringer_set.discard("P") # remove() throws error if not exists. 
print(stringer_set)