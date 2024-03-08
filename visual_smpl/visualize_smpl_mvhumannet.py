import numpy as np
import os
#import sys
import torch
import smplx
import pickle

from scipy.spatial.transform import Rotation
#import pickle
import cv2
from utils_mvhuman import rotation_matrix_to_angle_axis, transform_can_smpl
# import SMPL
#import json

model_smplx = smplx.create(os.path.expanduser(r"smpl_\SMPL_NEUTRAL.pkl"),model_type="smplx",)

model_smpl = smplx.create(os.path.expanduser(r"smpl_\SMPL_NEUTRAL.pkl"), model_type="smpl",)


pkl_path = r'data/000075.pkl'
name = os.path.split(pkl_path)[1][:-4]


smpl_param_path = pkl_path
with open(smpl_param_path, 'rb') as f: 
    smpl_param = pickle.load(f)

full_pose = smpl_param['full_pose'][0].numpy()
poses = np.array([Rotation.from_matrix(mat).as_rotvec() for mat in full_pose]).ravel()
betas_smpl = torch.tensor(smpl_param['betas'])
body_pose_smpl =torch.tensor(poses[3:][None]).float()
global_orient_smpl = rotation_matrix_to_angle_axis(smpl_param['global_orient'][0])[None]

output_smpl = model_smpl(betas=betas_smpl, body_pose=body_pose_smpl, return_verts=True,)
vertices_smpl = output_smpl.vertices[0].detach().cpu().numpy().squeeze()


output_smpl_T = model_smpl(betas=betas_smpl, body_pose=torch.zeros(1,69), return_verts=True,)
pelvis_pos_smpl = output_smpl_T.joints[0][:1].detach().numpy().copy()[0]
smpl_Th = smpl_param['joints'][:, 0].detach().cpu().numpy() - cv2.Rodrigues(global_orient_smpl[0][0].numpy())[0].dot(pelvis_pos_smpl)

verts_smpl = vertices_smpl.dot(cv2.Rodrigues(global_orient_smpl[0][0].numpy())[0].T) + smpl_Th

# file = open("%s_output_smpl_pc.obj"%name, 'w')
# for v_index, v in enumerate(verts_smpl):
#     file.write('v %.4f %.4f %.4f \n' % (v[0], v[1], v[2]))
# file.close()



faces = model_smpl.faces.astype(np.int32)

file = open("%s_output_smpl.obj"%name, 'w')
for v in verts_smpl:
    file.write('v %.4f %.4f %.4f\n' % (v[0], v[1], v[2]))
for f in faces:
    f_plus = f + 1
    file.write('f %d %d %d\n' % (f_plus[0], f_plus[1], f_plus[2]))
file.close()
