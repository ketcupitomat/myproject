#1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#4
# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#5 
# The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])