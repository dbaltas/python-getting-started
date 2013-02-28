import pymongo

# create client
client = pymongo.MongoClient("localhost", 27017)
#create database
db = client.demo_store

#print with arguments. Arguments in tuple. ',' is required to tell python this is a tuple if only one item.
print "created database: %s" % (db.name, )

db.customers
print "created collection: %s" % ('customers', )
print "remove all %s from collections, if any" % ('customers', )
db.customers.remove()

print db.customers.save({'name' : 'Bill', 'city' : 'London'})
print db.customers.save({'name' : 'John', 'city' : 'Paris'})
print db.customers.save({'name' : 'Jane', 'city' : 'London'})
print "added %d items in collection %s" % (db.customers.count(), 'customers')
