# Testing and refactoring exercise
This is an in-class opportunity to practice some code improvement to be
completed individually or as a pair. It's based off of the debugging lab by
Github user `spiside`:

[Debugging Lab](https://github.com/spiside/pdb-tutorial)


## Getting started

First, run main.py a few times. If you recall from the debugging exercises,
there were a couple of immediately visible bugs - both of those have been fixed.
However, the code is not bug-free, and it's also made a lot of messy choices!
You're welcome to look at the code with your editor or `pdb` to get a better sense
of what's going on.

Then, take a minute to set a few goals for what behaviors to test and how you'd
like to improve the code. Put these in instructions.txt under the corresponding
questions. I'd recommend starting modestly and adding items to the list as you
go. These lists should be pretty connected to each other: 

* Some changes you make could be *refactoring*, or rewriting the code to be
cleaner without changing the behavior: in this case, it's a good idea to plan
out test cases to check that behavior hasn't changed.

* Some changes you make could be *improvements or fixes*, which will change the
behavior of the code to a preferable one. It's a good idea to write the test
cases for the behavior you want to have: the test should fail when you first
write it, then succeed later once you fix it.

## Testing with unittest

There are a number of different Python resources that exist to help automate
tests. One module built in to Python is called `unittest`, which has classes
containing methods that support standard functionality you'd want to write
tests, including nice assert statements to compare values, built-in
functionality to `setUp` and `tearDown` objects and data for complex tests, and
support to `mock` out fake objects, functions, etc. when you want to mimic parts
of your codebase instead of calling into complex/slow/resource
intensive/unpredictable code.

Right now, there's one test, which you can see in `tests/test_die.py`. It exists
inside the `TestDie` class following a standard pattern for creating tests in
`unittest`. You can follow this template to make a test file for `runner.py` as
well - that is, you can make a new Python file `test_runner`, make a class
`TestRunner` inheriting from `unittest.TestCase`, and write test case functions
whose names start with `test_` inside that class. You should be able to import
code from the local `dicegame` package, which is the package name for your
codebase.

If you want to run all the tests, you can navigate to the top-level directory of
the repository and run ```python3 -m unittest``` to run all of the tests that
can be discovered in the directory. It'll automatically discover all of the
tests in the folder. If you want to run subparts, you can add information about
where a specific file, class, or test is, e.g. ```python -m unittest
tests.test_die.TestDie.test_valid ```

(Note: the reason `unittest` works with no arguments has to do with telling
Python that the `tests` folder is its own module with an empty `__init__` file -
we're not going into why this matters, but if you have trouble getting
`unittest` to work in another project, make sure to check on that.)

Based on your plan in instructions.txt, add some tests to `test_die.py` and/or
`test_runner.py` based on your test goals. Here are some good starting points to
see examples of tests:
* [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
* [DataQuest tutorial for unit tests](https://www.dataquest.io/blog/unit-tests-python/)
* (Advanced) [Python examples of mock](https://docs.python.org/3/library/unittest.mock-examples.html)

I'd encourage you to try to add at least one test in test_runner that just makes
sure the runner actually runs (independently of whether it gives the right
output). As a hint, to simulate a user's input, you can use
`unittest.mock.patch` to basically overwrite what `input` means while the test
case is running, as [shown
here](https://stackoverflow.com/questions/46222661/how-to-mock-a-user-input-in-python).
Here, you'll probably want a sequence of inputs, which can be achieved using the
`side_effect` instead of `return_value`, like
```python
with mock.patch("builtins.input", side_effect=["input1", "input2", "input3"]):
    # do stuff
```

It's possible that in the process of writing tests for this code, you'll realize
that there are parts of the code organization that make it hard to test.
Sometimes, those are indicators of what you might want to refactor, so feel free
to add to/amend your list of items to refactor in `instructions.txt` as you go.
Don't forget to commit periodically!

## Code improvements
Once you've got a set of tests, it's easier to start adjusting the code. Work
through your list of changes in instructions.txt, taking care to run your tests
periodically to see if things are working as expected (whether you're changing
the behavior or trying to keep it constant). If you realize there are edge cases
that you didn't catch in your original test list for your changes, you may
decide to go back and add those tests. Make sure to commit between steps: if you
improve one part of the code and get your tests to pass, commit before you start
working on the next improvement.

Note that our focus is primarily on trying to make the organization of code
cleaner: while you can (and should) comment your code, use good variable names,
and put reasonable docstrings in the places you make changes, you're not
responsible for doing that outside of the code you touch.

## Turning it in
When you have your changes done, commit your code to GitHub and then submit the
link to your codebase to the Sakai assignment. Since Sakai is horrible, you'll
need to submit the link individually for each partner if you worked in a pair.