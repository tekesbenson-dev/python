# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

# Function to calculate Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

principal = 45000
rate = 7
time = 8

si = simple_interest(principal, rate, time)
print("Simple Interest (given values):", si)

print("\nOther Simple Interest Calculations:")

values = [
    (30000, 5, 4),
    (60000, 6, 3)
]

for p, r, t in values:
    interest = simple_interest(p, r, t)
    print("Principal:", p, "Rate:", r, "Time:", t, "SI:", interest)