## Effective Dictionaries {...}

Note:
Current time is 33 minutes
Try to bring down by 8 minutes w/o rushing

---

#### This Presentation (now): 
#### https://gitpitch.com/alphaharris/effective-dictionaries

------

#### Based on a True Blog Post: 
#### https://kite.com/blog/python/python-dictionaries

---

---

![](assets/img/skipping-steps.jpg)

---


### Aaron Harris

### aaron@kite.com

#### Dev Advocate + Consultant
(Full Stack, Focus on Data Integrations and Web Dev)

@ul
- Former Bartender
- Sometimes Realtor (not currently!)
@ulend



#### Quick poll... 

---

#### Defined a dictionary today?

---

#### Solved a problem with a dictionary this week?

---

@ul[spaced text-white]
- Make difficult things possible
- Interface
    - now[we][can][do][this]
- Cleaner, more readable Code
- Performance 
    - Just prefer dictionaries!
@ulend

Note:
- We won't be talking about performance
- Except to say that you should prefer dictionaries to lists

--- 
### Today...

@ul[spaced text-white]
- Defining and Iterating
- Schools of Data
- Handling JSON
- Comprehensions and Enhancements
@ulend


---

## Defining and Iterating

Note: 
- Dictionaries are a powerful structure
- Best way to learn is to get some practice!
---
### QUIZ!! @emoji[scream]

---

```python
        
my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    }

for k, v in my_dict:
    print('key: ', k)
    print('value: ',  v)

# how do we look?

```

@[2-6](Basic dictionary definition)
@[8-10](Iterating through a dictionary)
@[12](Yes! This will produce an error, but what?)

---

```Python
# ValueError: too many values to unpack (expected 2)
```

---

```python

my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    }

# .items() .keys() .values()
for k, v in my_dict.items():  
    print('key: ', k)
    print('value: ',  v)

# .keys() is nice for readability

```

Note:
Show code again for review

---

### Remember, remember the Fifth of the Members

```python
members = dir(dict)
[m for m in members if not m.startswith('__')][4]

# >>> 'items'

```

---

### 'items'  (:

---
### Why this is happening - 

- `for` is going to look for an iterator  `__iter__`

- "Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys())."

---


@ul[spaced text-white]
- `.items()`
- `.keys()`
- `.values()`
@ulend

Note: 
- .keys() and .values() are obvious
- .items() is a little weird
- Using keys and values loses the utility of our association
---

- Nothing magical is happening here, we're just getting d.keys()

- Also note that list(my_dict) will return a list of keys

---

### So, what is `.items()` ??

"Return a new view of the dictionary’s items (`(key, value)` pairs)."

Note:
These pairs are given to us as a Tuple

---

### What the heck is a view??
Is that even python?

---

"They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, 
the view reflects these changes."

"Keys and values are iterated over in insertion order."

---

### Iteration Gotchya - 

"Iterating views while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries."

"Changed in version 3.7: Dictionary order is guaranteed to be insertion order."

Note:
- Don't alter the shape of your dictionary while iterating
- The Python specification relies on abstractions like views
- You may not be exposed to these abstractions unless you read the docs

---

## Schools of Data (Relational v. Non-relational)

Note:
- Now that we know about iteration, we can look at use-cases
- Non-relational is a misnomer, not fair to define in opposition
- Prefer Nested, Tree-like, Associative

---

### Relational - 

![](assets/img/relational.jpg)

---

@ul[spaced text-white]
- Well Explored
- Organized, Predictable Schema
- More overhead (code, tools) less flexible
- Changing schema can be painful
@ulend

Note: 
- May follow SQLalchemy presentation, perfect!

---
### Nested or Tree

![](assets/img/inception.jpg)

---

@ul[spaced text-white]
- Flexible, great for handling *unknowns*
- Deep structures will slow you down
- Readabililty is "key"    
- ..................... ¯\\_(ツ)_/¯

@ulend

---

##### The deeper you go...
##### The faster time passes in the outside world

Note:
The movie Inception is a good analogy to nested data structures

---

![](assets/img/oldman.gif)

#### Full of regret
#### Waiting to die alone

---

@ul[spaced text-white]
- Get complicated quickly
- Might need recursion... and that's okay
- Don't be afraid to "curate"
  - one-off cherry-picking ... or ...
  - comprehensions to get specific values
- Other tools don't understand your tree
  - databases
  - apis (e.g. google sheets)
@ulend

Note:
We are not covering recursion today, but that is a great topic
When using recursion, ask how readable that is for your team
We will look at some examples of curation shortly

