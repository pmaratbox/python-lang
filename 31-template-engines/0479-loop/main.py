from jinja2 import Template

template = Template("{% for n in nums %}{{ n }}\n{% endfor %}")
print(template.render(nums=[1, 2, 3]).rstrip("\n"))
