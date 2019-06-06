import numpy as np

from ga.individual.individual import Individual


class ContinuousIndividual(Individual):

    def __init__(self, len_features, features_info):
        self._check_features_info_len(features_info, len_features)
        self._features_info = features_info
        super(ContinuousIndividual, self).__init__(len_features)


    def __eq__(self, other):
        return np.array_equal(
            self.features, other.features
        )

    def __lt__(self, other):
        return len(self.features) < len(other.features) or len(self.features) == len(other.features) and np.any(np.less(
            self.features, other.features
        ))

    def _check_features_info_len(self, features_info, features_len):
        if len(features_info) != features_len:
            raise ValueError("length of 'features_info' parameter shoulb be " + features_len)

    @property
    def features_info(self):
        return self._features_info

    def set_feature_at(self, index, new_value):
        if not (self.features_info[index].min_value <= new_value <=
                self.features_info[index].max_value):

            raise ValueError(
                "'new_value' parameter has to hold a " +
                "number between _features[index].min_value" +
                " and _features[index].max_value"
            )

        self._features[index] = new_value

    def _init_features(self, len_features):
        self._features = np.zeros((len_features, ), np.float)

        for i in range(len(self._features)):
            self._features[i] = self._features_info[i].min_value
