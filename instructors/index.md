---
layout: section
---
{% assign current_instructors = site.instructors | where: "status", "current" %}
##Current Instructors
{% for instructor in current_instructors %}
{{ instructor.output }}
* * *
{% endfor %}

{% assign past_instructors = site.instructors | where: "status", "past" %}
##Past Instructors
{% for instructor in past_instructors %}
{{ instructor.output }}
{: .instructor}
{% unless forloop.last %}* * *{% endunless %}
{% endfor %}
