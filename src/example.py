from register import superregister

# example usage

# declare path
folder = '../data/multichannel/'
hr_tiff_path = 'u_germline_hr.tif'
lr_tiff_path = 'u_germline_lr.tiff'
# specify where you put your csv's (can be different from the folder above)
csv_path = folder

# change working directory
os.chdir(folder)

# specify the number of roi ("cell") you saved
n_roi = 2

# read translation matrix
trans_mat = combine(csv_path, n_csv = n_roi)

# 1) register a low res movie (if you generated the ROI csv using compressed movie)
metadata = register(tiff_path,trans_mat,out_tiff_path,highres = False,compress = 3, pad = True)
    
# register a high res movie with the same matrix
super_register(folder,tiff_path=hr_tiff_path,n_roi=2,high_res=True,compress=3)

# if you used the original movie to generate the ROI csv, set compress=1
super_register(folder,tiff_path=hr_tiff_path,n_roi=2,high_res=True,compress=1)

    
trans_mat = combine(csv_path, n_csv = n_roi)
    metadata = register(tiff_path,trans_mat,out_tiff_path,highres = False,compress = 3, pad = True)
    return metadata   