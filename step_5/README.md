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

## Other Steps

[Step 1/2](https://github.com/rsm5139/learning-flask)

[Step 3: Pages and Templates](https://github.com/rsm5139/learning-flask/tree/master/step_3)

[Step 4: Database and Forms](https://github.com/rsm5139/learning-flask/tree/master/step_4)

*Coming Soon*

[Step 6: Reactive Design](#)