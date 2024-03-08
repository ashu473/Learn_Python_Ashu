# Rule 1: String & Numeric values can operate together with *
A,B=2,3
text="@"
print(A*text*3) # @@@@@@

# Rule 2: String & String can operate with +
a,b="2",3
text="@"
print((a+text)*b) # 2@2@2@
print(a+text*b) # 2@@@

# Rule 3: Numeric values can operate with all airthmetic operators
a,b=2,3
c=5
print(a+b*c) # 17

# Rule 4: Airthmetic expression with Integer and float will result in float
a,b=2,5.0
print(a*b) # 10.0
print(b/a) # 2.5
print(a-b) # -3.0
print(a+b) # 7
print(b//a) # Integer division(round of to low)-> 2.0
c,d=-12,5
print(c//d) # -3

# Rule 5: Remainder is negative when denominator is negative
a,b=-5,2
print(a%b) # 1
a,b=5,2
print(a%b) # 1
a,b=5,-2
print(a%b) # -1
a,b=-5,-2
print(a%b) # -1
