# GalDynPsrFreq Package

GalDynPsrFreq is a package for calculating dynamical contributions in the second derivative of the frequencies, spin or orbital, of pulsars in the Galactic field. It can calculate the fractional contributions or the excess terms, e.g. \ddot{f}/f|_excess where f is either the orbital frequency or the spin frequency. Various dynamical contributions, including the Shklovskii effect (the contribution due to the proper motion) or due to the acceleration of the pulsar caused by the gravitational potential of the Galaxy, can be calculated. Two Models- one incorporating BH in Galactic potential, and one without the BH contribution, to perform these tasks are available in the package. Using the measured values of the frequency, frequency derivative, and frequency second derivative, GalDynPsrFreq can even compute the "intrinsic" values of the frequency second derivatives, provided no other extra contribution exist. 

Details on various dynamical effects and various models to estimate those are available in Pathak and Bagchi (arXiv:).

Brief outline of usage of GalDynPsr is given below.

# 1) Install GalDynPsrFreq as pip3 install GalDynPsrFreq or pip install GalDynPsrFreq (assuming you have numpy, scipy, and galpy already installed and working)

### If wished, one can change the values of Rs (galactocentric cylindrical radius of the sun), Vs  (rotational speed of the sun) etc in parameters.in file that can be found inside the GalDynPsr (installed directory). 
## But remember that galpy also has these values defined in the file '$home/.galpyrc'. One can in principle change these values. 
# However, the Milky Way potential in galpy was fitted with Rs = 8 kpc and vs = 220 in galpy


# 2) Import GalDynPsrFreq

import GalDynPsrFreq

# 3) In all of the following modules, the ordering of the arguments of the functions are very important.

# 4) Calculate excess terms of modelX ** Very important, model names are case sensitive!

GalDynPsrFreq.modelX.Expl(ldeg,  bdeg,  dkpc) and GalDynPsrFreq.modelX.Exz(ldeg,  bdeg,  dkpc)

The function Expl() calculates the excess term due to the relative acceleration of the pulsar parallel to the Galactic plane and the function Exz() calculates the excess term due to the relative acceleration of the pulsar perpendicular to the Galactic plane. Total dynamical contribution will be the sum of above two terms. Both of the above functions takes the arguments as the Galactic longitude in degrees (say ldeg), the Galactic latitude in degrees (say bdeg), the distance of the pulsar from the solar system barycenter in kpc (say dkpc); strictly in this order. One needs to assign the values of ldeg,  bdeg,  and dkpc before calling the above functions.


Remeber to replace modelX by the model you  want to use, like modelnoBH, modelBH, etc. Model names are case sensitive!

# 5) Calculate the Shklovskii term

The Shklovskii term can be calculated as GalDynPsrFreq.Shk.Exshk(dkpc,  mul, mub) 

where mul is the proper motion in the Galactic longitude direction (mas/yr) and mub is the proper motion in the Galactic latitude direction (mas/yr). dkpc is as usual the distance of the pulsar from the solar system barycenter in kpc. One needs to assign the values of these parameters first.


# 6) Print the basic parameters of the pulsars

GalDynPsrFreq.read_parameters.Rskpc returns the Galactocentric cylindrical radius of the sun.

GalDynPsrFreq.read_parameters.Vs returns the rotational speed of the sun.

GalDynPsrFreq.read_parameters.Rpkpc(ldeg,  bdeg,  dkpc) returns the value of Galactocentric cylindrical radius of the pulsar in kpc and GalDynPsrFreq.read_parameters.z(ldeg,  bdeg,  dkpc) returns the verical height of the pulsar from the Galactic plane. The meaning of the arguments are as usual.



# 8) Calculation of instrinsic frequnecy derivative and second derivative. Ordering of the arguments is important.


First assign values of ldeg,  bdeg,  dkpc,  (meaning of the parameters are as usual) and calculate the excess terms as usual:

fex_pl =  GalDynPsrFreq.modelX.Expl(ldeg, bdeg, dkpc) # excess term parallel to the Galactic plane

fex_z =  GalDynPsrFreq.modelX.Exz(ldeg, bdeg, dkpc) # excess term perpendicular to the Galactic plane

fex_shk =  GalDynPsrFreq.Shk.Exshk(dkpc, mul, mub) # excess term due to the Shklovskii effect



Now assign the values of the frequency 'f' in Hz, the measured value of the frequency derivative 'fdot_obs' in seconds^(-2); and calculate the dynamically caused values of the frequency derivatives (in seconds^-2) as:

GalDynPsrFreq.fdotint.fdotExpl(Ex_pl,f) # due to the parallel component of the acceleration

