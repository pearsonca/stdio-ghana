---
layout: presentation
title: git
---
<section markdown="block">
##What do you work on?

<aside class="notes" markdown="block">
Q\&A (1-2ish min per person, up to 10ish minutes - for people not inclined to answer, no-opt out with \"give 1 example, say one good thing about it, one bad thing\")
- what projects do you work on with other people?
- how do you share that work?
- what's good about those methods?  what problems you see?
- trying to incorporate their comments / improvements / etc into the work?

Discussion should elicit work like
- documents, small transformation programs / scripts (i.e., potentially single file)
- items with dependencies; e.g., a report with a figure that is produced from some spreadsheet,
programs with some minimal objects, or scripts that make use of some other utility code
- work with many separable dependencies

Solutions for sharing might range from
- print the work, have them comment on it in pen and ink
- email the file / files back and forth
- shared drive / cloud sharing solution

Expected Pros/Cons
- pro: expediency, obvious artefact (piece of paper, specific email)
- con: no log of what people said, lots of duplicate work, possible to misplace / mix up artefacts

</aside>
</section>

<section markdown="block">
##Version Control
<aside class="notes" markdown="block">
VC addresses those problems by establishing a formal language for working with people
(including future / past snapshots of yourself).

All provides few basic notions:

- what is the current version
- what is the history leading up to that?
- who made which changes?

`git` provides one twist, **alternative versions**, and then tools to use them.
</aside>
</section>

<section markdown="block">
##Serial Git
<aside class="notes" markdown="block">
- fork [hellogit](https://github.com/pearsonca/hellogit) project
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
##Effective Habits
<aside class="notes" markdown="block">
- commit, commit, commit
- afraid to commit b/c fiddling around, not sure, etc?  branch, and then commit, commit, commit

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

<section markdown="block">
##Organizing with Github
<aside class="notes" markdown="block">
Github offers additional work organization tools:
 - issues - things that need to be done / fixed / etc; can be assigned to individuals
 - milestones - collections of issues

separate from version control aspect, but VC aware.  Can use commit messages to link issue resolution
with particular commit / pull request
</aside>
</section>
