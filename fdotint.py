import math




def fdotExpl(Ex_pl,f):
   return Ex_pl*f;


def fdotExz(Ex_z,f):
   return Ex_z*f;


def fdotGal(Ex_pl,Ex_z,f):
   a = (Ex_pl + Ex_z)*f
   return a;


def fdotShk(Ex_shk,f):
   return Ex_shk*f;


def fdotint(Ex_pl,Ex_z,Ex_shk,fdotobs,f):
   a1 = (Ex_pl + Ex_z + Ex_shk)*f
   a2 = fdotobs - a1
   return a2;






