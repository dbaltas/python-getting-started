#! /usr/bin/python

import sys
import os

this_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(this_path)

from Employee import *
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
Employee.displayEmployee(emp1)
