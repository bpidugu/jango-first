# jango-first

- python -m pip install Django
- django-admin startproject smartnotes . 
- python manage.py runserver
- app creation:  django-admin startapp home



## Migrations

- Migrate command
- python manage.py migrate
- create super user: python manage.py createsuperuser


## ORM
- classes -> Make Migrations -> Migrate -> Database
- create new app: django-admin startapp notes
- add app in settings.py when a new app is created
- create model: notes in notes->models.py file
- Migrations: python manage.py makemigrations
- Apply Migrations: python manage.py migrate
- Create NotesAdmin class in notes->admin.py file
  
## Django shell
- python manage.py shell
- query: from notes.models import Notes
- mynote = Notes.objects.get(pk='1')
- mynote.title
-  new_note = Notes.objects.create(title="A Second note", text="This is a second note created through shell")
-  Notes.objects.all()
-  Notes.objects.filter(title__startswith="First")
-  Notes.objects.filter(text__icontains="Django")
-  Notes.objects.exclude(text__icontains="Django")
-  Notes.objects.filter(text__icontains="Django").exclude(title__icontains='Django')