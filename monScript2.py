def estAdmissible(note):
    return note >= 10

etudiants = {
    1000: {"nom": "JOHN", "prenom": "DOE", "note": 15},
    2000: {"nom": "BOB", "prenom": "CARLON", "note": 9},
    3000: {"nom": "RAYANE", "prenom": "SMITH", "note": 13}
}

for id, info in etudiants.items():
    if estAdmissible(info["note"]):
        print(f"{info['prenom']} {info['nom']} est admissible.")
