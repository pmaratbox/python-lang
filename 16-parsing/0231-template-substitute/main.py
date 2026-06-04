import re


def substitute(template, values):
    return re.sub(r"\{(\w+)\}", lambda m: values[m.group(1)], template)


print(substitute("hi {name}", {"name": "Ada"}))
