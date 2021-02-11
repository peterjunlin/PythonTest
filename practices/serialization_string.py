def format_with_formatted_string_literal():
    name = 'Nancy'
    age = 20
    p = 3.1415926

    # string and integer
    s = f'{name}: {age}'
    assert s == 'Nancy: 20'

    # double with precision
    s = f'pi = {p:.3f}'
    assert s == 'pi = 3.142'

    # double with width
    s = f'pi = ({p:10.3f})'
    assert s == 'pi = (     3.142)'


def format_with_string_format():
    name = 'Nancy'
    age = 20

    # using position
    s = '{0}: {1}. Hello, {0}!'.format(name, age)
    assert s == 'Nancy: 20. Hello, Nancy!'

    # using variable name
    s = '{name} is {age} years old. Hello, {name}!'.format(name='Peter', age=20)
    assert s == 'Peter is 20 years old. Hello, Peter!'

    # using dictionary
    d = {'name': 'Peter', 'age': 20}
    s = '{0[name]} is {0[age]} years old. Hello, {0[name]}!'.format(d)
    assert s == 'Peter is 20 years old. Hello, Peter!'


def format_with_manual_format():
    name = 'Nancy'
    age = 20

    s = name.rjust(10) + repr(age).rjust(10)
    assert s == '     Nancy        20'


if __name__ == '__main__':
    format_with_formatted_string_literal()
    format_with_string_format()
    format_with_manual_format()
