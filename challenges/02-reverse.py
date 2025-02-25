# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

def string_reverse(string):
    # reversed_string = ''

    # for x in string:
    #     reversed_string = x + reversed_string

    rev = [x for x in string]
    rev.reverse()
    return rev


print(string_reverse('hello'))
