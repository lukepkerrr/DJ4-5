from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    context = dict()

    if request.method == 'GET':
        form = CalcForm(request.GET)
        if form.is_valid():
            full_price = form.cleaned_data['initial_fee'] + (form.cleaned_data['initial_fee'] * form.cleaned_data['rate'] // 100)
            per_month = full_price // form.cleaned_data['months_count']
            context['common_result'] = full_price
            context['result'] = per_month
    else:
        form = CalcForm

    context['form'] = form

    return render(request, template, context)
