# Overview

The goal of this activity is to have you evaluate static code analysis tools and learn how they can help improve the quality of your code. 

# Python Coverage

Begin by copying /src and /tests from Activity 19 (white‑box testing). Then, use Python’s **coverage** tool to measure how thoroughly your tests exercise your code. Install coverage via pip:

```
pip3 install coverage
```

Next, run your tests exactly as you did before, but this time prefix your command with **coverage run** so coverage can record the execution data. After the tests ran, you can generate the report using: 

```
coverage report
```

A more detailed report can be generated in html using: 

```
coverage html
```

# Python PyLint

[Pylint](https://www.pylint.org/) checks for coding standards, errors, and offers suggestions for improvement. It is highly configurable, can detect unused code, and supports writing custom plugins. 

Pylint can be installed using: 

```
pip3 install pylint
```

To have **pylint** check **bank_account.py**, run: 

```
pylint src/bank_account.py
```

**pylint** will analyse the code and give it a rate from 0-10. 

Improve your code based on pylint's suggestions. 

# Python Bandit

Python [Bandit](https://bandit.readthedocs.io/en/latest/) can be used to find common security issues in Python code. Install bandit using: 

```
pip3 install bandit
```

Run bandit on [src/insecure.py](src/insecure.py) using: 

```
bandit -r src/insecure.py > bandit_report.txt
```

Make the corrections suggested by bandit. 