import math
import numpy as np
import read_parameters as par



def fdotdotSB3cal(vrad,aT,muT,alpha):
    yrts = par.yrts
    c= par.c
    mastorad = par.mastorad

    #tsbvrad = (1./c)*(3.*(1000.0*vrad)*(((mastorad/yrts)*muT)**2.)) 
    tsbt = (1./c)*(aT*((mastorad/yrts)*muT)*math.cos(alpha) - 3.*(1000.0*vrad)*(((mastorad/yrts)*muT)**2.))
    return tsbt;

