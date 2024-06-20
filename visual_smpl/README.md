For the convenience of using MVHumanNet dataset, we provide __a script to project smplx onto the image plane__ and __a script to visualize our estimation of SMPL__.

### To project smplx onto the image plane

1. Download all files under folder of __*"visual_smpl"*__.

2. Configure the environment. (e.g. trimesh, matplotlib)

3. run the __*"visualize_project_smplx_mvhumannet.py"*__ script.

4. You will easily obtain a result (__*projection_result.jpg*__).


### To visualize smpl

1. Download all files under folder of __*"visual_smpl"*__.

2. Configure the environment. (e.g. torch, smpl, scipy, cv2)

3. run the __*"visualize_smpl_mvhumannet.py"*__ script.

4. You will easily obtain an obj file (__000075_output_smpl.obj__) corresponding to __./data/000075.pkl__.


Feel free to use this script to visualize other SMPL parameters in MVhumanNet.



### To visualize json to smplx mesh onto the image plane
1. Download SMPLX_NEUTRAL.pkl(about 518 mb) from https://github.com/vchoutas/smplx#downloading-the-model.

2. Put SMPLX_NEUTRAL.pkl to the path of "\smpl_\smplx"

3. run the __*"visualize_json2smplx.py"*__ script.
   
4. You will easily obtain a result (__*json2smplx.jpg*__).

