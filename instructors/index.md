---
layout: section
---
##Current Instructors
{% assign current_instructors = site.instructors | where: "status", "current" %}
{% for instructor in current_instructors %}
{{ instructor.output }}
{% unless forloop.last %}* * *{% endunless %}
{% endfor %}

{% assign past_instructors = site.instructors | where: "status", "past" %}
##Past Instructors
{% for instructor in past_instructors %}
{{ instructor.output }}
{% unless forloop.last %}* * *{% endunless %}
{% endfor %}
