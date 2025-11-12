"""
Script de test pour le système de gestion de bibliothèque
Ajoute des données d'exemple pour tester le système
"""

from bibliotheque import Bibliotheque


def initialiser_donnees_test():
    """Initialise la bibliothèque avec des données de test"""
    
    biblio = Bibliotheque()
    
    print("🔄 Initialisation des données de test...\n")
    
    # Ajouter des livres
    print("📚 Ajout des livres...")
    livres = [
        ("978-2-7440-7326-9", "Introduction à l'Algorithmique", "Thomas H. Cormen", 2009),
        ("978-2-2120-6750-2", "Python pour les Nuls", "John Paul Mueller", 2019),
        ("978-2-2120-5678-1", "Structure de Données en C", "Tanenbaum", 2015),
        ("978-2-7440-1234-5", "Base de Données Relationnelles", "Ramez Elmasri", 2017),
        ("978-2-2120-9876-3", "Réseaux Informatiques", "Andrew Tanenbaum", 2018),
        ("978-2-7440-5555-6", "Intelligence Artificielle", "Stuart Russell", 2020),
        ("978-2-2120-7777-8", "Systèmes d'Exploitation", "Abraham Silberschatz", 2016),
        ("978-2-7440-8888-9", "Génie Logiciel", "Ian Sommerville", 2019),
        ("978-2-2120-3333-4", "Architecture des Ordinateurs", "David Patterson", 2014),
        ("978-2-7440-4444-5", "Programmation Web", "Jon Duckett", 2021),
    ]
    
    for isbn, titre, auteur, annee in livres:
        biblio.ajouter_livre(isbn, titre, auteur, annee)
    
    print()
    
    # Ajouter des utilisateurs
    print("👥 Ajout des utilisateurs...")
    utilisateurs = [
        ("U001", "Benali", "Ahmed", "ahmed.benali@univ.dz"),
        ("U002", "Kaddour", "Fatima", "fatima.kaddour@univ.dz"),
        ("U003", "Meziane", "Karim", "karim.meziane@univ.dz"),
        ("U004", "Boudiaf", "Sarah", "sarah.boudiaf@univ.dz"),
        ("U005", "Hamidi", "Yacine", "yacine.hamidi@univ.dz"),
        ("U006", "Cherif", "Amina", "amina.cherif@univ.dz"),
        ("U007", "Mansouri", "Mehdi", "mehdi.mansouri@univ.dz"),
    ]
    
    for id_user, nom, prenom, email in utilisateurs:
        biblio.ajouter_utilisateur(id_user, nom, prenom, email)
    
    print()
    
    # Effectuer quelques emprunts
    print("📋 Création d'emprunts de test...")
    emprunts = [
        ("978-2-7440-7326-9", "U001", 14),  # Ahmed emprunte Algorithmique
        ("978-2-2120-6750-2", "U001", 14),  # Ahmed emprunte Python
        ("978-2-2120-5678-1", "U002", 14),  # Fatima emprunte Structure de Données
        ("978-2-7440-1234-5", "U003", 14),  # Karim emprunte Base de Données
        ("978-2-2120-9876-3", "U004", 14),  # Sarah emprunte Réseaux
        ("978-2-7440-5555-6", "U005", 14),  # Yacine emprunte IA
    ]
    
    for isbn, id_user, duree in emprunts:
        biblio.emprunter_livre(isbn, id_user, duree)
    
    print()
    
    # Simuler quelques retours pour créer de l'historique
    print("📥 Simulation de quelques retours...")
    biblio.retourner_livre("978-2-2120-6750-2", "U001")  # Ahmed retourne Python
    biblio.retourner_livre("978-2-2120-5678-1", "U002")  # Fatima retourne Structure de Données
    
    print()
    
    # Emprunter à nouveau pour augmenter les statistiques
    print("📋 Emprunts supplémentaires pour les statistiques...")
    biblio.emprunter_livre("978-2-2120-6750-2", "U002", 14)  # Fatima emprunte Python
    biblio.emprunter_livre("978-2-2120-5678-1", "U001", 14)  # Ahmed emprunte Structure de Données
    
    print()
    
    # Sauvegarder les données
    print("💾 Sauvegarde des données de test...")
    biblio.sauvegarder_donnees()
    
    print("\n" + "=" * 60)
    print("✅ Données de test initialisées avec succès !")
    print("=" * 60)
    
    # Afficher un résumé
    print("\n📊 Résumé des données créées :")
    biblio.statistiques_generales()
    
    return biblio


def tester_fonctionnalites():
    """Test des principales fonctionnalités"""
    
    print("\n" + "=" * 60)
    print("🧪 TEST DES FONCTIONNALITÉS")
    print("=" * 60)
    
    biblio = Bibliotheque()
    biblio.charger_donnees()
    
    # Test 1 : Afficher tous les livres
    print("\n--- TEST 1 : Affichage des livres ---")
    biblio.afficher_livres()
    
    # Test 2 : Afficher tous les utilisateurs
    print("\n--- TEST 2 : Affichage des utilisateurs ---")
    biblio.afficher_utilisateurs()
    
    # Test 3 : Recherche de livres
    print("\n--- TEST 3 : Recherche de livres par auteur 'Tanenbaum' ---")
    resultats = biblio.rechercher_livre("auteur", "Tanenbaum")
    if resultats:
        for livre in resultats:
            print(livre)
    
    # Test 4 : Emprunts en cours
    print("\n--- TEST 4 : Emprunts en cours ---")
    biblio.afficher_emprunts_en_cours()
    
    # Test 5 : Statistiques
    print("\n--- TEST 5 : Livres les plus empruntés ---")
    biblio.livres_plus_empruntes(5)
    
    print("\n--- TEST 6 : Utilisateurs les plus actifs ---")
    biblio.utilisateurs_plus_actifs(5)
    
    print("\n--- TEST 7 : Statistiques générales ---")
    biblio.statistiques_generales()
    
    # Test 8 : Test des limites
    print("\n--- TEST 8 : Test de la limite d'emprunts (3 max) ---")
    print("Tentative d'emprunter un 4ème livre pour Ahmed (U001)...")
    biblio.emprunter_livre("978-2-7440-8888-9", "U001", 14)
    
    # Test 9 : Test d'emprunt d'un livre déjà emprunté
    print("\n--- TEST 9 : Test d'emprunt d'un livre déjà emprunté ---")
    print("Tentative d'emprunter un livre déjà emprunté...")
    biblio.emprunter_livre("978-2-7440-7326-9", "U002", 14)
    
    print("\n" + "=" * 60)
    print("✅ Tests terminés !")
    print("=" * 60)


def menu_test():
    """Menu pour choisir le type de test"""
    print("\n" + "=" * 60)
    print("🧪 MENU DE TEST - SYSTÈME DE BIBLIOTHÈQUE")
    print("=" * 60)
    print("\n1. Initialiser les données de test")
    print("2. Tester les fonctionnalités")
    print("3. Tout exécuter (initialisation + tests)")
    print("0. Quitter")
    print("=" * 60)
    
    choix = input("\n👉 Votre choix : ").strip()
    
    if choix == "1":
        initialiser_donnees_test()
    elif choix == "2":
        tester_fonctionnalites()
    elif choix == "3":
        initialiser_donnees_test()
        input("\n⏸️  Appuyez sur Entrée pour continuer avec les tests...")
        tester_fonctionnalites()
    elif choix == "0":
        print("👋 Au revoir !")
    else:
        print("❌ Choix invalide.")


if __name__ == "__main__":
    menu_test()
