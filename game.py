import random

def bigNums(i, a):
  b = random.sample(a, k=i)
  return b

def smallNums(i):
  return [random.randint(1, 10) for _ in range(i)]

# Change these values as needed
bigNum = [25, 50, 75, 100] # Change the big numbers, can have more or less numbers
totalNums = 6 # Change the total amount of numbers you can use. 
goal = random.randint(100, 999) # Change the lower and upper bound of the goal
# Do not change anything below

if totalNums < len(bigNum):
  lim = totalNums
else:
  lim = len(bigNum)

while True:
  try:
    i = int(input("How many big numbers do you want: "))
    if i > lim:
      print(f"You may not have more than {lim} big numbers")
    elif i < 0:
      print("You may not have a negative number of big numbers")
    else:
      break
  except:
    print("The amount of big numbers must be an integer")

numbers = bigNums(i, bigNum) + smallNums(totalNums-i)
print(f"Your numbers are {numbers}")
print(f"The goal to reach is {goal}")
