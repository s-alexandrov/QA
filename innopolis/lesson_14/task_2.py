def gen_func():
    h = 1
    x = 1
    while True:
        yield x + h
        x, h = h, h + h


for i in gen_func():
    print(i, '\n', 10)