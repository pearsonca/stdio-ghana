---
layout: presentation
title: Software Engineering Reuse
year: 2014
---
<section markdown="block">
<h3 style="text-align:center">Software Engineering Reuse</h3>
<h5 style="text-align:center">Prerequisites: Object Oriented Programming</h5>
<dt>Jonathon Parker</dt><dd>Employed at iBASEt</dd>
<dt>Dane Brown</dt><dd>Professor of Practice, USNA</dd>
</section>

<section markdown="block">
#####Why Reuse?

When you sit down to write a module of code, there is a very strong probability that you are NOT the first person in the world to need that module.  In most of these cases, the functionality you need has already been written and available for you to use.  This saves you time and the module usually has been rigorously tested for errors.
{: .fragment}

</section>

<section markdown="block">
<h5 style="text-align:center">Types of Reuse</h5>
Libraries - The programming language authors or a third party has built the functionality into the language or a module of code you can reference.

Code Reuse - A module of code written by you or a member on your team can be reused with little or no modification to solve a new problem.

Pattern Reuse - The type of problem you are trying to solve has been solved before.  The strategy used to solve it can be reused and implemented in any programming language.
</section>

<section markdown="block">
The phrase that comes to mind for this situation is:  

<h5 style="text-align:center">DON`T REINVENT THE WHEEL!</h5>
</section>

<section markdown="block">
<h5 style="text-align:center">Libraries</h5>
  
Python Standard Library - This library comes with every release of Python.  There are so many modules we could spend a full 2 weeks getting familiar with them.  A non-exhaustive list includes packages for:
  
 * Strings
 * Data types
 * Mathematics
 * Operating System interaction
 * File System interaction
 * Data Archiving and Persistence
 * Communications (especially Internet protocols)
 * And much, much more!	
</section>

<section markdown="block">
Example:  You need to calculate absolute values of numbers in your code module.  Should you write a function to do that from scratch?  Are you the first software engineer to need an absolute value? Of course not!  This functionality exists in the appropriately titled \"math\" package.

The math module documentation provides the following information:

~~~
math.fabs(x)
Return the absolute value of x.
~~~

Which you access by importing the module by typing the important statement in the header of your Python script
and later in your code call fabs(x) with:

~~~
import math
...  
y = math.fabs(x)
~~~
</section>

<section markdown="block">
Python Package Index (PyPI) - While the Python Standard Library is rich, it does not include every possible need.  Generous individuals, groups and institutions have created and made public packages of modules designed to work with Python.  There are more than 40,000 Python packages in PyPI!  There are additional Python packages that are not included in PyPI.  We will not cover all of these today.

Before you write a module of code, I recommend you browse PyPI
https://pypi.python.org/pypi?:action=browse and search the internet for pre-existing implementations.
</section>

<section markdown="block">
In order to download and install other modules or packages, you need to install the \"pip\" program. Instructions on the website walk you through it.

Picking a good package is a challenge.  You may have many to choose from and their quality and features will vary.  Do research and test before you commit to develop code with a particular package.
</section>

<section markdown="block">
About Frameworks: Some packages you see in pip are \"Frameworks\".  A framework is different than a typical package.

<center>What is a Framework?</center><br/>
A framework is a package with a set of functions for a particular task.  A framework hides low level details of the functions which typically speeds development time and improves readability.  We will not explore Frameworks further in this course.

The best known Framework for Python is called Django.  It is used to create web applications.
</section>

<section markdown="block">
<h5 style="text-align:center">Code Reuse</h5>
You or someone in your organization wrote code in the past that is applicable to a current requirement.
So it is an easy task to reuse this code, right?
</section>

<section markdown="block">
<p style="text-align:center;">WRONG!</p>
</section>

<section markdown="block">
Code reuse is a very challenging proposition for organizations.  Why?  The basic concept is that code is written to solve a particular set of problems under a deadline.  Code reuse runs into the following types of challenges.
</section>

<section markdown="block">
a. Organization. A package intended for reuse must be fully featured and meet more than the narrow needs of the original authors.  This requires planning and strong support from the organization`s leadership.
</section>

