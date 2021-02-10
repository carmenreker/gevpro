Assignment
==========

In this assignment you will work with XML, JSON, strings and various data
structures.

Like last week, go to your repository and unzip the assignment files:

	$ cd gevpro
	$ unzip week2.zip

Commit the original files to your repository.

Step 1: Finding Adjectives (4.5 Points)
----------------------------------

Cornetto is a digital lexical database for Dutch. The full version is available
on RUG Linux computers in `/net/corpora/Cornetto2.0`. The assignment directory
contains a small sample of Cornetto's word list in the file `cdb-sample.xml`.
This sample file is enough to do the assignment.

Create a Python module `cdb` with a function `get_adjectives`. The function takes
as argument the path to a Cornetto database XML file such as `cdb-sample.xml`
or `/net/corpora/Cornetto2.0/cdb2.0.id.xml`. It returns a collection of
adjectives in the database.

Requirements:

* Use `xml.etree.ElementTree` to read the XML file and iterate over its `cid`
  elements. Each element corresponds to a word.
* The returned collection consists of Python strings. It contains the
  values of the `form` attributes of `cid` elements.
* In the returned collection, include only adjectives. `cid` elements corresponding
  to adjectives have `ADJ` as the value of their `pos` (part of speech) attribute.
* Use a filtered list comprehension to filter out the non-adjectives.
* Some words have duplicate entries. Make sure the returned collection contains
  each adjective only once. Use the appriopriate data structure to enforce this.
* cdb.py should define a main function

Step 2: Solving Word Search Puzzles (4.5 Points)
------------------------------------------------

Create a module `wordsearch` with a function `solve`. The function takes the
path to a text file with a word search puzzle, e.g. `puzzle1.txt`:

    WMELKXIS
    WHWBRZDA
    SESIXUTN
    RIBAEHDI
    EFBCETKS
    TFFEHDLN
    AOSISSAC
    WKFQTSKQ

The function returns a list of all words hidden in rows (from left to right) and
columns (from top to bottom). For example, for the above puzzle, it should
return `{'MELK', 'KLAK'}`.

In order to find the words, your program needs a list of possible words.
Your `solve` function should take as second argument a filename in json format,
such as the provided `words.json`. Load this file with the json module.

Create a main function so that you can solve a given puzzle from the command
line. Use the module `getopt` or `argparse` to provide a command line
interface. It should take the puzzle file as argument; if no words file is
given as argument, it should load the default (`words.json`).

Step 3: Advanced Word Search (1 Point)
--------------------------------------

Add a feature for advanced word search; when enabled, the solve
function also find words that run backwards, i.e., from right to left or from
bottom to top. For the above puzzle, it should return `{'MELK', 'KLEM',
'CASSIS', 'KLAK', 'WATER', 'KOFFIE', 'KALK', 'INAS', 'SINAS'}`.

The feature should be invoked using an extra argument `advanced` to
the `solve` function, which defaults to False if not specified:

    def solve(puzzlefile, wordlist, advanced=False):

No unit test is provided for the bonus step; you should write your own unit test for it.
Extend your command line interface to optionally use this functionality (off by
default).

Step 4: Run the Unit Tests
--------------------------

From the current directory, run the following command:

    pytest

If you completed steps 1–2, all tests should pass. Note that additional tests
may be used to grade your work.

Run `pycodestyle` on your code and ensure there are no errors or warnings.

Final step: Submit your work
----------------------------

Run `git status` to see all the files you modified and created. There
should be two untracked files: `cdb.py` and `wordsearch.py`. `git add`
them. Commit the changes with a descriptive message.  Push them to your
private repository (the same one as previous week) using this command:

    git push

Go to https://github.com and check the files to verify all your
changes have arrived (you may have to login first).

Finally, submit via Nestor. Again, you do not have to attach any files, just
submit the URL of your private GitHub repository. Do NOT forget this step!
Without this, we cannot keep track of your work and your grades.

