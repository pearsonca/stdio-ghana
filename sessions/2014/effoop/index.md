---
layout: presentation
year: 2014
title: Effective OOP
instructors:
 - Carl
---

<section markdown="block">
###Why Use Objects?
<aside class="notes" markdown="block">
QA with students; I'd say the gist of it is that thinking with objects lets one
*do* software engineering.  Goal of this session would be to have the students
experience some ways in which objects enable best practices.
</aside>
</section>

<section markdown="block">
###Dividing Work

<aside class="notes" markdown="block">
interfaces / contracts as a way to divy up a job

- describes which side does what
- having them lets you focus on one piece at a time
- or if working in a team, dividing up work between developers
- disciplined use keeps you from entangling ideas too much
- when used with good API thinking, also a powerful way to communicate about
a data structure

Use some of the Python OOP syntax to have take something bad and make it good?
</aside>

</section>

<section markdown="block">
###Do Not Repeat Yourself

<aside class="code" markdown="block">
Using abstract classes to provide facade.  Using generics
(aka, typing / interfaces) to writing algorithms once (e.g., sorting)
</aside>
</section>

<section markdown="block">
###Thinking with Tests

<aside class="notes" markdown="block">
Revisit mock objects.

If you've translated requirements into tests, and then digested those
requirements into a series of tests, also corresponding with tests,
can think of combination of interface + tests as being the specification
for objects.
</aside>
</section>

<section markdown="block">
###Self Documenting Code
<aside class="notes" markdown="block">
Objects are a means of saying these things go together.

Also, a way to make other things not be concerned with the details.  Let's
the code speak more to what it's doing.
</aside>
</section>

<section markdown="block">
##OPP Danger Zone
</section>

<section markdown="block">
##Too Much Magic

<aside class="notes" markdown="block">
When things are too abstracted to be able to figure out what's going on where.

Hard to debug problems -- often because interpreter reports errors in strange
places.
</aside>
</section>

<section markdown="block">
##Inheritence vs Composition
</section>
