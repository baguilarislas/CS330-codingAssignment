# CS330-codingAssignment

## Purpose of the project

This project displays an FSM use in which a security keypad is used in order to test a string of inputs in order to lock or unlock a door

The file machine.py contains the algorithm which the controller of the machine works and the file time_test.py contains a guesser which generates randome keystrokes for the machine in order to test how much a brute force attack would take to break the security 

# Pre Requisites: 
### The instructions below are for a Linux environment (Ubuntu 22.04).
1. Python
2. Git

# Installation :
1. To install `python`:
```
$ sudo apt update
$ sudo apt install python3
```

2. To install the `coverage` module :
```
$ pip install coverage
```

3. To install `git`:
```
$ sudo apt-get update
$ sudo apt-get install git-all
```

# Configuration: 
1. Clone the repository
```
  $ git clone https://github.com/baguilarislas/CS330-codingAssignment.git
  $ cd CS330-codingAssignment
```
2. Run unit tests 
```
 $ python3 -m coverage run -m unittest
```
3. View unittest coverage report:
```
 $ python3 -m coverage report
```
To run the execuatble: 
First part , run machine.py, the Security Device simulator:
```
$ ./machine.py
```
Second part, run 
```
 $ ./time_test.py
```
This is the brute force attack simulator

# Author:
Braulio Aguilar Islas

# Questions:
baguilarislas@hawk.iit.edu
