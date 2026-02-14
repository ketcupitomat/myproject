#1
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#2
def min_max(a, b):
    return min(a, b), max(a, b)

small, big = min_max(3, 10)
print(small, big)
