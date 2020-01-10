# EUD based NTCP Calculator
EUD based Normal Tissue Complication Probability
# Introduction
This program based on EUD phenomenological model by Niemierko.
Using logistic function the NTCP is calculated by Niemierko
inspired by his work and also a free Matlab calculator and radbiomod calculator this program has been created.
"This is purely for research and not for clinical use"
# Dependencies
Python3 https://www.python.org/downloads/
Pandas version 0.25.3 https://pypi.org/project/pandas/
matplotlib version 3.1.2 https://pypi.org/project/matplotlib/
PrettyTable version 3.1.2 https://pypi.org/project/PrettyTable/
xlrd version 1.2.0 https://pypi.org/project/xlrd/
in case tkinter is not installed. install tkinter

# How to Use
1)export Differential DVH in csv format from TPS.
2) save thr volume and dose for region of interest in .xls format
3) like the below picture
![excel](/home/thirumurugan/Pictures/readme.png)
2) The dose and volume columns are given title as dose and volume. every character should be in lower case.
3) a sample speadsheet is attached for reference
4)
5) First step import the .xls file
6) 2 nd step choose either emami et all parameters from menu in top left corner or from Niemierko menu
7) 3 rd step click calculate
# manual value entry
1) import file 
2) click clear button
3) type parameters in the box
4) click manual value entry button
5) click calculate
6) if needed to do next manual entry. click clear button before entering values.
7) please dont change just a single parameter. click clear and retype all values from start