<section markdown="block">
b. Economics.  A code reuse strategy requires additional work.  The time and funding to package code for reuse may not be available.
</section>

<section markdown="block">
c. Administration.  Code to be reused must be available in a central location, maintained, documented and its existence communicated to the entire organization.
</section>

<section markdown="block">
d. Politics.  Some organizations have hostile internal politics and use of code written by other work
groups might be resisted due to a loss of prestige or perceived loss of control of a project.
</section>

<section markdown="block">
e. Psychology.  For a variety of reasons, individual developers may resent using key components for their project that they did not write.
</section>

<section markdown="block">
<h5 style="text-align:center">Quick exercise.</h5>

* Break into groups of 4-5
* Discuss where these challenges might manifest themselves in an academic environment.
* Each group will present one such manifestation to the class.
* You have 10 minutes.
</section>

<section markdown="block">
If your organization has the leadership to overcome these issues, great!  You are very lucky and your
development will be eased.  Because code reuse is a difficult proposition, this rarely happens.

Thus code is typically reused in an ad hoc fashion, obtained from developers in your local work group. So before you code, ask around.  In this case, the source is typically copied to the new project and modified and retested.
</section>

<section markdown="block">
Design Patterns:  The purpose of software is to solve problems!  If code you need to solve a problem has been written before, surely the problem has been solved before.  Or at least some of the problem.
</section>

<section markdown="block">
<h5 style="text-align:center">What is a Design Pattern?</h5>
* A general solution to a problem.  
* Can be implemented in (almost) any language.  
<br />
The original and famous Design Patterns book (Design Patterns: Elements of Reusable Object-Oriented Software) contained 23 patterns, with additional ones identified since.  I will briefly cover 2 example patterns today.
</section>

<section markdown="block">
<center>The Factory Pattern</center><br/>
The factory pattern creates objects that inherit from an abstract class.  The actual subclass is not
decided until runtime.  As long as the subclasses implement the required interface(s), they can be handled
identically by the rest of the program while retaining the characteristics of the subclass.

Example: An audio editing program that needs to handle different audio formats with the same set of functions.
So regardless of the audio type (.au, .wav, .mp3, etc.), you can get a generic audio object that can be
handled by the program in the same way.
</section>

<section markdown="block">
<center>The Strategy Pattern</center><br/>
The strategy pattern allows the behavior of an function to be changeable at runtime.  This is done by defining a common interface that a family of functions implements.  As the state of the program or an object changes, its function implementation can be changed appropriately.

Example: Scientific application that processes different types of datasets.  The manner in which the distance between individual data examples is measured is different depending on the dataset.  A family of distance(example_a, example_b) functions can be defined and the appropriate one chosen when the type of dataset is determined.
</section>

<section markdown="block">

Exercise 1: Write a script to calculate the weekly pay for employees.  Where appropriate, use applicable Python library modules.

Program should print out \"employee name: pay\" for each Employee

The pay scale depends on number of years of service:

0 to <2 = 500  
4 to <8 = 1000  
8 to <12 = 1100  
12+   = 1200  

you may assume 365 days = 1 year
</section>

<section markdown="block">

Some code to get you started.  It might need modification as you discover useful library modules:

~~~
class Employee():
    def __init__(self, name, start_date):
        self.name = name
	self.start_date = start_date


Andrew = Employee("Andrew", "2012/08/01")
Barbara = Employee("Barbara", "2004/01/19")
Clare = Employee("Clare", "2007/11/30")
Daniel = Employee("Daniel", "2001/05/23")
Edith = Employee("Edith", "2010/07/04")
~~~
</section>

<section markdown="block">
Exercise 2: You are planning a large software system to be written in Python.  The system will monitor Twitter for tweets that mention particular types of activty.  These are environmental changes, damage or pollution.  The system will plot the location of the activity on Google Maps.

Search PyPi for at least three useful packages that might assist you.

<span style="opacity:0.0">python-twitter1.3.1, nltk, pykml 0.1.0</span>

</section>


