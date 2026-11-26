>>> library.objects.all()
<QuerySet [<library: Aprender Python 3.17>, <library: Bases de Datos y SQL>]>

>>> library.objects.count()
2

>>> library.objects.get(pk=1)
<library: Aprender Python 3.17>

>>> Project.objects.filter(name="Tarea1")
<QuerySet [<Project: Tarea1>]>

>>> library.objects.filter(name__contains="Python")
<QuerySet [<library: Aprender Python 3.17>]>

>>> library.objects.filter(description__contains="Es un libro para aprender python")
<QuerySet [<library: Aprender Python 3.17>]>