GalDynPsrFreq.fdotint.fdotExz(Ex_z,f) # due to the perpendicular component of the acceleration

GalDynPsrFreq.fdotint.fdotShk(Ex_shk,f) # due to the Shklovskii effect

The total dynamically caused value of fdot is the addition of the above three terms. The intrinsic value of the frequency derivative can be calculated by subtracting that sum from the measured value of the frequency derivative. GalDynPsrFreq can perform this task for us by:

GalDynPsrFreq.fdotint.fdotint(Ex_pl,Ex_z,Ex_shk,fdot_obs,f) 

The total dynamical contribution in the frequency derivative, i.e. the sum of GalDynPsrFreq.fdotint.fdotExpl(Ex_pl,f) and GalDynPsrFreq.fdotint.fdotExz(Ex_z,f) can be printed as:
GalDynPsrFreq.fdotint.fdotGal(Ex_pl,Ex_z,f)


For dynamical contributions in the second derivative of frequency, we use the following modules from GalDynPsrFreq

GalDynPsrFreq.fdotdotexcBH.fdotdotexcwBHcal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk)
GalDynPsrFreq.fdotdotint.fdotdotintcal(fddotfex,f,fdotdotobs)


### All the above points will be clearer from the following examples ################



#####  Instructions to use GalDynPsrFreq #####  

# Call GalDynPsrFreq as:-


import GalDynPsrFreq

## Provide the following values in your code ###

# ldeg = Galactic logitude in degrees, bdeg = Galactic latitude in degrees, dkpc = distance to pulsar in kpc

########### Example-1 #################
ldeg =20.0

bdeg = 45.0

dkpc = 1.2

############# Extract important parameters say values of Rp (in kpc) and z (in kpc)  ##########

Rpkpc = GalDynPsr.read_parameters.Rpkpc(ldeg, bdeg, dkpc)

zkpc = GalDynPsr.read_parameters.z(ldeg, bdeg, dkpc)


#################  Compute excess Shklovskii term. Here Exshk() calculates the dynamical contribution (or the excess term) due to Shklovskii effect #################################

#### We need to provide the values of proper motion in Galactic longitude direction and proper motion in the Galactic latitude direction########

##mul = proper motion in Galactic longitude direction (mas/yr), mub = proper motion in Galactic latitude direction (mas/yr)



mul = 22.0
mub = 1.2



ExcessSh = GalDynPsrFreq.Shk.Exshk(dkpc, mul, mub)



### Example ###

############  ModelnoBH    ###############



fexpl = GalDynPsr.modelnoBH.Expl(ldeg,  bdeg,  dkpc) #calculates the planar contribution to the excess term

fexz = GalDynPsr.modelnoBH.Exz(ldeg,  bdeg,  dkpc) #calculates the perpendicular contribution to the excess term

totalfexGal = fexpl+fexz



### Example ###

############  ModelBH   ###############



fexpl = GalDynPsrFreq.modelBH.Expl(ldeg,  bdeg,  dkpc) #calculates the planar contribution to the excess term

fexz = GalDynPsrFreq.modelBH.Exz(ldeg,  bdeg,  dkpc) #calculates the perpendicular contribution to the excess term

totalfexGal = fexpl+fexz



######################### For Intrinsic frequency derivative calculations ###############################

## Parameters required for spin (or orbital) frequency derivative calcuations:- f = frequency in Hz, fdotobs = measured frequency derivative in s^-2

#fdotExpl(Excess_pl,f) calculates the planar contribution to the frequency derivative 

#fdotExz(Excess_z,f) calculates the perpendicular contribution to the frequency derivative
 
#fdotGal(Excess_pl,Excess_z,f) calculates the sum of planar and perpendicular contributions to the frequency derivative

#fdotShk(Excess_shk,f) calculates the Shklovskii contribution to the frequency derivative

#fdotint(Excess_pl,Excess_z,Excess_shk,fdotobs,f) calculates the intrinsic frequency derivative




### Example ###

#modelBH and 

ldeg = 20.
bdeg=20.
vrad = 20.
f = 50.
dkpc = 2.
mul = 20.
mub = 20.
fdotobs = -1.43e-15
fdotdotobs = 1.2e-28


fex_pl = GalDynPsrFreq.modelBH.Expl(ldeg,  bdeg,  dkpc)

fex_z = GalDynPsrFreq.modelBH.Exz(ldeg,  bdeg,  dkpc)

fex_shk = GalDynPsrFreq.Shk.Exshk(dkpc,  mul, mub)



fdotExpl =  GalDynPsrFreq.fdotint.fdotExpl(Ex_pl,f)

