# order not maintained in set
s = {2,2,3,4,5,6}
print(s)
# for empty set creation use set()

emptySet = set()
print(type(emptySet))

s1 = {1,2,3,4,5}
s2 = {5,11,12,13,14,15}
s3 = s1.union(s2)
print(s1.union(s2))
#print(s1,s2)
print(s1.intersection(s2))
print(s3.issubset(s2))
print(s2.issubset(s3))
# pop() will randomly remove any value from set --- print(s2.pop())

