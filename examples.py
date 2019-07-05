"""
Defining and iterating
"""
my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
}

# .items() .keys() .values()
for k, v in my_dict.items():
    print('key: ', k)
    print('value: ', v)

# .keys() is nice for readability

"""
Handling JSON
"""

import requests

r = requests.get('some_dat_site')
r.json  # what's the difference here ?
r.text

my_data = r.json
type(my_data)
# dict()

# Okay, we have a dict! Now what?


"""
Comprehensions and Enhancements
"""

# list comp

# dict comp

# defaultdict

# OrderedDict

"""
Interacting with Pandas
"""
