# 📁 Structure du Projet - Système de Bibliothèque

## Fichiers du Projet

```
📦 Projet Bibliothèque
├── 📄 bibliotheque.py              # Programme principal
├── 📄 test_bibliotheque.py         # Script de test et initialisation
├── 📄 README_BIBLIOTHEQUE.md       # Documentation complète
├── 📄 GUIDE_UTILISATION.md         # Guide d'utilisation rapide
├── 📄 STRUCTURE_PROJET.md          # Ce fichier
├── 📄 livres.json                  # Données des livres (généré)
├── 📄 utilisateurs.json            # Données des utilisateurs (généré)
└── 📄 emprunts.json                # Données des emprunts (généré)
```

## Description des Fichiers

### 📄 bibliotheque.py (Programme Principal)
**Taille** : ~700 lignes  
**Contenu** :
- Classe `Livre` : Gestion des livres
- Classe `Utilisateur` : Gestion des utilisateurs
- Classe `Emprunt` : Gestion des emprunts
- Classe `Bibliotheque` : Système principal
- Fonction `main()` : Interface utilisateur
- Menu interactif avec 15 options

**Utilisation** :
```bash
python3 bibliotheque.py
```

### 📄 test_bibliotheque.py (Tests et Initialisation)
**Taille** : ~180 lignes  
**Contenu** :
- Fonction `initialiser_donnees_test()` : Crée des données d'exemple
- Fonction `tester_fonctionnalites()` : Teste toutes les fonctionnalités
- Menu de test interactif

**Utilisation** :
```bash
python3 test_bibliotheque.py
```

### 📄 Fichiers JSON (Données)

#### livres.json
Structure d'un livre :
```json
{
  "isbn": "978-2-7440-7326-9",
  "titre": "Introduction à l'Algorithmique",
  "auteur": "Thomas H. Cormen",
  "annee": 2009,
  "disponible": false,
  "nombre_emprunts": 1
}
```

#### utilisateurs.json
Structure d'un utilisateur :
```json
{
  "id_utilisateur": "U001",
  "nom": "Benali",
  "prenom": "Ahmed",
  "email": "ahmed.benali@univ.dz",
  "livres_empruntes": ["978-2-7440-7326-9"],
  "historique_emprunts": 2
}
```

#### emprunts.json
Structure d'un emprunt :
```json
{
  "isbn": "978-2-7440-7326-9",
  "id_utilisateur": "U001",
  "date_emprunt": "2025-11-12",
  "date_retour_prevue": "2025-11-26",
  "date_retour_effective": null
}
```

## Architecture du Code

### Diagramme de Classes

```
┌─────────────────────┐
│      Livre          │
├─────────────────────┤
│ - isbn              │
│ - titre             │
│ - auteur            │
│ - annee             │
│ - disponible        │
│ - nombre_emprunts   │
├─────────────────────┤
│ + to_dict()         │
│ + from_dict()       │
│ + __str__()         │
└─────────────────────┘

┌─────────────────────┐
│   Utilisateur       │
├─────────────────────┤
│ - id_utilisateur    │
│ - nom               │
│ - prenom            │
│ - email             │
│ - livres_empruntes  │
│ - historique_emprunts│
├─────────────────────┤
│ + to_dict()         │
│ + from_dict()       │
│ + __str__()         │
└─────────────────────┘

┌─────────────────────┐
│      Emprunt        │
├─────────────────────┤
│ - isbn              │
│ - id_utilisateur    │
│ - date_emprunt      │
│ - date_retour_prevue│
│ - date_retour_effective│
├─────────────────────┤
│ + to_dict()         │
│ + from_dict()       │
└─────────────────────┘

┌─────────────────────────────────────┐
│         Bibliotheque                │
├─────────────────────────────────────┤
│ - livres: Dict[str, Livre]          │
│ - utilisateurs: Dict[str, Utilisateur]│
│ - emprunts: List[Emprunt]           │
├─────────────────────────────────────┤
│ GESTION DES LIVRES                  │
│ + ajouter_livre()                   │
│ + supprimer_livre()                 │
│ + rechercher_livre()                │
│ + afficher_livres()                 │
│                                     │
│ GESTION DES UTILISATEURS            │
│ + ajouter_utilisateur()             │
│ + supprimer_utilisateur()           │
│ + afficher_utilisateurs()           │
│                                     │
│ GESTION DES EMPRUNTS                │
│ + emprunter_livre()                 │
│ + retourner_livre()                 │
│ + afficher_emprunts_en_cours()      │
│                                     │
│ STATISTIQUES                        │
│ + livres_plus_empruntes()           │
│ + utilisateurs_plus_actifs()        │
│ + statistiques_generales()          │
│                                     │
│ PERSISTANCE                         │
│ + sauvegarder_donnees()             │
│ + charger_donnees()                 │
└─────────────────────────────────────┘
```

## Flux de Données

### 1. Démarrage du Programme
```
main()
  ↓
Bibliotheque()
  ↓
charger_donnees()
  ↓
Lecture des fichiers JSON
  ↓
Affichage du menu
```

### 2. Emprunt d'un Livre
```
emprunter_livre(isbn, id_user)
  ↓
Vérifications :
  - Livre existe ?
  - Utilisateur existe ?
  - Livre disponible ?
  - Limite d'emprunts respectée ?
  ↓
Créer Emprunt
  ↓
Mettre à jour Livre (disponible = False)
  ↓
Mettre à jour Utilisateur (ajouter à livres_empruntes)
  ↓
Incrémenter statistiques
```

