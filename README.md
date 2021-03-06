# Context-Free-Grammar-Validator
This is a validator for the context-free grammar in chomsky normal form only.
It checks whether a string is valid under a given grammar -- that is, whether said string can be derived from the set of production rules defined in the grammar file.


### Context-free Grammar
Grammar is a set of production rules described using symbols and a transformation operator "->".
We can divide symbols into two groups: *Terminals* which are the symbols that make up a string and *Non-terminals* which do not.
To check the validity of a string we verify if it can be derived from the set of production rules.
For example string "aaabbb" is valid under these production rules but "ababab" is not:
```
E -> aEb
E -> ab
```
We can easily check this by applying the first rule twice and the second rule once.
But there is no way to produce "ababab".


### Chomsky normal form
A context-free grammar is said to be in Chomsky normal form when all of its production rules are of the form:
- *A* -> *BC*
- *A* -> *a*

where *A*, *B* and *C* are *Non-terminals* and *a* is a *Terminal*


### Some technical details
- Rules have to be placed in separate lines or be separated by spaces
- Spaces before and after "->" operator are mandatory
- The first symbol in the grammar file is implicitly assumed to be the origin
- `~` is a reserved character and serves the purpose of an arbitrary symbol (for example `A -> ~` means A can be transformed into any other symbol)
- `E -> {a,b,c}` is a syntactic sugar for `E -> a  E -> b E -> c` 


### Running the script
In order to run the script on a string STRING and a grammar GRAMMAR simply type:
```
python validator.py --grammar GRAMMAR STRING
```
Note that STRING can also be a text file.
Adding a `-v` flag will also validate the grammar file itself -- pretty cool, huh :)


### Some examples
```
python validator.py --grammar ARITHMETIC.txt "1 + 2*(10 - 1)*(5/3)"
> String is valid
```

```
python validator.py --grammar ARITHMETIC.txt "1 + (10 + ("
> String is not valid
```

```
python validator.py --grammar ARITHMETIC.txt "01 + 1"
> String is not valid
```


