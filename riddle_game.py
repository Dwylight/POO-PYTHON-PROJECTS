import random
class Game:
    def __init__(self):
       self.renitialiser_partie()


    def regles_du_jeu():
        print("**************")
        print("RIDDLE GAME")
        print("**************")
        print()
        print("Bienvenue dans le jeu de devinettes!")
        print()
        print("L'objectif est simple: deviner l'entier qui se trouve entre un intervalle choisi avec le moins de tentatives possibles.")
        print(" - Vous avez un score initial de 40 points.")
        print(" - Chaque tentative ratée vous enlève 10 points")
        print(" - Chaque fois que vous ratez, vous avez la possibilité de demander des indices, mais vous perdez 5 points")
        print(" - Vous pouvez reéssayer jusqu'à ce que votre score soit nul, et là vous aurez perdu")
        print("Bonne chance!")
        print()
        commencer = input("Commencer le jeu (o/n): ")
        if commencer.lower() == "n":
            exit()
        else:
            print()
        
    def demander_borne(self):
        while True:
            print("Donnez les bornes de votre intervalle de nombre:")
            try:
                self.inf = int(input("Entrez la borne inférieure: "))
                self.sup = int(input("Entrez la borne supérieure: "))               
            except ValueError:
                print("Bornes non valides! Entrez uniquement des nombres entiers")
                continue
            if self.inf >= self.sup :
                print("Erreur! La borne supérieure doit être supérieure à la borne inférieure.")
            else:
                break
               
            

    def partie(self):
        while True:
            print("Tentative", self.nombre_de_tentatives + 1)
            try:
                self.nombre_proposé = int(input("Entrez le nombre: "))
            except ValueError:
                print("Entrez un nombre valide!")
                continue
            if self.nombre_proposé != self.nombre:
                self.score -= 10
                self.nombre_de_tentatives += 1
                print("Raté!")
                if self.score >= 5:
                    choix = input("Il vous reste " + str(self.score) + " points. Voulez vous un indice?(o/n): ")
                    if choix.lower() == "o":
                        self.demander_indice()
                if self.score <= 0:
                    print("Perdu! Désolé, vous n'avez plus de point, le nombre gagnant était: "+ str(self.nombre))
                    if self.question():
                        self.renitialiser_partie()
                    else:
                        break
            else:
                print("Félicitations, vous avez gagné, votre score est :", self.score)
                if self.question():
                    self.renitialiser_partie()
                else:
                    break

    def demander_indice(self):
        self.score -= 5
        if self.nombre_proposé > self.nombre:
            print("Le nombre est plus petit!")
        else:
            print("Le nombre est plus grand!")

    def renitialiser_partie(self):
        print("_______________________________")
        print()
        self.nombre_de_tentatives = 0
        self.score = 40
        self.demander_borne()
        self.nombre = random.randint(self.inf, self.sup)

    def question(self):
        choix = input("Voulez vous recommencer?(o/n): ")
        return choix.lower() == "o"
            



    
    
    

Game.regles_du_jeu()
partie1 = Game()
partie1.partie()
       
        



