#! /usr/bin/python
# comments
print '> print hello-world'
print 'hello-world'

# write to file
print '> write to file'
file = open('a.txt', 'w')
file.write('hey there\n')
file.write('hey you')
file.close

# read from file
print '> read from file into list'
file = open('a.txt', 'r')
lines = file.readlines()
print 'Type of file.readlines:' + type(lines).__name__
# list to string
print '> list to string'
print (':').join(lines)

print '> remove file from file system'
# delete file / call os method
import os
os.remove('a.txt')