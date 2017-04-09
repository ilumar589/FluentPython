def chain(*iterables, **dict):
    for it in iterables:
        for i in it:
            yield i


def execute():
    s = 'ABC'
    t = tuple(range(3))
    d = {"val1": 1, "val2": 2}
    print(list(chain(s, t, **d)))

execute()
