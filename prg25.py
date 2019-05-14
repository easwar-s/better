import statistics
val = input("Enter the numbers separated by space")
list = val.split()
print("median value is: %s" % (statistics.median(val)))
