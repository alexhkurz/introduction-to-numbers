# README

Download [python](https://www.python.org/downloads/). Run in a terminal (or an IDE such as IDLE)

    python groupoku.py

Depending on your installation you might need to run `python3 groupoku.py`, but nowadays I would expect that you have python3, and not python2, installed by default.

Running `python groupoku.py` should give the output

    0 1 2 3
    1 2 3 0
    2 3 0 1
    3 0 1 2
    is associative
    has neutral element
    has inverses

This tells you that for this particlar table, the laws of a group are satisfied. Moreover the operation is commutative. We therefore think it is justified to call this operation an "addition".

If you want to get an idea how this works look at the code of [groupoku.py](groupoku.py) and [Group.py](Group.py).

To check other tables, modify the code in [groupoky.py](groupoky.py) accordingly.
