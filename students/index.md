---
layout: section
---
{% assign current_students = site.students | where: "year", 2014 %}
##Current Students
{% for student in current_students %}
{{ student.output }}
* * *
{% endfor %}

{% assign past_students = site.students %}
##Past Students
{% for student in past_students %}
{% unless student.year == 2014 %}
{{ student.output }}
{% endunless %}
{% endfor %}
