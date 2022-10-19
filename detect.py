import os
import argparse
import subprocess

from modules.utils.read_config import read_config
from modules.utils.set_names import set_class_names


if __name__ == "__main__":
    CFG_PATH = 'config.ini'
    INFERENCE_MODEL_DATA = 'inference_model_data'

    config = read_config(CFG_PATH)
    darknet_path, model_cfg_name = config['darknet_path'], config['model_cfg_name']
    model_weights_name, class_names = config['model_weights_name'], config['class_names']

    parser = argparse.ArgumentParser()
    parser.add_argument("img_path", type=str, help="Image path")
    img_path = parser.parse_args().img_path

    inference_model_data = os.listdir(INFERENCE_MODEL_DATA)
    main_path = os.path.dirname(os.path.realpath(__file__)) + '/'
    if not (os.path.exists('dataset.data') or os.path.exists('dataset.names')):
        set_class_names(class_names, main_path)

    dd_path = main_path + 'inference_model_data/dataset.data'
    mcfg_path = main_path + 'inference_model_data/' + model_cfg_name
    mweights_path = main_path + 'inference_model_data/' + model_weights_name

    command = f"""
    cd {darknet_path} &&
    ./darknet detector test {dd_path} {mcfg_path} {mweights_path} {img_path}
    """
    subprocess.call(command, shell=True)