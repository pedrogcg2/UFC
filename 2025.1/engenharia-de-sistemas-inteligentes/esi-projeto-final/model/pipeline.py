import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import keras_tuner as kt
from cnnhypermodel import CNNHyperModel
import pickle
import logging

def load_dataset(path_features:str, path_patterns:str) -> (np.ndarray, np.ndarray):
    return (np.load(path_features), np.load(path_patterns))


def split_data(x, y):
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.2)
    return (x_train, x_test, y_train, y_test, label_encoder) 


def optimize_models_hyperparams(label_encoder:LabelEncoder, x_train:np.ndarray, y_train:np.ndarray) -> kt.Tuner:        
    num_classes = len(label_encoder.classes_)
    input_shape = x_train[0].shape

    tuner = kt.BayesianOptimization(hypermodel=CNNHyperModel(num_classes, input_shape),
                                    objective = 'val_accuracy',
                                    directory='hyperparams',
                                    project_name='birds')

    tuner.search(x_train, y_train, epochs=100, validation_split=0.25, callbacks=create_callbacks())

    return tuner

def create_callbacks():
    return [EarlyStopping(monitor='val_loss', patience=10), ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5)]

def build_champion_model(x_train, y_train, x_test, y_test, tuner, label_encoder):
    best_hp = tuner.get_best_hyperparameters()[0]
    model = tuner.hypermodel.build(best_hp)
    
    model.fit(x_train, y_train, epochs=100, validation_data=(x_test, y_test), callbacks=create_callbacks())
    save_model(model, "bird_classifier", label_encoder)


def save_model(model, model_name, label_encoder): 
    with open(f"../api/model-{model_name}.pkl", "wb") as model_file:
        pickle.dump(model, model_file)
    np.save(f"../api/encoder-{model_name}.npy", label_encoder.classes_)


def make_model(x, y): 
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_split=0.2, random_state=42)
    
    tuner = optimize_models_hyperparams(label_encoder, x_train, y_train)
    
    build_champion_model(x_train, y_train, x_test, y_test, tuner, label_encoder)

def load_model(path):
    return pickle.load(open(path, 'rb'))

def run_pipe():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='pipeline.log', encoding='utf-8', level=logging.DEBUG)
    logger.debug("[MODEL] - Loading dataset")
    x, y = load_dataset("features.npy", "patterns.npy")
    logger.debug("[MODEL] - Selecting best hyperparamaters")
    x_train, x_test, y_train, y_test, label_encoder = split_data(x, y)
    tuner = optimize_models_hyperparams(label_encoder, x_train, y_train)
    logger.debug("[MODEL] - Training model with best hyperparamaters")
    build_champion_model(x_train, y_train, x_test, y_test, tuner, label_encoder)
    logger.debug("[MODEL] - Saved trained model")


if __name__ == '__main__':
    run_pipe()

