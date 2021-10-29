import hug

@hug.get()
def sum(num1:hug.types.number=3, num2:hug.types.number=5):
    return {
        'sum': num1 + num2
    }
