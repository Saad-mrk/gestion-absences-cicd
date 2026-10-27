import pytest

from gestion_absences import (
    ajouter_absence,
    est_absent,
    nombre_jours,
    total_jours_absence,
)


def test_ajouter_absence():
    absences = []

    absence = ajouter_absence(
        absences,
        "Nadia",
        "2026-10-05",
        "2026-10-06",
        "Congé annuel",
    )

    assert len(absences) == 1
    assert absence["employe"] == "Nadia"


def test_nombre_jours_inclusif():
    absence = {
        "employe": "Nadia",
        "debut": "2026-10-05",
        "fin": "2026-10-07",
        "motif": "Congé annuel",
    }

    assert nombre_jours(absence) == 3


def test_total_jours_pour_un_employe():
    absences = []
    ajouter_absence(absences, "Nadia", "2026-10-05", "2026-10-06", "Congé")
    ajouter_absence(absences, "Nadia", "2026-11-10", "2026-11-10", "Maladie")
    ajouter_absence(absences, "Omar", "2026-10-05", "2026-10-07", "Congé")

    assert total_jours_absence(absences, "Nadia") == 3


def test_employe_absent_a_une_date():
    absences = []
    ajouter_absence(absences, "Nadia", "2026-10-05", "2026-10-07", "Congé")

    assert est_absent(absences, "Nadia", "2026-10-06") is True
    assert est_absent(absences, "Nadia", "2026-10-08") is False


def test_date_de_fin_invalide():
    with pytest.raises(ValueError):
        ajouter_absence(
            [],
            "Nadia",
            "2026-10-10",
            "2026-10-08",
            "Congé",
        )
