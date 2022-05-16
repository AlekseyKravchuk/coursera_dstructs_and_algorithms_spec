from functools import wraps


def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(open_tag, msg, close_tag)

        # Return the decorated function
        return wrapper

    # Return the decorator
    return decorator


@html(r'<b>', r'</b>')
def s_html_wrapped(msg):
    print(f'function "{s_html_wrapped.__name__}" has been started.')
    return msg


if __name__ == '__main__':
    msg = 'Text to be enclosed into html tags'
    # open_tag = r'<b>'
    # close_tag = r'</b>'

    wrapped = s_html_wrapped(msg)
    print(wrapped)
