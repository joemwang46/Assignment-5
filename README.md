

Steps to run code:
1. clone repo. all files should be in the same directory
2. pip install -r requirements.txt
3. run tests.


Results:

(finm) joewang@Joes-MacBook-Pro-182 Assignment 4 % coverage run -m pytest -q
...............                                                                                                                                        [100%]
15 passed in 0.21s
(finm) joewang@Joes-MacBook-Pro-182 Assignment 4 % coverage report --fail-under=90

Name               Stmts   Miss  Cover
--------------------------------------
broker.py             19      1    95%
conftest.py           12      0   100%
engine.py             15      0   100%
strategy.py           30      3    90%
test_broker.py        25      0   100%
test_engine.py        46      0   100%
test_strategy.py      11      0   100%
--------------------------------------
TOTAL                158      4    97%
