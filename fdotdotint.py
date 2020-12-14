import math


def fdotdotintcal(fddotfex,f,fdotdotobs):
    fddotint = fdotdotobs-f*fddotfex
    return fddotint;
