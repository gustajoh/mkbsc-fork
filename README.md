# Multiplayer Knowledge Based Subset Construction Fork

Authors: Gustaf Bergmark & Gustaf Johansson

This forked version adds compatability with our [MAGIIAN game generator and statistical analysis tools.](https://github.com/gustafbergmark/MKBSC-Statistical-Analysis)

An extensive description of the mkbsc implementation can be found in the [original repo](https://github.com/HelmerNylen/mkbsc) developed by August Jacobsson & Helmer Nylén

## Requirements
This library uses the following external programs, which need to be installed for the library to work.
- [NetworkX](https://networkx.github.io/), which can be installed via `pip3 install networkx`
- [pydot](https://github.com/erocarrera/pydot), which can be installed via `pip3 install pydot`
- [Graphviz](https://www.graphviz.org/), which can be downloaded from their website

Note: the library was written for Python 3.5, NetworkX 2.1 and pydot 1.2.4. To increase the chance that everything works as intended you may wish to use those versions.

## Our additions

A few but important functions were added in order to make this implementation of the MKBSC usable with our random MAGIIAN game generator.

### main.py
In `generatedgames.txt` you will find the same set of 5 randomly generated MAGIIAN games we provided [here,](https://github.com/gustafbergmark/MKBSC-Statistical-Analysis) the idea is that you can generate a set of games with our generator and plug that file into `main.py` which will apply the MKBSC and determine whether they are stable or divergent. It will then update the `stable` value and write to `analysedgames.txt`. This will in turn make it possible to make use of the statistical analysis tools provided here https://github.com/gustafbergmark/MKBSC-Statistical-Analysis.

### firstIteration.py
During our research project we felt that it might be interesting to analyse only the first expansion of MAGIIAN games, so this function takes a set of games and prints the first iteration of each game to another file. The `firstiterations.txt` file is the result when the 5 generated games provided in `generatedgames.txt` is used with the function.

### print.py
This function looks at each game from a set of games and generates a folder with pictures of the game itself and the first 4 expansions. The generated folders are labeled in such a way that it tells you if the game is divergent or stable. **OBS!** it's very important that you have the "pictures" folder downloaded otherwise this will not work.

### parse.py
This is a helper function which reformats the data from a generated MAGIIAN in such a way that the implemented MKBSC can be ran on it.


