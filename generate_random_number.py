import time
def random_number(low, high):
    return (low + (time.time()*1000) % (high - low))

limit_l = int(input("Enter the lower limit of range: "))
limit_h = int(input("Enter the upper limit of range: "))
rand = random_number(limit_l, limit_h)
print(rand)