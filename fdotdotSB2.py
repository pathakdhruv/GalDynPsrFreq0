import math
import numpy as np
import read_parameters as par
from Shk import Exshk
from galpy.potential import MWPotential2014
from galpy.potential import KeplerPotential
from galpy.potential import evaluatezforces, evaluateRforces, evaluatePotentials
from galpy.potential import evaluatez2derivs,evaluateR2derivs,evaluateRzderivs
from galpy.util import bovy_conversion
from astropy import units as u




def fdotdotSB2cal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,fex_pl,fex_z,fex_shk,appl,apz,aspl):

    Rskpc = par.Rskpc
    Vs = par.Vs

    yrts = par.yrts
    c= par.c
    kpctom = par.kpctom
    Rs = Rskpc*kpctom
    mastorad = par.mastorad
    b = bdeg*par.degtorad
    l = ldeg*par.degtorad
    fex_tot = fex_pl + fex_z + fex_shk

    be = (dkpc/Rskpc)*math.cos(b) - math.cos(l)
    coslam =  be*(Rskpc/Rpkpc)

    res1 = 2.*(mastorad/yrts)*(mub*((math.sin(b)/c)*(appl*coslam + aspl*math.cos(l)) - (math.cos(b)/c)*apz) - mul*(math.sin(l)/c)*(appl*(Rskpc/Rpkpc)-aspl))

    res2 = 2.*fex_tot*(math.cos(b)*math.cos(l)*(aspl/c) + (mastorad/yrts)*mub*(1000.*Vs/c)*math.sin(b)*math.sin(l) - (mastorad/yrts)*mul*(1000.*Vs/c)*math.cos(l))

    res= res1+res2
    return res;


