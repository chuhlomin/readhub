readhub
=======

Prerequisites
-------------

* [nodejs](http://nodejs.org)
* [grunt-cli]() (`sudo npm install -g grunt-cli`)
* python 2.7
* [pip](http://pip.readthedocs.org/en/latest/index.html) (`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python get-pip.py`)
* [virtualenv](https://virtualenv.pypa.io/en/latest) (`sudo pip install virtualenv`)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) (`sudo pip install virtualenvwrapper`)
* [PostgreSQL](http://www.postgresql.org) or [Postgres.app](http://postgresapp.com) for OSX

Setup database
--------------

    CREATE ROLE readhub_user WITH LOGIN CREATEDB;
    CREATE DATABASE readhub_db;
    GRANT ALL PRIVILEGES ON DATABASE readhub_db to readhub_user;

Installation
------------

    sudo npm install
    ./node_modules/.bin/bower install
    grunt
    
    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv readhub
    workon readhub
    pip install -r requirements.txt
    
    export SETTINGS='config.Config'
    python manage.py db init
    
    sh run.sh
