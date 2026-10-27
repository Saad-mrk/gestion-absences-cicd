# Atelier DevOps : gestion des absences

Ce projet remplace la mini-calculatrice du TP par une mini-application Python de
gestion des absences des salariés.

## Fonctionnalités

- Ajouter une absence avec un employé, une période et un motif.
- Vérifier que les dates sont valides et dans le bon ordre.
- Calculer la durée d'une absence.
- Calculer le nombre total de jours d'absence d'un employé.
- Vérifier si un employé est absent à une date donnée.

## Installation et tests locaux

```bash
python -m venv venv
```

Sous Windows PowerShell :

```powershell
venv\Scripts\Activate.ps1
```

Sous macOS/Linux :

```bash
source venv/bin/activate
```

Puis, dans tous les cas :

```bash
python -m pip install -r requirements.txt
python -m pytest -v
python -m pip install flake8
python -m flake8 . --max-line-length=100 --exclude=venv
```

Les tests doivent afficher `5 passed` et Flake8 ne doit afficher aucune erreur.

## Pipeline CI/CD

La pipeline GitHub Actions est dans `.github/workflows/pipeline.yml`.

1. `lint` vérifie le style Python.
2. `test` exécute les cinq tests automatiquement.
3. `build` attend la réussite de `lint` et `test`, puis crée l'artefact `gestion-absences-paquet`.
4. `deploy` télécharge l'artefact et simule le déploiement uniquement sur `main`.

Les jobs `lint` et `test` s'exécutent en parallèle. Si un test échoue, `build` et
`deploy` sont bloqués.

## Déroulement du TP

### 1. Créer le dépôt

Créer un dépôt vide nommé `gestion-absences-cicd` sur GitHub, puis exécuter :

```bash
git init
git add .
git commit -m "Premier commit : gestion des absences et tests"
git branch -M main
git remote add origin https://github.com/VOTRE-NOM/gestion-absences-cicd.git
git push -u origin main
```

### 2. Observer la pipeline

Ouvrir l'onglet **Actions** du dépôt GitHub. Le graphique doit afficher `lint` et
`test` en parallèle, puis `build`, puis `deploy`.

### 3. Provoquer un échec

Dans `gestion_absences.py`, modifier temporairement le calcul de la durée :

```python
return (fin - debut).days
```

Lancer les tests, constater l'échec, puis envoyer le changement :

```bash
git add gestion_absences.py
git commit -m "Bug volontaire dans le calcul des jours"
git push
```

La pipeline doit bloquer `build` et `deploy`. Remettre ensuite `+ 1`, vérifier les
tests et pousser la correction.

### 4. Travailler avec une Pull Request

```bash
git switch -c ajout-export-absences
```

Ajouter une fonctionnalité et son test, puis :

```bash
git add .
git commit -m "Ajout d'une fonctionnalite"
git push -u origin ajout-export-absences
```

Créer une Pull Request vers `main`. Sur la Pull Request, `lint`, `test` et `build`
doivent passer, tandis que `deploy` est ignoré. Après la fusion dans `main`, une
nouvelle pipeline exécute aussi `deploy`.
