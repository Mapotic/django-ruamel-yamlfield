# Django Ruamel YAML field


Django Ruamel YAML field allow you store yaml data to database.
Is inspired by django-yamlfield.

In addition allow store comments, block texts, ... 

```yaml
data:
  key: some_key
  template: |
    {% for item in data %}
      {{ run(item) }}
    {% endfor %}
  # this is commented text
foo:
  - alpha
  - beta
```
