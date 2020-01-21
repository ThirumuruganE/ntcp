![icon](https://user-images.githubusercontent.com/26036836/72178678-6447d280-3409-11ea-9e48-6bb0e41f82db.png)
# EUD based NTCP Calculator
EUD based Normal Tissue Complication Probability
## Introduction
This program based on EUD phenomenological model by Niemierko.\
Using logistic function the NTCP is calculated by Niemierko\
inspired by his work and also a free Matlab calculator and radbiomod calculator this program has been created.\
"This is purely for research and not for clinical use"
## Dependencies
##### Install following packages
Python3 https://www.python.org/downloads/ \
Pandas version 0.25.3 https://pypi.org/project/pandas/ \
matplotlib version 3.1.2 https://pypi.org/project/matplotlib/ \
PrettyTable version 3.1.2 https://pypi.org/project/PrettyTable/ \
xlrd version 1.2.0 https://pypi.org/project/xlrd/ \
in case tkinter is not installed. install tkinter

## How to run

#### In Ubuntu this program just runs with double click
run the code <sudo chmod u+x ntcp.py> from the directory in which the python file is placed to double click and run the program.
and also change the preference as seen below in file manager
![readme1](https://user-images.githubusercontent.com/26036836/72175217-a10fcb80-3401-11ea-93a5-133efdac63db.png)


#### In case of other OS run the program from terminal.

## How to use
1. Take the region of interest(e.g.optic chiasm) "Differential DVH" values i.e. volume and dose in .xls format. The name of column should be in lower case as shown below.(volume and dose)

![readme](https://user-images.githubusercontent.com/26036836/72164318-79ae0400-33eb-11ea-9239-f1817b7794f4.png)

2. Import the .xls file.
3. Select parameters from menu either emami et al, or Gay and niemierko.
4. click calculate
5. In case of manual calculation enter all the parameters and click manual input button
6. before next manual. click clear button and enter the parameters from first.
7. again click manual input button.
8. click calculate.

## References
1. RADBIOMOD: A simple program for utilising biological modelling in radiotherapy plan evaluation
Chang, Joe H. et al.
Physica Medica: European Journal of Medical Physics, Volume 32, Issue 1, 248 - 254
2. Wu, Q., Mohan, R., Niemierko, A., & Schmidt-Ullrich, R. (2002). Optimization of intensity-modulated radiotherapy plans based on the equivalent uniform dose. International Journal of Radiation Oncology* Biology* Physics, 52(1), 224-235.
3. Gay, H. A., & Niemierko, A. (2007). A free program for calculating EUD-based NTCP and TCP in external beam radiotherapy. Physica Medica, 23(3-4), 115-125.

### Screenshot

![scrr](https://user-images.githubusercontent.com/26036836/72689521-37499d00-3b38-11ea-8ebd-b0b7d2bac014.png)
