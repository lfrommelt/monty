
## Your turn

Write code that checks whether there is a key 'animal' in the dict bello.
If there is no such key, create a key 'animal' and set it to True if bello is of the 'type' 'dog'

```python
bello = {"name": "bello", "type": "dog", "age": 6}

# TODO your code goes here
```


## Solution

```{ .python .exec }
bello = {"name": "bello", "type": "dog", "age": 6}

if 'animal' in bello and bello['animal']:
    print('Bello already is an animal.')
else:
    if bello['type'] == 'dog':
        bello['animal'] = True

print(bello['animal'])
```






## PINGO - OOP II

```
class Dog:
    def walk(self):
        return "*walking*"

    def speak(self):
        return "Woof!"

class JackRussellTerrier(Dog):
    def speak(self):
        return "Arff!"

bobo = JackRussellTerrier()
bobo.walk()
```

```
bobo = JackRussellTerrier()
bobo.speak()
```

    a) Woof!
    b) Arff!
    c) *walking*
    d) AttributeError: 'JackRussellTerrier' object has no attribute 'walk'


