---
layout: section
---
##Summary

The pilot course successful demonstrated that it was both possible and valuable to
deliver software engineering training to undergraduate and soon-to-be graduate
students at the University of Ghana. The pilot, as expected, also identified
several opportunities for improvement in the course content, delivery, and logistical support.

##Personnel

US
: Carl A. B. Pearson, LCDR, Postdoctoral Researcher, Emerging Pathogens Institute, University of Florida
: Dane A. Brown, LT, Professor of the Practice, Electrical and Computer Engineering, US Naval Academy
: Thomas J. Hladish, Postdoctoral Researcher, Emerging Pathogens Institute, University of Florida

Ghana
: Ferdinand Katsriku, Chair of the Dept. of Computer Science, University of Ghana
: Erasmus Achianor, Principle ICT Assistant in Dept. of Computer Science, University of Ghana

##Review of Course

The course ran as a series of sessions alternating between software engineering topics and language overviews.
The days also included warm-up activities, and coached project work.  One session at the end was open for
students to request the topic.

The software engineering topics were:

- A Software Engineer's Tools (included version control, collaboration tools, planning documentation, IDEs, workflow tools)
- Architecture Decisions (desktop vs web-based vs mobile vs cluster, and cross cutting)
- Object Oriented Programming & Test-Driven Design / Development
- Using Existing Code (where to look for existing open source solutions, how to integrate with them)
- Serialization and Client-Server Concerns
- User Interface (covering both graphical & command line / API)
- Parallel Processing & Functional Programming Paradigms
- Security (this was the requested topic)

The language topics were

- Command Line Scripting / Programs (unix / windows command line tools + scripting languages)
- Java / JVM languages (and general discussion of interpreted - virtualized - compiled - machine code spectrum)
- C++ (including discussion of Make, Qt)
- Python (and discussion of other interpreted, dynamic languages like Perl)
- R & Octave (and some mention of other pure numerics, graphing, and analysis languages like SASS, Matlab)
- HTML + Javascript (and JSON, and popular JS frameworks like jQuery)
- GIS

##Outcomes / Lessons Learned

The course slides and exercises produced are openly available indefinitely. The material was presented to
approximately 20 students ("approximately" addressed later), who formed several project groups.
Ultimately, those groups presented their development work on several projects:

- A modification of the classic Snake Game in Java
- A web site for providing information on available transportation routes
- A mobile weather application
- A 3D rendering of a University of Ghana lab space

The student feedback was uniformly passionate about the course, and overall positive.

The students were very positive about the push to be questioning and the push to find the answers
themselves, though they admitted to finding initially very difficult. Faculty at U of Ghana indicated
that most education, even at the post-secondary level, is in the lecture-to-rote-recall mode, rather
than Socratic-inquiry mode.

The students were positive about the exposure to several programming languages, but noted that more
focus would have benefited the project outcomes.

The students noted several challenges with logistics (namely, transportation and housing uncertainty).
These challenges made attendance by full project groups spotty, leading to challenges in accomplishing
group work.

The students were very positive about instructor availability and interaction, as well as the intensive
nature of the course. They found the social events to really encourage interaction outside of class on
course material, not just for fun activities.

From the instructor side, we noted that projects suffered substantially from both overly ambitious scope
and group attendance. Some of the students had very limited programming background; some overcame that
deficiency during the course, but some did not, and that made the engineering topics very difficult for
them to appreciate.

##Summary Conclusions from Feedback & Observations

- Narrow down on languages: while the exposure to several languages was listed as a positive aspect of
the course, it was particularly overwhelming for the students with limited background. Picking a particular
language will allow instructors to focus more on the engineering questions, rather than the programming
questions.
- Pre-screen for projects: students were initially positive about the opportunity to do whatever they
wanted, but were rapidly discouraged by the scope of the challenges. They indicated a preference for
projects that were real (vice toy homework problems), but more bite size and with a well-defined ultimately
deliverable.
- Improve logistical support: The biggest hurdle for many of the students was simply being able to
participate in class, or for their partners to be able to participate in class. We also experienced
difficulties with the software configuration on the machines.

Students are, in general, not ready for direct support of the ONR funder's desired projects as part of
this course, or even for coursework tailored toward that direct support. What they need is to have general
perspective (e.g., how to work as developer, both independently and as part of a team) motivated by a practical,
but introductory project. However, several students were paired with researchers at U. of Ghana after the
course and are undertaking projects this coming academic year.

##Plan for FY14

All of the original personnel are planning to be available for the course in summer 2014.

We are revamping the course material to de-emphasize the wide diversity of languages (though we plan
to keep a session on matching programming to task). We have preliminarily selected Python as the focus
language, as it has a small learning curve, straightforwardly motivates all of the engineering topics, and
is a common language for initial development in scientific and engineering applications.

We are addressing the logistical issues by identifying on-campus housing and funding for students.
We are also going to pre-produce an installation image with all necessary software for the course
pre-configured.

We hope to bring US undergraduates this year. We expect those students to generally have a better
handle on working independently, and to diffuse that trait to the Ghanaian students. We think the US students
will benefit from practical experience with an developing market.

##Specific Session Revisions

We plan to revise the language sessions in the following way:

- Keep Command Line Interfaces session, but change the context to be using Python from the command
line and in conjunction with other command line tools
- Keep the HTML+JS session, but focused on as a frontend to some Python tool
- Keep GIS session, but with a focus on using it in conjunction with Python
- the Java / JVM languages and R / Octave will dropped entirely
- the Python session will expand into 3 sessions: basic syntax, IO, and advanced syntax
- the C/C++ session will be heavily modified to focus on Python to C/C++ bindings
- The tools session will be focused on applying the tools with Python as the language (e.g., PyDev plugin Eclipse)
- Architecture will focus on how Python presents on these various platforms, and how to integrate them via Python
- OOP+TDD will take on a Python-oriented flavor. Specially address how OOP "works" (and sometimes doesn't) with a
dynamic language, and discuss best practices with a unit testing framework (probably PyUnit, possibly
alternative from [this list](https://wiki.python.org/moin/PythonTestingToolsTaxonomy))
- Using existing code will re-orient to focus on the Python standard library (how to use the docs for it, e.g.)
and Python eggs
- Serialization will remain largely the same, but will include Python-specific read-write exercises
for databases (plan for SQLite), flat files both binary and text, and "over-the-wire"
- For user interface, we will have a simple pre-packaged backend process and have exercises to write
front end + glue from the command line, for the desktop, and for some mobile interface (probably in a desktop
simulator, however)
- For parallel processing, the examples will switch to be MPI with Python
