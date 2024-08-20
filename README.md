# openPanthera

## About

Open Panthera is an SQL builder and migration tool. \
Panthera is not new. Not a revolution. \
That solution is popular in banks and mission-critical systems. But most of the similar tools are the close source. \
The primary logic is simple: The outside client only calls the inbuild functions and procedures. So the system SQL injection prof and easily portable to other technologies. \
The benefits:
   1. Can be safe like an ORM.
   2. Unlike an ORM not stacked with one programing language.
   3. Panthera logic has some performance benefits as well.



Panthera has four versions.
   1. Open Panthera is an easy-to-use open-source implementation built in python. Almost ready to use.
   2. Noname Panthera a nodejs implementation. (Working in Progress)
   3. PHP Panthera.
   4. Sweet Panthera is a closed-source implementation. Fully operational.




# Why use Panthera?

Panthera is a straightforward solution for enforcing data management on SQL, making it easier for different systems to access the same data collections.
When using Panthera, the correct approach involves limiting the backend software access to direct database queries. That forces the developers to call a function or a procedure, ensuring safer data management.
Panthera is optimal for Test-Driven Development (TDD).


# Why not use Panthera? 

However, using Panthera requires significant additional development time and is not suitable for Domain-Driven Design (DDD) development.
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

The main reason the Panthera exists is my AI addiction. My latest AI project tries to do something almost impossible. Build a system that gives the result on a Raspberry Pi 5 that other systems provide on a large Nvidia cluster. For that goal, the data is the key.  More data in smaller places is the key to better results. 



# !Security WARNING!

Panthera is safe onlY IF you always use the provided layer.
Panthera cannot fix Human stupidity. Sorry :(
