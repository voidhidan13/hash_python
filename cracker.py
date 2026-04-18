import hashlib

# Voici le Hash volé dans la base de données secrète
HASH_CIBLE = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"

def craquer_mot_de_passe(file_name="admin.txt"):
  
# On ouvre le dictionnaire en lécture
  with open(file_name, "r") as dictionnaire:
     for mot in dictionnaire:
      # On encode et nettoie tous les mots avec stip. et encode.
      mot_octet = mot.strip().encode("utf-8")
        # On hash les mots un par un et on les rend lisible avec hexdigest
      mot_hash = hashlib.sha256(mot_octet).hexdigest()
       # Si les mots hashés on les memes valeurs la boucle s'arrete
      if mot_hash == HASH_CIBLE :
         mot_de_passe = mot_hash 
          # On affiche le hash qui correspond avec le mot sous sa forme d'origine
         print(f"Mot de passe trouvé {mot}")
         break
     return mot_de_passe

def main():
    print("Démarrage du piratage...")
    craquer_mot_de_passe()

if __name__ == "__main__":
    main()