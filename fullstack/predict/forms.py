"""Formulários."""

from django import forms


DEFAULT_CLASS = "border border-gray-300 rounded-md p-2 w-full"


class DataToPredictForm(forms.Form):
    """Formulário para predição de dados."""

    age = forms.IntegerField(
        label="Idade", widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS})
    )
    gender = forms.ChoiceField(
        label="Gênero",
        choices=[("M", "Masculino"), ("F", "Feminino")],
        widget=forms.Select(attrs={"class": DEFAULT_CLASS}),
    )
    height = forms.FloatField(
        label="Altura (cm)", widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS})
    )
    weight = forms.FloatField(
        label="Peso (kg)", widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS})
    )
    body_fat = forms.FloatField(
        label="Gordura corporal (%)",
        widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS}),
    )
    diastolic = forms.IntegerField(
        label="Pressão arterial diastólica",
        widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS}),
    )
    systolic = forms.IntegerField(
        label="Pressão arterial sistólica",
        widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS}),
    )
    grip_force = forms.FloatField(
        label="Força de preensão (N)",
        widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS}),
    )
    sit_bend_forward = forms.FloatField(
        label="Flexão do tronco (cm)",
        widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS}),
    )
    sit_ups_count = forms.IntegerField(
        label="Número de abdominais",
        widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS}),
    )
    broad_jump = forms.FloatField(
        label="Salto em distância (cm)",
        widget=forms.NumberInput(attrs={"class": DEFAULT_CLASS}),
    )
