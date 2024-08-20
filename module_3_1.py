calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    string_ = (len(string), string.upper(), string.lower())
    return string_


def is_contains(string, list_to_search):
    count_calls()
    string_ = string.upper()
    list_ = None
    for i in list_to_search:
        if string_ == i.upper():
            list_ = True
            break
        elif string_ != i.upper():
            list_ = False
    return list_


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
