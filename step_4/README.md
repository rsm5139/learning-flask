# Step 4: Database and Forms

## Step 4.1: Installing PostgreSQL

The next couple of Flask examples will require a database to manage data. For that, we'll need [PostgreSQL](https://www.postgresql.org). Download the latest version and follow the setup instructions [here](http://postgresapp.com).

After setup is complete, open a command terminal and type ```psql```. Now you are ready to interact with PostgreSQL. Create a new database with the following command:

```
create database learning_flask
```

Note that ```learning_flask``` can be any name you want for the database. Now, connect to the new database:

```
\c learning_flask
```

Yes, that command does in fact start with ```\```. It's a little strange, but that's how it works. Now, create a new table for this example:

```
CREATE TABLE step_4 (
uid serial PRIMARY KEY,
name VARCHAR(100) not null,
comment VARCHAR(140) not null );
```

Finally, add an entry into this table to get things started:

```
INSERT INTO step_4 (name, comment) VALUES ('Flask', 'Hello, world!');
```

You can confirm the entry was added with:

```
SELECT * FROM step_4;
```

## Step 4.2: Install Flask-SQLAlchemy

If you installed all of the packages from [step 1.3](https://github.com/rsm5139/learning-flask), then you can skip this step. Never-the-less, it doesn't hurt to check that Flask-SQLAlchemy is installed. Enter the following command to install it:

```
pip install flask-sqlalchemy
```

Also, install Psycopg2 with ```pip install psycopg2```.

## Step 4.3: Install Flask-WTF

Same thing as the last step. You either installed this in [step 1.3](https://github.com/rsm5139/learning-flask), or you can install this now with ```pip install flask-wtf```.

## Step 4.4: Running the Example

Compile the step 4 example with the ```python routes.py``` command. Refresh your Flask app browser window or navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000). 

There are 2 new files in this example: ```forms.py``` and ```models.py```. The former defines the class for the comment form, and the latter defines the class for the database. These classes are imported and used by ```routes.py```. The data are the passed off to the template to be utilized by Jinja2.

This example simply takes a username and a comment, saves it to the database, and display's a list of previous names and comments. Not too complicated, but the next [example](https://github.com/rsm5139/learning-flask/tree/master/step_5) will go even deeper by authorizing a user and creating a session.

## Other Steps

[Step 1/2](https://github.com/rsm5139/learning-flask)

[Step 3: Pages and Templates](https://github.com/rsm5139/learning-flask/tree/master/step_3)

*Coming Soon*

[Step 5: Authentication and Sessions](https://github.com/rsm5139/learning-flask/tree/master/step_5)

[Step 6: Reactive Design](#)