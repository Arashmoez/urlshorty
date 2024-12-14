import random , string
def code_generator(length=6):
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

