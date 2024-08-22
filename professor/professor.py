import random 

def main(): 
    
    level = [1, 2, 3]
    
    def get_level():
        while True:  
            try: 
                input_level = int(input('Level: '))
                if input_level in level: 
                    return input_level
                else:
                    continue 
            except ValueError:
                continue   
    
    select_level = get_level()
        
    def generate_integer(level):
        if level == 1: 
            return random.randint(0, 9)
        elif level == 2: 
            return random.randint(10,99)
        elif level == 3: 
            return random.randint(100,999)
        else:
            raise ValueError()

    score = 0
    for _ in range(10):  
        x = generate_integer(select_level)
        y = generate_integer(select_level)
        attempts = 0 
        while attempts < 3: 
            try: 
                user_answer = int(input(f'{x} + {y} = '))
                if user_answer == x + y: 
                    score += 1  
                    break 
                else:
                    attempts += 1 
                    if attempts <= 3:
                        print ('EEE')
                        continue
                    else:
                        print (f'{x} + {y} = {x + y}') 
            except ValueError: 
                continue
            
    print (f'Score: {score}/10')
if __name__ == "__main__":
    main()