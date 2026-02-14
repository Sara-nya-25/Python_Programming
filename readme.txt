The PYTHONPATH Trick
To set a permanent path so you can use the simple pytest command without the python -m prefix,
you need to tell your environment (and PyCharm) that your project root is a source of code.

The pytest.ini File (Recommended)
This is the most "set it and forget it" method. By creating a configuration file in your project root, pytest will always know how to handle your paths.

Create a file named pytest.ini in your Python_Programming folder.

Paste the following content:

Ini, TOML
[pytest]
pythonpath = .
testpaths = LAB_2 LAB_3 LAB_4 LAB_5

Now you can simply run: pytest -rA LAB_5/TDD_2_Count_words_test.py and it will work every time.

or

On Windows (PowerShell):

PowerShell
$env:PYTHONPATH = "."
pytest -rA LAB_5/

why we use __init__.py

It Creates a "Package" Structure
Without __init__.py, your folders are just "loose" directories. With them, they become Python Packages.

Cross-Folder Imports: If you want a file in LAB_5 to import a utility script from LAB_2, Python will only allow it
if both folders are recognized as packages.

Namespace Safety: It prevents naming conflicts if you happen to have two files named utils.py in different labs.

Standardized Discovery
pytest is designed to find and run tests across your entire project.

Without init: You often have to run tests one by one, or use specific flags to help Python find your code.

With init: You can simply type pytest at the very root of your project, and it will intelligently navigate through LAB_1, LAB_2, etc.,
and run everything at once because it recognizes the whole tree as a single application.

Professional Standards
In the "real world" (Open Source, Work, etc.), Python code is almost always distributed as packages.
Learning to manage the path now saves you from a massive headache
 later when you try to deploy code or install your own project as a library.

 When you added __init__.py, you turned LAB_5 into a sub-package of Python_Programming.
 Before: Python treated LAB_5 as the starting point.

After: Python treats Python_Programming as the starting point, and LAB_5 as a member.

The "Sweet Spot" Workflow
Since you already have the __init__.py files there, the best way to move forward is to always run your tests from the root using the module flag:
python -m pytest LAB_5/TDD_2_Count_words_test.py

To avoid typing python -m pytest LAB_5/ set pythonpath variable in terminal or set pytest.ini file in project root directory i.e. python programming.