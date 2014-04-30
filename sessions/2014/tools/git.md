---
layout: presentation
title: git
---
<section markdown="block">
##What do you work on?
<aside class="notes" markdown="block">
- what projects do you work on with other people?
- how do you share that work?
- what problems do you run into when trying to share the work?
- trying to incorporate their comments / improvements / etc into the work?
</aside>
</section>

<section markdown="block">
##Version Control
<aside class="notes" markdown="block">
VC addresses those problems by establishing a formal language for working with people
(including future / past snapshots of yourself).

All provides a few basic notions:
- what is the current version
- what is the history leading up to that?
- who made which changes?

`git` provides one twist -- alternative versions -- and then things to do with them.
</aside>
</section>

<section markdown="block">
##Serial Git
<aside class="notes" markdown="block">
- fork hellogroup project (e.g., this repo?)
- have people make some series of changes, locally and remotely
- first local changes, then commit + push
- then remote changes (via web interface) and commit (with insta-push)
- then local changes (pre pull) and show conflicts resolution
</aside>
</section>

<section markdown="block">
##Parallel Git
<aside class="notes" markdown="block">
- Q&A about branches:
 * they represent parallel work
 * like parallel computation, best when shared state can be avoided
 * how to avoid that kind of shared state? that's a long discussion - the point of a software engineering course
- using forks, initiate pull requests
- need some pulls that can be unproblematically parallel
- then show how some create the need for merging
</aside>
</section>

<section markdown="block">
##Troubleshooting
<aside class="notes" markdown="block">
- first mantra: don't panic - you are using distributed version control.
practically impossible to destroy work unless you set out to destroy work
- ways to avoid troubleshooting:
 * start work by pulling, regularly push, and always finish work with a push
 * work in branch 
- easiest sol'n duplicate the stuff you're trying to hold on to
- rewind the source until config isn't screwed
- careful cut and paste back from the duplicated stuff back into what you have
</aside>
</section>
