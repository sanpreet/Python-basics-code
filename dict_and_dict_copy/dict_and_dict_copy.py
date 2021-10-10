"""
When one make the copy of the dictionary, if the copy is modified
the original does not change
if one equate the original dictionary to the new variable, if the
new variable changes the original dictionary is also reflected.
"""

original = {1: 'one', 2: 'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

original = {1: 'one', 2: 'two'}
new = original
print("---------------------------------")
# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

