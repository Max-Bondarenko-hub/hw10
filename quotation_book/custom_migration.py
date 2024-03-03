import os
import django

from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotation_book.settings")
django.setup()

from quotes.models import Quotes, Authors, Tag

client = MongoClient("mongodb+srv://maxzonk:pass123@cluster-test.vaduamc.mongodb.net/test?retryWrites=true&w=majority")
db = client.archive

authors = db.authors.find()
for author in authors:
    Authors.objects.get_or_create(
        fullname=author["fullname"],
        born_date=author["born_date"],
        born_location=author["born_location"],
        description=author["description"].strip(),
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quotes.objects.filter(quote=quote["quote"])))

    if not exist_quote:
        author = db.authors.find_one({"_id": quote["author"]})
        a = Authors.objects.get(fullname=author["fullname"])
        q = Quotes.objects.create(quote=quote["quote"], author=a)
        for tag in tags:
            q.tags.add(tag)
