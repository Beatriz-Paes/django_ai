import openai
from django.contrib import messages
from django.shortcuts import redirect, render

from django_ia.settings import OPENAI_KEY
from webapp.models import Historic

languages = [
    "c",
    "c#",
    "c++",
    "c-like",
    "css",
    "csv",
    "django",
    "elixir",
    "go",
    "graphql",
    "html",
    "java",
    "javascript",
    "markup",
    "markup - templating",
    "perl",
    "php",
    "python",
    "regex",
    "ruby",
    "rust",
    "sql",
    "xml - doc",
    "yaml",
]


def correction(request):
    params = {
        "view": {
            "id": "correction",
            "title": "Code Correction",
        },
        "languages": languages,
    }
    if request.method == "POST":
        params["code"] = request.POST["code"]
        params["language"] = request.POST["language"]

        if params["language"] == "Select the language":
            messages.error(
                request, message="The language is required, please select one!"
            )
            return render(request, "correction.html", params)

        openai.api_key = OPENAI_KEY
        openai.Model.list()

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Respond only with code. Fix this {params['language']} code: {params['code']}.",
                temperature=0,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            params["response"] = response["choices"][0]["text"].strip()

            register = Historic(
                question=params["code"],
                response=params["response"],
                language=params["language"],
                user=request.user,
                type=params["view"]["id"],
            )
            register.save()

        except Exception as e:
            params["code"] = e

    return render(request, "correction.html", params)


def creation(request):
    params = {
        "view": {
            "id": "creation",
            "title": "Code Creation",
        },
        "languages": languages,
    }
    if request.method == "POST":
        params["code"] = request.POST["code"]
        params["language"] = request.POST["language"]

        if params["language"] == "Select the language":
            messages.error(
                request, message="The language is required, please select one!"
            )
            return render(request, "creation.html", params)

        openai.api_key = OPENAI_KEY
        openai.Model.list()

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Respond only with code. {params['code']} in {params['language']}.",
                temperature=0,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            params["response"] = response["choices"][0]["text"].strip()

            register = Historic(
                question=params["code"],
                response=params["response"],
                language=params["language"],
                user=request.user,
                type=params["view"]["id"],
            )
            register.save()
        except Exception as e:
            params["code"] = e

    return render(request, "creation.html", params)


def general(request):
    params = {
        "view": {
            "id": "general",
            "title": "General Questions",
        }
    }
    if request.method == "POST":
        params["code"] = request.POST["code"]

        if not params["code"]:
            messages.error(request, message="You have not entered an instruction!")
            return render(request, "general.html", params)

        openai.api_key = OPENAI_KEY
        openai.Model.list()

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"{params['code']}",
                temperature=0,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            params["response"] = response["choices"][0]["text"].strip()

            register = Historic(
                question=params["code"],
                response=params["response"],
                user=request.user,
                type=params["view"]["id"],
            )
            register.save()
        except Exception as e:
            params["code"] = e

    return render(request, "general.html", params)


def historic(request):
    registers = Historic.objects.filter(user_id=request.user.id)

    params = {
        "view": {
            "id": "historic",
            "title": "Historic",
        },
        "registers": registers,
    }
    return render(request, "historic.html", params)


def historic_delete(request, id):
    register = Historic.objects.get(pk=id)
    register.delete()
    messages.success(request, "Record deleted :)")
    return redirect("historic")
