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


class partial():
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        def _partial_fn(*inner_args):
            return self.fn(*args, *inner_args)
        return _partial_fn
