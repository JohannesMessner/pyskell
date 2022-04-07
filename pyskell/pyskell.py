def partial(fn, arg):
    def partial_fn(*args):
        return fn(arg, *args)
    return partial_fn