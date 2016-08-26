# Django Sortable Column
A simple Django templatetag to renders a sortable column to support sorting in tables
# Usage
## Setup
Add "sortable_column" to your INSTALLED_APPS setting like this:
```
INSTALLED_APPS = [
  ...
  'sortable_column',
]
```

Additionally, include the following snippet at the top of any template that makes use of
the pagination tags:

```python
{% load bootstrap_pagination %}
```
