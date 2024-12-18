from django.shortcuts import render

from .states import states


def index(request):
    return render(request, "regis1/base.html")


def state_list(request):
    template_name = "regis1/state_list.html"

    regions = (
        ("n", "Norte"),
        ("ne", "Nordeste"),
        ("s", "Sul"),
        ("se", "Sudeste"),
        ("co", "Centro-Oeste"),
    )

    context = {"regions": regions}
    return render(request, template_name, context)


def get_states(region):
    return [state for state in states.get(region).items()]


def state_result(request):
    template_name = "regis1/state_hx.html"
    region = request.GET.get("region")

    ufs = {
        "n": get_states("Norte"),
        "ne": get_states("Nordeste"),
        "s": get_states("Sul"),
        "se": get_states("Sudeste"),
        "co": get_states("Centro-Oeste"),
    }

    context = {"ufs": ufs[region]}
    return render(request, template_name, context)


def state_drop(request):
    template_name = "regis1/drop_hx.html"
    region = request.GET.get("region")

    ufs = {
        "n": get_states("Norte"),
        "ne": get_states("Nordeste"),
        "s": get_states("Sul"),
        "se": get_states("Sudeste"),
        "co": get_states("Centro-Oeste"),
    }

    context = {"ufs": ufs[region]}
    return render(request, template_name, context)
