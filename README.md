# personalizedexams

This is a small framework explaining how to run python directly from LaTex. We use this to generate personalized exams. See this presentation.

## General compilation process:
![alt text](https://github.com/jensdittrich/personalizedexams/blob/main/process1.png "process")

## Create problem and solution separately:
![alt text](https://github.com/jensdittrich/personalizedexams/blob/main/process2.png "process")

## Create many variants of the same exam:
![alt text](https://github.com/jensdittrich/personalizedexams/blob/main/process3.png "process")

## compile

```console
foo@bar:~$ MATRICULATIONID=132 SEED=12 pdflatex --enable-pipes --shell-escape exam.tex
```
compiles the pdf using SEED as the seed for the pseudo-random engine
