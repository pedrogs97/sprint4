"""Classes auxiliares para do modelo de predição."""

from typing import Union
from joblib import load
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from django.conf import settings
from pandas import DataFrame, read_csv


class PredictModel:
    """Classe para do modelo de predição."""

    MAP_NUM_TO_CLASS = {1: "A", 2: "B", 3: "C", 4: "D"}
    __model: Union[SVC, None] = None
    instance = None

    def __init__(self):
        """Construtor."""
        self.instance = self.get_instance

    def __check_model(self):
        """Método para verificar se o modelo foi carregado."""
        if not self.__model:
            self.get_instance()

    @classmethod
    def get_instance(cls):
        """Método para obter a instância do modelo de predição."""
        if not cls.instance:
            cls.instance = cls()
        if not cls.__model:
            model_path = settings.MODEL_PATH
            cls.__model = load(model_path)
        return cls.instance

    def classificar(self, data):
        """Método para predizer os dados."""
        self.__check_model()
        return self.MAP_NUM_TO_CLASS[self.__model.predict(data)[0]]

    def treinar(self, input_data, expected_output):
        """Método para treinar o modelo."""
        self.__check_model()
        self.__model.fit(input_data, expected_output)
        return self.__model

    def avaliar(self, input_data, expected_output):
        """Método para avaliar o modelo."""
        self.__check_model()
        return self.__model.score(input_data, expected_output)


class PreProcessor:
    """Classe para pré-processamento dos dados."""

    MAP_FORM_TO_COLS = {
        "age": "age",
        "gender": "gender",
        "height": "height_cm",
        "weight": "weight_kg",
        "body_fat": "body fat_%",
        "diastolic": "diastolic",
        "systolic": "systolic",
        "grip_force": "gripForce",
        "sit_bend_forward": "sit and bend forward_cm",
        "sit_ups_count": "sit-ups counts",
        "broad_jump": "broad jump_cm",
    }

    def __init__(self) -> None:
        self.scaler: StandardScaler = load(settings.FIT_PATH)

    def pre_processar(self, dataset, percentual_teste, seed=7):
        """Pré-processamento dos dados."""
        x_train, x_test, y_train, y_test = self.__preparar_holdout(
            dataset, percentual_teste, seed
        )

        return (x_train, x_test, y_train, y_test)

    def __preparar_holdout(self, dataset: DataFrame, percentual_teste: int, seed: int):
        """Separação dos dados em treino e teste."""
        x = dataset.drop("class", axis=1)
        y = dataset["class"]
        return train_test_split(x, y, test_size=percentual_teste, random_state=seed)

    def preparar_novos_dados(self, cleaned_data: dict):
        """Prepara os novos dados para predição."""
        form = {}
        for key, value in cleaned_data.items():
            form[self.MAP_FORM_TO_COLS[key]] = [value]
        df = DataFrame(form, index=[0])
        df["gender"] = df["gender"].map({"M": 1, "F": 2})
        return self.scaler.transform(df)


class PostProcessor:
    """Classe para pós-processamento dos dados."""

    MAP_CLASS_TO_NUM = {"A": 1, "B": 2, "C": 3, "D": 4}
    MAP_CLASS_TO_NUM_GENDER = {"M": 1, "F": 2}

    def __init__(self) -> None:
        self.df = read_csv(settings.CSV_PATH)
        self.df["gender"] = self.df["gender"].map({"M": 1, "F": 2})
        self.df["class"] = self.df["class"].map({"A": 1, "B": 2, "C": 3, "D": 4})

    def __categorize_age(self, age):
        if age < 20:
            return "Menor de 20"
        if 20 <= age < 30:
            return "20-29"
        if 30 <= age < 40:
            return "30-39"
        if 40 <= age < 50:
            return "40-49"
        return "50 ou mais"

    def __calculate_mean_classification(self, df, height_threshold, gender):
        # Filtrar os dados
        filtered_df = df[
            (df["height_cm"] >= height_threshold) & (df["gender"] == gender)
        ]

        # Agrupar por faixa etária e calcular a média da classificação
        mean_classification = (
            filtered_df.groupby("age_group")["class"].mean().reset_index()
        )
        mean_classification["class"] = mean_classification["class"].round().astype(int)
        return mean_classification

    def compare_result_mean(self, result, age, height_threshold, gender):
        """Compara o resultado com a média."""
        gender = self.MAP_CLASS_TO_NUM_GENDER[gender]
        result = self.MAP_CLASS_TO_NUM[result]
        print(result, age, height_threshold, gender)
        age_group = self.__categorize_age(age)
        self.df["age_group"] = age_group
        mean_classification = self.__calculate_mean_classification(
            self.df, height_threshold, gender
        )
        print(mean_classification)
        age_group_mean = mean_classification[
            mean_classification["age_group"] == age_group
        ]

        if not age_group_mean.empty:
            mean_value = age_group_mean["class"].values[0]

            if result == mean_value:
                return "O resultado está igual à média da classificação para o grupo etário"
            if result < mean_value:
                return "O resultado está acima da média da classificação para o grupo etário"
            if result > mean_value:
                return "O resultado está abaixo da média da classificação para o grupo etário"
        else:
            return "Grupo etário não encontrado nos dados"