fdotExz =  GalDynPsrFreq.fdotint.fdotExz(Ex_z,f)

fdotGal =  GalDynPsrFreq.fdotint.fdotGal(Ex_pl,Ex_z,f)

fdotShk =  GalDynPsrFreq.fdotint.fdotShk(Ex_shk,f)

fdotint = GalDynPsrFreq.fdotint.fdotint(Ex_pl,Ex_z,Ex_shk,fdotobs,f)


######################### For Intrinsic second derivative of frequency calculations ###############################

Without BH contribution:-
fddotfex = GalDynPsrFreq.fdotdotexc.fdotdotexccal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk)

With BH contribution:-
fddotfex = GalDynPsrFreq.fdotdotexcBH.fdotdotexcwBHcal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk)

fddotint = GalDynPsrFreq.fdotdotint.fdotdotintcal(fddotfex,f,fdotdotobs)



######### Example- when working inside the GalDynPsrFreq Directory #######


import math
from modelBH import Expl
from modelBH import Exz
from Shk import Exshk
from fdotdotint import fdotdotintcal
from fdotdotexcBH import fdotdotexcwBHcal
from fdotint import fdotint
import read_parameters as par

ldeg = 20.
bdeg=20.
vrad = 20.
f = 50.
dkpc = 2.
mul = 20.
mub = 20.
fdotobs = -1.43e-15
fdotdotobs = 1.2e-28

Rpkpc = par.Rpkpc(ldeg, bdeg, dkpc)
zkpc =par.z(ldeg, bdeg, dkpc)
fex_pl= Expl(ldeg, bdeg, dkpc)
fex_z= Exz(ldeg, bdeg, dkpc)
fex_shk= Exshk(dkpc, mul, mub)
fdot_int = fdotint(fex_pl,fex_z,fex_shk,fdotobs,f)
fddotfex = fdotdotexcwBHcal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk)
fddotint = fdotdotintcal(fddotfex,f,fdotdotobs)

print(fdotobs,fdot_int,fdotdotobs,fddotint)

#####################################################################



#==========================================================================================
##### Contents of the Package ####

Datafiles:

parameters.in: Input file contains values of different constants which are subject to change with improvements in measurements. User can change the values of constants if the need be. These constants are Vs, sigVs (error in Vs), Rskpc (Rs in kpc units), sigRs (error in Rskpc), b0reid14 (dv/dR), sigb0r (error in dv/dR), b0dt91 (slope parameter), sigb0dt (error in slope parameter).

README.txt: Contents of this README.md file inside package along with code files.

Description of different codes:

read_parameters.py: Contains various constants used in the package as well as functions to calculate Rp(kpc) and z(kpc). 

modelnoBH.py: Model noBH - Calculates ‘Rforce’ in galpy (without BH) and ‘zforce’ in galpy (without BH)

modelBH.py: Model BH - Calculates ‘Rforce’ in galpy (with BH) and ‘zforce’ in galpy (with BH)

Shk.py: Calculates the Shklovskii term d(mu_T*mu_T)/c. Takes user input of proper motion in galactic longitude and galactic latitude.

galpyMWRfo.py: Using evaluateRforces function in galpy(without BH) to get (parallel component of relative accleration)/c 

galpyMWBHRfo.py: Using evaluateRforces function in galpy(with BH) to get (parallel component of relative accleration)/c

galpyMWZfo.py: Using evaluatezforces function in galpy(without BH) to get (perpendicular component of relative accleration)/c 

galpyMWBHZfo.py: Using evaluatezforces function in galpy(with BH) to get (pependicular component of relative accleration)/c

fdotint.py: Calculates frequency derivative contributions from parallel and perpendicular components relative accleration, and from Shklovskii term. Also, calculates the intrinsic frequency drivative. 

fdotdotSB1.py: Calculates first square bracket term of Eq. () of the paper Pathak and Bagchi ().

fdotdotSB2.py: Calculates second square bracket term of Eq. () of the paper Pathak and Bagchi ().

fdotdotSB3.py: Calculates third square bracket term of Eq. () of the paper Pathak and Bagchi ().

fdotdotSB4.py: Calculates fourth square bracket term of Eq. () of the paper Pathak and Bagchi ().

fdotdotexc.py: Calculates the excess second derivative of frequency by frequency ratio, using the MWPotential2014 (without BH) of galpy as the Galactic potential  

fdotdotexcBH.py: Calculates the excess second derivative of frequency by frequency ratio, using the MWPotential2014 (with BH) of galpy as the Galactic potential

fdotdotint.py: Calculates the intrinsic frequency second derivative

############################################################


