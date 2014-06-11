---
layout: presentation
year: 2014
title: Testing
instructors:
 - Carl
 - Jonathon
---
<section markdown="block">
###How Do You Test Code?

<aside class="notes">
QA: what they think testing means in software.  How does that relate to
testing in other contexts?
</aside>
</section>

<section>
<section markdown="block">
###Why Test?

<aside class="notes">
fundamentally not about proving software works: but rather finding that it
doesn't work for conditions people care about.
</aside>
</section>

<section markdown="block">
###Compare:

- debugging
- static analysis
- testing
- compiler / interpreter errors
- runtime error handling (`try/catch` blocks)

<aside class="notes" markdown="block">
- automated: interpreter driven, only about syntax,
not about *universe* program represents
- testing: expressing program *universe*, check for satisfying its rules,
also a way to communicate with other developers
- debugging: about finding out what's breaking where when you know something is wrong
</aside>
</section>

</section>

<section markdown="block">
###Standard Library Unit Testing
[unittest](https://docs.python.org/3.4/library/unittest.html)
and [unittest.mock](https://docs.python.org/3.4/library/unittest.mock.html)

###External Library / Tool
[py.test](http://pytest.org/latest/)

<aside class="notes" markdown="block">

[exercise using those](sessions/2014/testing/exercises.html)

</aside>
</section>

<section markdown="block">
##Testing: When? How?

- pre/during development
- debugging
- automating

<aside class="notes" markdown="block">
- during development: figuring out what to make, how to make it in small steps
- during development: making sure everyone is on the same page
- during debugging: describe what the problem actually is
- long term value: future changes can be validated as not breaking established
code
- getting the right amount: testing is about being confident in results;
impossible to be perfectly confident, need to figure out right level of concern,
how to mitigate it via right amount of testing
</aside>

</section>

<section markdown="block">
##Other Testing

- design-by-contract
- performance
- error handling
- stochastic
- pen-and-paper

<aside class="notes" markdown="block">
- design-by-contract: leverage static analysis / options for dynamic analysis
- performance: big-O estimation, confirming algorithm satisfies that
- performance: finding hottest spots + replacing them (rather than write
	the whole thing in `C`)
- error handling: expected errors (e.g., IO) versus usage errors (wrong arguments)
also useful when fixing problems, communicating with other developers by having
useful crash messages rather than basically random junk
- stochastic: for simulations, verifying expected distributions
- pen-and-paper: write down what you expect to observe, try the software
why write it down? forces you to commit your expectations
</aside>

</section>

<section markdown="block">
##Interesting Resources

- [PythonTesting.net](http://pythontesting.net/)

</section>
