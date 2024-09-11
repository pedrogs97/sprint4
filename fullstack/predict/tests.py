"""Testes"""

import pytest
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
from django.conf import settings
from joblib import load
import pandas as pd


@pytest.fixture
def model():
    """Fixture para carregar o modelo."""
    return load(settings.MODEL_PATH)


@pytest.fixture
def scaler():
    """Fixture para carregar o scaler."""
    return load(settings.FIT_PATH)


@pytest.fixture
def test_data(scaler):
    """Fixture para carregar os dados de teste."""
    df_to_test = pd.read_csv(settings.CSV_TEST_PATH)
    df_to_test["gender"] = df_to_test["gender"].map({"M": 1, "F": 2})
    df_to_test["class"] = df_to_test["class"].map({"A": 1, "B": 2, "C": 3, "D": 4})

    x_test = scaler.transform(df_to_test.drop("class", axis=1))
    y_test = df_to_test["class"]
    return x_test, y_test


def test_accuracy(model, test_data):
    """Teste de acurácia."""
    x_test, y_test = test_data
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    assert accuracy >= 0.70, f"Acurácia {accuracy} está abaixo do mínimo de 70%"


def test_f1_score(model, test_data):
    """Teste de F1-Score."""
    x_test, y_test = test_data
    y_pred = model.predict(x_test)
    f1 = f1_score(y_test, y_pred, average="weighted")
    assert f1 >= 0.70, f"F1-Score {f1} está abaixo do mínimo de 59%"


def test_recall(model, test_data):
    """Teste de Recall."""
    x_test, y_test = test_data
    y_pred = model.predict(x_test)
    recall = recall_score(y_test, y_pred, average="weighted")
    assert recall >= 0.70, f"Recall {recall} está abaixo do mínimo de 60%"


def test_precision(model, test_data):
    """Teste de Precisão."""
    x_test, y_test = test_data
    y_pred = model.predict(x_test)
    precision = precision_score(y_test, y_pred, average="weighted")
    assert precision >= 0.70, f"Precisão {precision} está abaixo do mínimo de 59%"
