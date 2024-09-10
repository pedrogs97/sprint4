"""Views."""

from django.shortcuts import render
from .forms import DataToPredictForm
from .model import PredictModel, PreProcessor, PostProcessor


def index(request):
    """Página inicial."""
    if request.method == "POST":
        form = DataToPredictForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            model = PredictModel()
            pre_processador = PreProcessor()
            pos_processador = PostProcessor()
            data_df = pre_processador.preparar_novos_dados(data)
            prediction = model.classificar(data_df)
            compare = pos_processador.compare_result_mean(
                prediction, data["age"], data["height"], data["gender"]
            )
            return render(
                request,
                "index.html",
                {"form": form, "result": prediction, "compare": compare},
            )
    else:
        form = DataToPredictForm()
    return render(request, "index.html", {"form": form})
