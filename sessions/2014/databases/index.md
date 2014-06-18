---
layout: presentation
year: 2014
title: Databases
instructors:
 - Jonathon
---
<section markdown="block">
<p >Database:</p>
An organized collection of related data.  

A database could be a collection of alphabetized paper files.
</section>

<section markdown="block">
An electronic database uses software to store data in an organized way.  

The software allows the user to update, view and search data.
</section>

<section markdown="block">
<p style="text-align:center">Why not just store the database your program needs in a text file?</p>
</section>

<section markdown="block">

* Speed when database (file) becomes large.
* Only one user can update file at a time.
* Only simple data structures can be (easily) implemented.
* Hard to share data.
* Every access function must be written by hand.

</section>

<section markdown="block">
Database software solves all these problems and solves problems that do not arise until the database becomes large. 

</section>

<section markdown="block">
There are many different kinds of software systems that call themselves databases.  For the purpose of this lecture, I will limit the material to _relational_ databases.
</section>

<section markdown="block">
<p style="text-align:center">Relational Databases use Tables to Store Data</p>
  

| Course Name        | Course Number          | Dept | Credits  |
| :-------------|:-------------:|-----:|-----:|
| Intro to Python | CAP101 | CS | 3 |
| Stat Methods I  | STA511 | MA | 3 |
| Intro to Algorithms | COT401 | CS | 3 |

<br/>
A conceptual relational database table is shown above.  

Each row in a database represents a unique record in the table.  Each column in a row is called a field.  Each field can hold different types of data.

The rows of a database table are different from each other. Rows are uniquely identified by a value called a _primary key_.  In this example, the Course Number is the primary key.

</section>

<section markdown="block">
A relational database typically consists of multiple tables.  The tables are related by identical column values. The primary key of one table can be listed in the column of another table.  When this occurs, this value is called a _foreign key_.  Use of a foreign key allows the linking of tables together.
</section>

<section markdown="block">

| Course Name        | Course Number          | Dept | Credits  |
| :-------------|:-------------:|-----:|-----:|
| Intro to Python | CAP101 | CS | 3 |
| Stat Methods I  | STA511 | MA | 3 |
| Intro to Algorithms | COT401 | CS | 3 |

<br/>

| StudentID        | Term |  Course Number |
| :---------|:-----:|-------:|
| S0011 | F13 | CAP101 |
| S0012 | F13 | STA511 |
| S0099 | F13 | COT401 |

<br/>

In this case the Course Number is a foreign key in the student schedule table.

</section>

<section markdown="block">
In the previous example, the keys are human-readable strings.  In modern Relational DataBase Management Systems (RDBMS), keys are auto-generated.  

Would you want to create by hand a set of unique identifiers for a million row table?
</section>

<section markdown="block">
<p style="text-align:center"></p>
Relational databases are built to not have redundant data.  For a university database, the student personal information would be stored in one table.  The primary key of that table would link any and all data in that table to related tables such as Course Schedule or Final Grades.  The student\'s name, for example, would not be repeated.
  
Why would you NOT want to repeat the same data in multiple tables?

The degree to which databases succeed in preventing redundancy is captured in a set of definition called \"Normal Forms\".  Further discussion is outside the scope of the course.
</section>

<section markdown="block">
<p style="text-align:center"></p>
</section>

<section markdown="block">
<p style="text-align:center"></p>
</section>

<section markdown="block">
<p style="text-align:center"></p>
</section>

<section markdown="block">
<p style="text-align:center"></p>
</section>

<section markdown="block">
<p style="text-align:center"></p>
</section>

<section markdown="block">
<p style="text-align:center"></p>
</section>




