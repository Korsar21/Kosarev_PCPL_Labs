import random
def gen_random(num_count, begin, end):
    for i in range(0, num_count):
        print(random.randint(begin, end), end=' ')

gen_random(5,1,10)