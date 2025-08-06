import kagglehub
import os
from collections import Counter
import numpy as np
import tensorflow as tf
from matplotlib.image import imread
import logging
                
def download_dataset(url: str) -> str:
    path = kagglehub.dataset_download(url)
    return path 

def get_labels_to_predict(path: str) -> list: 
    labels_existents = dict()
    
    for filename in os.listdir(path):
        label = filename.split("_")[-1] 
        if (label not in labels_existents):
            labels_existents[label] = 1
            continue
        labels_existents[label] = labels_existents[label] + 1
    
    folders_counter = Counter(labels_existents.values())
    best_size = 0
    for size, count in folders_counter.items():
        if (count >= 4 and size > best_size and size > 5):
            best_size = size
    
    choosen_labels = [k for k,v in labels_existents.items() if v == best_size] 
    
    print(choosen_labels)
    return choosen_labels

def extract_dataset(path: str, labels_to_predict:list, feature_label:str, pattern_label:str) -> dict:

    data = {pattern_label: [], feature_label: []}
    image_height = 128
    image_width = 128
    image_size = [image_height, image_width]

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        label = filename[4:].replace("_", " ").split(" ")[-1]
        if (label not in labels_to_predict):
            continue
        for image in os.listdir(full_path):
            img_full_path = os.path.join(full_path, image)
            
            img_bytes = imread(img_full_path)
            img_constant = tf.constant(img_bytes)
            if (len(img_constant.shape) < 3):
                img_constant = img_constant[..., tf.newaxis]
                img_constant = tf.image.grayscale_to_rgb(img_constant)
            img_constant = tf.image.central_crop(img_constant, 0.8)
            img_resized = tf.image.resize(img_constant, image_size)
            data[pattern_label].append(label)
            data[feature_label].append(img_resized.numpy())

    return data

def save_dataset(data: dict, feature_label:str, pattern_label:str):
    features = np.array(data[feature_label])
    patterns = np.array(data[pattern_label])

    np.save("../model/features.npy", features)
    np.save("../model/patterns.npy", patterns)


def run_pipe():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='pipeline.log', encoding='utf-8', level=logging.DEBUG)
    logger.debug("[DATA] - Downloading dataset")
    path = download_dataset("wenewone/cub2002011") + "/CUB_200_2011/images"
    logger.debug("[DATA] - Extracting labels to use")
    labels = get_labels_to_predict(path)
    logger.debug(f"[DATA] - Found labels: {labels}")
    
    feature_label = "image" 
    pattern_label = "species"

    logger.debug("[DATA] - Extracting data from dataset of respective labels")
    data = extract_dataset(path, labels, feature_label, pattern_label)
    logger.debug("[DATA] - Saving data as numpy arrays")
    save_dataset(data, feature_label, pattern_label)
    logger.debug("[DATA] - Data extracted successfully")


if (__name__ == "__main__"):
    run_pipe()