---

## Consuming JSON

---

### Typical use-case with Requests

Note: 
- TomTom is a great resource for batched requests
- This example needs to be fleshed out

---

```python
tt_key = '123'

import requests
output = '.json?'
endpoint = 'https://api.tomtom.com/search/2/batch' + output
address = '701 Brazos St, Austin, TX 78701'

# https://api.tomtom.com/search/2/batch.json?key=*****
headers = {'Content-Type': 'application/json'}
data = {
    "batchItems": [
        # {"query": "/geocode/ " + address + ".json"} for address in address_dicts.values()]
        {"query": "/geocode/ " + address + ".json"}]
}
params = {
    'key': tt_key,
    # limit geography (optional)
    'countrySet': 'US',
    'topLeft': '30.506667,  -97.967834',
    'bttmRight': '30.022733, -97.443237',
}
r = requests.post(endpoint, params=params, headers=headers, json=data)
print(r.url)
results = r.json()
type(results)
# dict()
```

---

###  Okay, we have a dict! Now what?
```python
first_result = {'type': 'Point Address', 'id': 'US/PAD/p0/3077466', 'score': 11.9658,
 'address': {'streetNumber': '701', 'streetName': 'Brazos Street', 'municipalitySubdivision': 'Austin, Downtown',
             'municipality': 'Austin', 'countrySecondarySubdivision': 'Travis', 'countryTertiarySubdivision': 'Austin',
             'countrySubdivision': 'TX', 'postalCode': '78701', 'extendedPostalCode': '787012262', 'countryCode': 'US',
             'country': 'United States', 'countryCodeISO3': 'USA',
             'freeformAddress': '701 Brazos Street, Austin, TX 78701', 'localName': 'Austin',
             'countrySubdivisionName': 'Texas'}, 'position': {'lat': 30.26895, 'lon': -97.74042},
 'viewport': {'topLeftPoint': {'lat': 30.26985, 'lon': -97.74146},
              'btmRightPoint': {'lat': 30.26805, 'lon': -97.73938}},
 'entryPoints': [{'type': 'main', 'position': {'lat': 30.2691, 'lon': -97.74095}}]}
```

---

### How to go from JSON to Pandas? 

---

Note:
This is a typical pattern for getting data.

---


```python

import pandas as pd

# Pandas will do it's best to store this data
row = pd.Series(first_result)
print(row)


```

---

```text
type                                               Point Address
id                                             US/PAD/p0/3077466
score                                                    11.9658
address        {'streetNumber': '701', 'streetName': 'Brazos ...
position                     {'lat': 30.26895, 'lon': -97.74042}
viewport       {'topLeftPoint': {'lat': 30.26985, 'lon': -97....
entryPoints    [{'type': 'main', 'position': {'lat': 30.2691,...
dtype: object
```


Note:
- Packages often abstract away things we need
- Use discretion when a package is "too easy"
- Airtable has a very friendly api with dynamic documentation
- If you are ever writing API documentation, make it look like airtable
- You can make entries from your phone!

--- 

### Curating with comprehensions

---

- We have our data, but we need rows
- Maybe we're sending this straight to a spreadsheet
- Maybe we just want readable rows... for reasons!

---

### Basic Dict comprehension pattern

---

- Like .items, .keys, .values, this is worthy of memorization
- Dict comps are maybe more powerful than list comps
- Same reason that dicts are sometimes more powerful than lists

---

### `{ <k> : <v> for i in iterable }`
```python

iterable = [1, 2, 3]

[ x for x in iterable ]

# { k : v for x in iterable }
{str(x) : x for x in iterable}

# this is sadly the only example I found in the psf docs :(
{x: x**2 for x in (2, 4, 6)}

```

Note:
- Some of the most powerful one-liners are dict comps
- Nested, Ternary logic for total transformation
- Official documentation is sparse here, but accurate
- Many tutorials like mine that cover patterns and gotchyas
- that iterable could be an expression that returns an iterable (like a lambda)
- most dict comps in the wild are not nearly that clean

---

### Curation example

---

```text
type                                               Point Address
id                                             US/PAD/p0/3077466
score                                                    11.9658
address        {'streetNumber': '701', 'streetName': 'Brazos ...
position                     {'lat': 30.26895, 'lon': -97.74042}
viewport       {'topLeftPoint': {'lat': 30.26985, 'lon': -97....
entryPoints    [{'type': 'main', 'position': {'lat': 30.2691,...
dtype: object
```

---

`{ k: y for i in <iterable>}`

