Notes:

Non-functional requirements

    Accessibility
    Capacity, current and forecast
    Compliance
    Documentation
    Disaster recovery
    Efficiency
    Effectiveness
    Extensibility
    Fault tolerance
    Interoperability
    Maintainability
    Privacy
    Portability
    Quality
    Reliability
    Resilience
    Response time
    Robustness
    Scalability
    Security
    Stability
    Supportability
    Testability

some guidance for producing the slides:
 - to make the markdown work, there are two changes that are needed: rename index.html -> index.md, and then the slide elements must be declared as
```
<section markdown="block"><!-- n.b. the markdown attribute is critical here -->
...markdown format here, e.g.
#TITLE will yield <h1>TITLE</h1>
to insert a <br/> use '  ' -- i.e., two spaces -- at the end of a line.  For normal paragraph breaks, use line breaks:

para1

para2

etc
</section>
```
 - relative to text alignment, let me know what you want generally (my personal preference is left aligned everything past opening slide) and I'll fix the styling so that it applies across the sessions
 - if you want to keep text around as notes (and indeed, have them available as notes), use:
```
<section markdown="block">
blah, blah, blah
<aside class="notes" markdown="block">
...markdown formated stuff
</aside>
</section>
```
