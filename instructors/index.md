---
layout: section
---
{% for instructor in site.instructors %}
{{ instructor.output }}
{% unless forloop.last %}* * *{% endunless %}
{% endfor %}
