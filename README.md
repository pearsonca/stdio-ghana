#stdio-ghana

[view course site](http://pearsonca.github.io/stdio-ghana/)

[apply to participate](http://goo.gl/d68nbg)

##Instructor Guidance

To edit / create sessions:
 1. go the the sessions/YYYY/$session folder
 2. the `index.html` or `index.md` (html vs markdown; markdown will supersede
html, and is necessary to have the content parsed as markdown) file is the
main session slides
 3. the yaml header material (the content between the `---`s) specifies all the
necessary header and footer material for the slides (e.g., the doctype, opening
html/head/body elements, closing elements) via the layout value
 4. so to add / edit slides, just add / edit the section elements.
 5. for non-slide content (e.g., if you need the students to download some
prepared content for an exercise), add it to this directory as well.
 6. for markdown slides: we are using the [kramdown](http://kramdown.gettalong.org/syntax.html) engine; detailed documentation in the link

To run the site locally, install jekyll according to GH instructions, then clone
the repository.  In the root of the clone, call

``` bash
jekyll serve -w --config=_config.yml,_locconfig.yml
```

This causes jekyll to serve the site on `localhost:4000`, and reload (`-w` option) whenever
content files are updated (changes to yml files will trigger the process to
indicate it is reloading, but **will not actually cause those changes to be reflected**).
The `--config` flag uses the global site config data, but overrides the relevant
url variables with the `_locconfig.yml` file.

If on a system with bash scripting available (typical *nix system, Windows with
Powerbash or the like installed), you may simply use the script `./run.sh` to
serve the site.

Notes on making session slides:
- if you use `<section markdown="block">` for slides + `.md` instead of `.html`
extension, [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) syntax should just work.
- may need to wary of mixing that with code highlighting
- if you use `<aside class="notes"> ... </aside>`, you can write notes
- the notes may also use markdown, if you add the `markdown="block"` attribute
to the aside element.

##Kramdown Reference
available [here](http://kramdown.gettalong.org/syntax.html)

##Integrated "Theme" Reference
available [here](http://www.ece.rutgers.edu/~marsic/books/SE/projects/Restaurant/RestaurantAutomation.pdf)

##Doing Site Editing w/ Atom
The [atom.io](http://atom.io) editor is pretty great.  You can use atom for jekyll
development in a convenient way:

1. open a terminal, navigate to the project root, and then `./run.sh` to start
the jekyll process.
2. open atom, then open that root directory (clover-O on OSX).
3. [one time]: install package that will do html previews (i.e., watch the html
  file and reload it if it changes, also render it as it appears in a web browser).
  @pearsonca uses "Atom Html Preview" package.
4. open `_site/index.html` in atom, then activate preview of that page.  You may
close the editing tab for index.html
5. restrictions: html preview may not support all browser capabilities (e.g., no
  back button)

As you develop, jekyll will update the rendered files, and the preview plugin
will reload them.  @pearsonca : I expect that there will soon be a plugin that also addresses
the jekyll startup + provides the terminal output (e.g., when regens occur) in-editor.
