import numpy as np
class KNearestNeighbor:
    def __init__(self, distance_func='euclidian', k=1):
        self.training_data = None
        self.class_data = None
        self.k = k
        self.inv_cov = None
        match distance_func:
            case 'mahalanobis':
                self.distance_func = self._mahalanobis_distance
            case 'euclidian': 
                self.distance_func = self._euclidian_distance

    def _mahalanobis_distance(self, X):
        candidates = None
        for x in X:
            diff = self.training_data - x
            distance = np.sqrt(np.sum(diff @ self.inv_cov @ diff.T,axis=1)).reshape(-1, 1)
            min_values = np.argpartition(distance, self.k, axis=0)[0:self.k].reshape(1, -1)
            candidates = min_values if candidates is None else np.r_[candidates, min_values]

        return candidates


    def _euclidian_distance(self, X):
        candidates = None
        for x in X:
            distance = np.sqrt(np.sum((self.training_data - x) ** 2, axis=1)).reshape(-1, 1)
            min_values_idx = np.argpartition(distance, self.k, axis=0)[0:self.k].reshape(1, -1)
            candidates = min_values_idx if candidates is None else np.r_[candidates, min_values_idx]
        
        return candidates


    def fit(self, X, Y):
        self.training_data = X
        self.class_data = Y 
        
        features_means = np.mean(X, axis=0).reshape(1, -1)
        centered_features = X - features_means
        n = X.shape[0] 
        cov = 1 / (n - 1) * (np.transpose(centered_features) @ centered_features)
        
        self.inv_cov = np.linalg.pinv(cov)
        

    def predict(self, X):
        candidates = self.distance_func(X)
        pred = []
        for candidate in candidates: 
            classes = self.class_data[candidate]     
            classes_count = np.unique(classes, return_counts=True) 
            
            if len(classes_count[0]) == 1 or self.k == 1:
              pred.append(int(classes_count[0][0]))
              continue

            predicted_class = None
            predicted_class_count = None
            for class_, count in zip(classes_count[0], classes_count[1]):
              if predicted_class is None or count > predicted_class:
                predicted_class = int(class_)
                predicted_class_count = count
            
            pred.append(predicted_class)      
                    
        result = np.array(pred).reshape(-1, 1)
        return result
