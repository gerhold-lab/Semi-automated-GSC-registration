from register import superregister

# example usage

# declare path
folder = '../data/multichannel/'
hr_tiff_path = 'u_germline_hr.tif'
lr_tiff_path = 'u_germline_lr.tiff'

# register a low res movie (if you generated the ROI csv using compressed movie)
# suppose you have 2 ROI csv...
super_register(folder,tiff_path=lr_tiff_path,n_roi=2,high_res=False,compress=3)
    
# register a high res movie with the same matrix
super_register(folder,tiff_path=hr_tiff_path,n_roi=2,high_res=True,compress=3)

# if you used the original movie to generate the ROI csv, set compress=1
super_register(folder,tiff_path=hr_tiff_path,n_roi=2,high_res=True,compress=1)

    
