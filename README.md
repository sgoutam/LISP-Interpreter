# LISP-Interpreter
###Built up on the LISP Interpreter by Peter Norvig  
This is a terminal based interpreter for the esoteric language Lisp ( or CLISP ).  
I was learning compiler design when I came across Peter Norvigs' blog on LISP.
I used his program, split it up into modules, built a run-time environment for it to work on.  
I still have to work on it though. I wanted to build a compiler for a self made functional language.  
Will work on it once I get some free time.
Lisp is the second-oldest high-level programming language after Fortran.

Today, the most widely known general-purpose Lisp dialects are Common Lisp and Scheme.

Lisp was invented by John McCarthy in 1958 while he was at the Massachusetts Institute of Technology (MIT). It is machine-independent.

It is expression-based. LISP expressions are called symbolic expressions or s-expressions. Any s-expression is a valid program. LISP programs run either on an interpreter or as compiled code. The interpreter checks the source code in a repeated loop, which is also called the read-evaluate-print loop (REPL). It reads the program code, evaluates it, and prints the values returned by the program.

Mentioned below are some valid S-Expressions and valid Scheme code.

- (+ 9 11 7) ;Return 27 as result when run on the command line (interpreter)

- (write(+ 9 11 7)) ;This is to run the program as a compiled code.

- (write(+ (* (/ 9 5) 60) 32)) ;It uses prefix notation. Easier to generate parse trees

- (write-line "Hello World") ;Classic Hello World Program

LISP is case-insensitive.

An atom is a number or string of contiguous characters. It includes numbers and special characters.

Valid Atoms:

- hello

- name

- abc123

- *hello*

- 1234567

A **list** is a sequence of atoms and/or other lists enclosed in parentheses.

-   (this is a list)
-   (a (b c) d (e (f g)))

A **string** is a group of characters enclosed in double quotation marks.

-   "Hello World"
-   "(a (b c)) within quotes is a string not a list"
-   Functions in LISP are also treated as a list.
-   cos(45) is written as (cos 45)

f(x) will be written as (f x)

Modules
-------

### *1.**  Lexical analysis *

Lexical analysis is the first phase of a compiler. It takes the modified source code from language preprocessors that are written in the form of sentences. The lexical analyzer breaks these syntaxes into a series of tokens, by removing any whitespace or comments in the source code.

If the lexical analyzer finds a token invalid, it generates an error. The lexical analyzer works closely with the syntax analyzer. It reads character streams from the source code, checks for legal tokens, and passes the data to the syntax analyzer when it demands.

### *2\. Syntax analysis and Semantic analysis*

Syntax analysis or parsing is the second phase of a compiler. In this chapter, we shall learn the basic concepts used in the construction of a parser.

 A lexical analyzer can identify tokens with the help of regular expressions and pattern rules. But a lexical analyzer cannot check the syntax of a given sentence due to the limitations of the regular expressions. Regular expressions cannot check balancing tokens, such as parenthesis. Therefore, this phase uses context-free grammar (CFG), which is recognized by push-down automata.

Semantics of a language provide meaning to its constructs, like tokens and syntax structure. Semantics help interpret symbols, their types, and their relations with each other. Semantic analysis judges whether the syntax structure constructed in the source program derives any meaning or not.

### *3\. Intermediate Code Generation*

A source code can directly be translated into its target machine code, then why at all we need to translate the source code into an intermediate code which is then translated to its target code.

- If a compiler translates the source language to its target machine language without having the option for generating intermediate code, then for each new machine, a full native compiler is required.

- Intermediate code eliminates the need of a new full compiler for every unique machine by keeping the analysis portion same for all the compilers.

- The second part of compiler, synthesis, is changed according to the target machine.

- It becomes easier to apply the source code modifications to improve code performance by applying code optimization techniques on the intermediate code.

### *4\. Code Optimization*

Optimization is a program transformation technique, which tries to improve the code by making it consume less resource (i.e. CPU, Memory) and deliver high speed.

In optimization, high-level general programming constructs are replaced by very efficient lowlevel programming codes. A code optimizing process must follow the three rules given below:

- The output code must not, in any way, change the meaning of the program.

- Optimization should increase the speed of the program and if possible, the program should demand less number of resources.

- Optimization should itself be fast and should not delay the overall compiling process.

### *5\. Code Generator*

Code generation can be considered as the final phase of compilation. Through post code generation, optimization process can be applied on the code, but that can be seen as a part of code generation phase itself. The code generated by the compiler is an object code of some lower-level programming language, for example, assembly language. We have seen that the source code written in a higher-level language is transformed into a lower-level language that results in a lower-level object code, which should have the following minimum properties:

- It should carry the exact meaning of the source code.

- It should be efficient in terms of CPU usage and memory management.

***6\. REPL (Read-Evaluate-Print-Loop)***

 This module creates an input prompt for the input of expressions. Works similar to the terminal prompt. It takes the input expression and then sends the expression for evaluation.

***7\. Parser***

This module splits the input expression into lexemes and converts them into atoms and then converts these atoms into semantic rules based on the environment definition in "lispeval.py"

***8\. Eval***

In this module, we evaluate the semantic expressions obtained earlier for the given expression based on Python compiler
