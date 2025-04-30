from random import randint

print("Hello, Monty'S Python!")
word = "word bro"
print("Stringy"[0:3], word[5:8], [1,'dude'[3]])
print('a', 'b', 'c', 'd', 'e', sep=' | ', end=' \n <<<>>> \n')

def get_num_list():
    lst = []
    sequence = input("Enter a list of numbers seperated by coma [,]\n").strip()
    lst = sequence.split(",")
    print(lst)
    return [int(num) for num in lst]

user_nums = get_num_list()
nums = [1,2,3,4,5,6,7,8,9,10]

if(len(user_nums) > 0):
    nums = user_nums

print(nums[::1])
print(f"2 steps nums: {nums[::2]}")
rtwo_nums = nums[::-2]
print(f"2 steps reversed nums: {rtwo_nums}")
print(f"reversed nums: {nums[::-1]}")

rnums = []
for elem in range(len(nums)):
    rnums.insert(0,nums[elem])
print(f"Manual Reverse nums{rnums}")

randnums = []
for _ in range(20):
    randnums.append(randint(1, 500))
print(f"500 Random nums: {randnums}")

even_nums = []
for num in randnums:
    if num % 2 == 0:
        even_nums.append(num)
print(f"Even nums: {even_nums}")
# List Comprehension 
odd_nums = [num for num in randnums if num % 2 != 0]
print(f"Odd nums: {odd_nums}")

def args_print(*words):
    for word in words:
        print("Ice " + word + " Ice")
args_print("sup", "ok", "more", "further")