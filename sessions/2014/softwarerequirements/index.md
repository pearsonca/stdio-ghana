---
layout: presentation
year: 2014
title: Software Requirements
---

<section markdown="block">
###Software Requirements
  <h5>Prerequisites: Basic Python Programming</h5>
  <dt>Jonathon Parker</dt><dd>Employed at iBASEt</dd>
  <dt>Carl Pearson</dt><dd>Postdoctoral Researcher, UF</dd>
</section>

<section markdown="block">
Why Requirements?

Unless you are purely a hobbyist or a student, software projects are undertaken because an organization
needs the software to increase productivity of workers or to perform a task that cannot be done
economically by a human worker.

The software engineering team must understand what the customer wants out of the software, so that they
know what to build.
</section>

<section data-background="requirements_toon.jpg" data-background-width="513px" data-background-height="594px" markdown="block">

</section>

<section markdown="block">
Motivational Quotation #1

> The hardest part of building a software system is deciding precisely what to build.  No other part
> of the conceptual work is so difficult as establishing the detailed technical requirements... No
> other part of the work so cripples the resulting system if done wrong.  No other part is more difficult
> to rectify later.
</section>

<section markdown="block">
Motivational Quotation #2

> Therefore the most important function that software builders do for their clients is the iterative
> extraction and refinement of the product requirements.  For the truth is, the clients do not know what
> they want.  They usually do not know what questions must be answered, and they almost never have thought
> of the problem in the detail that must be specified.&quot;
>
> Brooks, Fred P. (1986). "No Silver Bullet - Essence and Accident in Software Engineering."
> Proceedings of the IFIP Tenth World Computing Conference: 1069-1076.
</section>

<section markdown="block">
What is a Software Requirement?

A condition or capability needed by a customer to solve a problem or achieve an objective, or
needed to satisfy a contract or other formal document.
</section>

<section markdown="block">
Two types of software requirements:

Functional requirement - What the customer wants the software to do.

Nonfunctional requirement - Places constraints on how the software meets requirements.
</section>

<section markdown="block">
Important Aside

Study of the issues surrounding software requirements could be the content of a semester long course,
a dissertation, or a book.  

There are many different software development <b><i>methodologies</i></b>, with proponents of particular
methods (often) bitterly disagreeing with each other on the subject.  

Each software development methodology has its own style of handling software requirements.
</section>

<section markdown="block">
Thus, I cannot cover them all in one lesson.

I can, however, briefly give you my opinion on the subject of methodologies. They are situationally dependent.
For certain projects, methodology A can have great success, for other projects the best choice might
be methodology B.  Some methodologies that would be ideal cannot be implemented due to external factors,
such as contracts.
</section>

<section markdown="block">
So, it is good to read up on or experience many from the following list:

- Waterfall
- Prototype model
- Iterative
- Spiral
- Scrum
- RUP
- XP
- Agile
- TDD
- FDD
</section>

<section markdown="block">
Another important definition!

Use Case: A description of important interactions between an actor (usually a person) and the software system.  These interactions must yield a result of value to the actor.  Sometimes diagrams are used to illustrate a use case, but these are rarely sufficient.

Use cases are a primary means of discovering requirements.
</section>

<section markdown="block">
Here is a brief overview of the formal style used commonly in software engineering literature.
</section>

<section markdown="block">
Software Requirements can be broken into 5 Phases

1. Elicitation
2. Analysis
3. Specification
4. Validation
5. Management
</section>

<section markdown="block">
Elicitation: Uncovering customer needs and wants and nonfunctional requirements.
 
Multiple sources of information can be used.
- Stakeholders (May have different needs and you need to meet them all)
- Goals (How do the stakeholders see the software benefiting the organization?  Uncover nonfunctional
requirements)
- Domain Knowledge (How is business done in this industry?)
- Operation and organizational environment (Consistency)
</section>

<section markdown="block">
Multiple techniques can be used:
- Interviews - 1v1
- Facilitated meetings - groups
- Observation - of how proposed users currently perform tasks to be handled by the software
- Scenarios - Software developers describing sets of use cases to the customer.  This can
identify misperceptions early on and uncover new requirements.
</section>

<section markdown="block">
All of these techniques require skill and experience.  This is a different skill set from writing functioning code!
</section>

<section markdown="block">
Analysis.  In this phase, the requirements are studied to see if a system can be built from them.
Common flaws include:
- Contradictions
- Incomplete
- Vague
- Obviously wrong.
</section>

<section markdown="block">
Specification.  Formal capture of the requirements into a properly formatted document.  Requirements must be:
- Specific - clear, concise and exclusive
- Correct - must accurately describe the system function
- Complete - must describe everything about the system
- Consistent - non-contradictory or not-exclusive of other requirements
- Attainable - possible for software to meet this goal
- Verifiable - can we test that the requirement has been met?
</section>

<section markdown="block">
Validation. 

The stakeholders agree that the requirement meet their needs.

This is typically accomplished by the customer reading and agreeing to the specification.
</section>

<section markdown="block">
Management.  

A successful project will have subject matter experts on the entire set of requirements.

The development team must ensure all requirements are completed and tested.
</section>

<section markdown="block">
One final note:

Requirements can change (!) during a project.  When changes to requirements occur, this can
necessitate changes to other requirements and code already written.  This adds to development time.
It is critical that this additional time is accurately estimated.
</section>

<section markdown="block">
Exercise:

The class is broken up into teams, each of which is competing for a software development project.  
Each instructor is a stakeholder and can be interviewed for 10 minutes.  
(This requires that each instructor will need to role-play and have different goals and priorities)
Follow up questions may be asked at a roundtable discussion by all teams (round-robin).  
The team that best describes the system wins the contract.
</section>
