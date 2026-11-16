from django.db import migrations, models


def migrate_old_author_names(apps, schema_editor):
    Libro = apps.get_model('catalogo', 'Libro')
    Autor = apps.get_model('catalogo', 'Autor')
    db = schema_editor.connection.alias
    for libro in Libro.objects.using(db).exclude(autor='').iterator():
        parts = libro.autor.strip().split(None, 1)
        nombre = parts[0]
        apellido = parts[1] if len(parts) > 1 else 'Sin apellido'
        autor, _ = Autor.objects.using(db).get_or_create(
            nombre=nombre, apellido=apellido, nacionalidad='No especificada')
        libro.autores.add(autor)


class Migration(migrations.Migration):
    dependencies = [('catalogo', '0002_libro')]
    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
            ],
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores', 'ordering': ['apellido', 'nombre']},
        ),
        migrations.AddField(
            model_name='libro', name='autores',
            field=models.ManyToManyField(blank=True, related_name='libros', to='catalogo.autor'),
        ),
        migrations.RunPython(migrate_old_author_names, migrations.RunPython.noop),
        migrations.RemoveField(model_name='libro', name='autor'),
    ]
