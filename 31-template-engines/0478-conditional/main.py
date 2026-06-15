from jinja2 import Template

template = Template("{% if logged_in %}welcome{% else %}guest{% endif %}")
print(template.render(logged_in=True))
