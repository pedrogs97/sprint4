# Sprint 4 - Classificação de Performance Esportiva

Este projeto implementa um modelo de classificação de performance esportiva, baseado em diversos fatores como idade, altura, gênero, entre outros. O objetivo é treinar um modelo preditivo que, a partir dos dados fornecidos, possa classificar o desempenho de atletas.

## Funcionalidades

- **Treinamento de modelo:** Um pipeline completo que processa os dados, treina um modelo de classificação e salva o modelo treinado.
- **Predição:** Com base nos dados de um novo atleta, o modelo faz a predição de sua classificação de performance.
- **Testes automatizados:** Testes para garantir que o modelo atinge requisitos mínimos de performance, como acurácia e métricas de classificação.

## Tecnologias Utilizadas

- **Python 3.10 ou superior**
- **scikit-learn**
- **pandas**
- **pytest**
- **Django**
- **joblib**

## Pré-requisitos

Certifique-se de ter instalado:

- Python 3.10
- Um ambiente virtual configurado

### Instalando as Dependências

Dentro do diretório do projeto, execute:

```bash
pip install -r requirements.txt
```
ou
```bash
poetry install
```

## Execução do Projeto

Pode-se executar o projeto através do script `run.sh`, certifique-se de que o arquivo run.sh possui permissão de execução, ou com o com o comando:

```bash
python fullstack/manage.py runserver
```

## Testes

O projeto inclui um conjunto de testes automatizados que podem ser executados utilizando o script `test.sh`, ou com o comando:

```bash
pytest fullstack/predict/tests.py
```

Esses testes verificam a acurácia, precisão, recall e F1-score do modelo.
