# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 07:11:13 2021

@author: James Goodman
"""
import numpy as np

from IPython import get_ipython

import time

import sys

import pickle
# %%
# which pokemon should you ban me from using to give yourself the best chance of winning?
# which pokemon should I ban you from using to give myself the best chance of winning?
# which pokemon's removal would most change the GSC metagame?
# assign any positive decimal number to your estimate of how strong a teammate this pokemon is for your teams.
# assign any positive decimal number to your estimate of how strong an opponent this pokemon is for your teams.
# assign any positive decimal number to your estimate of how strong this pokemon is in the GSC metagame.

# going to do pairwise ranking instead of trying to make a big list de novo
# in part to limit biases and working memory constraints
# google scholar search term: "ranking or pairwise discrimination" or "ranking or pairwise discrimination psychophysics"

# for now, let's just assess #3:
# ya know, there was probably a way to automate this data entry
# copy-paste the list into a text document, then download that as a csv or something
# oh well, whatever
#pokemonlist = list( {'Quagsire','Machamp','Zapdos','Gengar','Marowak','Vaporeon','Rhydon','Skarmory', \
#'Blissey','Forretress','Steelix','Exeggutor','Tentacruel','Umbreon','Golem','Heracross', \
#'Starmie','Alakazam','Jolteon','Miltank','Snorlax','Misdreavus','Dragonite','Charizard', \
#'Tyranitar','Raikou','Espeon','Moltres','Cloyster','Suicune','Porygon2','Houndoom','Jynx', \
#'Smeargle','Nidoking','Articuno','Ampharos','Donphan','Scizor','Kingdra','Sandslash', \
#'Muk','Clefable','Meganium','Omastar','Venusaur','Entei','Jumpluff','Gligar','Kangaskhan', \
#'Piloswine','Aerodactyl','Typhlosion','Pikachu','Hitmonlee','Qwilfish','Shuckle','Tauros', \
#'Nidoqueen','Blastoise','Raichu','Electabuzz','Ursaring','Slowbro','Lapras','Lanturn', \
#'Politoed','Crobat','Electrode','Victreebel'} ) # trim

# print('%s %s' % ('hello', 'world'))

# q = input('which is better: %s or %s?: ' % ('pizza (P)','burgers (B)'))

# %% input method that properly handles interrupts
# except, y'know, it DOESN'T AT ALL!!!!!!!!
#def bing(promptstring):
#    try:
#        usrinput_ = input(promptstring)
#        return usrinput_
#    except:
#        print('wtf')
#        sys.exit()
# %% stratify pokemon by tier
# here, we simply list everything exhaustively
OUpokes   = list({'Blissey','Cloyster','Exeggutor','Forretress','Gengar','Golem','Heracross',\
           'Jynx','Machamp','Marowak','Miltank','Misdreavus','Nidoking','Raikou',\
           'Rhydon','Skarmory','Snorlax','Starmie','Steelix','Suicune','Tyranitar','Umbreon',\
           'Vaporeon','Zapdos'})
BLpokes = list({'Aerodactyl','Alakazam','Articuno','Charizard','Clefable','Donphan','Dragonite','Entei',\
           'Espeon','Houndoom','Jolteon','Kangaskhan','Kingdra','Lapras','Meganium','Moltres','Muk',\
           'Porygon2','Scizor','Smeargle','Tauros','Tentacruel','Typhlosion','Ursaring','Venusaur'})
# this includes NUBL as well. I cull all pokemon which are not fully evolved (except for Scyther, since his BST doesn't change upon evolution, and Pikachu, whose Light Ball makes it a stronger attacker than its evolution, Raichu).
UUpokes   = list({'Ampharos','Arcanine','Bellossom','Blastoise','Crobat','Dodrio',\
                  'Electabuzz','Electrode','Girafarig','Gligar','Granbull','Gyarados',\
                  'Hypno','Jumpluff','Kabutops','Lanturn','Magneton','Mr. Mime','Nidoqueen',\
                  'Omastar','Pikachu','Piloswine','Pinsir','Politoed','Quagsire','Qwilfish',\
                  'Sandslash','Scyther','Slowbro','Slowking','Victreebel','Vileplume',\
                  'Feraligatr','Golduck','Poliwrath','Raichu'})
# this list again culls everything which is not fully evolved. There are no compelling exceptions, unlike in UU. I also omit Unown because come the fuck on.
NUpokes    = list({'Aipom','Arbok','Ariados','Azumarill','Beedrill','Butterfree','Corsola',\
                   'Delibird','Dewgong','Ditto','Dugtrio','Dunsparce','Farfetch\'d',\
                   'Fearow','Flareon','Furret','Hitmonchan','Hitmonlee','Hitmontop',\
                   'Kingler','Ledian','Lickitung','Magcargo','Magmar','Mantine','Murkrow',\
                   'Ninetales','Noctowl','Octillery','Parasect','Persian','Pidgeot',\
                   'Primeape','Rapidash','Raticate','Seaking','Shuckle','Sneasel','Stantler',\
                   'Sudowoodo','Sunflora','Tangela','Togetic','Venomoth','Weezing',\
                   'Wigglytuff','Wobbuffet','Xatu','Yanma'})


catpokes  = OUpokes + BLpokes + UUpokes + NUpokes
randinds  = np.random.permutation(len(catpokes))

catpokes  = [ catpokes[randinds[x]] for x in range(len(randinds)) ]


# %%
exec(open("quicksort_test.py").read())

# %% test
#qq = ['C','B','D','A']
#quickSort(qq,0,3)

# %%
npokes       = len(catpokes)
quickSort(catpokes,0,npokes-1)
        
sortedlist = catpokes
# %%
with open('viabilitylist.pickle', 'wb') as handle:
    pickle.dump(sortedlist, handle, protocol=pickle.HIGHEST_PROTOCOL)

# %%
with open('viabilitylist.pickle', 'rb') as handle:
    b = pickle.load(handle)

# %%
print(sortedlist == b)
        
        
        
        
        