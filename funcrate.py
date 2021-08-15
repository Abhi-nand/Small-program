#using def function example
def computepay(h,r):
    if h<=40:
        p=h*r
    else:
        p=40*r+((h-40)*r*1.5)
    return p
h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
p = computepay(h,r)
print("Pay",p)
