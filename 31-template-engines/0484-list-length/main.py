from jinja2 import Template

print(Template("{{ items | length }}").render(items=[1, 2, 3]))
