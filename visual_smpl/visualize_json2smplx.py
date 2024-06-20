''' 
1. Download SMPLX_NEUTRAL.pkl(about 518 mb) from https://github.com/vchoutas/smplx#downloading-the-model). 
2. Put SMPLX_NEUTRAL.pkl to the path of "\smpl_\smplx"
'''

import os
import cv2
import sys

from mytools.smplmodel import  load_model
from os.path import join
import numpy as np
import trimesh

import natsort
import glob
import argparse
import shutil

from mytools.camera_utils import read_camera_mvhumannet
from mytools.writer import FileWriter

import matplotlib.pyplot as plt
import pickle




img_path =  r'data/0380_img.jpg'

json_filename = r'data/000075.json'
intri_name = r'data/camera_intrinsics.json'
extri_name =  r'data/camera_extrinsics.json'

cam_i = "CC32871A059"
camera_scale_fn = r'data/camera_scale.pkl'



camera_scale = pickle.load(open(camera_scale_fn, "rb"))
if camera_scale ==120 / 65:
    image_size = [4096, 3000]
else:
    image_size = [2448, 2048]


from mytools.reader import read_smpl
# json_filename = join(path_i, r"smplx/smpl/%06d.json"%(int(frame_num/5-1)))
param = read_smpl(json_filename)[0]
body_model = load_model(gender='neutral', model_type='smplx',model_path='smpl_')
vertices = body_model(return_verts=True, return_tensor=False, **param)
mesh = trimesh.Trimesh(vertices=vertices[0], faces=body_model.faces)
# mesh.export(outpath)
vertices = np.array(vertices[0])
faces = np.array(body_model.faces)

cameras_gt = read_camera_mvhumannet(intri_name, extri_name,camera_scale)



render_data = {}
assert vertices.shape[1] == 3 and len(vertices.shape) == 2, 'shape {} != (N, 3)'.format(vertices.shape)
# pid = self.pid
pid ,nf = 0,0
render_data = {'vertices': vertices, 'faces': faces, 'vid': pid, 'name': 'human_'}
cameras = {'K': [], 'R':[], 'T':[]}

sub_vis = [cam_i]
# if len(sub_vis) == 0:
    # sub_vis = ["22327084"]
for key in cameras.keys():
    cameras[key] = np.stack([cameras_gt[cam][key] for cam in sub_vis])



config={}
write_smpl  = FileWriter("", config=config)

data_images = cv2.imread(img_path)
data_images = cv2.resize(data_images,[image_size[0], image_size[1]], interpolation=cv2.INTER_AREA)
# data_mask = cv2.imread(mask_path,-1)

render_data_input = {"0":render_data}

# NoSuchDisplayException: Cannot connect to "None"
outname_cache = (r'smplx.jpg')
smpl_img = write_smpl.vis_smpl(render_data_input, [data_images], cameras, outname_cache, add_back=False)
smpl_img_re = cv2.resize(smpl_img,[image_size[0], image_size[1]], interpolation=cv2.INTER_AREA)

# plt.imshow(smpl_img_re)
# plt.imshow(data_images)

# plt.imshow(data_images +smpl_img_re[:,:,:3])

smpl_img_re_mask = 1- smpl_img_re[:,:,3:4]/255
# # smpl_img_re_mask
# plt.imshow(smpl_img_re_mask)

plt.imshow((data_images*smpl_img_re_mask +smpl_img_re[:,:,:3]).astype("uint8"))

        
        
        
        
        
        
        
        
    
