from jinja2 import Template

template = Template("{{ user.name }}")
data = {"user": {"name": "alice"}}
print(template.render(**data))
