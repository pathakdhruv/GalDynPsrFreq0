import math
import numpy as np
import read_parameters as par
from galpy.potential import evaluatezforces, evaluateRforces, evaluatePotentials
from galpy.potential import evaluatez2derivs,evaluateR2derivs,evaluateRzderivs
from galpy.util import bovy_conversion
from astropy import units as u



def fdotdotSB1cal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,vrad,coslam,alpha,appl,apz,aspl,aT,MWPot):

    Rskpc = par.Rskpc
    Vs = par.Vs
    conversion = par.conversion
    yrts = par.yrts
    c= par.c
    kpctom = par.kpctom
    Rs = Rskpc*kpctom
    mastorad = par.mastorad

    normpottoSI = par.normpottoSI
    normForcetoSI = par.normForcetoSI
    normjerktoSI = par.normjerktoSI

    b = bdeg*par.degtorad
    l = ldeg*par.degtorad

    muT = (mub**2. + mul**2.)**0.5     
 
    zdot = (1000.0*vrad)*math.sin(b)+(mastorad/yrts)*mub*(dkpc*kpctom)*math.cos(b) 
    Rpdot = (1./(Rpkpc*kpctom))*(((dkpc*kpctom)*(math.cos(b)**2.) - Rs*math.cos(b)*math.cos(l))*(1000.0*vrad) + (Rs*(dkpc*kpctom)*math.sin(b)*math.cos(l) - ((dkpc*kpctom)**2.)*math.cos(b)*math.sin(b))*((mastorad/yrts)*mub) + Rs*(dkpc*kpctom)*math.sin(l)*((mastorad/yrts)*mul))
    #phiR2a = evaluateR2derivs(MWPot,Rpkpc/Rskpc,zkpc/Rskpc)
    phiR2 = normjerktoSI*evaluateR2derivs(MWPot,Rpkpc/Rskpc,zkpc/Rskpc)
    phiz2 = normjerktoSI*evaluatez2derivs(MWPot,Rpkpc/Rskpc,zkpc/Rskpc)
    phiRz = normjerktoSI*evaluateRzderivs(MWPot,Rpkpc/Rskpc,zkpc/Rskpc)
    phiR2sun = normjerktoSI*evaluateR2derivs(MWPot,Rskpc/Rskpc,0.0/Rskpc) 
    phiRzsun = normjerktoSI*evaluateRzderivs(MWPot,Rskpc/Rskpc,0.0/Rskpc)
    aspldot = phiR2sun*Rpdot + phiRzsun*zdot
    appldot = phiR2*Rpdot + phiRz*zdot
    apzdot = phiRz*Rpdot + phiz2*zdot
    
    #if coslam != 0.0 and Rpkpc != 0.0 and math.cos(b) != 0.0:
    
    lamdot = (1./coslam)*((Rs*math.cos(l)*((mastorad/yrts)*mul))/((Rpkpc*kpctom)*math.cos(b)) - (Rs*math.sin(l)/((Rpkpc*kpctom)**2.))*Rpdot)  
    ardot1 = math.sin(b)*(appl*coslam + aspl*math.cos(l))*((mastorad/yrts)*mub)         
    ardot2 = math.cos(b)*(appldot*coslam + aspldot*math.cos(l))
    ardot3 = apzdot*math.sin(b)
    ardot4 = appl*math.cos(b)*(Rskpc*math.sin(l)/Rpkpc)*lamdot
    ardot5 = aspl*math.sin(l)*((mastorad/yrts)*mul)
    ardot6 = apz*math.cos(b)*((mastorad/yrts)*mub)
    ardot = ardot1 - ardot2 - ardot3 + ardot4 + ardot5 - ardot6
   
    jerkt = (1./c)*(ardot - aT*((mastorad/yrts)*muT)*math.cos(alpha))   
    return jerkt;
   

