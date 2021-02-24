Assignment for Week 4
=====================

Get the Starter Code
--------------------

On the command line, unzip the assigment and add it to your repository:

	$ unzip week4.zip
	$ git add [...]
	$ git commit [...]

Problem: extract tokenized sentences from idiosyncratic text file
-----------------------------------------------------------------

The files `nos*.txt.gz` are gzip-compressed files which contain news articles
from nos.nl, February 2021. The goal of this assignment is to extract all
sentences from such a file in tokenized format. In the output, each line
consists of a sentence where all tokens (words or punctuation) are separated by
a single space.

As you can see in the example document, articles start and end with some
meta-information and headings which we ignore for the purpose of this exercise.
In the body of the article, paragraphs are easily recognized because each
paragraph starts on a new line. The identification of sentences and tokens is
much harder!

Examples of the required output for the `nos*.txt.gz` files is provided
in the corresponding `nos*.sents` files.

Your program `extract_sents.py` should take a single file name argument, which
is the compressed input file. It should write the resulting tokenized sentences
to standard output. Thus, we will run your program as follows:

    python3 extract_sents.py nos001.txt.gz > output.sents
    diff output.sents nos001.sents

Here, `diff` is the standard Unix command which shows the differences between
two similar files (including whitespace differences!). Use this command to test
your code on the given files.

It is quite tricky to build a sentence splitter / tokenizer which handles
all possible exceptions and difficult cases. We will evaluate your solution by
comparing it not only on the basis of the data given in the assigment, but also
on texts from De Volkskrant.
To get 6 points, ensure that your tokenizer reproduces the tokenization of the
supplied articles (you can add a special case for each mistake it makes).
The remaining points are awarded for well-structured and readable code, and
based on the performance of the tokenizer on other news articles.

You are not allowed to use an existing library such as NLTK or Spacy. You
should write your own code. It is recommended to solve the task systematically in
several steps:

1. remove unwanted text
2. split text in sentences
3. split sentences into tokens (punctuation/words)
4. handle special cases (these are often language-specific!)

In a rule-based system, adding a rule can affect other rules. The order of
rules can also be important (special cases should be applied before general
cases). You can write some tests for simple and tricky cases. This way you can
ensure that adding a rule does not introduce new mistakes.

Hint: read the Python regular expression documentation carefully. To match
sentences spread over multiple lines, you may need to use the `re.DOTALL` flag.

Final: Submit Your Work
------------------------

Use `pycodestyle` to check your code for issues. Run `git status` to see all
the files you modified and created. Add them all and commit the changes with a
meaningful message. Push them to your private repository. Go to GitHub and
check the files to verify all your changes have arrived.

Finally, submit the URL of your private GitHub repository via Nestor.
Do NOT forget this step!
