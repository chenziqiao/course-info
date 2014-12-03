# Lecture Notes for CIS 355 Fall 2015

These are the notes on what I think is most important to know from the lectures 
and demonstrations we had this semester. If you think something here is missing
or wrong, please let me know! I will prepare a much better edited version of
these notes for the coming Spring semester. Thanks for serving as "beta testers"
for CIS 355, and helping me discover how to teach it.

## Material from first half of semester

The final exam mostly covers the second half of the semester, which did not draw
on the Kimball book very much.  However, I may still ask a few questions about
dimensional modeling and star schemas.  Review my slide decks on those topics,
including the midterm review slides.  You may be required to sketch a simple 
star schema, or interpret ones that I have provided.

The rest of these notes pertain to the topics we explored after the midterm.


## Notes on Cloud Computing

The "cloud" that we're interested in is IaaS or PaaS (infrastructure, or
platform, "as a service").  "As a service" means you pay for usage, per hour,
per processor, or per gigabyte (or some other measure).  This has the advantage
of turning a "fixed cost" (buying and setting up servers) into a "variable cost"
so you don't need a lot of money to start a project or a business.

The line between IaaS and PaaS is not very distinct.  In theory, IaaS means 
you're getting just the servers, and setting them up yourself, and PaaS means
some software (like a database server) is pre-loaded.

It's important to know that we're NOT talking about SaaS (software as a service)
here.  That refers to online applications, like TurboTax or Dropbox, which are
3rd-party software that you access through the Internet instead of downloading.
IaaS and PaaS are platforms upon which you build your own systems.

Cloud services like Amazon Web Services (AWS) and Microsoft Azure make economic
sense because different companies use computing resources at different times. A
company like Amazon has to buy a lot of servers to handle the holiday rush, but
they are probably under-used for the rest of the year.  So Amazon started 
"renting out" their servers, processors, and hard drives as IaaS/PaaS.  If
their customers have heavy workloads at different times of day or year, they
use the resources more efficiently than if everyone bought their own equipment.

Storing data in the cloud means splitting it across multiple servers.  This 
could mean one of the following:
- **Sharding**: Different parts of the data set are on different servers.  The
database may be partitioned into equally-sized shards, or logically organized
by some meaningful criterion such as date or region.
- **Replication**: The same data may be stored in more than one place.  Any of
the distributed servers could handle any query on its own.
- **Sharding *and* Replication**: The data may be partitioned to get it into 
manageable chunks, and those chunks may themselves the replicated for 
availability or redundancy.

You should know about the **CAP Theorem**.  In a nutshell, it is claimed that
no distributed system can achieve all three of the following: Consistency,
Availability, and Partition-tolerance.  Since a sharded or replicated
database is by definition "partition-tolerant", this really means you face a
trade-off of consistency (the ability to be certain that the data you get out
of the system is correct) and availability (the ability to get a query 
answered immediately).

Think about it this way: if I withdraw money from an ATM, the ATM is updating
one node of the bank's database with my new account balance.  If my wife is 
checking our balance and hits a different node, and that node doesn't yet know
about my update, it can do one of two things:
- Check with all the other nodes to make sure it has the absolute freshest data,
or
- Immediately respond with the latest balance information it knows about, which
will not include my withdrawal.

The first option will guarantee an accurate response to my wife's query, but may
take a lot of time.  That's a choice of consistency over availability.  The 
second option will give her a much faster response, but the data will be
inaccurate (at least sometimes).  A bank would probably choose consistency, but 
other applications (like websites) may favor availability.

There's no way to avoid this trade-off, but it doesn't have to be all of one or
all of the other.  You could place yourself somewhere in the middle.  For 
example, your distributed database might not check with *all* other nodes for
fresh data, but just some of them.

 

## Data Formats + Scripting Languages -- 11/3

#### Data formats -- CSV, XML, JSON

Relational databases (and nonrelational ones) are great for storing data. But
this data isn't easily transferred between systems because its actual format
on disk is proprietary and opaque.  We talked in this lecture about three
formats for *data interchange* that you should know:
- CSV (comma-separated values)
- XML (extensible markup language)
- JSON (javascript object notation)

All of these use plain text files, so you can open them in any text editor,
whether it be Notepad++, Vim, Emacs, Sublime Text, or some other.

CSV is just what it sounds like: rows of data with commas separating the columns.
This is a fine way to send tabular data with defined rows and columns, like the
data from a single relational table.  If you wanted to send more than one table,
you'd need to send more than one CSV file, and the files could get huge if there
were lots of "optional" columns that are mostly empty.  

XML is generalized from HTML and it allows you to describe the data in an 
object-oriented way with nested structures.  It is meant to be self-documenting,
so you could send a complex data structure with sub-structures and your recipient
would be able to interpret it.  It's a little wordy, though, and although it's
easy enough for humans to understand, it's not trivial to write a computer
program to decode it.

