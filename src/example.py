from register import register, combine
import os

# example usage

# declare path
folder = '../data/multichannel/'
hr_tiff = 'germline_hr.tif'
lr_tiff = 'germline_lr.tiff'
hr_output = 'r_'+hr_tiff
lr_output = 'r_'+lr_tiff
# You can also separate inout and output by giving them full path 

# specify where you put your csv's (can be different from the folder above)
csv_path = folder

# change working directory  (if you used relative path rather than absolute path)
os.chdir(folder)

# specify the number of roi ("cell") you saved
n_roi = 2

# read translation matrix
trans_mat = combine(csv_path, n_csv = n_roi)

# 1) register a low res movie (if you generated the ROI csv using compressed movie)
metadata = register(lr_tiff,trans_mat,lr_output,highres = False,compress = 3, pad = True)
    
# 2) register a high res movie with the same matrix
metadata = register(hr_tiff,trans_mat,hr_output,highres = True,compress = 3, pad = True)

# 3) if you used the original movie to generate the ROI csv, set compress=1
metadata = register(hr_tiff,trans_mat,hr_output,highres = True,compress = 1, pad = True)

