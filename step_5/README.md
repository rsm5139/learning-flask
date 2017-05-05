# Step 5: Authentication and Sessions

## Step 5.1: Create step_5 Table

We'll need a new table for this step. Creating it works the same as the last step, so I'm going to list out what to enter in your terminal line-by-line.

```
psql
\c learning_flask
CREATE TABLE step_5 (
uid serial PRIMARY KEY,
first_name VARCHAR(25) not null,
last_name VARCHAR(25) not null,
email VARCHAR(120) not null unique,
pwdhash VARCHAR(100) not null);
```

## Step 5.2: Running the Example

Compile the step 5 example with the ```python routes.py``` command. Refresh your Flask app browser window or navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000). 

There is a lot added to this example as compared to the last one. First, there are 4 pages: the home page or "index," a registration page, a login page, and a secret page. The secret page can only be accessed by users who are logged in. Go ahead and click the link for "Register" and create an account. (No reason to use any of your real information to do this; you can use a fake email like "fake@fake.com.") After you have registered, try clicking the link for "Secret." You are now on the secret page. Now click "logout" and try to click "Secret" again. You'll end up at the login page.

The key to authentication is to set a session cookie when the user logs in. 

```
if user is not None and user.check_password(password):
    session["email"] = form.email.data
```

Then, secret pages can check for this cookie before the page is loaded:

```
if "email" not in session:
    return redirect(url_for("login"))
```

While this example works well as a demonstration, it is not robust enough for a live site. For starters, an error will be thrown if an email is reused during registration. It would be nice to add functionality to handle this error. 

## Other Steps

[Step 1/2](https://github.com/rsm5139/learning-flask)

[Step 3: Pages and Templates](https://github.com/rsm5139/learning-flask/tree/master/step_3)

[Step 4: Database and Forms](https://github.com/rsm5139/learning-flask/tree/master/step_4)

*Coming Soon*

[Step 6: Reactive Design](https://github.com/rsm5139/learning-flask/tree/master/step_6)