The relatively new fashion in data interchange is JSON.  Like XML, it allows you
to specify objects with nested lists and sub-objects, so you can transmit 
complex data.  But since it simply uses the internal notation of the programming
language JavaScript, most languages can interpret it with a bit of trivially
simple coding.  It is less human-friendly than XML, but most programmers prefer
its efficiency.

You don't need to be fluent in these formats, but you should be able to recognize
them and tell them apart.

#### Scripting Languages

Scripting languages are often described as the "glue" of big data.  When you are
connecting many parts of a data pipeline, including loading data from source
systems via an API, transforming it into a different format, loading it into a
database, and preparing an application front-end for users, some programming is 
helpful.

Scripting languages like Python, Perl, Ruby, R, and others, are programming 
languages with very little overhead compared to what you might call production
class compiled languages like C# and Java.  In a scripting language, you often 
just write one or two lines of code and you can run it as-is.  They may not have 
the performance of compiled languages, but are very efficient for automating
simple tasks.


## NoSQL Databases -- Martin Fowler video

There were a lot of good points made in the Martin Fowler video on NoSQL databases
and it might be worth watching again.  The link is here: http://youtu.be/qI_g07C_Q5I

Some key points:

- There are several benefits of SQL-based relational databases, among them:
    - They manage concurrency (i.e. many users can access a relational database 
      at the same time) through transactions.
    - SQL has become an industry-wide standard language for accessing data.
    - They have become important for data *integration*.
    - They have become important for *reporting*.
- One big problem with relational databases is the "impedance mismatch" problem
  where a logical entity or practical concept must be split up into many 
  different tables in order to save it to the database. (2:00-2:40 in the video)
- There's no perfect definition of NoSQL.  The term actually started as a hashtag
  for a meetup.  But NoSQL databases tend to have the following common features:
    - non-relational:  they don't use the metaphors of tables and rows
    - cluster-friendly:  designed to be distributed across multiple computers
    - open-source
    - 21st century web-era origins:  i.e., other non-relational databases from the 
      1970s to 1990s are not included in the NoSQL category
    - schema-less
- On the last point, although NoSQL databases usually don't require an *explicit*
  schema, you still have some *implicit* schema in the way you query them.  If you
  query a NoSQL database for items with the product_id equal to 4555, you imply
  that every product must have something called "product_id" which is a number. If
  some products called it "product_num" or "SKU", it would be impossible to use
  the system.  So the database may not enforce the schema for you, but you still
  need to have one.
- The four main types of NoSQL databases are key-value stores, document stores,
  column-oriented databases, and graph databases.
- The first two types (key-value and document-oriented) are so similar that Fowler
  groups them under the term "aggregate-oriented" databases.
- Aggregate-orientation fits nicely into cluster computing situations: by keeping
  all the data related to an aggregate together, you can enable queries without 
  having to communicate with several different nodes of the cluster. (19:05 to 
  about 20:00 on the video)
- Aggregate-oriented databases aren't good at every type of query (20:30 to 21:58).
  Fowler's example shows that traditional, relational databases are better at
  slice-and-dice type queries where you're effectively "changing the aggregation".
- The many types of NoSQL databases offer different *data models*.  Part of your
  decision about which type to choose depends on "how do you intend to work with
  your data?". (24:55 to 25:25)
- Fowler goes on to give a good explanation of the CAP Theorem and the trade-off
  between consistency and availability.  His "hotel booking" example is worth
  watching again.  The key point: *the trade-off between consistency and
  availability is a business choice*. (36:15 to 39:15)

## MongoDB and MapReduce

Jared Rosoff's video "MongoDB Schema Design: How to Think Non-Relational", a few
minutes of which we watched in class, is a good introduction to what one of those
aggregate-oriented databases looks like in practice, and how a document-oriented
schema might be designed or queried.  (http://youtu.be/PIWVFUtBV1Q, first 23 1/2
minutes or so.)

A couple of points worth remembering:

- MongoDB, like some other document stores, uses a JSON-like format to structure
  data.
- The schema does not need to be fully specified in advance, and can be altered
  in practice.  In the example, Rosoff adds a "comment" (a new sub-structure) to
  a "book" (the original structure) in his database. (Around 15:30)
- (Around 17:45) A document store can represent, in one document, what would take
  several tables in a relational database.