```python

# What we want for each address match
row = {
    'type': '...',
    'streetName': '...',
    'lat': '...',
    'lon': '...',
}

```

---


```python

# How we get it

table = {results.index(r): {
    'type': r['type'],
    'streetName': r['address']['streetName'],
    'lat': r['position']['lat'],
    'lon': r['position']['lon'],
} for r in results}

# results is a list, so we don't need .items()

```


---


```python
{0: {'lat': 30.26895,
     'lon': -97.74042,
     'streetName': 'Brazos Street',
     'type': 'Point Address'}}
# Now that will taste good to Pandas

```

---

### Time Out for Readability

---

### Worst case scenario

- Dash + Mapbox
- Defining a massive dictionary
- Don't realize it's a comprehension until line 150
- Whole thing passes JSON to the api

Note:
- Dash is very cool if you don't want to write JS
- Interface has changed several times
- Problem space is not that well-explored
- Examples seem to come from JS Developers

---

### The code - Basic Mapbox usage

```python

def bigfoot_map(sightings):
    # groupby returns a dictionary mapping the values of the first field 
    # 'classification' onto a list of record dictionaries with that 
    # classification value.
    classifications = groupby('classification', sightings)
    return {
        "data": [
                {
                    "type": "scattermapbox",
                    "lat": listpluck("latitude", class_sightings),
                    "lon": listpluck("longitude", class_sightings),
                    "text": listpluck("title", class_sightings),
                    "mode": "markers",
                    "name": classification,
                    "marker": {
                        "size": 3,
                        "opacity": 1.0
                    }
                    # ... forever in some cases
                }
                for classification, class_sightings in classifications.items()
                #... this goes on for a while
                ]
                }
              
```

Note:
- notice the expressions in the calls
- can you tell this api 

---

### Good place to use dict() constructor for readability

```python

data : [
    dict(
        type="scattermapbox",
        lat=listpluck("latitude", class_sightings),
        lon=listpluck("longitude", class_sightings),
        text=listpluck("title", class_sightings),
        mode="markers",
        name=classification,
        marker={
            size: 3,
            opacity: 1.0}
    )
]
# ... forever

```

Note:
- Better highlighting
- Eliminates some indentation
- Eliminates quotets
- IMHO this is more readable in *some* cases

---

![](assets/img/dict_example.png)

Note:
- This image is just to show highlighting in IDEs

---

## Collections and Best Practices

---

### Learning from the documentation

When it comes to built-ins, clicking through to source in your IDE is only
going to give you some fake stubs (at least in the case of PyCharm)

---

- We must rely on our old friend, the documentation

- Perhaps more importantly, run your own experiments and see how it behaves
(or doesn't behave) for yourself.

"There is currently only one standard mapping type, the dictionary. "

Note: Mapping Type is another abstraction to know about

---

### The all powerful .get() method

"Return the value for key if key is in the dictionary, else default. 
If default is not given, it defaults to None...
### ...so that this method never raises a KeyError."

Note:
- This assumes you didn't introduce some other error in defining

---

"If `__missing__()` is not defined, KeyError is raised."
- missing can be defined, but better to use `defaultdict` or `.get()`

---



### defaultdict

- A perfectly good alternative to .get()
- The name says what it does (supplies a default)
- `None` doesn't break your code

---

### OrderedDict

@ul[spaced text-white]

- Since 3.7, dictionaries are ordered out of the box
- Mixed blessing, since most Python will be < 3.7 for some time
- Especially in Scientific domains where Python 2 (!) is *still* popular

@ulend


---

@ul[spaced text-white]

- Show what's happening
- Show *why* it needs to be ordered
- Try not to rely on order

@ulend

---

#### OrderedDict Powers Package-specific Types

@ul[spaced text-white]

- Parsers (LXML, etc.)
- Data APIs (along with other classes, helps to abstract away paging)
- BeautfulSoup 

@ulend

Note:
These packages didn't throw away their OrderedDict when the built-in changed. 

---

## Conclusion - WYSK

@ul[spaced text-white]

- Focus on readability
- Remember, remember ... these important members: 
- `.items()` `.keys()` `.values()`
- Practice dictionary comps `{k:v for i in iterable}`
- `Code[to][the][interface]`

@ulend

---

### Thanks! APUG @emoji[heart] @emoji[heart]

---

## Q/A  

### aaron@kite.com
#### https://kite.com/blog/python/python-dictionaries

Note:
- I can only speak from my own experience
- I am not a core developer
- Please jump in if you know better than I do!
---

### Thanks! APUG @emoji[heart] @emoji[heart]

---