# GalDynPsrFreq Package

GalDynPsrFreq is a package for calculating dynamical contributions in the second derivative of the frequencies, spin or orbital, of pulsars in the Galactic field. It can calculate the fractional contributions or the excess terms, e.g. \dot{f}/f|_excess and \ddot{f}/f|_excess, where f is either the orbital frequency or the spin frequency. Various dynamical contributions to the first derivative of frequency (spin or orbital), including the Shklovskii effect (the contribution due to the proper motion) or due to the acceleration of the pulsar caused by the gravitational potential of the Galaxy, can also be calculated. For the case of calculating the excess terms in the first derivative of frequency, as well as, the case for the second derivative of frequency, two models are available for each case- one incorporating BH in Galactic potential, and one without the BH contribution. Using the measured values of the frequency, frequency derivative, and frequency second derivative, GalDynPsrFreq can even compute the "intrinsic" values of the frequency derivative, as well as, the frequency second derivative, provided no other extra contribution exist. 

Details on various dynamical effects and formalism to estimate those are available in Pathak and Bagchi (arXiv: 1909.13113).

Brief outline of usage of GalDynPsr is given below.

# 1) Install GalDynPsrFreq as pip3 install GalDynPsrFreq (assuming you have numpy, scipy, and galpy already installed and working)

### If wished, one can change the values of Rs (galactocentric cylindrical radius of the sun), Vs  (rotational speed of the sun) etc in parameters.in file that can be found inside the GalDynPsrFreq (installed directory). 
## But remember that galpy also has these values defined in the file '$home/.galpyrc'. One can in principle change these values. 
# However, the Milky Way potential in galpy was fitted with Rs = 8 kpc and vs = 220 in galpy.


# 2) Import GalDynPsrFreq

import GalDynPsrFreq


# 3) In all of the following modules, the ordering of the arguments of the functions are very important.


# 4)

A) Observable parameters needed to compute \dot{f}/f|_excess and \dot{f}/f|_intrinsic: Galactic longitude in degrees (say ldeg), Galactic latitude in degrees (say bdeg), the distance of the pulsar from the solar system barycenter in kpc (say dkpc), proper motion in Galactic longitude in mas/yr (say mul), proper motion in Galactic latitude in mas/yr (say mub), frequency in Hz (say f), and observed frequency derivative in s^{-2} (say fdotobs).

B) Observable parameters needed to compute \ddot{f}/f|_excess and \ddot{f}/f|_intrinsic: Galactic longitude in degrees (say ldeg), Galactic latitude in degrees (say bdeg), the distance of the pulsar from the solar system barycenter in kpc (say dkpc), proper motion in Galactic longitude in mas/yr (say mul), proper motion in Galactic latitude in mas/yr (say mub), radial component of the relative velocity of the pulsar with respect to the solar system barycenter in km/s (say vrad), frequency in Hz (say f), observed frequency derivative in s^{-2} (say fdotobs), and observed frequency second derivative in s^{-3} (say fdotdotobs).  

The frequency and its derivatives can either be spin or orbital.



# 5) Calculate excess terms for the first frequency derivative using either the model that does not take into account BH contribution to Milky Way Potential (modelnoBH), or the model that takes into account BH contribution to Milky Way Potential (modelBH). For the purpose of understanding their usage let us refer to them as modelX ** Very important, model names are case sensitive!

GalDynPsrFreq.modelX.Expl(ldeg, bdeg, dkpc) and GalDynPsrFreq.modelX.Exz(ldeg, bdeg, dkpc)

The function Expl() calculates the excess term due to the relative acceleration of the pulsar parallel to the Galactic plane and the function Exz() calculates the excess term due to the relative acceleration of the pulsar perpendicular to the Galactic plane. Total dynamical contribution from Galactic potential will be the sum of above two terms. One needs to assign the values of ldeg,  bdeg, and dkpc before calling the above functions.

Remember to replace modelX by the model you want to use, i.e., modelnoBH or modelBH. Model names are case sensitive!



# 6) Calculate the Shklovskii term contribution to the frequency derivative

The Shklovskii term can be calculated as GalDynPsrFreq.Shk.Exshk(dkpc,  mul, mub) 

where mul is the proper motion in the Galactic longitude direction (mas/yr) and mub is the proper motion in the Galactic latitude direction (mas/yr). dkpc is as usual the distance of the pulsar from the solar system barycenter in kpc. One needs to assign the values of these parameters first. This term is independent of the Galactic potential model.



# 7) Print the basic parameters of the pulsars

GalDynPsrFreq.read_parameters.Rskpc returns the Galactocentric cylindrical radius of the sun.

GalDynPsrFreq.read_parameters.Vs returns the rotational speed of the sun.

GalDynPsrFreq.read_parameters.Rpkpc(ldeg,  bdeg,  dkpc) returns the value of Galactocentric cylindrical radius of the pulsar in kpc.

GalDynPsrFreq.read_parameters.z(ldeg,  bdeg,  dkpc) returns the perpendicular displacement of the pulsar from the Galactic plane. 
The meaning of the arguments are as usual.



# 8) Calculation of instrinsic frequency derivative. Ordering of the arguments is important.

