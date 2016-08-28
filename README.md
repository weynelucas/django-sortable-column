# Django Sortable Column
A simple Django templatetag to renders a sortable column to support sorting in tables
# Usage
## Setup
Add `sortable_column` to your `INSTALLED_APPS` setting like this:
```
INSTALLED_APPS = [
  ...
  'sortable_column',
]
```

Additionally, include the following snippet at the top of any template that makes use of
the sortable column tags:

```html
{% load sortable_column %}
```
## Examples

```html
{% sortable_column request=request property="title" title="Title" %}
{% sortable_column request=request property="title" title="Title" style="width: 200px" %}
{% sortable_column request=request property="publication_date" title="Publication Date" default_order="desc" %}
```

the following results for the code snippet above are:
```html
<th class="sortable">
    <a href="/your/path?myaction?order=asc;sort=title">
        Title
    </a>
</th>

<th class="sortable" style="width: 200px">
    <a href="/your/path?order=asc;sort=title">
        Title
    </a>
</th>

<th class="sortable">
    <a href="/your/path?order=desc;sort=publication_date">
        Publication Date
    </a>
</th>
```
#sortable_column
##Arguments
* `property` - name of the property relating to the field
* `title` - title caption for the column
* `request` - request object containing the parameters
* `default_order` (optional) - default order for the property; choose between 'asc' (default if not provided) and 'desc'
* `style` (optional) - the sytle attribute of rendered html tag

##Configuration Settings
Is possible configure the sortable columns properties on your settings file (`settings.py`) adding a dictionary `SORTABLE_COLUMN_SETTINGS` like this:

```python
SORTABLE_COLUMN_SETTINGS = {
  'class-name': 'sortable',
  'icon': 'fa fa-sort',
  'icon-asc':'fa fa-sort-asc',
  'icon-desc':'fa fa-sort-desc',
  'icon-placement': 'left',
}
```

the attributes of settings (all optionals) are:

* `class-name`: the class name of th tag rendered by template tag ('sortable' if not provided)
* `icon`: name of icon to represent the default sort (empty string if not provided)
* `icon-asc`: name of icon to represent the asc sort  (empty string if not provided)
* `icon-desc`: name of icon to represent the desc sort  (empty string if not provided)
* `icon-placement`: placement of the icon in relation to the tile caption; choose between 'left' (default if not provided) or 'rigth'

the attributes `icon`, `icon-asc` and `icon-desc` can be a class name of empty elements like in glyphicons from [Bootstrap](http://getbootstrap.com/components/#glyphicons) or icons from [Font Awesome](http://fontawesome.io/icons/) toolkit (remember to add these libraries on your pages if you want to render its related icons)
```python
'icon': 'glyphicon glyphicon-sort'
```
or a path to image in your static files
```python
'icon-desc': STATIC_URL + 'images/sort-desc.png'
```

To the `SORTABLE_COLUMN_SETTINGS` configured like at the begining of this topic, the code snippet 
```html
{% sortable_column request=request property="title" title="Title" %}
```
will result in
```html
<th class="sortable">
    <a href="/your/path?order=asc;sort=title">
        <i class="fa fa-sort"></i>
        Title
    </a>
</th>
```
