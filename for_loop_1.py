raw_input('Part 1')
my_list = ['cat', 'dog']
print 'The value of my_list is: ' + str(my_list)

new_item = 'bird'
print 'The value of new_item is: ' + str(new_item)

print 'Now adding new_item to the list.'
my_list.append(new_item)
print 'With my_list.append(new_item)'
print 'The value of my_list is: ' + str(my_list)

raw_input('Part 2')
my_list = [1, 2, 3, 4, 5]
print 'The value of my_list: ' + str(my_list)
print 'Printing each item in the list...'
for item in my_list: # 'item' can be any variable name.
    print item

print 'Now printing each item multiplied by itself...'
for item in my_list:
    processed = item ** 2
    print processed

print 'Now adding 10 to the list'
my_list.append(10)

for item in my_list:
    processed = item ** 2
    print processed


x = 'hello world'.split(' ')
# x is ['hello', 'world']
x = 'hello world'.split('w')
# x is ['hello ', 'orld']


x = 'hello world'.replace('l', 'm')
# x is 'hemmo wormd'

x = 'hello'
x.upper()
# x is 'HELLO'
x.lower()
# x is 'hello'

x = ['good', 'morning']
y = ' '.join(x)
# y is 'good morning'
z = '#'.join(x)
# z is 'good#morning'
