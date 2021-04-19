# personalizedexams


## compile

```console
foo@bar:~$ MATRICULATIONID=132 SEED=12 pdflatex --enable-pipes --shell-escape exam.tex
```
compiles the pdf using SEED as the seed for the pseudo-random engine
