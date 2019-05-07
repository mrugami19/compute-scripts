#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Mutual Information Example
#
# https://github.com/agentile/ML-NLP-Algorithms
#
# @author Anthony Gentile <agentile@uw.edu>
from datetime import datetime
from math import log

# Calculate MI for 2x2 matrix
def calc_mi(matrix):
    # Lets turn our matrix cells into 
    # floats to help with our further calculations
    n11 = float(matrix[0])
    n10 = float(matrix[1])
    n01 = float(matrix[2])
    n00 = float(matrix[3])
    
    # Lets store the total count
    n = n11 + n10 + n01 + n00
    
    # Calculate the information of the term given the class by summing 
    # up the calculations for each matrix cell.
    line1 = (n11 / n) * log((n * n11) / ((n11 + n10) * (n11 + n01)), 2)
    line2 = (n01 / n) * log((n * n01) / ((n01 + n00) * (n11 + n01)), 2)
    line3 = (n10 / n) * log((n * n10) / ((n11 + n10) * (n10 + n00)), 2)
    line4 = (n00 / n) * log((n * n00) / ((n01 + n00) * (n10 + n00)), 2)
    
    return line1 + line2 + line3 + line4
    
if __name__ == '__main__':
    # Start timer
    start = datetime.now()






    #0.0001105355861	
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #
    matrix = [10,23,143,99824]
	# MODIFY ONLY THIS MATRIX #    
	# MODIFY ONLY THIS MATRIX #
	# MODIFY ONLY THIS MATRIX #







    print "%1.13f" % calc_mi(matrix)

        
    # End timer
    end = datetime.now()
    print 'Time elapsed: ' + str(end - start)
