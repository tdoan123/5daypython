"""
First time trying to write a docstring to demo how it works 
"""

print ('Begining of module')


x = 100 

y = [10, 20, 30]

z = {'a': 1, 'b':2, 'c':3}

def hello(name):
    """
    to write description of the function.  
    Exepects - Modifies - Returns 
    """
    return f'Hello =, {name}'

surprise = 5


class NewCLass:  
    """_summary_
    """
    def __init__ (self, abc):
        """_summary_

        Args:
            abc (_type_): _description_
        """
        self.abc = abc 
        
print ('ending up model')