/*
Starting a server from scratch


INITIAL SETUP
make directory for application
install/run a pipenv shell
install pylint, autopep8, and django
django admin start project

pylint file and select interpereter
create .vscode and <project_name>api directories

gitignore & update settings
base django tables



WORKFLOW
Models - templates for how your data will be represented
    migrate models
        this creates empty tables for when it's time to "seed" the data

Fixtures - dummy data
    loaddata - self explanitory: they load your dummy data into the empty
    tables we made in migrations
        .fixture <-- needs to match the model classname (singular or plural [in my case, singular]) 

Views
    these modules hanbdle the retrieve/list/create/update/destroy
    functionality of whatever view/resource we want to manipulate





*/