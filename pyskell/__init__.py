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
