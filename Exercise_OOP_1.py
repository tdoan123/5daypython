class Scoop(object):
    def __init__ (self, flavor): 
        self.flavor = flavor  
    
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)

for one_scoop in [s1,s2,s3]: 
    print(one_scoop.flavor)
    
# I can replace [s1, s2, s3] in line 11, by  assigned them into a variable  

flavor_list = [s1, s2, s3]
print (flavor_list)

for flavor in flavor_list: 
    print(flavor)
'''
interesting: the output is: 
<__main__.Scoop object at 0x00000239C667FA90>
<__main__.Scoop object at 0x00000239C667E9D0>
<__main__.Scoop object at 0x00000239C667FED0>

why is this? and what does it mean?  

# update note: figure out that in order for the line 20 to work, I have to put .flavor
I guess the reason is to have appoint the function to the attributes of the class 
# todo: check for the terms being used for different components in Class  
'''
    
# seem like the only option that I know of at this momment is use the loop search
for flavor in flavor_list: 
    print(f'flavor 1: ', s1)
    print(f'flavor 2: ', s2)
    print(f'flavor 3: ', s3)
    
''' output: 
flavor 1:  <__main__.Scoop object at 0x00000239C667FA90>
flavor 2:  <__main__.Scoop object at 0x00000239C667E9D0>
flavor 3:  <__main__.Scoop object at 0x00000239C667FED0>
flavor 1:  <__main__.Scoop object at 0x00000239C667FA90>
flavor 2:  <__main__.Scoop object at 0x00000239C667E9D0>
flavor 3:  <__main__.Scoop object at 0x00000239C667FED0>
flavor 1:  <__main__.Scoop object at 0x00000239C667FA90>
flavor 2:  <__main__.Scoop object at 0x00000239C667E9D0>
flavor 3:  <__main__.Scoop object at 0x00000239C667FED0>

# what is this? how come it is only display the value type?  
'''


