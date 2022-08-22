# VR-scripts
 
"VR" being "viability rankings"

Here, I wrote a couple of quick scripts to automate a binary ranking procedure. 

Basically, it uses a sorting algorithm and assumes persistent transitivity among options to efficiently rank dozens of alternatives via serial A/B testing.

I never had a reason to scale it beyond my own personal use case, though.

You can run yourself through the test sequence by cd'ing to the directory of this repo and typing `python -m viabilityranking` into your command line (assuming you have a python install).

And thereafter print the result by typing `python -m displayList`.

Sorry for getting your hopes up if you're into virtual reality.

A proof-of-concept virtual reality environment is in another repo of mine, though: https://github.com/jmgoodman/MuJoCo-For-Wheatstone-VR