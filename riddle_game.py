import random
class Game:
    def __init__(self):
        self.score = 40
        self.nombre_de_tentatives = 0
        self.demander_borne()
        self.nombre = random.randint(self.inf, self.sup)

    def regles_du_jeu():
        print("**************")
        print("RIDDLE GAME")
        print("**************")
        print()
        print("Bienvenue dans le jeu de devinettes!")
        print()
        print("L'objectif est simple: deviner l'entier qui se trouve entre un intervalle choisi avec le moins de tentatives possibles.")
        print(" - Vous avez un score initial de 100 points.")
        print(" - Chaque tentative ratée vous enlève 10 points")
        print(" - Chaque fois que vous ratez, vous avez la possibilité de demander des indices, mais vous perdez 5 points")
        print(" - Vous pouvez reéssayer jusqu'à ce que votre score soit nul, et là vous aurez perdu")
        print("Bonne chance!")
        print()
        commencer = input("Commencer le jeu (oui/non): ")
        if commencer.lower() == "non":
            exit()
        else:
            print("_______________________________")
            print()
        
    def demander_borne(self):
        print("Donnez les bornes de votre intervalle de nombre:")
        borne_inf = int(input("Entrez la borne inférieure: "))
        borne_sup = int(input("Entrez la borne supérieure: "))
        self.inf = borne_inf
        self.sup = borne_sup

    def partie(self):
        while True:
            print("Tentative", self.nombre_de_tentatives + 1)
            nombre_proposé = int(input("Entrez le nombre: "))
            self.nombre_proposé = int(nombre_proposé)
            if self.nombre_proposé != self.nombre:
                self.score -= 10
                self.nombre_de_tentatives += 1
                print("Raté!")
                if self.score >= 5:
                    choix = input("Il vous reste " + str(self.score) + " points. Voulez vous un indice?(oui/non): ")
                    if choix.lower() == "oui":
                        self.demander_indice()
                if self.score <= 0:
                    print("Perdu! Désolé, vous n'avez plus de point, le nombre gagnant était: "+ str(self.nombre))
                    choix1 = input("voulez vous recommencer?(oui/non): ")
                    if choix1.lower == "oui":
                        print("_______________________________")
                        print()
                        self.nombre_de_tentatives = 0
                        self.score = 40
                        self.demander_borne()
                        self.nombre = random.randint(self.inf, self.sup)
                    else:
                        break
            else:
                print("Félicitations, vous avez gagné, votre score est :", self.score)
                choix = input("Voulez vous recommencer?(oui/non): ")
                if choix.lower() == "oui":
                    print("_______________________________")
                    print()
                    self.nombre_de_tentatives = 0
                    self.score = 40
                    self.demander_borne()
                    self.nombre = random.randint(self.inf, self.sup)
                else:
                    break

    def demander_indice(self):
        self.score -= 5
        if self.nombre_proposé > self.nombre:
            print("Le nombre est plus petit!")
        else:
            print("Le nombre est plus grand!")

    

Game.regles_du_jeu()
partie1 = Game()
partie1.partie()
       
        



