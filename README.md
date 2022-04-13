# Stuck with Python but you actually want to use Haskell?

This is a silly package that (ab)uses Python operator overloading to reproduce beloved features from functional programming.

You can do:

**Currying**

```python
@curry
def f(a, b, c):
  return a + b + c
  
f(1, 2, 3)
Out[0]: 6

g = f << 1
g << 2 << 3
Out[1]:  6

f << 1 << 2 <<< 3
Out[2]: 6
```

**Infix Notation**

```python
@infix
def plus(a, b):
  return a + b
  
1 |plus| 2
Out[0]: 3
```

**Functional Programming!**


```python
@curry
def foldl(fn, x, xs):
    return x if not xs else fold << fn << (x |fn| xs[0]) << xs[1:]
    
sum = foldl << plus << 0

sum([1, 2, 3])
Out[0]: 6
```

Big **credit** goes to these guys:
- http://tomerfiliba.com/blog/Infix-Operators/
- https://sagnibak.github.io/blog/python-is-haskell-currying/
