"""Prétraitement des données du projet WHO Life Expectancy."""


def imputer_par_statut(X_reference, X_a_imputer, variables_numeriques):
    """Remplace les valeurs numériques manquantes par des médianes.

    Pour chaque indicateur, la fonction utilise la médiane du statut de
    développement. Si cette médiane est indisponible, elle utilise la
    médiane globale. Les deux sont calculées sur X_reference.

    Args:
        X_reference: Données d’entraînement utilisées pour calculer les médianes.
        X_a_imputer: Données à traiter, contenant la colonne `status`.
        variables_numeriques: Noms des colonnes numériques à imputer.

    Returns:
        Une copie de X_a_imputer avec les valeurs numériques imputées.
    """
    medianes_par_statut = (
        X_reference.groupby("status")[variables_numeriques].median()
    )
    medianes_globales = X_reference[variables_numeriques].median()

    X_impute = X_a_imputer.copy()

    for colonne in variables_numeriques:
        medianes_du_statut = X_impute["status"].map(medianes_par_statut[colonne])
        X_impute[colonne] = (
            X_impute[colonne]
            .fillna(medianes_du_statut)
            .fillna(medianes_globales[colonne])
        )

    return X_impute
