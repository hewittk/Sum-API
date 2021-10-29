import hug

@hug.get()
def sum(num1:hug.types.number=3, num2:hug.types.number=5):
    return {
        'First number': num1,
        'Second number': num2,
        'Sum': num1 + num2
    }
