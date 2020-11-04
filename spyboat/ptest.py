#!/usr/bin/env python

## This is the central processing script.
## Gets interfaced both by Galaxy and the
## command line tool of SpyBOAT


import argparse
import sys
import multiprocessing as mp
import numpy as np
# -------------------------------------------------------------------------------
# the function to be executed in parallel, Wavelet parameters are global!

def trafo_movie(movie, ncpu_req, a,b):

    def process_array(movie):

        movie = movie * a + b

        return movie
    
    
    ncpu_avail = mp.cpu_count() # number of available processors
    print(f"Starting {ncpu_req} process(es)..")


    # initialize pool
    pool = mp.Pool( ncpu_req )
    
    # split input movie row-wise (axis 1, axis 0 is time!)
    movie_split = np.array_split(movie, ncpu_req, axis = 0)

    # start the processes, result is list of tuples (phase, period, power)
    res_movies = pool.map( process_array, [movie for movie in movie_split] )


