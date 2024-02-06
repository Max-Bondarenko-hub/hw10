from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Authors, Tag, Quotes
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def main(request, page=1):
    quotes = Quotes.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


@login_required
def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:main")
        else:
            return render(request, "quotes/tag.html", {"form": form})

    return render(request, "quotes/tag.html", {"form": TagForm()})


@login_required
def author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(to="quotes:main")

    return render(request, "quotes/author.html", {"form": AuthorForm()})


@login_required
def quote(request):
    tags = Tag.objects.all()
    authors = Authors.objects.all()

    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            choice_authors = Authors.objects.filter(fullname__in=request.POST.getlist("authors"))
            if choice_authors.exists():
                new_quote.author = choice_authors.first()

            new_quote.save()

            return redirect(to="quotes:main")
        else:
            return render(request, "quotes/quote.html", {"tags": tags, "authors": authors, "form": form})
    print("last return")
    return render(request, "quotes/quote.html", {"tags": tags, "authors": authors, "form": QuoteForm()})


def about_author(request, author_name):
    author = get_object_or_404(Authors, fullname=author_name)
    return render(request, "quotes/about_author.html", context={"author": author})


def quotes_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes_with_tag = Quotes.objects.filter(tags=tag)
    return render(request, "quotes/quotes_by_tag.html", context={"tag": tag, "quotes": quotes_with_tag})