A brief video featuring Jim Hoskins (http://youtu.be/WovfjprPD_I) shows what a
MapReduce type of query looks like in MongoDB.  The MapReduce algorithm is often
associated with Hadoop, but other distributed systems like MongoDB can support
it, too.

- A "map" function is run on every record in the database (on all the nodes,
  independently) and sends data to an intermediate data structure.
- It is commonly said that, instead of bringing the data to the program that needs 
  it, we're sending the program to the data where it is stored.
- A "reduce" function processes those intermediate data structures to get the
  ultimate result.
- This is powerful because the "map" functions may run in parallel on many nodes,
  then send their results to one or a few nodes for the final "reduce" step.

The video of Jesse Anderson demonstrating MapReduce with playing cards may also
be helpful if you're having trouble with how it works: http://youtu.be/bcjSe0xCHbE

  
  
## Hadoop & Spark -- Chris & Schuyler's topics

Chris and Schuyler gave a talk and demonstration on Hadoop and then on an 
alternative called Apache Spark.  Some of the things you should know about these
tools are:

- Hadoop includes two things: Hadoop Distributed File System (HDFS) is a
  system for storing huge amounts of data on a computer cluster transparently
  (as if it were one big disk).  Hadoop is also an infrastructure that supports
  MapReduce programs.
- Hadoop is an open-source project under the aegis of Apache, but it is pretty
  hard to use "out of the box".  Chris showed us a "distribution" of Hadoop
  from Hortonworks.  There are other distributions from other companies such
  as Cloudera, MAPR, etc.  The benefits of using a distribution include
  graphical user interfaces that make it much easier to use the technology.
- **Hive** is a tool for writing SQL-like queries that are automatically
  transformed into MapReduce jobs and executed on Hadoop.  Hive is used by a
  lot of organizations to do things like data warehousing with massive data.
- Apache Spark is an alternative to Hadoop/MapReduce that has shown dramatically
  faster queries.  The main difference is that it does more work in-memory
  instead of using disks.
- Because it's so new, though, there aren't any user friendly "distributions"
  of Apache Spark yet.
  
Their slide deck on Apache Spark is in the CIS355 GitHub repo.  


## Data Warehousing Appliances -- Alex N's topic

Alex N talked to the class about data warehouse appliances.  A **complete data
warehouse appliance** is an integrated "box" including hardware, software, the
database, an operating system, etc, all the things needed to load and query
big data.  Some examples are Oracle's Exadata, SAP HANA, and IBM DB2.

The characteristics of a data warehouse appliance are:

- Workload optimized (designed for optimal performance at DW tasks)
- Extreme scalability
- Highly reliable
- Simplicity of operation

They are intended to be "black box" systems that can be set up quickly and 
don't require a lot of maintenance.

Although these appliances are expensive, Alex argued that for many companies,
they are a better option than the do-it-yourself (DIY) approach, mainly because
they reduce the need for expensive support.

Alex also showed a few slides on *columnar databases* which are commonly used
with big data warehouses.  These are relational databases in the sense that
they are *logically* structured into tables and rows and columns.  However, 
they are physically organized differently on disk.  While traditional RDBMSs
keep *rows* together on disk, columnar databases keep *columns* together.

His slide #16 is a good vizualization of this.

What it means is that queries which look at a single column across thousands 
or millions of rows can run very quickly.  That kind of query is uncommon in 
transactional systems, but very common in analytical systems like data
warehouses.

Alex's slide deck is in the CIS355 GitHub repo.



## R vs Python -- Manoj's presentation

Manoj gave a good talk about R and Python, two scripting languages that are 
often used in big data analytics.  R is designed for statistics, and Python
is more of a general purpose language with some statistical libraries. 

Going along with my notes on scripting languages, above, I think the main
take-away is that either of them could be a good choice (and so could Ruby,
or Javascript, or Perl).  Use what you know and prefer.

Manoj's slide deck is in the CIS355 GitHub repo.


## Data Dive into a game API -- Alex P's topic

Alex P gave an interactive demonstration of a data dive into the API of
the game League of Legends (from Riot Games).  It was pretty topic-specific,
but a great opportunity to see what a JSON API looks like in practice, and
how to write a Python script to extract data from it.  I tried to think
about what to generalize from this talk, and here are a few key points:

- API = *application programming interface*.  Basically an API is a way that
  you can give other people access to some data or functionality, without
  giving them privileged access to your servers or sharing your passwords.
  APIs are generally designed so that they can be used by machines -- instead
  of sharing pretty web pages, they usually communicate in CSV, JSON, or XML.
- Typically an API has a URL, like a web address.  You can write a script in
  Python or any language that sends a request to the URL and parses the data
  that is returned.
- Exploratory data analysis like this requires *domain knowledge*.  The class
  saw Alex going back and forth from the data to his understanding of how the
  game worked and what it might mean.

## Big Data Analytics

The only reading from the Kimball book in the second half of the course was 
Chapter 21 on Big Data Analytics.  See my slides on that topic for the main
points I want you to know.
