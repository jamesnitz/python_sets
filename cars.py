# A set is a collection of things, like a list, 
# but the collection is both unordered, and contains no duplicate elements. 
# Developers use sets to easily filter down other collections to unique elements, 
# and to see if two, or more, collections share any similar items.

# Using set() to create a set
languages = set()

# Using curly braces allows you to initialize the set with values
languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }
if 'spanish' in languages:
  print("true")

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print("intersect and see who attended both events")
print(a.intersection(b))
print(b.intersection(a))
print("symmetric difference and see who attended only one event")
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(" difference and see which members only attened one and not the other")
print(a.difference(b))
print(b.difference(a))
print(" see a list of all participants")
print(a.union(b))
