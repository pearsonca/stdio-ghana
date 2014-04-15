---
layout: presentation
year: 2014
---
<section>
	<h3>Software Engineering Best Practices</h3>
	<h5>Prerequisites: OOP, Testing, Debugging</h5>
	<dt>Jonathon Parker</dt><dd>Employed at iBASEt</dd>
	<dt>Tom Hladish</dt><dd>Postdoctoral Researcher, UF</dd>
</section>
<section>
A new software project that is unconstrained or only lightly constrained by existing structures
is an optimal situation to be in as an engineer.  The project may be delivered to the customer
on time and accepted, but subsequent defects will be found and additional features will be identified.
This phase is called the maintenance phase, and if the project is successful, this will be where the
majority of the development time occurs.
</section>
<section>
Many of these best practices are focused on the maintenance for a software project.  If done correctly,
it will improve reliability of the software when it is in maintenance and reduce the amount of time
to maintain the project.
</section>
<section>
Many of these best practices partially overlap and support each other.
These best practices also aid original design and debugging.
</section>
<section>
Write code for the maintainer!  It is difficult to go back and look at code you wrote a year ago,
think about how difficult it is to look at code someone else wrote.  You want to make the
maintenance programmer’s job as easy as possible.  To this end, consider these practices:
</section>
<section>
<h5>Coding Conventions</h5>

A coding convention is a set of rules for writing and organizing code.  Following the set of
rules will not guarantee good quality code.  The purpose of a coding convention is to communicate
intent between developers.  The actual convention used is not important; what is important is
that it is adhered to.
</section>

<section markdown="block">
You can have conventions for:

* Comments
* Indent style (not applicable to Python)
* Naming
* Programming practices

I will not cover all of these today.  I would like to cover Common Naming Conventions.  

</section>

<section markdown="block">
* UpperCamelCase (often used for classes)
* lowerCamelCase (often used for class methods and variables)
* CAPITAL_UNDERSCORE (often used for constants)
* Single characters are often used for short temporary variables such as indexes.  The characters
i, j, k are often used as integers; c, d, e are often used as characters; s is often used as a string.
</section>

<section>
<h5>Engineering Practices</h5>
</section>

<section>
Don’t Make Me Think – Any code written should be easy to read and understood with the minimum
effort required.  This is also relevant to GUI design.
</section>

<section>
Do the simplest thing that could possibly work – Avoid unnecessary complexity.  This supports “Don’t Make Me Think”.
</section>

<section>
Abstraction Principle – Each significant piece of functionality in the program should be
implemented in just one place in the source code.  
</section>

<section>
Single Responsibility Principle – A component of code (class or function) should perform a single well defined task.
</section>

<section>
Don’t Repeat Yourself (DRY) – Any series of steps that are performed multiple times should be put
into a programming construct such a loop, function or class.  That ensures the series of steps is
performed the same way every time. This is related to the Abstraction Principle (mentioned earlier)
</section>

<section>
You aren’t going to need it (YAGNI) – Do not implement functionality until you need it.  The danger
is if you don’t use it, the unused function may have a defect or maintenance changes elsewhere will
introduce a defect.  A maintenance programmer may see the previously unused function, believe it works
and try to use it.
</section>

<section>
Minimize Coupling: Coupling is when a section of code depends on another section of code.  This most
often happens when a variable is set with a value used much later on.  The danger is that a
maintenance programmer might move a section of code outside its scope, which will break the code, or
to a location within scope where the dependent variables have been set with inappropriate values.
</section>

<section>
Reuse:  Search built-in functions and libraries before implementing your own functions.
</section>

<section>
<h5>For Object Oriented Programming</h5>
</section>

<section>
Open/Closed Principle – Make sure objects you create are open for extension, but closed for
modification.  Why is this important?  Keeping objects open for extension allows reuse of code
that meets your or another programmer’s needs with addition of features.  Keeping objects
closed for modifications prevents changes that could break use of that object elsewhere in the code.
</section>

<section>
Hide implementation details – Behind object methods and instantiation so that they are unaffected
by changes elsewhere and vice versa.
</section>

<section>
Law of Demeter – Put simply, an object can only communicate with classes it inherits from, objects
it contains, and objects passed by argument to a method.
</section>

<section>
<h5>Additional Practices</h5>
</section>

<section>
Refactor often – Refactoring is reorganizing your code to ensure the above principles are adhered
to.  As a side benefit, it can also expose defects in the coding.  Remember to update your comments too!
</section>

<section>
Tools - Pick a small set of software engineering tools and learn them well.
</section>

<section>
Code defensively - Think about what can go wrong and apply good practices appropriately.
</section>

<section>
Assignment.  This code module is poorly designed.  Identify all design flaws.  Explain what problems the
flaws can cause.  Modify the code to repair the flaws.  Defend your modifications.
</section>
