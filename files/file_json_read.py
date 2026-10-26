import os
# import json
import pickle

'''my_json_file = os.path.join('..','data','rates.json')

with open(my_json_file) as f:
    data = json.load(f)
    rates_dict = data[0]
    weekdays_dict = data[1]
    print(rates_dict)
    print(rates_dict['USD'])
    print(type(rates_dict['USD']))
    print(weekdays_dict)'''

my_pkl_file = os.path.join('..','data','rates.pkl')

with open(my_pkl_file,'rb') as f:
    data = pickle.load(f)
    rates_dict = data[0]
    weekdays_dict = data[1]
    print(rates_dict)
    print(rates_dict['USD'])
    print(type(rates_dict['USD']))
    print(weekdays_dict)

# json also identifies the data types
# into json file you can only dump single objects (?)
# pickle can also do that, but json is readable for humans and easier to operate on (?)
# pickle's advantages is that it is faster, as it doesn't need to change anything
# to text - especially seen with big files

# open format (json) vs closed format (pickle, half-closed format, cause any python interpreter can read it
# but no human can read it naturally, also adding extention is not necessary)

# xml - similar to html -> preferred and not replaced by json anywhere where more formal document is needed
# encryption, digital signature (typically government stuff will use XML)
# json does not have standardized validation, unlike xml (xss thing, used to specify the formatting
# of xml file - defining how the file looks, structure etc. "namecodes" ?)

# open format (csv, xlsx) vs closed format (xls)
# use open formats if you want to export, share data with others.
# unless you need the ultra-performance (or use it only for purposes of single app) - still worth having
# a copy of it in open format for showing.

