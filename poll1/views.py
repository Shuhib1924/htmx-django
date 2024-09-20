from django.shortcuts import render
from faker import Faker
from random import randint

fake = Faker()


def index(request):
    purchases = [
        {
            "name": "Computing for Beginners",
            "category": "Book",
            "price": "$29.99",
            "buyer": "mr-celloist1@gmail.com",
        },
        {
            "name": "Computing for Beginners",
            "category": "Book",
            "price": "$29.99",
            "buyer": "ztod-a@gmail.com",
        },
        {
            "name": "Why the President is secretly turning into a cat - And not how you think",
            "category": "Video",
            "price": "$9.75",
            "buyer": "alex.g@gmail.com",
        },
        {
            "name": "Computing for Beginners",
            "category": "Book",
            "price": "$29.99",
            "buyer": "rob.moggak@gmail.com",
        },
    ]
    return render(request, "poll1/index.html", context={"purchases": purchases})


def row(request):
    new_purchases = []
    for _ in range(randint(0, 2)):  # generate random purchases.
        purchase = {
            "name": f"Computing for a {fake.job()}",
            "category": "Book",
            "price": f"${randint(10, 100)}.{randint(0, 99)}",
            "buyer": fake.email(),
        }
        new_purchases.append(purchase)

    return render(request, "table-rows.html", context={"purchases": new_purchases})
