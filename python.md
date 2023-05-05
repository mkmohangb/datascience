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
