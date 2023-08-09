#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:48:37 2023

@author: ljnolan

Zotool Version 1.0

This tool is meant to make corrections to the standard output .bib file from
Zotero.  I hope it will be generally useful to a wide audience, but it is
written from an astronomy perspective, mostly pulling from NASA/Harvard ADS.
"""

def zotool(bib, journal_dict=None, annoy=True):
# =============================================================================
# This function takes the path of a .bib file from Zotero (str bib), and an
# optional dictionary of journal abbreviations.  Included in this file is one
# for AASTeX. The function assumes that, in the case of similar journal names
# (i.e. Astrophysical Journal, Astrophysical Journal Letters), the longest name
# should override the shorter ones. There is also a toggle (boolean annoy) for
# a couple behaviors I want, such as renaming a particular citation.
#
# DISCLAIMER: I have BetterBibTex installed in my Zotero but I have things set
# to use Zotero's default behavior so this probably isn't needed.
# =============================================================================
   with open(bib, 'r') as file:
      data = file.readlines()
      
   for n, line in enumerate(data):
      if annoy:
         annoy_dict={'collaboration_observation_2016':'LIGO_observation_2016'}
         for key in annoy_dict.keys():
            while key in line:
               targ = line.find(key)
               line = line[:targ] + annoy_dict[key] + line[targ+len(key):]
      if journal_dict is not None:  
         if 'journal = ' in line:
            ed = False
            for key in journal_dict.keys():
               wk = line.find(key)
               if wk > 0:
                  if not ed:
                     ed = True
                     dupesave = key
                     repla = journal_dict[key]
                     wherkey = wk
                  else:
                     if len(key) > len(dupesave):
                        dupesave = key
                        repla = journal_dict[key]
                        wherkey = wk
            if ed:
               if dupesave == '{\\textbackslash}':
                  mor = len(dupesave)
                  line = line[:wherkey] + repla + line[wherkey+mor:]
               else:
                  whbr = line.find('{') + 1
                  line = line[:whbr] + repla + '},'
      data[n] = line
            
   with open(bib, 'w') as file:
      file.writelines(data)
   return


aas_dict_rev = {'\\aj':'Astronomical Journal',
'\\araa':'Annual Review of Astronomy and Astrophysics',
'\\apj':'Astrophysical Journal',
'\\apjl':'Astrophysical Journal Letters',
'\\apjs':'Astrophysical Journal Supplement',
'\\ao':'Applied Optics',
'\\apss':'Astrophysics and Space Science',
'\\aap':'Astronomy and Astrophysics',
'\\aapr':'Astronomy and Astrophysics Reviews',
'\\aaps':'Astronomy and Astrophysics, Supplement',
'\\azh':'Astronomicheskii Zhurnal',
'\\baas':'Bulletin of the AAS',
'\\icarus':'Icarus',
'\\jrasc':'Journal of the RAS of Canada',
'\\jaavso':'Journal of the American Association of Varialbe Star Observers',
'\\memras':'Memoirs of the RAS',
'\\mnras':'Monthly Notices of the Royal Astronomical Society',
'\\pra':'Physical Review A: General Physics',
'\\prb':'Physical Review B: Solid State',
'\\prc':'Physical Review C',
'\\prd':'Physical Review D',
'\\pre':'Physical Review E',
'\\prl':'Physical Review Letters',
'\\psj':'Planetary Science Journal',
'\\pasp':'Publications of the ASP',
'\\pasj':'Publications of the ASJ',
'\\qjras':'Quarterly Journal of the RAS',
'\\skytel':'Sky and Telescope',
'\\solphys':'Solar Physics',
'\\sovast':'Soviet Astronomy',
'\\ssr':'Space Science Reviews',
'\\zap':'Zeitschrift fuer Astrophysik',
'\\nat':'Nature',
'\\iaucirc':'IAU Cirulars',
'\\aplett':'Astrophysics Letters',
'\\apspr':'Astrophysics Space Physics Research',
'\\bain':'Bulletin Astronomical Institute of the Netherlands',
'\\fcp':'Fundamental Cosmic Physics',
'\\gca':'Geochimica Cosmochimica Acta',
'\\grl':'Geophysics Research Letters',
'\\jcp':'Journal of Chemical Physics',
'\\jgr':'Journal of Geophysics Research',
'\\jqsrt':'Journal of Quantitiative Spectroscopy and Radiative Trasfer',
'\\memsai':'Mem. Societa Astronomica Italiana',
'\\nphysa':'Nuclear Physics A',
'\\physrep':'Physics Reports',
'\\physscr':'Physica Scripta',
'\\planss':'Planetary Space Science',
'\\procspie':'Proceedings of the SPIE',
'\\actaa':'Acta Astronomica',
'\\caa':'Chinese Astronomy and Astrophysics',
'\\cjaa':'Chinese Journal of Astronomy and Astrophysics',
'\\jcap':'Journal of Cosmology and Astroparticle Physics',
'\\na':'New Astronomy',
'\\nar':'New Astronomy Review',
'\\pasa':'Publications of the Astron. Soc. of Australia',
'\\rmxaa':'Revista Mexicana de Astronomia y Astrofisica',
'\\maps':'Meteoritics and Planetary Science',
'\\aas':'American Astronomical Society Meeting Abstracts',
'\\dps':'American Astronomical Society/Division for Planetary ' + 
'Sciences Meeting Abstracts',
'\\':'{\\textbackslash}'}

aas_dict = {v: k for k, v in aas_dict_rev.items()}
bibfile = 'Paper/fabulovs22.bib'
zotool(bibfile, journal_dict=aas_dict)
