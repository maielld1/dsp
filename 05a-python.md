# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are both data structures that store ordered sequences of objects. Both can contain any type of object, but tuples, unlike lists, are immutable. This means that once created, their contents cannot be modified. Since lists can be modified, they do not provide a valid hash method for dictionaries. It is for this reason that only tuples work as keys in dictionaries, as keys also need to be immutable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets are both mutable. However, sets can only contain unique objects and are unordered. In addition, sets require all items to be hashable. As a result, sets tend to be faster than lists for finding an element, especially for larger lists. In the worst case for lists, the required element might be right at the end, so the entire list would have to be searched through. Sets can be used to perform operations such as unions and intersections. For example:

a = set(["California", "Illinois", "New York"]) b = set(["California"])

a.intersection(b) will produce the elements that are common to both sets - in this case, California. Sets can also be used to find the non duplicate items of a list.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

lambda in Python allows for the creation of compact, one-line functions that are anonymous (not bound to a name). In particular, they do not have a return statement. On their own, they are useful at simplifying code as shown in the below example, which is a lambda function that returns the cube of x:

cube = lambda x: x**3

The above line of code is simpler (but not by a lot) than having to define a new function with def that then returns a value. Lambdas become much more powerful when used as parameters in other functions such as sorted, map, and filter, with which one-line functions can be created that would otherwise require some kind of loop. The below example uses a lambda function in the key argument to sorted (from https://wiki.python.org/moin/HowTo/Sorting):

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
sorted(student_tuples, key = lambda student: student[2])   # sort by age
The function returns the following output, with the ages of the students sorted in ascending order:

[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

Here, lambda is passing the index of the object that is being iterated over - in this case, student_tuples - to the key parameter of the sorted function.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

A list comprehension is a way of constructing a list using set builder notation. It is a succinct way to generate a list in one line. The following list comprehension generates a list that contains the cubes of all numbers from 0 to 9.

cubes = [i**3 for i in range(10)]

An equivalent list can be generated using the map function as follows:

list(map(lambda i: i**3, range(10)))

Finally, the list can be further refined using filter. The below list will only contain those values in cubes that are less than 100.

list(filter(lambda i: i < 100, cubes))

The syntax for set comprehensions is identical to list comprehensions, except they use {} instead of []:

cubes_set = {i**3 for i in range(10)}

A dictionary comprehension is used to generate a new dictionary as shown below:

cubes_dict = {i: i**3 for i in range(10)}

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





