from django.shortcuts import render

from .states import states


def index(request):
    regions = (
        ("n", "Norte"),
        ("ne", "Nordeste"),
        ("s", "Sul"),
        ("se", "Sudeste"),
        ("co", "Centro-Oeste"),
    )

    context = {"regions": regions}
    return render(request, "regis2/index.html", context)


def get_states(region):
    return [state for state in states.get(region).items()]


def state(request):
    print("test")
    print(request.GET.get)
    region = request.GET.get("region")

    ufs = {
        "n": get_states("Norte"),
        "ne": get_states("Nordeste"),
        "s": get_states("Sul"),
        "se": get_states("Sudeste"),
        "co": get_states("Centro-Oeste"),
    }

    context = {"ufs": ufs[region]}
    return render(request, "regis2/state.html", context)


def drop(request):
    print("test")
    print(request.GET.get)
    region = request.GET.get("region")

    ufs = {
        "n": get_states("Norte"),
        "ne": get_states("Nordeste"),
        "s": get_states("Sul"),
        "se": get_states("Sudeste"),
        "co": get_states("Centro-Oeste"),
    }

    context = {"ufs": ufs[region]}
    return render(request, "regis2/drop.html", context)