### 3. Retour d'un Livre
```
retourner_livre(isbn, id_user)
  ↓
Vérifications :
  - Livre existe ?
  - Utilisateur existe ?
  - Emprunt existe ?
  ↓
Mettre à jour Emprunt (date_retour_effective)
  ↓
Vérifier retard
  ↓
Mettre à jour Livre (disponible = True)
  ↓
Mettre à jour Utilisateur (retirer de livres_empruntes)
```

### 4. Sauvegarde des Données
```
sauvegarder_donnees()
  ↓
Convertir objets en dictionnaires
  ↓
Écrire dans livres.json
  ↓
Écrire dans utilisateurs.json
  ↓
Écrire dans emprunts.json
```

## Règles de Gestion Implémentées

### 🔒 Contraintes d'Intégrité

1. **ISBN Unique** : Chaque livre a un ISBN unique
2. **ID Utilisateur Unique** : Chaque utilisateur a un ID unique
3. **Limite d'Emprunts** : Maximum 3 livres par utilisateur
4. **Disponibilité** : Un livre emprunté n'est pas disponible
5. **Suppression Protégée** : 
   - Livre emprunté → non supprimable
   - Utilisateur avec emprunts → non supprimable

### 📅 Gestion des Dates

- **Format** : YYYY-MM-DD (ISO 8601)
- **Durée par défaut** : 14 jours
- **Détection de retard** : Automatique lors du retour
- **Calcul** : Utilisation de `datetime` et `timedelta`

### 📊 Statistiques Suivies

1. **Par Livre** :
   - Nombre total d'emprunts
   - Statut actuel (disponible/emprunté)

2. **Par Utilisateur** :
   - Nombre d'emprunts en cours
   - Historique total des emprunts

3. **Globales** :
   - Total de livres
   - Total d'utilisateurs
   - Total d'emprunts (historique)
   - Emprunts en cours

## Technologies Utilisées

### Bibliothèques Python Standard

```python
import json          # Sauvegarde/chargement des données
import os            # Vérification de l'existence des fichiers
from datetime import datetime, timedelta  # Gestion des dates
from typing import List, Dict, Optional   # Type hints
```

### Concepts de Programmation

- ✅ **POO** : Classes, encapsulation, méthodes
- ✅ **Type Hints** : Annotations de types pour la clarté
- ✅ **Docstrings** : Documentation des fonctions
- ✅ **Gestion d'erreurs** : Validation et messages clairs
- ✅ **Sérialisation** : Conversion objets ↔ JSON
- ✅ **Collections** : Dictionnaires, listes
- ✅ **Algorithmes** : Tri, recherche, filtrage

## Évolutions Possibles

### 🚀 Améliorations Futures

1. **Interface Graphique** : Tkinter ou PyQt
2. **Base de Données** : SQLite ou PostgreSQL
3. **Authentification** : Système de login
4. **Notifications** : Rappels de retour par email
5. **Amendes** : Calcul automatique des pénalités
6. **Réservations** : Système de réservation de livres
7. **Catégories** : Classification des livres par genre
8. **Recherche Avancée** : Filtres multiples
9. **Export** : Génération de rapports PDF
10. **API REST** : Service web avec Flask/FastAPI

### 🔧 Optimisations Techniques

1. **Cache** : Mise en cache des recherches fréquentes
2. **Index** : Indexation pour recherches rapides
3. **Validation** : Validation plus stricte des emails/ISBN
4. **Logging** : Système de logs pour audit
5. **Tests Unitaires** : Suite de tests avec pytest
6. **Configuration** : Fichier de configuration externe
7. **Multilingue** : Support de plusieurs langues

## Conformité au Cahier des Charges

### ✅ Fonctionnalités Requises

| Fonctionnalité | Statut | Fichier | Ligne |
|----------------|--------|---------|-------|
| Ajouter livre | ✅ | bibliotheque.py | 78-88 |
| Supprimer livre | ✅ | bibliotheque.py | 90-103 |
| Rechercher livre | ✅ | bibliotheque.py | 105-120 |
| Afficher livres | ✅ | bibliotheque.py | 122-132 |
| Ajouter utilisateur | ✅ | bibliotheque.py | 136-146 |
| Supprimer utilisateur | ✅ | bibliotheque.py | 148-161 |
| Afficher utilisateurs | ✅ | bibliotheque.py | 163-173 |
| Emprunter livre | ✅ | bibliotheque.py | 177-217 |
| Retourner livre | ✅ | bibliotheque.py | 219-260 |
| Emprunts en cours | ✅ | bibliotheque.py | 262-276 |
| Top livres | ✅ | bibliotheque.py | 280-292 |
| Top utilisateurs | ✅ | bibliotheque.py | 294-306 |
| Statistiques | ✅ | bibliotheque.py | 308-324 |
| Sauvegarder | ✅ | bibliotheque.py | 328-348 |
| Charger | ✅ | bibliotheque.py | 350-373 |

### 📋 Critères d'Évaluation

- ✅ **Code propre et commenté**
- ✅ **Structure POO claire**
- ✅ **Gestion des erreurs**
- ✅ **Interface utilisateur intuitive**
- ✅ **Persistance des données**
- ✅ **Fonctionnalités complètes**
- ✅ **Documentation complète**
- ✅ **Tests fonctionnels**

## Support et Contact

Pour toute question sur la structure du projet :
- Consultez les fichiers de documentation
- Examinez les commentaires dans le code
- Testez avec `test_bibliotheque.py`

---

**Projet réalisé dans le cadre du cours ALGO3 - L2 ISIL Groupe C**
