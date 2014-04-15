stdio-ghana
===========

Repository for course materials

view course site at: http://pearsonca.github.io/stdio-ghana/

applications for 2014: http://goo.gl/d68nbg

To edit / create sessions:
 1. go the the sessions/YYYY/$session folder
 2. the `index.html` file is the main session slides
 3. the yaml header material (the content between the `---`s) specifies all the necessary header and footer material for the slides (e.g., the doctype, opening html/head/body elements, closing elements)
 4. so to add / edit slides, just add / edit the section elements.
 5. for non-slide content (e.g., if you need the students to download some prepared content for an exercise), add it to this directory as well.

To run the site locally, install jekyll according to GH instructions, then clone the repository.  In the root of the clone, call `jekyll serve --baseurl ""`

Notes on making session slides:
- if you use `<section markdown="block">` for slides + `.md` instead of `.html`
extension, [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax should just work.
- may need to wary of mixing that with code highlighting
- if you use `<aside class="notes"> ... </aside>`, you can write notes
- the notes may also use markdown, if you add the `markdown="block"` attribute
to the aside element.
