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

Problems with text files

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
Relational databases are built to not have redundant data.  For a university database, the student personal information would be stored in one table.  The primary key of that table would link any and all data in that table to related tables such as Course Schedule or Final Grades.  The student\'s name, for example, would not be repeated in these tables.
  
Why would you NOT want to repeat the same data in multiple tables?

The degree to which databases succeed in preventing redundancy is captured in a set of definition called \"Normal Forms\".  Further discussion is outside the scope of the course.
</section>

<section markdown="block">
For some applications, the database will intentionally have tables with redundant data.  This is called de-normalized data.  

Why might an organization want to do this?

</section>

<section markdown="block">
<p style="text-align:center">Using a database</p>

The software developer will interact with the database via a management tool, a library or for precise work, Structured Query Language (SQL).  

In a language like Python, you write the step by step procedure of what you want the program to do.  These languages are called _procedual languages_. SQL is different.  Typically, you write code or a statement that describes the __result__ you wish to achieve.  Such languages are called _declarative_ languages.
</section>

<section markdown="block">
<p style="text-align:center">Some SQL</p>

{% highlight sql %}
SELECT student_name, phone_number from student_info

UPDATE student_info
SET phone_number='03292524583'
WHERE student_id = 'S00019' 

SELECT student.student_name, schedule.course_number
FROM student_info
INNER JOIN schedule
ON student.student_id = schedule.student_id
ORDER BY student.student_name

{% endhighlight %}
<br />
SQL is a rich language and has been in use for over 40 years.  Learning SQL is a seperate course from Python.

</section>

<section markdown="block">
<p style="text-align:center">Advantages of using an RDBMS</p>

* Scalability
* Distributed (multiple users can access over network)
* Reduced redundancy of data
* Backup and recovery
* Transactions (logging of who made what changes when)
* Fine-grained security
* Can represent complex structures
* Complex queries/reports possible.

</section>

<section markdown="block">
<p style="text-align:center">Python and DB</p>
  
The Python Database API (DB-API) defines a standard interface for Python database access modules. It’s documented in PEP 249.  Most modern databases support PEP 249.
</section>

<section markdown="block">
<p style="text-align:center">Example using MySQL</p>

{% highlight python %}

#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    for row in rows:
        print row

con.close()

{% endhighlight %}

</section>

<section markdown="block">
<p style="text-align:center">Questions?????</p>
</section>


