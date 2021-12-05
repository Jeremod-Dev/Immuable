try:
    from os import error,path
    import os
    import urllib.request
    import sys
    from pdf2image import convert_from_bytes, convert_from_path
except:
    print("Dependance.s manquante.s")

def download(annee:int, semaine:int):
    pathPng =f"A{annee}/A{annee}_S{semaine}.png"
    pathPdf = f"A{annee}/A{annee}_S{semaine}.pdf"
    
    url = f"http://edt-iut-info.unilim.fr/edt/{pathPdf}"
    try:
        urllib.request.urlretrieve(url,pathPdf)
        ficPng = convert_from_path(pathPdf)
        for page in ficPng:
            page.save(pathPng, 'PNG')
            rmCommand = f"rm ./A{annee}/A{annee}_S{semaine}.pdf"
            os.system(rmCommand)

    except(error):
        sys.stderr.write(error)

if __name__ == '__main__':
    if len(sys.argv)==3:
        download(sys.argv[1],sys.argv[2])
    elif len(sys.argv)==2 and sys.argv[1]=="constructor":
        print(" ===== Constuction du projet =====")
        try:
            os.system(f"mkdir A1 |& mkdir A2 |& mkdir A3")
        except:
            sys.stderr.write("[Error]: Création arborescence\n\n")
        
        try:
            os.system(f"python -m pip install pillow urllib3 pdf2image")
        except:
            sys.stderr.write("[Erreur] Nous vous demandons d'installer les dépendances python manuellement: urllib3 pdf2image pillow \n\n")
    elif len(sys.argv)==1:
        print(" ======= Notice d'installation =======\nCe projet est autodéployant sous Unix",
        "uniquement (independant de la distribution)\n1 - Créer un dossier de projet et installer poppler en ajoutant dans le PATH\n2 -",
        "Mettre ce fichier dans le dossier\n3 - Relancer ce fichier avec le parametre 'constructor'",
        "\n4 - Une fois le projet créé lancer le programme avec en parametre <annee> <semaine>",
        "\n======================================")
    else:
        sys.stderr.write("[Erreur] Nombre argument.\nmain.py -> help page\nmain.py <constructor> -> installation\nmain.py <annee> <semaine> -> recuperation EDT\n")