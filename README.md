# jango-first
-…or create a new repository on the command line
echo "# jango-first" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/bpidugu/jango-first.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/bpidugu/jango-first.git
git branch -M main
git push -u origin main
## Steps
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

## Dynamic Template
- create list in notes->views.py
- class based views
## Static files
- create folder 'static' under root branch
-  add STATICFILES_DIRS in settings.py
-  To add base template:  BASE_DIR / 'static/templates' in settings.py file
-  add bootstrap css in base.html

## CRUD
- CreateView





ID: 6046220e-31ae-4b12-ae6b-77a7c0cfd4e8
CREATE_TIME: 2022-12-09T04:59:32+00:00
DURATION: 2M4S
SOURCE: gs://antioch-dev-369805_cloudbuild/source/1670561972.374135-4c4af7a9f5d1428abed32e506fcf6055.tgz
IMAGES: gcr.io/antioch-dev-369805/antimage (+1 more)
STATUS: SUCCESS



TySn6Q2C6DFv9ldtR7dtKsFoDfbwWY


gcloud run services update antiochcms-cloud \
  --platform managed \
  --region $REGION \
  --image gcr.io/${PROJECT_ID}/antimage