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


class curry:
    def __init__(self, fn):
        self.__name__ = fn.__name__
        if type(fn) == curry:
            self.fn = fn.fn
        else:
            self.fn = fn

    def __lshift__(self, other):
        num_args = self.fn.__code__.co_argcount
        if num_args <= 1:
            ret = self.fn(other)
            if isinstance(ret, types.FunctionType):
                return curry(ret)
            else:
                return ret
        return curry(curry_(self.fn, known_args=(), new_args=(other,)))

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)


class infix(object):
    # credit: http://tomerfiliba.com/blog/Infix-Operators/
    def __init__(self, fn):
        self.fn = fn
    def __or__(self, other):
        return self.fn(other)
    def __ror__(self, other):
        return infix(partial(self.fn, other))
    def __call__(self, v1, v2):
        return self.fn(v1, v2)


@curry
def fold(fn, x, xs):
    return x if not xs else fold << fn << (x |fn| xs[0]) << xs[1:]


@curry
def reduce(fn, xs):
    return fold(fn, xs[0], xs[1:])


@infix
def plus(a, b):
    return a + b

