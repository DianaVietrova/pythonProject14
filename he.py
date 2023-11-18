result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a  больше или равно b")
        if b > 100:
            raise IndexError("b  меньше или равно 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except IndexError as ie:
        print(f"IndexError: {ie}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)

