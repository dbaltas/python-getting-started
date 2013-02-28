## Intro
Illustrates how to use a mongo driver through python
[PyMongo] [1] will be used as it is most actively supported at the time of this writing

## Installation
### Installing Mongo
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
echo -e "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" | sudo tee  /etc/apt/sources.list.d/10gen.list > /dev/null
sudo apt-get update
sudo apt-get install mongodb-10gen
```
### Installing PyMongo
either through Easy install
    sudo easy_install pymongo
or through pip
    pip install pymongo==2.1.1

## Sample
Script creates a customers collection in the demo_store database and insert 3 customers.

run sample with
    python mongo.py

To validate that the script run, from terminal connect to mongo:

    mongo demo_store

And from the mongo prompt run:

    db.customers.find()

which should return something like this

    { "_id" : ObjectId("512f40232ee6d30202fdd077"), "city" : "London", "name" : "Bill" }
    { "_id" : ObjectId("512f40232ee6d30202fdd078"), "city" : "Paris", "name" : "John" }
    { "_id" : ObjectId("512f40232ee6d30202fdd079"), "city" : "London", "name" : "Jane" }

[1]: http://api.mongodb.org/python/current/ "PyMongo: MongoDB driver for Python"