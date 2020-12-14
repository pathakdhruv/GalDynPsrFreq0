import math
import numpy as np
import read_parameters as par



def fdotdotSB4cal(f,fdotobs,fex_pl,fex_z,fex_shk):

    fex_tot = fex_pl + fex_z + fex_shk
    fourthterm = 2*fex_tot*(fdotobs/f)
    return fourthterm;

    


