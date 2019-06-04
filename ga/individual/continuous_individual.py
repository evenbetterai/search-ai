import numpy as np

from ga.individual.individual import Individual


class ContinuousIndividual(Individual):
    def __init__(self, len_features, features_info):
        super(ContinuousIndividual, self).__init__(len_features)
        self.features_info = features_info

    @property
    def features_info(self):
        return self._features_info

    @features_info.setter
    def features_info(self, new_features_info):
        if len(new_features_info) == len(self._features):
            raise ValueError(
                "'new_features_info' parameter should "
                + "have the same length as 'features' "
                + "attribute"
            )

        self._features_info = new_features_info

    def set_feature_at(self, index, new_value):
        if not (
            self._features[index].min_value
            <= new_value
            <= self._features[index].max_value
        ):

            raise ValueError(
                "'new_value' parameter has to hold a "
                + "number between _features[index].min_value"
                + " and _features[index].max_value"
            )

        self._features[index] = new_value

    def _init_features(self, len_features):
        self._features = np.zeros((len_features,), np.float)

        for i in range(len(self._features)):
            self._features[i] = self._features_info[i].min_value