First assign values of ldeg,  bdeg, and dkpc  (meaning of the parameters are as usual), and calculate the excess terms for frequency first derivative as usual:

fex_pl =  GalDynPsrFreq.modelX.Expl(ldeg, bdeg, dkpc) # excess term parallel to the Galactic plane

fex_z =  GalDynPsrFreq.modelX.Exz(ldeg, bdeg, dkpc) # excess term perpendicular to the Galactic plane

fex_shk =  GalDynPsrFreq.Shk.Exshk(dkpc, mul, mub) # excess term due to the Shklovskii effect


Now assign the values of the frequency 'f' in Hz, the measured value of the frequency derivative 'fdotobs' in seconds^(-2); and calculate the dynamically caused values of the frequency derivatives in seconds^(-2) as:

GalDynPsrFreq.fdotint.fdotExpl(fex_pl,f) # due to the parallel component of the acceleration

GalDynPsrFreq.fdotint.fdotExz(fex_z,f) # due to the perpendicular component of the acceleration

GalDynPsrFreq.fdotint.fdotShk(fex_shk,f) # due to the Shklovskii effect

The total dynamically caused value of fdot is the addition of the above three terms. The intrinsic value of the frequency derivative can be calculated by subtracting that sum from the measured value of the frequency derivative. GalDynPsrFreq can perform this task for us by:

GalDynPsrFreq.fdotint.fdotint(Ex_pl,Ex_z,Ex_shk,fdotobs,f) 

The total dynamical contribution due to the Galactic potential in the frequency derivative, i.e. the sum of GalDynPsrFreq.fdotint.fdotExpl(Ex_pl,f) and GalDynPsrFreq.fdotint.fdotExz(Ex_z,f) can be printed as:

GalDynPsrFreq.fdotint.fdotGal(Ex_pl,Ex_z,f)



# 9) Calculation of excess terms in the frequency second derivative. Ordering of the arguments is important.

For dynamical contributions in the second derivative of frequency, we use the following modules from GalDynPsrFreq

a)When not incorporating BH contribution to Milky Way Potential: Model fdotdotexc -
fddotfex = GalDynPsrFreq.fdotdotexc.fdotdotexccal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk) 

b) When incorporating BH contribution to Milky Way Potential: Model fdotdotexcBH -
fddotfex = GalDynPsrFreq.fdotdotexcBH.fdotdotexcwBHcal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk)

Arguments fex_pl,fex_z, and fex_shk are defined in point 8, while the rest of the argument definitions are described in point 4.  



# 10) Calculation of intrinsic frequency second derivative. Ordering of the arguments is important.

GalDynPsrFreq.fdotdotint.fdotdotintcal(fddotfex,f,fdotdotobs)

fddotfex is the excess terms in the frequency second derivative, defined in point 9. The rest of the argument definitions are described in point 4. 



### All the above points will be clearer from the following demonstration ################



#####  Instructions to use GalDynPsrFreq #####  

# Call GalDynPsrFreq as:-


import GalDynPsrFreq


#### Provide the following values in your code ####

# ldeg = Galactic logitude in degrees, bdeg = Galactic latitude in degrees, dkpc = distance to pulsar in kpc


ldeg =20.0

bdeg = 20.

dkpc = 2.0

############# Extract important parameters say values of Rp (in kpc) and z (in kpc)  ##########

Rpkpc = GalDynPsrFreq.read_parameters.Rpkpc(ldeg, bdeg, dkpc)

zkpc = GalDynPsrFreq.read_parameters.z(ldeg, bdeg, dkpc)


#################  Compute excess Shklovskii term for frequency first derivative using Exshk() #################################

#### We need to provide the values of proper motion in Galactic longitude direction and proper motion in the Galactic latitude direction#####

##mul = proper motion in Galactic longitude direction (mas/yr), mub = proper motion in Galactic latitude direction (mas/yr)

mul = 20.
mub = 20.

ExcessSh = GalDynPsrFreq.Shk.Exshk(dkpc, mul, mub)



############## Compute excess terms for the first frequency derivative due to Galactic potential ####################

######## ModelnoBH  (not incorporating BH contribution to Milky Way Potential)   ##########

fex_pl = GalDynPsr.modelnoBH.Expl(ldeg,  bdeg,  dkpc) #calculates the planar contribution to the excess term

fex_z = GalDynPsr.modelnoBH.Exz(ldeg,  bdeg,  dkpc) #calculates the perpendicular contribution to the excess term

totalfexGal = fex_pl+fex_z

#########----------------------OR---------------------------############

####### ModelBH (incorporating BH contribution to Milky Way Potential)  ##########

fex_pl = GalDynPsrFreq.modelBH.Expl(ldeg,  bdeg,  dkpc) #calculates the planar contribution to the excess term

fex_z = GalDynPsrFreq.modelBH.Exz(ldeg,  bdeg,  dkpc) #calculates the perpendicular contribution to the excess term

totalfexGal = fex_pl+fex_z



######################### For Intrinsic frequency derivative calculations ###############################

