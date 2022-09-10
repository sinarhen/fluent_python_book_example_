import html
import numbers
from functools import singledispatch


@singledispatch
def htmlize(obj):
    html_obj = html.escape(repr(obj))
    return f'<pre>{html_obj}</pre>'


@htmlize.register(str)
def _(text):
    h = html.escape(text).replace('\n', "</br>\n")
    return f'<p>{h}</p>'


@htmlize.register(numbers.Integral)
def _(num):
    return f'<p>{num}</p>'
