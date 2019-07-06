# Wiki Scraper
## Purpose
This program tests the hypothesis that the Philosophy page on Wikipedia is reachable from any other Wikipedia page,
simply by clicking the first link in each article that points to another Wikipedia page.

The program finds the first qualifying link on each page, starting from a given article, and recursively
iterates until reaching the Philosophy page or finding a loop in the graph.

## Requirements
* beautifulsoup4==4.7.1
* certifi==2019.6.16
* chardet==3.0.4
* idna==2.8
* requests==2.22.0
* soupsieve==1.9.2
* urllib3==1.25.3

requirements.txt provided for convenience.

## Execution
Execute wiki_scraper.py in the terminal, using the Python 3 interpreter.
For example, 
```
python3 wiki_scraper.py
```

You will be prompted to provide a URL to an English Wikipedia page, e.g.
```
Please enter the URL of the first Wikipedia page: https://en.wikipedia.org/wiki/Python_(programming_language)
```

## Output
The process will complete and then write to standard output, e.g.

```
Please enter the URL of the first Wikipedia page: https://en.wikipedia.org/wiki/Python_(programming_language)

The process took 27 steps to terminate.


Python (programming language) (https://en.wikipedia.org/wiki/Python_(programming_language))
Interpreted language (https://en.wikipedia.org/wiki/Interpreted_language)
Programming language (https://en.wikipedia.org/wiki/Programming_language)
Formal language (https://en.wikipedia.org/wiki/Formal_language)
Mathematics (https://en.wikipedia.org/wiki/Mathematics)
Ancient Greek (https://en.wikipedia.org/wiki/Ancient_Greek)
Greek language (https://en.wikipedia.org/wiki/Greek_language)
Modern Greek (https://en.wikipedia.org/wiki/Modern_Greek)
Dialect (https://en.wikipedia.org/wiki/Dialect)
Latin (https://en.wikipedia.org/wiki/Latin)
Classical language (https://en.wikipedia.org/wiki/Classical_language)
Language (https://en.wikipedia.org/wiki/Language)
Linguistic system (https://en.wikipedia.org/wiki/Linguistic_system)
Ferdinand de Saussure (https://en.wikipedia.org/wiki/Ferdinand_de_Saussure)
Switzerland (https://en.wikipedia.org/wiki/Switzerland)
Sovereign state (https://en.wikipedia.org/wiki/Sovereign_state)
International law (https://en.wikipedia.org/wiki/International_law)
Nation (https://en.wikipedia.org/wiki/Nation)
Community (https://en.wikipedia.org/wiki/Community)
Level of analysis (https://en.wikipedia.org/wiki/Social_unit)
Social science (https://en.wikipedia.org/wiki/Social_science)
Discipline (academia) (https://en.wikipedia.org/wiki/Discipline_(academia))
Knowledge (https://en.wikipedia.org/wiki/Knowledge)
Fact (https://en.wikipedia.org/wiki/Fact)
Reality (https://en.wikipedia.org/wiki/Reality)
Object of the mind (https://en.wikipedia.org/wiki/Object_of_the_mind)
Object (philosophy) (https://en.wikipedia.org/wiki/Object_(philosophy))
Philosophy (https://en.wikipedia.org/wiki/Philosophy)
```
