# openPanthera

## About

In Short: Open Panthera is an SQL builder and migration tool. \
Open Panthera is a straightforward solution for enforcing data management on SQL, making it easier for different systems to access the same data collections. \
The primary logic is simple outside the database only calls the inbuild functions and procedures. So the system SQL injection prof and easily portable to other technologies.


Panthera has four versions. 
   1. Open Panthera is an easy-to-use open-source implementation built in python. (Alpha state)
   2. Noname Panthera a nodejs/deno/bun implementation. (Working in Progress)
   3. PHP Panthera. (Alpha state)
   4. Sweet Panthera is a closed-source rust implementation. (stable)


# Why use Panthera?

When using Panthera, the correct approach involves limiting the backend software access to direct database queries. \
That forces the developers to call a function or a procedure, ensuring safer data management. \
Panthera is optimal for Test-Driven Development (TDD). \
Panthera logic has performance benefits. \


# Why not use Panthera? 

  1. Panthera is designed for simplifying the management of complex data schemas, not the schema. If you want to simplify the schema, Panthera is not what you are looking for.
  1. Using Panthera requires significant additional development time. 
  1. For fast, rapid development alternative solutions like ORM, graphql, or Flatdb are far better than Panthera. 
  1. It is not suitable for Domain-Driven Design (DDD) development, and the benefits of Panthera for Continuous Integration (CI) development are questionable.
  1. In my view, this system has no benefit on most SAAP solutions. 




Using Panthera requires significant additional development time and is not suitable for Domain-Driven Design (DDD) development.
The benefits of Panthera for Continuous Integration (CI) development are also questionable.


# Instructions

## Install

```
pip3 install openPanthera

```


## Usage

```
python3 -m openPanthera.menu
```


# Controll and comands.


The open Panthera has two control interfaces.
Command line interface ``` python3 -m openPanthera.cli ``` , and menu interface ```python3 -m openPanthera.menu``` .
Both interface has the same commands. 
Every command is built from two words. 
Module and function. Every command has a shorter method. The short method is two characters.  

# Modules


## show or s.

Show system or database information. 


## directory or d.

All directory tree-related commands belong to this module.


## build or b.


Build command. This runs the build scripts. However, some build functions execute functions that belong to different modules. 
For example bc. Call a destroy before building everything again.


## x

This is a destructive module. 
Every destroy function belongs to that module.



## migration or m 

This is a data migration module has two functions backup and restore.



# My note.

The main reason the Panthera exists is my AI addiction. My latest AI project tries to do something almost impossible. Build a system that gives the result on a Raspberry Pi 5 that other systems provide on a large Nvidia cluster. For that goal, the data is the key.  More data in smaller places is the key to better results. \
Panthera helped me shrink the IMDB database to 40 megabytes and the en wiki to less than 500 megabytes without negatively affecting performance, keeping the data still easily readable. In fact, it positively affected performance; I was able to reduce the response time to under 20 ms with the Wikipedia data collection. It's important to note that I am storing meaning, not just texts. This way, I am storing almost the same data in the SQL that I am using for machine learning. \
Because of my limited time, I have codes in ADA, Rust, C++, Python, PHP, and Javascript that I do not want to rewrite because of the time. But I use the same database. It's a solution to manage the database in one and provide an API. But with the API the single server has to be available every time. For example, if I build a php layer Apache always has to be there over the SQL master to slave replicas in the middle to serve the API.
Extra note : In my view, this system has no benefit on most SAAP solutions. 
For fast, rapid development alternative solutions like ORM, graphql, or Flatdb are far better than Panthera. 



# !Security WARNING!

Panthera is safe onlY IF you always use the provided layer.
Panthera cannot fix Human stupidity. Sorry :(
