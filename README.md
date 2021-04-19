# personalizedexams

This is a small framework explaining how to run python directly from LaTex. We use this to generate personalized exams. See this presentation.


Inline-style: 
![alt text](https://github.com/jensdittrich/personalizedexams/blob/main/process.png "process")


## compile

```console
foo@bar:~$ MATRICULATIONID=132 SEED=12 pdflatex --enable-pipes --shell-escape exam.tex
```
compiles the pdf using SEED as the seed for the pseudo-random engine
