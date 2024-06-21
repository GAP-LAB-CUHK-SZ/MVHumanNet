# MVHumanNet: A Large-scale Dataset of Multi-view Daily<br> Dressing Human Captures (CVPR 2024)
## [Project Page](https://x-zhangyang.github.io/MVHumanNet/) | [Paper (Arxiv)](https://arxiv.org/abs/2312.02963) | [Dataset](https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet/)

<img src="./figures/teaser_.png" width="1080"/>

by Zhangyang Xiong#, Chenghong Li#, Kenkun Liu#, Hongjie Liao, Jianqiao Hu, Junyi Zhu, Shuliang Ning, Lingteng Qiu, Chongjie Wang, Shijie Wang, 
Shuguang Cui and [Xiaoguang Han*](https://gaplab.cuhk.edu.cn/) from [GAP-Lab](https://gaplab.cuhk.edu.cn/). 



## Introduction

MVHumanNet contains **4,500** human identities,  **9,000** daily outfits,  **60,000** motion sequences,  **645 million** with extensive annotations, including human masks, camera parameters , 2D and 3D keypoints, SMPL/SMPLX parameters, and corresponding textual descriptions.

**The rest data will be available soon.**
## Updates （MVHumanNet_Part1 and MVHumanNet_Part2 are available now!）

- 2024.06.21: **MVHumanNet_Part2 is released!** :fire::fire::fire::fire::fire::fire::fire:
  > We provide links to download MVHumanNet data. Please fill this [form](https://forms.gle/a4DXEyoFcQEHoRjx7) to get the download all links (you don't need to fill the previous forms).
  > 
  > Currently MVHumanNet_Part1 and MVHumanNet_Part2 contain about **4000** IDs and **8000** outfits. The rest of the data will be updated to the same links later.
  

- 2024.05.29: **Script for downloading MVHumanNet**
  > We provide the [script](https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet/blob/main/download_tool_mvhuman.py) to download all the contents of the dataset. Before using it, please make sure you have filled out our form and obtained the download links.

- 2024.05.24: Textual descriptions of MVHumanNet are released! [Textual descriptions](https://github.com/GAP-LAB-CUHK-SZ/MVHumanNet/tree/main/textual_description):fire::fire::fire::fire::fire::fire::fire:

- 2024.05.07: **MVHumanNet_Part1 is released!** :fire::fire::fire::fire::fire::fire::fire:
  > MVHumanNet_Part1 contains about **2500** IDs and **4800** outfits.
  > We provide links to download the MVHumanNet_Part1. Please fill out the [form](https://docs.google.com/forms/d/1pN5JoMj9HgvVrWY_U4mJlmoQHXLPRHwVa6PRlAhLRDs) to get the download links.
  

- 2023.12.20 Samples of MVHumanNet are available now！！！
  > These samples contain **100** outfits, with 6+1 motions sequences for each. 
  > We provide a link to download the samples. Please fill out this [form](https://docs.google.com/forms/d/e/1FAIpQLSeI5ywaBKgbmIBajuXGyo_u8F3nJIANMFww9tr9f0ylecSUuw/viewform?usp=sf_link) to get the download link.



### Folder structure 
```
|-- ROOT
    |-- outfits_ID # 100001
        |-- images    # Considering the limitation of storage space, we scaled the image to half the original size and masked some background.
            |-- camera_name
                |-- images  
            |-- camera_name
                |-- images
            ....
        |-- fmask   # corresponding masks.
            |-- camera_name
                |-- mask images 
            |-- camera_name
                |-- mask images 
            ....
        |-- annots # 2D image annotations by openpose.
            |-- camera_name
                |-- annotations  # json files
            |-- camera_name
                |-- annotations  # json files
            ....
        |-- openpose
            |-- camera_name
                |-- 2D keypoints  # json files
            |-- camera_name
                |-- 2D keypoints  # json files
            ....
        |-- smpl_param  #  optimizes from multi-view images
            |-- PKL files
        |-- smplx  #  optimizes from multi-view images
            |-- 3D keypoints
                |-- json files # 3D keypoints
            |-- smpl
                |-- json files 
            |-- smplx_mesh  
                |-- obj files  # smplx meshs
        |-- camera_extrinsics.json   # extrinsics of all cameras
        |-- camera_intrinsics.json   # intrinsics of all cameras
        |-- camera_scale.pkl   #       

```



If you find our work useful in your research, please consider citing:
```
@article{xiong2023mvhumannet,
    title     = MVHumanNet: A Large-scale Dataset of Multi-view Daily Dressing Human Captures },
    author    = {Zhangyang Xiong, Chenghong Li, Kenkun Liu, Hongjie Liao, Jianqiao HU, Junyi Zhu, Shuliang Ning, Lingteng Qiu, Chongjie Wang, Shijie Wang, Shuguang Cui and Xiaoguang Han
},
    journal={arXiv preprint},
    year={2023}
}
```



## License

The data is released under the MVHumanNet Terms of Use, and the code is released under the Attribution-NonCommercial 4.0 International License.

Copyright (c) 2024




