"""Fonctions simples pour gérer les absences des salariés."""

from datetime import date


def _convertir_date(valeur):
    """Convertit une date ISO (AAAA-MM-JJ) en objet date."""
    try:
        return date.fromisoformat(valeur)
    except (TypeError, ValueError) as erreur:
        raise ValueError("La date doit être au format AAAA-MM-JJ") from erreur


def ajouter_absence(absences, employe, debut, fin, motif):
    """Ajoute une absence après avoir vérifié ses informations."""
    if not employe.strip():
        raise ValueError("Le nom de l'employé est obligatoire")
    if not motif.strip():
        raise ValueError("Le motif est obligatoire")

    date_debut = _convertir_date(debut)
    date_fin = _convertir_date(fin)
    if date_fin < date_debut:
        raise ValueError("La date de fin doit être après la date de début")

    absence = {
        "employe": employe,
        "debut": debut,
        "fin": fin,
        "motif": motif,
    }
    absences.append(absence)
    return absence


def nombre_jours(absence):
    """Retourne le nombre de jours d'une absence, début et fin inclus."""
    debut = _convertir_date(absence["debut"])
    fin = _convertir_date(absence["fin"])
    return (fin - debut).days + 1


def total_jours_absence(absences, employe):
    """Calcule le total de jours d'absence d'un employé."""
    return sum(
        nombre_jours(absence)
        for absence in absences
        if absence["employe"] == employe
    )


def est_absent(absences, employe, jour):
    """Indique si un employé est absent à une date donnée."""
    date_a_verifier = _convertir_date(jour)
    return any(
        absence["employe"] == employe
        and _convertir_date(absence["debut"]) <= date_a_verifier <= _convertir_date(absence["fin"])
        for absence in absences
    )
