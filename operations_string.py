s1 = "hello"
s2 = "world"
print(s1 + " " + s2)
print(s1, "hello")
print(3*s2)
print((10//2)*s1)
# len function gives you the size of the string
print(s1, len(s1))
print(3*s2, len(3*s2))
for c in s2:
    print(c*4, end="")

new_string = ""
for c in s2:
    new_string += c*4
print(new_string)

# in can be used to check if one string is inside another

