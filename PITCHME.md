

## Effective Dictionaries
## {  }
testing
---

![](assets/img/skipping-steps.jpg)

---


### Aaron Harris

### aaron@kite.com

#### Dev Advocate + Consultant
(Python, JavaScript, Automation)

(Bartending, Jury Duty ...)

Note:

- Notes for each slide may go here

---

##### This Presentation (now): 
##### https://gitpitch.com/alphaharris/thinking-in-dictionaries

------

#### Based on a True Blog Post: 
#### https://kite.com/blog/python/python-dictionaries

---

#### Quick poll... 

---

#### Solved a problem with a dictionary this week


---

#### Solved a problem with a dictionary this week

@ul[spaced text-white]
- Performance
- Interface
    - now[we][can][do][this]
- Better Code
@ulend



---

#### Who needed to 
####  look up dictionaries this week? 

--- 
### Today...
@ul[spaced text-white]
- Defining and Iterating
- Nested Data
- Handling JSON
- Comprehensions and Enhancements
- Working with Pandas (if we have time)
@ulend


---

### Defining and Iterating

Note: 

- Dictionaries are a powerful structure
- Best way to learn is to get some practice!
---
### TEST

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
@[8-10](Yes, there is a problem here...)
@[12](What's the error?)


---

#### ValueError: too many values to unpack (expected 2)

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

---

---

`for` is going to look for an iterator  `__iter__`

"Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys())."

- Nothing magical is happening here, we're just getting d.keys()

- Also note that list(my_dict) will return a list of keys

---

### So, what is .items() ??

"Return a new view of the dictionary’s items ((key, value) pairs)."

---

### What the heck is a view??
Is that even python?

"They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, 
the view reflects these changes."

"Keys and values are iterated over in insertion order."


Gothya - 
"Iterating views while adding or deleting entries in the dictionary may raise a RuntimeError or fail to iterate over all entries."
"Changed in version 3.7: Dictionary order is guaranteed to be insertion order."

---

### Kinds of Data (Nested, Relational)

---

### Relational - 

![](assets/img/relational.jpg)

---

@ul[spaced text-white]
- Well Explored
- Know your schema going in (hopefully)
- More overhead
@ulend

---

![](assets/img/inception.jpg)

---

### Nested - Don't Die Alone!


@ul[spaced text-white]
- Flexible, great for handling *unknowns*
- Two-edged-sword!!
- Deep structures will slow you down
- Readabililty is "key"    ¯\\_(ツ)_/¯

@ulend

---

##### The farther down you go...
##### The faster time passes in the outside world

![](assets/img/oldman.gif)

#### Full of regret
#### Waiting to die alone

---






@ul[spaced text-white]
- Gets complicated quickly
- Might need recursion... and that's okay
- Don't be afraid to "curate"
  - one-off cherry-picking ... or ...
  - comprehensions to get specific values
- Other tools don't understand your tree
  - databases
  - apis (e.g. google sheets)
@ulend

---



### Consuming JSON

---

### Typical use-case with Requests

---

```python
import requests

r = requests.get('some_dat_site')
r.json # what's the difference here
r.text

my_data = r.json
type(my_data)
# dict()

# Okay, we have a dict! Now what?

```

---

```python

# We want to do something with that data

# send specific values to airtable

# get summary statistics from Pandas

```

--- 

### Curating with comprehensions

- We have our data, but we need rows
- Maybe we're sending this straight to a spreadsheet
- Maybe we just want readable rows... for reasons!

### Basic Dict comprehension template

- Like .items, .keys, .values, this is worthy of memorization
- Dict comps are maybe more powerful than list comps
- Same reason that dicts are sometimes more powerful than lists

### Okay the pattern!

```python

[ x for x in iterable ]

{ k : v for x in iterable}

{x: x**2 for x in (2, 4, 6)}
# this is sadly the only example I found in the psf docs :(


```

- that iterable could be an expression that returns an iterable (like a lambda)

- most dict comps in the wild are not nearly that clean

---

### Time Out for Readability

---

### The worst case - Dash + Mapbox

- Defining a massive dictionary
- Don't realize it's a comprehension until line 150
---

![](assets/img/dict_example.png)

---

### Learning from the documentation

When it comes to built-ins, clicking through to source in your IDE is only
going to give you some fake stubs (at least in the case of PyCharm)

- We must rely on our old friend, the documentation

- Perhaps more importantly, run your own experiments and see how it behaves
(or doens't behave) for yourself.

"There is currently only one standard mapping type, the dictionary. "



---

### The all powerful .get() method

"Return the value for key if key is in the dictionary, else default. 
If default is not given, it defaults to None...
### ...so that this method never raises a KeyError."

---

"If `__missing__()` is not defined, KeyError is raised."
- missing can be defined, but better to use `defaultdict` or `.get()`

---
### Collections and Best Practices

---

```python

# list comps are easy to recognize
new_list = [x.name for x in my_list]

# How cool are dictionary comps??
dict_from_list = { x.name : x for x in my_list}

```

---


### defaultdict

- A perfectly good alternative to .get()
- The name says what it does (supplies a default)
- `None` doesn't break your code


### OrderedDict

- Since 3.7, dictionaries are ordered out of the box
- Mixed blessing, since most Python will be < 3.7 for some time
- Especially in Scientific domains where Python 2 (!) is *still* popular

- Better to use OrderedDict to let everyone know what's happening
- If your logic depends on that ordering, it should be clear how and why
- Even better to write code that doesn't rely on order

#### Plenty of Real World packages use OrderedDict
- Parsers (LXML, etc.)
- Data APIs (along with other classes, helps to abstract away paging)
- BeautfulSoup 


---

## Conclusion 

- Focus on readability
- Remember, remember ... the members: `.items()`, `.keys()`, `.values()`
- Practice dictionary comps `{k:v for x in iterable}`
- `Code[to][the][interface]`

Thanks! APUG <3 <3

---

## Q/A  

- Feel free to volunteer an answer
- I can only speak to my own experience

---