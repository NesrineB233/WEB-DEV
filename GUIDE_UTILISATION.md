# 🚀 Guide d'Utilisation Rapide - Système de Bibliothèque

## Démarrage Rapide

### 1️⃣ Première utilisation - Initialiser avec des données de test

```bash
python3 test_bibliotheque.py
```

Choisissez l'option **3** pour initialiser les données de test et voir les fonctionnalités en action.

### 2️⃣ Lancer le programme principal

```bash
python3 bibliotheque.py
```

## 📋 Scénarios d'Utilisation Courants

### Scénario 1 : Ajouter un nouveau livre

1. Lancez le programme : `python3 bibliotheque.py`
2. Choisissez l'option **1** (Ajouter un livre)
3. Entrez les informations :
   ```
   ISBN : 978-2-1234-5678-9
   Titre : Mon Livre
   Auteur : Nom Auteur
   Année de publication : 2023
   ```

### Scénario 2 : Enregistrer un nouvel utilisateur

1. Choisissez l'option **5** (Ajouter un utilisateur)
2. Entrez les informations :
   ```
   ID utilisateur : U008
   Nom : Nom
   Prénom : Prénom
   Email : email@univ.dz
   ```

### Scénario 3 : Emprunter un livre

1. Choisissez l'option **8** (Emprunter un livre)
2. Entrez :
   ```
   ISBN du livre : 978-2-7440-7326-9
   ID de l'utilisateur : U001
   Durée de l'emprunt en jours : 14
   ```

### Scénario 4 : Retourner un livre

1. Choisissez l'option **9** (Retourner un livre)
2. Entrez :
   ```
   ISBN du livre : 978-2-7440-7326-9
   ID de l'utilisateur : U001
   ```

### Scénario 5 : Rechercher un livre

1. Choisissez l'option **3** (Rechercher un livre)
2. Entrez :
   ```
   Critère : auteur
   Valeur à rechercher : Cormen
   ```

Critères disponibles : **titre**, **auteur**, **isbn**

### Scénario 6 : Voir les statistiques

- Option **11** : Top des livres les plus empruntés
- Option **12** : Top des utilisateurs les plus actifs
- Option **13** : Statistiques générales de la bibliothèque

## 💡 Conseils et Astuces

### ✅ Bonnes Pratiques

1. **Sauvegardez régulièrement** : Utilisez l'option **14** pour sauvegarder manuellement
2. **Vérifiez les emprunts en cours** : Option **10** avant de supprimer un livre ou utilisateur
3. **Consultez les statistiques** : Option **13** pour avoir une vue d'ensemble

### ⚠️ Points d'Attention

- Un utilisateur ne peut emprunter que **3 livres maximum** simultanément
- Un livre emprunté **ne peut pas être supprimé**
- Un utilisateur avec des emprunts en cours **ne peut pas être supprimé**
- Les retours en retard sont **automatiquement détectés**

## 🔍 Exemples de Recherche

### Rechercher par titre
```
Critère : titre
Valeur : Python
```
→ Trouve tous les livres contenant "Python" dans le titre

### Rechercher par auteur
```
Critère : auteur
Valeur : Tanenbaum
```
→ Trouve tous les livres de cet auteur

### Rechercher par ISBN exact
```
Critère : isbn
Valeur : 978-2-7440-7326-9
```
→ Trouve le livre avec cet ISBN précis

## 📊 Comprendre les Statistiques

### Statistiques Générales (Option 13)
```
📚 Total de livres : 10
   - Disponibles : 4
   - Empruntés : 6
👥 Total d'utilisateurs : 7
📋 Total d'emprunts (historique) : 8
📋 Emprunts en cours : 6
```

### Top des Livres (Option 11)
Affiche les livres classés par nombre total d'emprunts (historique complet)

### Top des Utilisateurs (Option 12)
Affiche les utilisateurs classés par nombre total d'emprunts effectués

## 🗂️ Gestion des Données

### Fichiers de Sauvegarde

Le système crée automatiquement 3 fichiers JSON :

- **livres.json** : Tous les livres avec leurs statistiques
- **utilisateurs.json** : Tous les utilisateurs avec leur historique
- **emprunts.json** : Historique complet des emprunts

### Sauvegarde et Chargement

- **Sauvegarde automatique** : À la fermeture du programme (option 0)
- **Sauvegarde manuelle** : Option 14
- **Chargement** : Automatique au démarrage ou option 15

## 🐛 Résolution de Problèmes

### Problème : "Erreur : Un livre avec l'ISBN XXX existe déjà"
**Solution** : Vérifiez que l'ISBN est unique. Utilisez l'option 4 pour voir tous les livres.

### Problème : "Erreur : Le livre est actuellement emprunté"
**Solution** : Attendez le retour du livre (option 9) avant de le supprimer.

### Problème : "Erreur : L'utilisateur a atteint la limite de 3 emprunts"
**Solution** : L'utilisateur doit retourner un livre avant d'en emprunter un nouveau.

### Problème : "Erreur lors du chargement des données"
**Solution** : Les fichiers JSON sont peut-être corrompus. Supprimez-les et réinitialisez avec `test_bibliotheque.py`.

## 📞 Support

Pour toute question ou problème :
1. Consultez le fichier **README_BIBLIOTHEQUE.md** pour plus de détails
2. Vérifiez que Python 3.6+ est installé : `python3 --version`
3. Assurez-vous d'avoir les droits d'écriture dans le répertoire

## 🎯 Workflow Typique d'une Session

```
1. Lancer le programme
   → python3 bibliotheque.py

2. Consulter les livres disponibles
   → Option 4

3. Consulter les utilisateurs
   → Option 7

4. Effectuer des emprunts
   → Option 8

5. Consulter les emprunts en cours
   → Option 10

6. Traiter les retours
   → Option 9

7. Voir les statistiques
   → Option 13

8. Sauvegarder et quitter
   → Option 0 (sauvegarde automatique)
```

## 🎓 Pour les Étudiants

Ce projet couvre les concepts suivants :
- ✅ Programmation Orientée Objet (POO)
- ✅ Structures de données (listes, dictionnaires)
- ✅ Gestion de fichiers (JSON)
- ✅ Manipulation de dates
- ✅ Validation des données
- ✅ Interface utilisateur en ligne de commande
- ✅ Gestion des erreurs

Bon apprentissage ! 📚✨