## Observable parameters required for spin (or orbital) frequency derivative calcuations: f = frequency in Hz, fdotobs = measured frequency derivative in s^-2
#Calculated parameters required: fex_pl = excess term in first derivative of frequency parallel to the Galactic plane in s^-1, fex_z = excess term in first derivative of frequency perpendicular to the Galactic plane in s^-1, fex_shk = excess term in first derivative of frequency due to Shklovskii effect in s^-1 

f = 50.

fdotobs = -1.43e-15

fdot_Expl = GalDynPsrFreq.fdotint.fdotExpl(fex_pl,f) #calculates the planar contribution to the frequency derivative 

fdot_Exz = GalDynPsrFreq.fdotint.fdotExz(fex_z,f) #calculates the perpendicular contribution to the frequency derivative
 
fdot_Gal = GalDynPsrFreq.fdotint.fdotGal(fex_pl,fex_z,f) #calculates the sum of planar and perpendicular contributions to the frequency derivative

fdot_Shk = GalDynPsrFreq.fdotint.fdotShk(fex_shk,f) #calculates the Shklovskii contribution to the frequency derivative

fdot_int = GalDynPsrFreq.fdotint.fdotint(fex_pl,fex_z,fex_shk,fdotobs,f) #calculates the intrinsic frequency derivative


#### Compute excess term for second derivative of frequency#################
#Additional observable parameters required: vrad = radial velocity in km/s
#Calculated parameters required- Rpkpc = Galactocentric cylindrical radius of the pulsar in kpc, zkpc = displacement of the pulsar perpendicular to the Galactic plane in kpc

vrad = 20.

########## Model fdotdotexc (not incorporating BH contribution to Milky Way Potential) ###########

fddotfex = GalDynPsrFreq.fdotdotexc.fdotdotexccal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk)

############----------------------OR-------------------------##################           

######### Model fdotdotexcBH  (incorporating BH contribution to Milky Way Potential)##########

fddotfex = GalDynPsrFreq.fdotdotexcBH.fdotdotexcwBHcal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk)


########### Intrinsic second derivative of frequency calculations ###########################
#Additional observable parameters required: fdotdotobs = observed second derivative of frequency in s^-3
#Calculated parameters required: fddotfex = excess term for second derivative of frequency in s^-2 

fdotdotobs = 1.2e-28

fddotint = GalDynPsrFreq.fdotdotint.fdotdotintcal(fddotfex,f,fdotdotobs)



###### Example ###############

#Using models modelBH and fdotdotexcBH  

import GalDynPsrFreq

ldeg = 20.

bdeg=20.

dkpc = 2.

mul = 20.

mub = 20.

vrad = 20.

f = 50.

fdotobs = -1.43e-15

fdotdotobs = 1.2e-28

Rpkpc = GalDynPsrFreq.read_parameters.Rpkpc(ldeg, bdeg, dkpc)

zkpc = GalDynPsrFreq.read_parameters.z(ldeg, bdeg, dkpc)

fex_pl = GalDynPsrFreq.modelBH.Expl(ldeg, bdeg, dkpc)

fex_z = GalDynPsrFreq.modelBH.Exz(ldeg, bdeg, dkpc)

fex_shk = GalDynPsrFreq.Shk.Exshk(dkpc, mul, mub)



fdot_Expl =  GalDynPsrFreq.fdotint.fdotExpl(fex_pl,f)

fdot_Exz =  GalDynPsrFreq.fdotint.fdotExz(fex_z,f)

fdot_Gal =  GalDynPsrFreq.fdotint.fdotGal(fex_pl,fex_z,f)

fdot_Shk =  GalDynPsrFreq.fdotint.fdotShk(fex_shk,f)

fdot_int = GalDynPsrFreq.fdotint.fdotint(fex_pl,fex_z,fex_shk,fdotobs,f)



fddotfex = GalDynPsrFreq.fdotdotexcBH.fdotdotexcwBHcal(ldeg,bdeg,dkpc,mul,mub,Rpkpc,zkpc,f,fdotobs,vrad,fex_pl,fex_z,fex_shk)

fddotint = GalDynPsrFreq.fdotdotint.fdotdotintcal(fddotfex,f,fdotdotobs)




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

fdotdotSB1.py: Calculates first square bracket term of Eq. (11) of the paper Pathak and Bagchi (arXiv: 1909.13113).

fdotdotSB2.py: Calculates second square bracket term of Eq. (11) of the paper Pathak and Bagchi (arXiv: 1909.13113).

fdotdotSB3.py: Calculates third square bracket term of Eq. (11) of the paper Pathak and Bagchi (arXiv: 1909.13113).

fdotdotSB4.py: Calculates fourth square bracket term of Eq. (11) of the paper Pathak and Bagchi (arXiv: 1909.13113).

fdotdotexc.py: Model fdotdotexc: Calculates the excess second derivative of frequency by frequency ratio, using the MWPotential2014 (without BH) of galpy as the Galactic potential  

fdotdotexcBH.py: Model fdotdotexcBH:  Calculates the excess second derivative of frequency by frequency ratio, using the MWPotential2014 (with BH) of galpy as the Galactic potential

fdotdotint.py: Calculates the intrinsic frequency second derivative

############################################################


