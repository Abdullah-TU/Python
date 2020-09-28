def doSomething(par):
    print("par:", par)
    try:
        print(" length:", len(par), end="")
        try:
            print(" Value at index 5:", par[5], end="")
            try:
                print(" As an integer:", int(par), end="")
            except ValueError:
                raise ValueError("ValueError: invalid literal for int() with base 10: '{}'".format(par))
        except IndexError:
            raise IndexError("IndexError: list index out of range")
        except KeyError:
            raise KeyError('KeyError: 5')
    except TypeError:
        raise TypeError("TypeError: object of type '{}' has no len()".format(type(par).__name__))
    finally:
        print()
# Add your new doSomething(par) below

# Add your new doSomething(par) above

for par in ["a string", 3.14, [1, 2, 3, 4], {}]:
  try:
    doSomething(par)
  except Exception as e:
    print(str(type(e)) + "\n", str(e))
