#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:39:54 2020
@filename: get_transformation_matrix.py
@author: Yifan Zhao
@description: Generating a transformation matrix from user-provided ROI
"""
import pandas as pd
import os
import numpy
from skimage.external import tifffile


def gt_transform_matrix(roi_df):
#    scale = 3 #1 for lowres; 3 for high res
    x = roi_df.iloc[:,0]
    y = roi_df.iloc[:,1]
    translation =[(0,0)]
    x0 = x[0]
    y0 = y[0]
    i = 1
    while i < len(x) :
        diff_x = int(round((x[i] - x0)))
        diff_y = int(round((y[i] - y0)))
        translation.append((diff_x, diff_y))        
        i+=1
    
    return translation


def translate(im_in, translation, highres = False, compress = 3):
    '''
    input: 
        im_in: input tiff
        translation: translation matrix 
    output:
        im_out: output tiff
    
    tifffile documentation: https://scikit-image.org/docs/0.12.x/api/skimage.external.tifffile.html

    '''
   
    # scalar multiply the translation matrix for high-res
    if highres == True:
        translation = numpy.array(translation) * compress
    
    
    n_frame, n_zstep, y_dim, x_dim = im_in.shape
    # create empty tiff
    im_out = numpy.zeros(im_in.shape)
    
    for t in range(n_frame):      
        print("Start processing t = " + str(t))
        trans_x, trans_y = translation[t]
        for z in range(n_zstep):
            for y in range(y_dim):
                for x in range(x_dim):
                    if (x+trans_x < 0) or (y+trans_y < 0):
                        continue
                    elif (x+trans_x >= x_dim) or (y+trans_y >= y_dim):
                        continue
                    else:
                        im_out[t][z][y][x] = int(im_in[t][z][y+trans_y][x+trans_x])

    
                        
    return im_out


def combine_roi(mat1, mat2):
    last_x, last_y = mat1[-1]
    mat2 =  [(a+last_x, b+last_y) for a, b in mat2 ]
    mat = mat1 + mat2
    return mat
    

if __name__ == "__main__":
    # example usage
    os.chdir("../data/")

    # --- step 1: get transformation matrix (2D) ---
    ROI = pd.read_csv("ROI.csv", header=None)
    gt_matrix = gt_transform_matrix(ROI)

#    # --- step 2: get ground truth tiff (low res) ---
#    tiff_path = 'low_res.tif'
#    im_in = tifffile.imread(tiff_path)
#    im_out = translate(im_in, gt_matrix)
#    with tifffile.TiffWriter('GT-' + tiff_path, bigtiff=True) as tif:
#        for i in range(im_out.shape[0]):
#            tif.save(im_out[i], compress = 6)

    # --- step 3: get ground truth tiff (high res) ---
    tiff_path = 'C2-2018-07-16_GSC_L4_L4440_RNAi_T0.tif'
    im_in = tifffile.imread(tiff_path)
    im_out = translate(im_in, gt_matrix, highres = True, compress = 3)
    with tifffile.TiffWriter('GT-' + tiff_path, bigtiff=True) as tif:
        for i in range(im_out.shape[0]):
            tif.save(im_out[i], compress = 6)
