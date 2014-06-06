<div class="blurb" markdown="block">
{% if page.imagetype %}![{{ page.name }}]({{ page.url | replace:'html', page.imagetype }}){: width="180px"}{% else %}![no image]({{ site.absoluteurl }}/404.jpg){% endif %}

###{{ page.name }}, *{{ page.role }}*

####{{ page.title }}, {{ page.affiliation }}, [@{{ page.github }}](http://github.com/{{ page.github }})

{{ content }}
</div>
