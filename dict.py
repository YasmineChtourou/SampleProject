# Conversion of nested dictionary into flattened dictionary 

from collections import MutableMapping 

def convert_flatten(d, parent_key ='', sep ='_'): 
    items = [] 
    for key, value in d.items(): 
        new_key = parent_key + sep + key if parent_key else key 
        if isinstance(value, MutableMapping): 
            items.extend(convert_flatten(value, new_key, sep = sep).items()) 
        else: 
            items.append((new_key, value)) 
    return dict(items) 

initial_dict = {"customer": {"name": "Micheal","age": 24,"location": {"city": "Paris","country": "France","zip_code": "75009",}}}

print ("final_dictionary", str(convert_flatten(initial_dict))) 
