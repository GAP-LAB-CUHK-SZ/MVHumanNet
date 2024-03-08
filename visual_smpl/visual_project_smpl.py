from mytools.camera_utils import read_camera_ours
from mytools.writer import FileWriter
import trimesh
import numpy as np
import cv2
import matplotlib.pyplot as plt


projection_results = "projection_results.jpg"



img_path =  r'data/0380_img.jpg'
# mask_path =   

obj_path = r'data/000075_smplx.obj'
intri_name = r'data/camera_intrinsics.json'
extri_name =  r'data/camera_extrinsics.json'
cameras_gt = read_camera_ours(intri_name, extri_name)

obj_data = trimesh.load(obj_path)

vertices = np.array(obj_data.vertices)
faces = np.array(obj_data.faces)



camera_render_list = ["CC32871A059",]
cam_i = camera_render_list

render_data = {}
assert vertices.shape[1] == 3 and len(vertices.shape) == 2, 'shape {} != (N, 3)'.format(vertices.shape)
# pid = self.pid
pid ,nf = 0,0
render_data = {'vertices': vertices, 'faces': faces, 'vid': pid, 'name': 'human_'}
cameras = {'K': [], 'R':[], 'T':[]}

sub_vis = cam_i
for key in cameras.keys():
    cameras[key] = np.stack([cameras_gt[cam][key] for cam in sub_vis])


outname_cache = ( 'smpl.jpg')


config={}
write_smpl  = FileWriter(r"/", config=config)

data_images = cv2.imread(img_path)
render_data_input = {"0":render_data}
shape_ori = data_images.shape
data_images_input = cv2.resize(data_images, [4096,3000])
smpl_img = write_smpl.vis_smpl(render_data_input, [data_images_input], cameras, outname_cache, add_back=False)







smpl_img_re = cv2.resize(smpl_img, (4096, 3000), interpolation=cv2.INTER_AREA)
smpl_mask = np.repeat(smpl_img_re[:,:,3:],3,2)/255
data_save = data_images_input * (1-smpl_mask) + smpl_img_re[:,:,:3]* (smpl_mask)

plt.imsave(projection_results, data_save.astype("uint8"))








