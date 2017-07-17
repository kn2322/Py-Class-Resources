# Copy and paste this code and run it while looking at this code!

raw_input('Part 1')

bread = 'tasty'


if bread == 'tasty': # Checks if bread is equal to tasty.
    print 'The bread is tasty!'
else: # If not equal.
    print 'The bread is NOT tasty.'


print 'the value of bread is: ' + bread
print "bread == 'tasty' evaluates to " + str(bread == 'tasty')

raw_input('Part 2')

bread = 'disgusting'

if bread == 'tasty':
    print 'The bread is tasty!'
else:
    print 'The bread is NOT tasty.'

print 'the value of bread is: ' + bread
print "bread == 'tasty' evaluates to " + str(bread == 'tasty')

raw_input('Part 3')

bread = 'okay'

if bread == 'tasty': # Goes first.
    print 'The bread is tasty!'
elif bread == 'okay': # Else if the bread is okay.
    print 'The bread is meh.'
else:
    pass # Placeholder to avoid error, does nothing

print 'the value of bread is: ' + bread
print "bread == 'tasty' evaluates to " + str(bread == 'tasty')
print "bread == 'okay' evaluates to " + str(bread == 'okay')

raw_input('Part 4')

bread = 'okay'

if bread != 'okay': # != is does not equal.
    print 'This bread is not okay.'
else:
    print 'This bread is okay.'

print 'the value of bread is: ' + bread
print "bread != 'okay' evaluates to " + str(bread == 'okay')

raw_input('Part 5')

letter = 'a'
print "letter in 'aeiou' evaluates to: " + str(letter in 'aeiou')
print "letter in 'xyz' evaluates to: " + str(letter in 'xyz')
print "letter in 'pancake' evaluates to: " + str(letter in 'pancake')
