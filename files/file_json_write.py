import os
# import json
import pickle

weekdays_dict = {1:'Monday',2:'Tuesday',3:'Wednesday'}
rates_dict = {'USD': 3.8,'PLN': 1,'EUR': 4.3}

my_list = [rates_dict,weekdays_dict] #making a list with 2 dictionaries

# my_json_file = os.path.join('..','data','rates.json')
my_json_file = os.path.join('..','data','rates.pkl')

with open(my_json_file,'wb') as f:
    pickle.dump(my_list,f)

# in json we can have tags and keep multidimensional objects (unlike CSV which is flat 2D)
#json always uses "" and can store any data.

#pickle (pkl) gives us results in bytes - not really readable by humans
