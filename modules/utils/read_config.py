import configparser
import json


def read_config(path):
    config = configparser.ConfigParser()
    config.read(path)

    darknet_path = config.get('Darknet', 'path')
    model_cfg_path = config.get('Model', 'config_name')
    model_weights_path = config.get('Model', 'weights_name')
    class_names = [config.get('Label', 'class_0'), config.get('Label', 'class_1'), config.get('Label', 'class_2')]

    return {
        'darknet_path': darknet_path,
        'model_cfg_name': model_cfg_path,
        'model_weights_name': model_weights_path,
        'class_names': class_names
    }