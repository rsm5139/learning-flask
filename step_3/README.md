# Step 3: Pages and Templates

Compile the app in the ```step_3``` folder using the ```python routes.py``` command. Take a look at the new example. There are 2 pages: Home and About. ```routes.py``` references the new page by adding an ```about()``` function. If you examine ```index.html``` and ```about.html```, they both start with ```{% extends "page.html" %}```. The content with the ```{% block %}{% endblock %}``` tags are inserted into the respective tags in ```page.html```. Notice that ```page.html``` looks like a regular webpage, apart from the ```{% block %}{% endblock %}``` tags. This template can be used over and over to save time when creating new pages.

Flask uses a templating system called Jinja2. To learn more about Jinja2, please visit the [documentation](http://jinja.pocoo.org/docs/2.9/) page.

## Other Steps

[Step 1/2](https://github.com/rsm5139/learning-flask)