---
layout: presentation
year: 2014
title: Distributed Computing
instructors:
 - Carl
---
<section markdown="block">
## What is a computer?

<aside class="notes" markdown="block">
Previous discussion will probably emphasis "serial" thinking.

This time highlight the "internet" perspective - when you visit
a website, that's your computer talking to another computer.  When
you load two websites, they don't always give you all the information
at the same time.  That's asynchrony
</aside>
</section>

<section markdown="block">
## Synchronous

vs.

## Asynchronous
<aside class="notes" markdown="block">
Quick vocab check.  Then exercise on with groups manually calculating things
in series vs parallel.
</aside>

</section>

<section markdown="block">
## What made the parallel version easy?

<aside class="notes" markdown="block">
Aside from simplicity of operation (do a sum or product, probably)

- None of the divided pieces depended on the others.
- the divided pieces were identical
- the integration step looked exactly like the divided steps

</aside>
</section>

<section markdown="block">
## Problems with Shared State?

<aside class="notes" markdown="block">
Again, some pen-and-paper exercises.  Dining philosophers?  Repeat the
earlier exercise, but with a tweak on where they record results.

Highlight:

- resource contention
- result overwrites

</aside>
</section>

<section markdown="block">
High level concepts available when shared state can be avoided:

- filter, map
- fold (plain, left, and right), scan

Ways to avoid shared state

- zip, join
- flatten

<aside class="notes" markdown="block">
Q&A about the concepts.  Write a dummy API for these concepts, have them
implement something using it.
</aside>

</section>
