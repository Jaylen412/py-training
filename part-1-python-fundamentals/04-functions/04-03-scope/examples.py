# 04-03 Scope


# Example 1: variables created inside a function are local
def make_greeting(name):
    message = f"Hello, {name}"
    return message


print(make_greeting("Ada"))
# print(message) here would fail with NameError: message only exists
# while make_greeting is running.

# Example 2: functions can read global variables
TAX_RATE = 0.2


def price_with_tax(price):
    return price * (1 + TAX_RATE)


print(price_with_tax(50))

# Example 3: assigning inside a function creates a NEW local variable
counter = 0


def increase_counter():
    counter = 100   # a local variable that happens to share the name
    return counter


print(increase_counter())
print(counter)

# Example 4: parameters are local too
number = 5


def double(number):
    number = number * 2
    return number


print(double(number))
print(number)

# Example 5: the global keyword (shown so you recognise it - avoid it)
score = 0


def add_point_global():
    global score
    score += 1


add_point_global()
add_point_global()
print("score is now", score)


# Example 6: the better way - pass data in, return data out
def add_point(current_score):
    return current_score + 1


score = 0
score = add_point(score)
score = add_point(score)
print("score is now", score)


# Example 7: why globals cause bugs - the result depends on hidden state
discount = 0.1


def sale_price(price):
    return price * (1 - discount)


print(sale_price(100))
discount = 0.5   # somewhere far away in a bigger program...
print(sale_price(100))


# The fix: make the dependency a parameter
def sale_price_clear(price, discount):
    return price * (1 - discount)


print(sale_price_clear(100, 0.1))
