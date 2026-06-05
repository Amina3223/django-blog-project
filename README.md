# Blog Django

## Introducció

Aquest projecte és un blog desenvolupat amb Django per al mòdul de Programació. L'aplicació permet gestionar posts, autors i etiquetes (tags) mitjançant una base de dades relacional i mostrar la informació de forma dinàmica a través de plantilles Django.

## Objectius principals

* Desenvolupar una aplicació web amb Django.
* Gestionar posts, autors i etiquetes.
* Utilitzar relacions entre models.
* Implementar pàgines dinàmiques amb plantilles.
* Utilitzar GitHub per al control de versions.
* Generar documentació automàtica amb Pydoc.
* Automatitzar processos amb GitHub Actions.

---

## Instal·lació ràpida

### Clonar el repositori

```bash
git clone https://github.com/Amina3223/django-blog-project.git
```

### Entrar al projecte

```bash
cd django-blog-project
```

### Instal·lar dependències

```bash
pip install -r requirements.txt
```

### Executar migracions

```bash
python manage.py migrate
```

### Carregar dades inicials

```bash
python manage.py loaddata blog/fixtures/initial_data.json
```

---

## Execució del projecte

### Executar el servidor local

```bash
python manage.py runserver
```

### URL d'accés

```text
http://127.0.0.1:8000/
```

---

## Tecnologies utilitzades

* Python
* Django
* SQLite
* HTML
* Bootstrap
* Git
* GitHub Actions

---

## Documentació Pydoc

La documentació del projecte es genera automàticament mitjançant GitHub Actions i Pydoc.

Un cop publicada amb GitHub Pages es podrà consultar des de l'enllaç següent:

```text
https://Amina3223.github.io/django-blog-project/
```
