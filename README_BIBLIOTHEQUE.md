# 📚 Système de Gestion de Bibliothèque Universitaire

## Description
Mini-projet ALGO3 - L2 ISIL Groupe C

Système complet de gestion d'une bibliothèque universitaire permettant de gérer les livres, les utilisateurs et les emprunts.

## Fonctionnalités

### 🔹 Gestion des Livres
- ✅ Ajouter un livre (ISBN, titre, auteur, année)
- ✅ Supprimer un livre
- ✅ Rechercher un livre (par titre, auteur ou ISBN)
- ✅ Afficher tous les livres avec leur statut

### 🔹 Gestion des Utilisateurs
- ✅ Ajouter un utilisateur (ID, nom, prénom, email)
- ✅ Supprimer un utilisateur
- ✅ Afficher tous les utilisateurs

### 🔹 Gestion des Emprunts
- ✅ Emprunter un livre (avec date de retour prévue)
- ✅ Retourner un livre (avec détection de retard)
- ✅ Afficher les emprunts en cours
- ✅ Limite de 3 emprunts simultanés par utilisateur

### 🔹 Statistiques
- ✅ Top des livres les plus empruntés
- ✅ Top des utilisateurs les plus actifs
- ✅ Statistiques générales de la bibliothèque

### 🔹 Persistance des Données
- ✅ Sauvegarde automatique dans des fichiers JSON
- ✅ Chargement des données au démarrage
- ✅ 3 fichiers : `livres.json`, `utilisateurs.json`, `emprunts.json`

## Installation et Exécution

### Prérequis
- Python 3.6 ou supérieur

### Lancement du programme
```bash
python3 bibliotheque.py
```

## Utilisation

### Menu Principal
Le programme affiche un menu interactif avec 15 options :

```
1.  Ajouter un livre
2.  Supprimer un livre
3.  Rechercher un livre
4.  Afficher tous les livres
5.  Ajouter un utilisateur
6.  Supprimer un utilisateur
7.  Afficher tous les utilisateurs
8.  Emprunter un livre
9.  Retourner un livre
10. Afficher les emprunts en cours
11. Livres les plus empruntés
12. Utilisateurs les plus actifs
13. Statistiques générales
14. Sauvegarder les données
15. Charger les données
0.  Quitter
```

### Exemples d'utilisation

#### 1. Ajouter un livre
```
Choix : 1
ISBN : 978-2-1234-5678-9
Titre : Introduction à l'Algorithmique
Auteur : Thomas H. Cormen
Année de publication : 2009
```

#### 2. Ajouter un utilisateur
```
Choix : 5
ID utilisateur : U001
Nom : Dupont
Prénom : Jean
Email : jean.dupont@univ.dz
```

#### 3. Emprunter un livre
```
Choix : 8
ISBN du livre : 978-2-1234-5678-9
ID de l'utilisateur : U001
Durée de l'emprunt en jours : 14
```

#### 4. Rechercher un livre
```
Choix : 3
Critère : auteur
Valeur à rechercher : Cormen
```

## Structure du Code

### Classes Principales

#### `Livre`
- Attributs : isbn, titre, auteur, annee, disponible, nombre_emprunts
- Méthodes : to_dict(), from_dict(), __str__()

#### `Utilisateur`
- Attributs : id_utilisateur, nom, prenom, email, livres_empruntes, historique_emprunts
- Méthodes : to_dict(), from_dict(), __str__()

#### `Emprunt`
- Attributs : isbn, id_utilisateur, date_emprunt, date_retour_prevue, date_retour_effective
- Méthodes : to_dict(), from_dict()

#### `Bibliotheque`
- Gère l'ensemble du système
- Contient toutes les méthodes de gestion

## Règles de Gestion

### Emprunts
- ✅ Un utilisateur peut emprunter maximum 3 livres simultanément
- ✅ Durée par défaut : 14 jours
- ✅ Détection automatique des retards
- ✅ Un livre emprunté ne peut pas être supprimé

### Utilisateurs
- ✅ Un utilisateur avec des emprunts en cours ne peut pas être supprimé
- ✅ Historique complet des emprunts conservé

### Livres
- ✅ ISBN unique pour chaque livre
- ✅ Suivi du nombre total d'emprunts

## Fichiers de Données

### `livres.json`
Contient tous les livres avec leurs informations et statistiques.

### `utilisateurs.json`
Contient tous les utilisateurs avec leur historique d'emprunts.

### `emprunts.json`
Contient l'historique complet de tous les emprunts (en cours et terminés).

## Fonctionnalités Avancées

### Sauvegarde Automatique
- Sauvegarde automatique lors de la fermeture du programme
- Possibilité de sauvegarder manuellement à tout moment

### Statistiques Détaillées
- Classement des livres par popularité
- Classement des utilisateurs par activité
- Vue d'ensemble de la bibliothèque

### Gestion des Erreurs
- Validation de toutes les entrées
- Messages d'erreur clairs et informatifs
- Prévention des opérations invalides

## Auteur
Mini-projet ALGO3 - L2 ISIL Groupe C

## Licence
Projet académique - Université
