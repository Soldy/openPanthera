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
  1. Using Panthera requires significant additional development time. For fast, rapid development alternative solutions like ORM, graphql, or Flatdb are far better than Panthera. 
  1. It is not suitable for Domain-Driven Design (DDD) development, and the benefits of Panthera for Continuous Integration (CI) development are questionable.
  1. In my view, this system has no benefit on most SAAP solutions. 



# Instructions

## Install

```
pip3 install openPanthera

```


## Usage

```
python3 -m openPanthera.menu
```

## How does it work? 

The Panthera currently has 12 different directories, each represent one type of SQL scripts.
These scripts and migrations are accessed or controlled through the menu and the CLI interface using commands.
It's important to note that Panthera does not manage the server itself; that needs to be done separately.


## Controll and comands.

The open Panthera has two control interfaces: 
   1. the command line interface ``` python3 -m openPanthera.cli ``` 
   1. the menu interface. ```python3 -m openPanthera.menu``` .

Both interfaces have the same commands.
The Panthera interface is a simple command interface, but this may change in the future.
If it does change, the menu should be renamed to "com," and a real menu interface will be implemented. 
Every command consists of two words: the module and the type. Additionally, every command has a shorter method, which is represented by two characters.

## Modules


### show or s.

Show system or database information. 


### directory or d.

All directory tree-related commands belong to this module.


### build or b.


Build command. This runs the build scripts. However, some build functions execute functions that belong to different modules. 
For example bc. Call a destroy before building everything again.

### x

This is a destructive module. 
Every destroy function belongs to that module.

### migration or m 

This is a data migration module has two functions backup and restore.

## Types. 

In our system, there are 20 different types. Among them, there are 12 script types, and 8 virtual types.
Some types are combinations of different categories, while others can represent multiple types from various modules,
not just their parent module. Additionally, there are virtual types that may not be fully related to their function or only partially related to it.


### table or t

Represent the ```10-table``` directory. Storing the main tables definition. At the moment the openPantera only supports build.


### link or l

Represent the ```15-table-link``` directory. Storing the link tables, most of the time many too many connection representations. At the moment the openPantera only supports build.


### function or f

Represent the ```20-function``` directory. Storing the definition of the functions. Panthera only lets you access stored functions and procedures. At the moment the openPantera only supports build. But in the j module implementation is planned.


### procedure or p

Represent the ```30-procedure``` directory. Storing the procedure of the definitions. Panthera only lets you access stored functions and procedures. At the moment the openPantera only supports build. But in the j module implementation is planned.


### view or v

Represent the ```40-view``` directory. Storing the view of the definitions. It's a good practice to build view tables for the foreign keys. That way they can call in multiple functions and procedures with less pain. Do not forget the Panthera is designed for TDD so the test has to be in place or that makes the system too fragile. At the moment the openPantera only supports build. But in the j module implementation is planned.


### index or i

Represent the ```50-index``` directory. Not supported in openPanthera at the moment.


### foreign or f

Represent the ```60-foreign``` directory. Storing the foreign key definitions.  At the moment the openPantera only supports build. The j module support never be implemented in the openPanthera, because increase the chance of human error.


### migration

Represent the ```70-migration``` directory. Migration support scripts. Not supported in openPanthera at the moment.


### seed or s

Represent the ```80-seed``` directory. Not supported in openPanthera at the moment.


### event or e

Represent the ```90-event``` directory. Not supported in openPanthera at the moment.


### init or i

This triggers the initializations. Initializing the Panthera basic table or the directory trees.


# My note.

The main reason the Panthera exists is my AI addiction. My latest AI project tries to do something almost impossible. Build a system that gives the result on a Raspberry Pi 5 that other systems provide on a large Nvidia cluster. For that goal, the data is the key.  More data in smaller places is the key to better results. \
Panthera helped me shrink the IMDB database to 40 megabytes and the en wiki to less than 500 megabytes without negatively affecting performance, keeping the data still easily readable. In fact, it positively affected performance; I was able to reduce the response time to under 20 ms with the Wikipedia data collection. It's important to note that I am storing meaning, not just texts. This way, I am storing almost the same data in the SQL that I am using for machine learning. \
Because of my limited time, I have codes in ADA, Rust, C++, Python, PHP, and Javascript that I do not want to rewrite because of the time. But I use the same database. It's a solution to manage the database in one and provide an API. But with the API the single server has to be available every time. For example, if I build a php layer Apache always has to be there over the SQL master to slave replicas in the middle to serve the API.
Extra note : In my view, this system has no benefit on most SAAP solutions. 
For fast, rapid development alternative solutions like ORM, graphql, or Flatdb are far better than Panthera. 



# !Security WARNING!

Panthera is safe onlY IF you always use the provided layer.
Panthera cannot fix Human stupidity. Sorry :(
