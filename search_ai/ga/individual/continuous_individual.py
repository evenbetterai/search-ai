import numpy as np
import random as rd

from search_ai.ga.individual.individual import Individual


class ContinuousIndividual(Individual):

    def __init__(self, features_info, randomize_features=True):
        self._features_info = list(features_info)
        super(ContinuousIndividual, self).__init__(len(features_info), randomize_features)

    @property
    def features_info(self):
        return self._features_info

    def get_feature_info_at(self, index):
        return self._features_info[index]

    def set_feature_info_at(self, index, feature_info):
        self._features_info[index] = feature_info

    def set_feature_at(self, index, value):
        if not (self._features_info[index].min_value <= value <=
                self._features_info[index].max_value):

            raise ValueError(
                "'value' parameter has to hold a " +
                "number between features_info[index].min_value" +
                " and features_info[index].max_value"
            )

        self._features[index] = value

    def _init_features(self, len_features, randomize=False):
        self._features = np.array([0] * len_features, np.double)

        if randomize:
            self._randomize_features()
        else:
            self._default_features()

    def _randomize_features(self):
        for i in range(len(self._features)):
            self._features[i] = rd.uniform(self._features_info[i].min_value, self._features_info[i].max_value)

    def _default_features(self):
        for i in range(len(self._features)):
                self._features[i] = self._features_info[i].min_value 
