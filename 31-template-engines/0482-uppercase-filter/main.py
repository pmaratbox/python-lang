from jinja2 import Template

print(Template("{{ name | upper }}").render(name="alice"))
