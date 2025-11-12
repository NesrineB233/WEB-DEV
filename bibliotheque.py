"""
Mini Projet ALGO3 - Gestion de Bibliothèque Universitaire
L2 ISIL - Groupe C
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class Livre:
    """Classe représentant un livre dans la bibliothèque"""
    
    def __init__(self, isbn: str, titre: str, auteur: str, annee: int, disponible: bool = True):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible
        self.nombre_emprunts = 0
    
    def to_dict(self) -> dict:
        """Convertit le livre en dictionnaire pour la sauvegarde"""
        return {
            'isbn': self.isbn,
            'titre': self.titre,
            'auteur': self.auteur,
            'annee': self.annee,
            'disponible': self.disponible,
            'nombre_emprunts': self.nombre_emprunts
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Livre':
        """Crée un livre à partir d'un dictionnaire"""
        livre = Livre(data['isbn'], data['titre'], data['auteur'], data['annee'], data['disponible'])
        livre.nombre_emprunts = data.get('nombre_emprunts', 0)
        return livre
    
    def __str__(self) -> str:
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"ISBN: {self.isbn} | Titre: {self.titre} | Auteur: {self.auteur} | Année: {self.annee} | Statut: {statut} | Emprunts: {self.nombre_emprunts}"


class Utilisateur:
    """Classe représentant un utilisateur de la bibliothèque"""
    
    def __init__(self, id_utilisateur: str, nom: str, prenom: str, email: str):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.livres_empruntes: List[str] = []  # Liste des ISBN empruntés
        self.historique_emprunts = 0
    
    def to_dict(self) -> dict:
        """Convertit l'utilisateur en dictionnaire pour la sauvegarde"""
        return {
            'id_utilisateur': self.id_utilisateur,
            'nom': self.nom,
            'prenom': self.prenom,
            'email': self.email,
            'livres_empruntes': self.livres_empruntes,
            'historique_emprunts': self.historique_emprunts
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Utilisateur':
        """Crée un utilisateur à partir d'un dictionnaire"""
        utilisateur = Utilisateur(data['id_utilisateur'], data['nom'], data['prenom'], data['email'])
        utilisateur.livres_empruntes = data.get('livres_empruntes', [])
        utilisateur.historique_emprunts = data.get('historique_emprunts', 0)
        return utilisateur
    
    def __str__(self) -> str:
        return f"ID: {self.id_utilisateur} | Nom: {self.nom} {self.prenom} | Email: {self.email} | Livres empruntés: {len(self.livres_empruntes)} | Total emprunts: {self.historique_emprunts}"


class Emprunt:
    """Classe représentant un emprunt"""
    
    def __init__(self, isbn: str, id_utilisateur: str, date_emprunt: str, date_retour_prevue: str):
        self.isbn = isbn
        self.id_utilisateur = id_utilisateur
        self.date_emprunt = date_emprunt
        self.date_retour_prevue = date_retour_prevue
        self.date_retour_effective: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convertit l'emprunt en dictionnaire pour la sauvegarde"""
        return {
            'isbn': self.isbn,
            'id_utilisateur': self.id_utilisateur,
            'date_emprunt': self.date_emprunt,
            'date_retour_prevue': self.date_retour_prevue,
            'date_retour_effective': self.date_retour_effective
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Emprunt':
        """Crée un emprunt à partir d'un dictionnaire"""
        emprunt = Emprunt(data['isbn'], data['id_utilisateur'], data['date_emprunt'], data['date_retour_prevue'])
        emprunt.date_retour_effective = data.get('date_retour_effective')
        return emprunt


class Bibliotheque:
    """Classe principale gérant la bibliothèque"""
    
    def __init__(self):
        self.livres: Dict[str, Livre] = {}
        self.utilisateurs: Dict[str, Utilisateur] = {}
        self.emprunts: List[Emprunt] = []
        self.fichier_livres = "livres.json"
        self.fichier_utilisateurs = "utilisateurs.json"
        self.fichier_emprunts = "emprunts.json"
    
    # ==================== GESTION DES LIVRES ====================
    
    def ajouter_livre(self, isbn: str, titre: str, auteur: str, annee: int) -> bool:
        """Ajoute un livre à la bibliothèque"""
        if isbn in self.livres:
            print(f"❌ Erreur : Un livre avec l'ISBN {isbn} existe déjà.")
            return False
        
        self.livres[isbn] = Livre(isbn, titre, auteur, annee)
        print(f"✅ Livre '{titre}' ajouté avec succès.")
        return True
    
    def supprimer_livre(self, isbn: str) -> bool:
        """Supprime un livre de la bibliothèque"""
        if isbn not in self.livres:
            print(f"❌ Erreur : Aucun livre trouvé avec l'ISBN {isbn}.")
            return False
        
        if not self.livres[isbn].disponible:
            print(f"❌ Erreur : Le livre est actuellement emprunté et ne peut pas être supprimé.")
            return False
        
        titre = self.livres[isbn].titre
        del self.livres[isbn]
        print(f"✅ Livre '{titre}' supprimé avec succès.")
        return True
    
    def rechercher_livre(self, critere: str, valeur: str) -> List[Livre]:
        """Recherche des livres par titre, auteur ou ISBN"""
        resultats = []
        critere = critere.lower()
        valeur = valeur.lower()
        
        for livre in self.livres.values():
            if critere == "titre" and valeur in livre.titre.lower():
                resultats.append(livre)
            elif critere == "auteur" and valeur in livre.auteur.lower():
                resultats.append(livre)
            elif critere == "isbn" and valeur == livre.isbn.lower():
                resultats.append(livre)
        
        return resultats
    
    def afficher_livres(self):
        """Affiche tous les livres de la bibliothèque"""
        if not self.livres:
            print("📚 La bibliothèque est vide.")
            return
        
        print(f"\n📚 Liste des livres ({len(self.livres)} livre(s)) :")
        print("=" * 120)
        for livre in sorted(self.livres.values(), key=lambda x: x.titre):
            print(livre)
        print("=" * 120)
    
    # ==================== GESTION DES UTILISATEURS ====================
    
    def ajouter_utilisateur(self, id_utilisateur: str, nom: str, prenom: str, email: str) -> bool:
        """Ajoute un utilisateur à la bibliothèque"""
        if id_utilisateur in self.utilisateurs:
            print(f"❌ Erreur : Un utilisateur avec l'ID {id_utilisateur} existe déjà.")
            return False
        
        self.utilisateurs[id_utilisateur] = Utilisateur(id_utilisateur, nom, prenom, email)
        print(f"✅ Utilisateur '{prenom} {nom}' ajouté avec succès.")
        return True
    
    def supprimer_utilisateur(self, id_utilisateur: str) -> bool:
        """Supprime un utilisateur de la bibliothèque"""
        if id_utilisateur not in self.utilisateurs:
            print(f"❌ Erreur : Aucun utilisateur trouvé avec l'ID {id_utilisateur}.")
            return False
        
        if self.utilisateurs[id_utilisateur].livres_empruntes:
            print(f"❌ Erreur : L'utilisateur a des livres empruntés et ne peut pas être supprimé.")
            return False
        
        nom = f"{self.utilisateurs[id_utilisateur].prenom} {self.utilisateurs[id_utilisateur].nom}"
        del self.utilisateurs[id_utilisateur]
        print(f"✅ Utilisateur '{nom}' supprimé avec succès.")
        return True
    
    def afficher_utilisateurs(self):
        """Affiche tous les utilisateurs de la bibliothèque"""
        if not self.utilisateurs:
            print("👥 Aucun utilisateur enregistré.")
            return
        
        print(f"\n👥 Liste des utilisateurs ({len(self.utilisateurs)} utilisateur(s)) :")
        print("=" * 120)
        for utilisateur in sorted(self.utilisateurs.values(), key=lambda x: x.nom):
            print(utilisateur)
        print("=" * 120)
    
    # ==================== GESTION DES EMPRUNTS ====================
    
    def emprunter_livre(self, isbn: str, id_utilisateur: str, duree_jours: int = 14) -> bool:
        """Permet à un utilisateur d'emprunter un livre"""
        if isbn not in self.livres:
            print(f"❌ Erreur : Aucun livre trouvé avec l'ISBN {isbn}.")
            return False
        
        if id_utilisateur not in self.utilisateurs:
            print(f"❌ Erreur : Aucun utilisateur trouvé avec l'ID {id_utilisateur}.")
            return False
        
        livre = self.livres[isbn]
        utilisateur = self.utilisateurs[id_utilisateur]
        
        if not livre.disponible:
            print(f"❌ Erreur : Le livre '{livre.titre}' est déjà emprunté.")
            return False
        
        if len(utilisateur.livres_empruntes) >= 3:
            print(f"❌ Erreur : L'utilisateur a atteint la limite de 3 emprunts simultanés.")
            return False
        
        # Créer l'emprunt
        date_emprunt = datetime.now().strftime("%Y-%m-%d")
        date_retour_prevue = (datetime.now() + timedelta(days=duree_jours)).strftime("%Y-%m-%d")
        
        emprunt = Emprunt(isbn, id_utilisateur, date_emprunt, date_retour_prevue)
        self.emprunts.append(emprunt)
        
        # Mettre à jour le livre et l'utilisateur
        livre.disponible = False
        livre.nombre_emprunts += 1
        utilisateur.livres_empruntes.append(isbn)
        utilisateur.historique_emprunts += 1
        
        print(f"✅ Livre '{livre.titre}' emprunté par {utilisateur.prenom} {utilisateur.nom}.")
        print(f"   Date d'emprunt : {date_emprunt}")
        print(f"   Date de retour prévue : {date_retour_prevue}")
        return True
    
    def retourner_livre(self, isbn: str, id_utilisateur: str) -> bool:
        """Permet à un utilisateur de retourner un livre"""
        if isbn not in self.livres:
            print(f"❌ Erreur : Aucun livre trouvé avec l'ISBN {isbn}.")
            return False
        
        if id_utilisateur not in self.utilisateurs:
            print(f"❌ Erreur : Aucun utilisateur trouvé avec l'ID {id_utilisateur}.")
            return False
        
        livre = self.livres[isbn]
        utilisateur = self.utilisateurs[id_utilisateur]
        
        if isbn not in utilisateur.livres_empruntes:
            print(f"❌ Erreur : L'utilisateur n'a pas emprunté ce livre.")
            return False
        
        # Trouver l'emprunt correspondant
        emprunt_trouve = None
        for emprunt in self.emprunts:
            if emprunt.isbn == isbn and emprunt.id_utilisateur == id_utilisateur and emprunt.date_retour_effective is None:
                emprunt_trouve = emprunt
                break
        
        if emprunt_trouve:
            emprunt_trouve.date_retour_effective = datetime.now().strftime("%Y-%m-%d")
            
            # Vérifier si le retour est en retard
            date_retour_prevue = datetime.strptime(emprunt_trouve.date_retour_prevue, "%Y-%m-%d")
            date_retour_effective = datetime.strptime(emprunt_trouve.date_retour_effective, "%Y-%m-%d")
            
            if date_retour_effective > date_retour_prevue:
                jours_retard = (date_retour_effective - date_retour_prevue).days
                print(f"⚠️  Attention : Retour en retard de {jours_retard} jour(s).")
        
        # Mettre à jour le livre et l'utilisateur
        livre.disponible = True
        utilisateur.livres_empruntes.remove(isbn)
        
        print(f"✅ Livre '{livre.titre}' retourné par {utilisateur.prenom} {utilisateur.nom}.")
        return True
    
    def afficher_emprunts_en_cours(self):
        """Affiche tous les emprunts en cours"""
        emprunts_en_cours = [e for e in self.emprunts if e.date_retour_effective is None]
        
        if not emprunts_en_cours:
            print("📋 Aucun emprunt en cours.")
            return
        
        print(f"\n📋 Emprunts en cours ({len(emprunts_en_cours)}) :")
        print("=" * 120)
        for emprunt in emprunts_en_cours:
            livre = self.livres.get(emprunt.isbn)
            utilisateur = self.utilisateurs.get(emprunt.id_utilisateur)
            if livre and utilisateur:
                print(f"Livre: {livre.titre} | Utilisateur: {utilisateur.prenom} {utilisateur.nom} | "
                      f"Date emprunt: {emprunt.date_emprunt} | Retour prévu: {emprunt.date_retour_prevue}")
        print("=" * 120)
    
    # ==================== STATISTIQUES ====================
    
    def livres_plus_empruntes(self, top_n: int = 5):
        """Affiche les livres les plus empruntés"""
        if not self.livres:
            print("📊 Aucun livre dans la bibliothèque.")
            return
        
        livres_tries = sorted(self.livres.values(), key=lambda x: x.nombre_emprunts, reverse=True)
        
        print(f"\n📊 Top {top_n} des livres les plus empruntés :")
        print("=" * 120)
        for i, livre in enumerate(livres_tries[:top_n], 1):
            print(f"{i}. {livre.titre} par {livre.auteur} - {livre.nombre_emprunts} emprunt(s)")
        print("=" * 120)
    
    def utilisateurs_plus_actifs(self, top_n: int = 5):
        """Affiche les utilisateurs les plus actifs"""
        if not self.utilisateurs:
            print("📊 Aucun utilisateur enregistré.")
            return
        
        utilisateurs_tries = sorted(self.utilisateurs.values(), key=lambda x: x.historique_emprunts, reverse=True)
        
        print(f"\n📊 Top {top_n} des utilisateurs les plus actifs :")
        print("=" * 120)
        for i, utilisateur in enumerate(utilisateurs_tries[:top_n], 1):
            print(f"{i}. {utilisateur.prenom} {utilisateur.nom} - {utilisateur.historique_emprunts} emprunt(s)")
        print("=" * 120)
    
    def statistiques_generales(self):
        """Affiche les statistiques générales de la bibliothèque"""
        total_livres = len(self.livres)
        livres_disponibles = sum(1 for livre in self.livres.values() if livre.disponible)
        livres_empruntes = total_livres - livres_disponibles
        total_utilisateurs = len(self.utilisateurs)
        total_emprunts = len(self.emprunts)
        emprunts_en_cours = sum(1 for e in self.emprunts if e.date_retour_effective is None)
        
        print("\n📊 Statistiques générales de la bibliothèque :")
        print("=" * 60)
        print(f"📚 Total de livres : {total_livres}")
        print(f"   - Disponibles : {livres_disponibles}")
        print(f"   - Empruntés : {livres_empruntes}")
        print(f"👥 Total d'utilisateurs : {total_utilisateurs}")
        print(f"📋 Total d'emprunts (historique) : {total_emprunts}")
        print(f"📋 Emprunts en cours : {emprunts_en_cours}")
        print("=" * 60)
    
    # ==================== SAUVEGARDE ET CHARGEMENT ====================
    
    def sauvegarder_donnees(self):
        """Sauvegarde toutes les données dans des fichiers JSON"""
        try:
            # Sauvegarder les livres
            with open(self.fichier_livres, 'w', encoding='utf-8') as f:
                livres_data = [livre.to_dict() for livre in self.livres.values()]
                json.dump(livres_data, f, ensure_ascii=False, indent=2)
            
            # Sauvegarder les utilisateurs
            with open(self.fichier_utilisateurs, 'w', encoding='utf-8') as f:
                utilisateurs_data = [utilisateur.to_dict() for utilisateur in self.utilisateurs.values()]
                json.dump(utilisateurs_data, f, ensure_ascii=False, indent=2)
            
            # Sauvegarder les emprunts
            with open(self.fichier_emprunts, 'w', encoding='utf-8') as f:
                emprunts_data = [emprunt.to_dict() for emprunt in self.emprunts]
                json.dump(emprunts_data, f, ensure_ascii=False, indent=2)
            
            print("✅ Données sauvegardées avec succès.")
            return True
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde : {e}")
            return False
    
    def charger_donnees(self):
        """Charge toutes les données depuis les fichiers JSON"""
        try:
            # Charger les livres
            if os.path.exists(self.fichier_livres):
                with open(self.fichier_livres, 'r', encoding='utf-8') as f:
                    livres_data = json.load(f)
                    self.livres = {livre['isbn']: Livre.from_dict(livre) for livre in livres_data}
            
            # Charger les utilisateurs
            if os.path.exists(self.fichier_utilisateurs):
                with open(self.fichier_utilisateurs, 'r', encoding='utf-8') as f:
                    utilisateurs_data = json.load(f)
                    self.utilisateurs = {user['id_utilisateur']: Utilisateur.from_dict(user) for user in utilisateurs_data}
            
            # Charger les emprunts
            if os.path.exists(self.fichier_emprunts):
                with open(self.fichier_emprunts, 'r', encoding='utf-8') as f:
                    emprunts_data = json.load(f)
                    self.emprunts = [Emprunt.from_dict(emprunt) for emprunt in emprunts_data]
            
            print("✅ Données chargées avec succès.")
            return True
        except Exception as e:
            print(f"❌ Erreur lors du chargement : {e}")
            return False


def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "=" * 60)
    print("📚 SYSTÈME DE GESTION DE BIBLIOTHÈQUE UNIVERSITAIRE 📚")
    print("=" * 60)
    print("\n--- GESTION DES LIVRES ---")
    print("1.  Ajouter un livre")
    print("2.  Supprimer un livre")
    print("3.  Rechercher un livre")
    print("4.  Afficher tous les livres")
    print("\n--- GESTION DES UTILISATEURS ---")
    print("5.  Ajouter un utilisateur")
    print("6.  Supprimer un utilisateur")
    print("7.  Afficher tous les utilisateurs")
    print("\n--- GESTION DES EMPRUNTS ---")
    print("8.  Emprunter un livre")
    print("9.  Retourner un livre")
    print("10. Afficher les emprunts en cours")
    print("\n--- STATISTIQUES ---")
    print("11. Livres les plus empruntés")
    print("12. Utilisateurs les plus actifs")
    print("13. Statistiques générales")
    print("\n--- DONNÉES ---")
    print("14. Sauvegarder les données")
    print("15. Charger les données")
    print("\n0.  Quitter")
    print("=" * 60)


def main():
    """Fonction principale du programme"""
    bibliotheque = Bibliotheque()
    
    # Charger les données au démarrage
    print("🔄 Chargement des données...")
    bibliotheque.charger_donnees()
    
    while True:
        afficher_menu()
        choix = input("\n👉 Votre choix : ").strip()
        
        if choix == "1":
            print("\n--- Ajouter un livre ---")
            isbn = input("ISBN : ").strip()
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()
            try:
                annee = int(input("Année de publication : ").strip())
                bibliotheque.ajouter_livre(isbn, titre, auteur, annee)
            except ValueError:
                print("❌ Erreur : L'année doit être un nombre.")
        
        elif choix == "2":
            print("\n--- Supprimer un livre ---")
            isbn = input("ISBN du livre à supprimer : ").strip()
            bibliotheque.supprimer_livre(isbn)
        
        elif choix == "3":
            print("\n--- Rechercher un livre ---")
            print("Critères de recherche : titre, auteur, isbn")
            critere = input("Critère : ").strip()
            valeur = input("Valeur à rechercher : ").strip()
            resultats = bibliotheque.rechercher_livre(critere, valeur)
            if resultats:
                print(f"\n✅ {len(resultats)} résultat(s) trouvé(s) :")
                for livre in resultats:
                    print(livre)
            else:
                print("❌ Aucun résultat trouvé.")
        
        elif choix == "4":
            bibliotheque.afficher_livres()
        
        elif choix == "5":
            print("\n--- Ajouter un utilisateur ---")
            id_utilisateur = input("ID utilisateur : ").strip()
            nom = input("Nom : ").strip()
            prenom = input("Prénom : ").strip()
            email = input("Email : ").strip()
            bibliotheque.ajouter_utilisateur(id_utilisateur, nom, prenom, email)
        
        elif choix == "6":
            print("\n--- Supprimer un utilisateur ---")
            id_utilisateur = input("ID de l'utilisateur à supprimer : ").strip()
            bibliotheque.supprimer_utilisateur(id_utilisateur)
        
        elif choix == "7":
            bibliotheque.afficher_utilisateurs()
        
        elif choix == "8":
            print("\n--- Emprunter un livre ---")
            isbn = input("ISBN du livre : ").strip()
            id_utilisateur = input("ID de l'utilisateur : ").strip()
            try:
                duree = input("Durée de l'emprunt en jours (défaut: 14) : ").strip()
                duree_jours = int(duree) if duree else 14
                bibliotheque.emprunter_livre(isbn, id_utilisateur, duree_jours)
            except ValueError:
                print("❌ Erreur : La durée doit être un nombre.")
        
        elif choix == "9":
            print("\n--- Retourner un livre ---")
            isbn = input("ISBN du livre : ").strip()
            id_utilisateur = input("ID de l'utilisateur : ").strip()
            bibliotheque.retourner_livre(isbn, id_utilisateur)
        
        elif choix == "10":
            bibliotheque.afficher_emprunts_en_cours()
        
        elif choix == "11":
            try:
                top_n = input("Nombre de livres à afficher (défaut: 5) : ").strip()
                top_n = int(top_n) if top_n else 5
                bibliotheque.livres_plus_empruntes(top_n)
            except ValueError:
                print("❌ Erreur : Le nombre doit être un entier.")
        
        elif choix == "12":
            try:
                top_n = input("Nombre d'utilisateurs à afficher (défaut: 5) : ").strip()
                top_n = int(top_n) if top_n else 5
                bibliotheque.utilisateurs_plus_actifs(top_n)
            except ValueError:
                print("❌ Erreur : Le nombre doit être un entier.")
        
        elif choix == "13":
            bibliotheque.statistiques_generales()
        
        elif choix == "14":
            bibliotheque.sauvegarder_donnees()
        
        elif choix == "15":
            bibliotheque.charger_donnees()
        
        elif choix == "0":
            print("\n💾 Sauvegarde automatique des données...")
            bibliotheque.sauvegarder_donnees()
            print("👋 Au revoir !")
            break
        
        else:
            print("❌ Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
