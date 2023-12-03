import yaml
import numpy as np
import argparse
import os
import cv2


def config_get():
    parser = argparse.ArgumentParser()
    # 参数配置文件路径
    parser.add_argument("--config", default='./configs.yml', type=str, required=False, help="Path to the config file")
    args = parser.parse_args()

    with open(os.path.join(args.config), "r") as f:
        config = yaml.safe_load(f)
    new_config = dict2namespace(config)

    return new_config


def dict2namespace(config):
    namespace = argparse.Namespace()
    for key, value in config.items():
        if isinstance(value, dict):
            new_value = dict2namespace(value)
        else:
            new_value = value
        setattr(namespace, key, new_value)
    return namespace

config = config_get()
cam_param = config.cameraParameters
Intrinsics = np.array(cam_param.Intrinsics)
Rotation = np.array(cam_param.Rotation)
Trans = np.array(cam_param.Translation).reshape(3,1)

img = cv2.imread('ship.png')
print(img.shape)