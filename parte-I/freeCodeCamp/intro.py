# variable ===========================================
name = "Hunter" # string
age = 24
_inteiro = int(34); _flutuante = float(54)

print(name + "\n" 
      + str(age) + "\n" 
      + str(_inteiro) + "\n" 
      + str(_flutuante))

#print(isinstance(age, int))

# types ===========================================

"""
bool for booleans
int for integers numbers
float for floating point numbers
list for lists
tuple for tuples
range for ranges
dict for dictionaries
set for sets
complex for complex numbers

"""

# operators ===========================================

#arithmetics ----
two = 1 + 1
one = 2 - 1
four = 2 * 2
two = 4 / 2
one = 4 % 3
nine = 3 ** 2
five = 33 // 6

#combining ----
two += one # three
four *= five # twenty

#comparison ----
a = 2; b = 9

exp = a == b # False
exp = a != b # True
exp = a > b  # False
exp = a <= b # True

cond = True 
cond1 = True; cond2 = False 
exp = not cond        # False
exp = cond1 and cond2 # False
exp = cond1 or  cond2 # True

#bitwise ----
bin1 = 1 # 01
bin2 = 2 # 10
bin3 = 3 # 11
bin = bin1 & bin2 # 00
bin = bin1 | bin2 # 11
bin = bin1 ^ bin3 # 10
# print(bin)
bin = ~bin2 # 01
bin = bin1 << 2 # 100
# print(bin)
bin = bin3 >> 1 # 001
# print(bin)

#others ----
name = "Gunter"
isGunter = "Gunter" 
num = 3
ot = isGunter is name # True
ot = num in range(4)      # True
# print(ot)

#ternário ----
