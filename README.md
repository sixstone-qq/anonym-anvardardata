# anonym-anvardardata
Anonymise user's data set for gathering stats

## Description of the problem to solve

Given a set of files, where each file belongs to a user's purchase
history, in a folder with the following format:

```json
{
  "purchases": [
    {"type": "airline", "amount": 100},
    {"type": "restaurant", "amount": 25},
    {"type": "coffee", "amount": 2},
    {"type": "airline", "amount": 250}
  ]
}
```

It calculates the following statistical measures:

* minimum
* maximum
* average (mean)
* median

To perform this calculation we have the following constraints:

* The data to report for each user must be done without using other
  users' data
* The data to report for each user and the statstical data will be
  done in two different programs
* Data to report from each user have the following tuple structure:

```
  | first | second    |
  |-------|-----------|
  | likes | green     |
  | likes | spinach   |
  | likes | ice-cream |
```

* The data will be aggregated to have the number of repeating tuples
  to count the number of users having that tuple. Example:

```
  | key  | value     | count |
  |------|-----------|-------|
  | city | Berlin    | 6     |
  | city | Zaragoza  | 1     |
  | city | Bucharest | 1     |
```

* The data will be anonymised by removing those triplets whose count
  is __5 or less__.

## Instructions to run it

Make sure you have `python 3.4` version installed and run the
following command:

    # ./process-user.py data | ./process-data-set.py

Having in `data` folder the JSON files with the user's data where
the user identifier is the file basename without the extension.

This will print the anonymised result as follows:

```
- min: 150

- max: 10000

- average: 8358.333333333334

- median: 10000.0
```
