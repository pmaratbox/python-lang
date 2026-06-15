from jinja2 import Template

template = Template(
    "{% for u in users %}{{ u.name }}: {{ u.age }}\n{% endfor %}"
)
data = {"users": [{"name": "alice", "age": 30}, {"name": "bob", "age": 25}]}
print(template.render(**data).strip())
