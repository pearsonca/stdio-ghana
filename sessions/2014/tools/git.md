---
layout: presentation
title: git
---
<section markdown="block">
##What do you work on?

<aside class="notes" markdown="block">
Q&A (1-2ish min per person, up to 10ish minutes - for people not inclined to answer, no-opt out with \"give 1 example, say one good thing about it, one bad thing\")

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

- print the work, have them comment on it manually
- email the file / files back and forth
- shared drive / cloud sharing solution
- saving multiple versions with modified file names, like XYZ\_MMDDYY\_FML.txt

Expected Pros/Cons

- pro: expediency, obvious artefact (piece of paper, specific email)
- con: no log of what people said, lots of duplicate work, possible to misplace / mix up artefacts

</aside>
</section>

<section markdown="block">
##Version Control
<aside class="notes" markdown="block">
Q&A: show of hands on who has heard of version control + some specific tools: cvs, svn/subversion, git, mercurial

Argument: VC addresses those problems by establishing a formal language for working with people
(including future / past snapshots of yourself).  Pros of formal language: powerful shorthand for common tasks, possible to build tools on top of that expression; cons: have to learn it, plenty of crappy implementations, and can get complicated for not-so common tasks

Any version control tool you are likely to see searching for one provides few basic notions:

- what is the reference \"thing\"
- what is the current version of that thing
- what is the history leading up to the current thing
- who did what during that history

`git` provides one additional twist, **alternative versions**, and then tools to use them.  The are some other
implementation advantages, but that's all under the hood.

</aside>
</section>

<section markdown="block">
##Serial Git

<aside class="notes" markdown="block">
Go over the notion of a linear version control.  Point is to have people do \"series\" work, from multiple locations.
Show that series work can still have \"parallel\" issues creep in.

Steps:

- fork [hellogit](https://github.com/pearsonca/hellogit) project
- have people make some series of changes, locally and remotely
- first local changes, then commit + push
- then remote changes (via web interface) and commit (with insta-push)
- then local changes (pre pull) and show conflicts resolution
- have people share commit access, do some changes to the same thing at the same time, show collisions

</aside>
</section>

<section markdown="block">
##Parallel Git

<aside class="notes" markdown="block">
The problems are typical to doing actual work, and are really a byproduct of the typical series / parallel
problem.  Activity is to highlight how `git` address parallel \"problem\": branches.

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
