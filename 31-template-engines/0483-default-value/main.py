from jinja2 import Template

print(Template("{{ name | default('anonymous') }}").render())
