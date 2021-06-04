# PyQt5-delineate-Project
The Pyqt5-delineate project adds a GUI (graphical user interface) as well as a series of other functionalities to delineate - a Python commandline tool for species delimitation.

Given a known population tree and optionally a speciation completion rate, calculate the probability of different partitions of population lineages into species, with the partition of the highest probability corresponding to the maximum likelihood species delimitation estimate. and makes the program compatible with Python 3. To see the original code of delineate, please visit [link] (https://github.com/jeetsukumaran/delineate).


By default, delineate-estimate will enumerate all possible partitions and their probabilities. For many studies, this will result in massive datafiles, hundreds to thousands of gigabytes, as millions or millions of millions or more partitions are written out. Remember, the number of partitions for a dataset of n lineages is the nth Bell number. For most studies, the vast majority of these partitions will be of very, very, very low probability. Considerable savings in time, disk space, and a significant slow down of the heat death of the universe can be achieved by restricting the report to only most probable partitions that collectively contribute to most of the probability.

Pyqt5-delineate furthermore implements the output of results in the .spart format, developed to provide a uniform and standardized format for species partition results.


# Features

* Spart format export option


# How to use it

* To open it as the original commandline tool.
```
python3 delineateestimate.py --help
```
Please use "lionepha-p095-hkyg.mcct-mean-age.tree.nex" as sample species tree file and "lionepha.run1.tsv" as constraint file.

* To use it as GUI tool.

```
 python3 estimate.py
 ```

  Please type on your terminal and follow the instructions. Please use "lionepha-p095-hkyg.mcct-mean-age.tree.nex" as sample species tree file and "lionepha.run1.tsv" as constraint file.  
