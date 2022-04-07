import types


def partial(fn, *args):
    def partial_fn(*inner_args):
        return fn(*args, *inner_args)
    return partial_fn


def curry_(fn, known_args, new_args):
    num_args = fn.__code__.co_argcount
    if len(known_args) + len(new_args) == num_args:
        return fn(*known_args, *new_args)
    else:
        return lambda x: curry_(fn, known_args + new_args, (x,))


def curry(fn):
    def curried(*args):
        return curry_(fn, known_args=(), new_args=args)
    return curried


class currify:
    def __init__(self, fn):
        self.__name__ = fn.__name__
        if type(fn) == currify:
            self.fn = fn.fn
        else:
            self.fn = fn

    def __lshift__(self, other):
        num_args = self.fn.__code__.co_argcount
        if num_args <= 1:
            ret = self.fn(other)
            if isinstance(ret, types.FunctionType):
                return currify(ret)
            else:
                return ret
        return currify(curry_(self.fn, known_args=(), new_args=(other,)))

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


# credit: http://tomerfiliba.com/blog/Infix-Operators/
class Infix(object):
    def __init__(self, fn):
        self.fn = fn
    def __or__(self, other):
        return self.fn(other)
    def __ror__(self, other):
        return Infix(partial(self.fn, other))
    def __call__(self, v1, v2):
        return self.fn(v1, v2)


@Infix
def infix_add(x, y):
    return x + y

