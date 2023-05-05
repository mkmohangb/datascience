### Iterators
  Any collection or container type can be made iterator. e.g. ```iter([1,2,3]), iter("foo"), iter({'foo': 1, 'bar': 2, 'baz': 3})```
 ``` 
  >>> a = ['foo', 'bar', 'baz']

  >>> itr = iter(a)
  >>> itr
  <list_iterator object at 0x031EFD10>

  >>> next(itr)
  'foo'
  ```
  ```next()``` raises ```StopIteration``` exception is raised when there is nothing left to return.
  
  <img src="https://user-images.githubusercontent.com/2610866/236466428-210efda8-f739-43f5-9010-9967868a4e93.png" width="250" height="250"/>

  https://realpython.com/python-for-loop/


### Generators
Generator method
```
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```
Generator expression
```
csv_gen = (row for row in open(file_name))
```

Performance comparison between list comprehension & generator expression

``` 
import cProfile
cProfile.run('sum([i*2 for i in range(10000)])')


cProfile.run('sum((i*2 for i in range(10000)))')
```
When you call a generator function or use a generator expression, you return a special _iterator_ called a generator.

Advanced generator methods:
```
send => send a value back to generator
throw
close => close the generation process

i = (yield num) #i will contain the value sent by send()
gen.send(100)
gen.close()

```

https://realpython.com/introduction-to-python-generators/
