---
layout: presentation
year: 2014
---
<section markdown="block">
###Software Engineering Best Practices
<h5>Prerequisites: OOP, Testing, Debugging</h5>
<dt>Jonathon Parker</dt><dd>Employed at iBASEt</dd>
<dt>Somebody</dt><dd>Some university</dd>
</section>

<section markdown="block">
What are \"Best Practices\"?

Approaches and techniques that reduce development time, improve quality and simplify maintenance.

\"Best Practices\" could be the sole subject of a two week course!  The content in this lesson will focus on practices that simplify maintenance, though others will be discussed.
</section>

<section markdown="block">

Why Maintenance?

The majority of the software lifecycle is spent in maintenance.  More time is spent correcting defects and adding features after the software is delivered than in its initial development.  Additionally, the same practices that simplify maintenance also support correcting defects in software during its initial development.
</section>
<section markdown="block">
To this end, consider these practices:
</section>
<section markdown="block">
<h5>Coding Conventions</h5>

A coding convention is a set of rules for writing and organizing code.  Following the set of
rules will not guarantee good quality code.  The purpose of a coding convention is to communicate
intent between developers.  The actual convention used is not important; what is important is
that it is adhered to.
</section>

<section markdown="block">
You can have conventions for:

* Comments
* Indent style
* Naming
* Programming practices

I will not cover all of these today.  I would like to cover Common Naming Conventions.

</section>

<section markdown="block">
* UpperCamelCase (often used for classes)
* lowerCamelCase (often used for class methods and variables)
* CAPITAL_UNDERSCORE (often used for constants)
* pot_hole_case (often used for variables and functions)
* Single characters are often used for short temporary variables such as indexes.  The characters
i, j, k are often used as integers; c, d, e are often used as characters; s is often used as a string.
</section>

<section>
Show some code here that is properly formatted
</section>

<section markdown="block">
<h5>Engineering Practices</h5>
There are legions of them.  Here are a few...
</section>

<section markdown="block">
Don`t Repeat Yourself (DRY) - Any series of steps that are performed multiple times should be put
into a programming construct such a loop, function or class.  That ensures the series of steps is
performed the same way every time.
</section>

<section markdown="block">
You aren`t going to need it (YAGNI) - Do not implement functionality until you need it.  The danger
is if you don`t use it, the unused function may have a defect or maintenance changes elsewhere will
introduce a defect.  A maintenance programmer may see the previously unused function, believe it works
and try to use it.
</section>

<section markdown="block">
Don`t Make Me Think - Any code written should be easy to read and understood with the minimum
effort required.  This concept is related to:

Do The Simplest Thing That Could Possibly Work - Avoid unnecessary complexity.
</section>

<section markdown="block">
Single Responsibility Principle - A component of code (class or function) should perform a single well defined task.  Code with unexpected side-effects can be overlooked by the maintenance programmer.
</section>

<section markdown="block">
Minimize Coupling - Coupling is when a section of code depends on another section of code.  Coupling is an advanced topic and there are many types.  One dangerous type is \"content coupling\". In content coupling, changes to data values in one section of code can directly effect the behavior of another section of code.
</section>

<section markdown="block">

About common sense, YAGNI contraversy.

Sometimes you do need to repeat yourself.

</section>

<section markdown="block">
<h5>For Object Oriented Programming</h5>
</section>

<section markdown="block">
Open/Closed Principle - Make sure objects you create are open for extension, but closed for
modification.  Why is this important?  Keeping objects open for extension allows reuse of code
that meets your or another programmer`s needs with addition of features.  Keeping objects
closed for modifications prevents changes that could break use of that object elsewhere in the code.
</section>

<section markdown="block">
Hide implementation details - Behind object methods and instantiation so that they are unaffected
by changes elsewhere and vice versa.
</section>

<section markdown="block">
Law of Demeter - Put simply, an object can only communicate with classes it inherits from, objects
it contains, and objects passed by argument to a method.
</section>

<section markdown="block">
<h5>Additional Practices</h5>
</section>

<section markdown="block">
Refactor often - Refactoring is reorganizing your code to ensure the above principles are adhered
to.  As a side benefit, it can also expose defects in the coding.  Remember to update your comments too!
</section>

<section markdown="block">
Tools - Pick a small set of software engineering tools and learn them well.
</section>

<section markdown="block">
Code defensively - Think about what can go wrong and apply good practices appropriately.
</section>

<section markdown="block">
Assignment.  This code module is poorly designed.  Identify all design flaws.  Explain what problems the
flaws can cause.  Modify the code to repair the flaws.  Defend your modifications.
</section>


