
from random import randint

def minimum(t):
    """
    renvoie l'indice du minimum de t
    """
    ind_min=0
    for i in range(len(t)):
        if t[i]<t[ind_min]:
            ind_min = i
    return ind_min

def ajouter_fin(t,v):
    """
    renvoie une tableau tab composé des éléments de t (dans le meme ordre) auquelles on a ajouté
    la valeur v
    """
    tab = [0]*(len(t)+1)
    for i in range(len(t)):
        tab[i]=t[i]
    tab[len(t)]=v
    return tab

def fusion (t1,t2):
    t=[]
    i1=0
    i2=0
    while i1<len(t1) and i2<len(t2):
        if type(t1[i1])==int and t1[i1]<t2[i2]:
            t= ajouter_fin(t, t1[i1])
            i1+=1
        elif not type(t1[i1])==int and not type(t1[i1])==tuple and t1[i1].valeur<t2[i2].valeur:
            t= ajouter_fin(t, t1[i1])
            i1+=1
        elif type(t1[i1])==tuple and t1[i1][0]<t2[i2][0]:
            t= ajouter_fin(t, t1[i1])
            i1+=1
        else:
            t = ajouter_fin(t, t2[i2])
            i2+=1
    if i1==len(t1):
        for e in t2[i2:]:
            t =ajouter_fin(t, e)
    else:
        for e in t1[i1:]:
            t =ajouter_fin(t, e)
    return t

def tri_fusion (t):
    """
    Renvoie le tableau t (de tuples ou d'entiers) trié dans l'ordre croisant
    """
    n=len(t)
    if n<=1:
        return t
    else:
        return fusion(tri_fusion(t[:n//2]),tri_fusion(t[n//2:]))

class Maillon:
    def __init__(self, v, s):
        self.valeur = v
        self.suivant = s

class ListeC:
    def __init__(self):
        """
        Crée une liste vide
        """
        self.tete = None
        self.queue = None
        self.taille = 0

    def estVide(self):
        """
        renvoie True si la liste est vide
        """
        return self.tete == None

    def ajouter_devant(self, v):
        """
        ajoute la valeur v au début de la liste
        """
        m = Maillon(v, self.tete)
        if self.estVide():
            self.queue = m
        self.tete = Maillon(v, self.tete)
        self.taille+=1


    def ajouter_derriere(self, v):
        """
        ajoute la valeur v à la fin de la liste
        """
        m = Maillon(v, None)
        if self.estVide():
            self.tete=m
        else:
            self.queue.suivant = m
        self.queue =m
        self.taille+=1

    def inserer(self, v, i):
        if i<0 or i>len(self):
            raise IndexError("indice incorrect")
        elif i == 0:
            self.ajouter_devant(v)
        elif i == len(self):
            self.ajouter_derriere(v)
        else:
            l = self.tete
            for _ in range(i):
                lp = l
                l = l.suivant
            m = Maillon(v, l)
            lp.suivant = m
        self.taille+=1

    def remplacer(self,v,i):
        if i<0 or i>len(self):
            raise IndexError("indice incorrect")
        elif i == 0:
            self.supprimer_tete()
            self.ajouter_devant(v)
        elif i == len(self)-1:
            self.supprimer_fin()
            self.ajouter_derriere(v)
        else:
            self.supprimer(i)
            self.inserer(v,i)

    def supprimer_tete(self):
        """
        Supprime le premier élément de la liste
        """
        if self.estVide():
            raise IndexError("suppression impossible")
        else:
            self.tete = self.tete.suivant
            #if self.tete.suivant == None: self.queue = self.tete
        self.taille-=1

    def supprimer_fin(self):
        """
        Supprime le dernier élément de la liste
        """
        if self.estVide():
            raise IndexError("suppression impossible")
        elif len(self) == 1:
            self.queue = None
            self.tete = None
        else:
            l = self.tete
            lp=None
            while l.suivant != None:
                lp = l
                l = l.suivant
            lp.suivant = None
            self.queue = lp
        self.taille-=1

    def supprimer(self, i):
        """
        Supprime l'élément à la position i de la liste
        """
        if i<0 or i>len(self):
            raise IndexError("indice incorrect")
        elif i == 0:
            self.supprimer_tete()
        elif i!=0 and i == len(self):
            self.supprimer_fin()
        else:
            l = self.tete
            for _ in range(i):
                lp = l
                l = l.suivant
            lp.suivant = l.suivant
        self.taille-=1

    def __str__(self):
        """
        Renvoie une chaîne de caractères permettant
        d'afficher la liste
        """
        s = ""
        l = self.tete
        while l!=None:
            s += str(l.valeur)+" "
            l = l.suivant
        return s

    def __len__(self):
        """
        Renvoie la taille de la liste
        """
        if self.taille<0:
            return 0
        return self.taille

    def __getitem__(self, i):
        """
        renvoie l'élément à la position i de la liste
        """
        if i<0 or i>=len(self):
            raise IndexError("indice inexistant")

        elif i==len(self)-1:
            return self.queue.valeur
        else:
            l = self.tete
            for _ in range(i):
                l = l.suivant
            return l.valeur

class Pile:

    def __init__(self):
        """
        creer une pile vide
        """
        self.p = ListeC()

    def estVide(self):
        """
        renvoie True si la pile est vide
        """
        return self.p.estVide()


    def empiler(self, val):
        """
        ajoute val à la pile
        """
        self.p.ajouter_devant(val)

    def sommet(self):
        """
        renvoie le sommet de la pile
        """
        return self.p[0]

    def depiler(self):
        """
        renvoie le sommet de la pile et le retire
        """
        if not self.estVide():
            v = self.p[0]
            self.p.supprimer_tete()
            return v

    def __str__(self):
        return str(self.p)

class Carte:

    def __init__(self, v):
        """
        Crée une Carte
        """
        self.valeur = v

        if self.valeur==55:
            self.penalite = 7
        elif self.valeur%10==0:
        	self.penalite = 3
        elif self.valeur%5==0:
        	self.penalite = 2
        elif self.valeur%11==0:
            self.penalite = 5
        else:
            self.penalite = 1

    def __str__(self):
        return str(self.valeur)+" 🐮 "*self.penalite

class Paquet:

    def __init__(self):
        """
        Crée un paquet de 104 cartes
        """
        self.cartes = Pile()
        for i in range(1,105):
            self.cartes.empiler(Carte(i))

    def distribuer_carte(self):
        """
        Renvoie la cartes du haut du paquets
        """
        return self.cartes.depiler()

    def distribuer(self, n):
        """
        Renvoie un tableau composés des n cartes du haut du paquets
        """
        cartes =[]
        for _ in range(n):
            cartes =ajouter_fin(cartes,self.distribuer_carte())
        return cartes

    def melanger(self, nb_iterations):
        """
        Mélange le Paquet nb_iterations fois
        """
        for _ in range(nb_iterations):
            i=randint(0, len(self.cartes.p)-1)
            j=randint(0, len(self.cartes.p)-1)
            self.echanger(i, j)

    def echanger(self, i, j):
        """
        Echange les cartes à l'indice i et j du paquet
        """
        tmp=self.cartes.p[i]
        self.cartes.p.remplacer(self.cartes.p[j], i)
        self.cartes.p.remplacer(tmp, j)
        #self.cartes.p[i]=self.cartes.p[j]
        #self.cartes.p[j]=tmp

def enlever(t, v):
    """
    Retire la valeur v du tableau t
    """
    return [t[i] for i in range(len(t)) if t[i].valeur !=v]

def enlever_indice(t, i):
    """
    Reproduis la fonction pop(), retire l'élément à l'indice i dans t
    """
    return [t[j] for j in range(len(t)) if j != i]

def estPresent(t, v):
    """
    Renvoie True si la valeur v est dans le tableau t sinon renvoie False
    """
    for c in t:
        if c.valeur == v:
            return True
    return False
def carte_a_jouer_IA(series, main):
    t = [9999]*len(main)
    carte_min = -1
    for j in range(len(main)):
        for i in range(4):
            if (main[j].valeur - series[i].queue.valeur.valeur) > 0 and (main[j].valeur - series[i].queue.valeur.valeur) < t[j]:
                t[j]= main[j].valeur - series[i].queue.valeur.valeur
    if t[minimum(t)] != 9999:
        return -1
    else:
        return main[minimum(t)]

class Joueur:
    def __init__(self, pseudo, bool_IA):
        """
        Crée un joueur
        """
        self.estIA = bool_IA
        self.nom = pseudo
        self.nb_penalite=0
        self.main = []

    def jouer(self, series):
        if self.estIA:
            return self.jouer_IA(series)
        else:
            return self.jouer_humain()

    def jouer_humain(self):
        """
        Demande une carte à jouer au joueur
        """
        s=""
        for e in self.main:
            s+= str(e)+" ❚ "
        print(self.nom, "voici vos cartes : ")
        print( s)
        print("")
        choix = int(input("Quelle carte vous choisissez de jouer ? "))
        while not estPresent(self.main, choix):
            print("Cette carte n'existe pas")
            choix = int(input("Quelle carte vous choisissez de jouer ? "))

        self.main = enlever(self.main, choix)
        return Carte(choix)

    def jouer_IA(self, series):
        """
        Choisi aléatoirement la carte à jouer du BOT
        -jouer dans la série avec la plus petit distance
        -est-ce que ca vaut le coup de prendre une série (compter nb tete beauf)
        """

        if carte_a_jouer_IA(series, self.main)== -1:
            aleatoire = randint(0,len(self.main)-1)
            carte = self.main[aleatoire]
            self.main= enlever_indice(self.main, aleatoire)
            return carte
        else:
            return carte_a_jouer_IA(series, self.main)

def serie_destinee(series, carte):
    """
    Renvoie l'indice de la liste Chainée dans séries auquelle la carte doit être jouée
    et le tableau des distance entre la carte et chaque série
    Sinon : Renvoie -1
    """
    t = [105]*4
    for i in range(4):
        if (carte.valeur - series[i].queue.valeur.valeur) > 0:
            t[i]= carte.valeur - series[i].queue.valeur.valeur

    if t[minimum(t)]==105:
        return -1
    return minimum(t)

def minimum_tete_boeuf(series,carte):
    """
    Renvoie l'indice de la serie qui a le moins de pénalités
    """
    t = [105]*4
    for i in range(4):
            cpt=0
            for j in range(len(series[i])):
                cpt+= series[i][j].penalite
            t[i]=cpt

    return minimum(t)

def classement_final(liste_joueurs):
    classement = []
    for j in liste_joueurs:
        classement = ajouter_fin(classement, (j.nb_penalite, j.nom))
    classement_trié = tri_fusion(classement)
    for i in range(len(classement_trié)):
        if i==0:
            print(str(i+1)+ "er 🏆: ", classement_trié[i][1], " avec ",classement_trié[i][0]," penalités" )
        else:
            print(str(i+1)+ "ème : ", classement_trié[i][1], " avec ",classement_trié[i][0]," penalités" )
def placement_carte(series, serie_destinee, c, historique_cartes):
    print("Série destinée pour ", c, "   :  ", serie_destinee+1)
    #La série destinée est non pleine (cas normal)
    if len(series[serie_destinee])<5:
        series[serie_destinee].ajouter_derriere(c)

    #La série destinée est pleine
    else:
        cpt=0
        while not series[serie_destinee].estVide():
            cpt+= series[serie_destinee].queue.valeur.penalite
            series[serie_destinee].supprimer_fin()
        historique_cartes[c].nb_penalite+=cpt
        series[serie_destinee].ajouter_derriere(c)

def jeu_du_6_qui_prend(nb_joueurs, nb_IA):
    """
    Jeu du 6 qui prend pour nb_joueurs joueurs et nb_IA BOTs
    """
    assert nb_joueurs+nb_IA>=3, "Il faut 3 joueurs minimum"
    assert nb_joueurs+nb_IA<=10, "Il faut 10 joueurs maximum"

    p = Paquet()
    p.melanger(200)
    joueurs = []
    series = [ListeC() for _ in range(4)]
    tours_max = 10 #int(input("Cb de tours vous voulez que la partie dure (10 normalement) ? "))
    historique_cartes= {}

    #Préambule (pseudo, Distribution des cartes)
    for i in range(nb_joueurs):
        pseudo = input("Entrez votre pseudo, joueur "+str(i+1)+ " : ")
        joueurs = ajouter_fin(joueurs, Joueur(pseudo, False))
        joueurs[i].main = p.distribuer(10)
        joueurs[i].main = tri_fusion(joueurs[i].main)
    for i in range(nb_IA):
        joueurs = ajouter_fin(joueurs, Joueur("BOT "+str(i+1), True))
        joueurs[nb_joueurs+i].main = p.distribuer(10)
    for i in range(4):
        series[i].ajouter_derriere(p.distribuer_carte())
    print("LA PARTIE COMMENCE! ⌛️")
    print("")


    for _ in range(tours_max):

        # Affichage des séries
        print("―――――――――――――――――――――――――――――――――――")
        for i in range(4):
            print("Série ", i+1, " :       avec", len(series[i]), "cartes")
            #print("―――――――――――――――")
            for j in range(len(series[i])):
                print(series[i][j])
            print("―――――――――――――――――――――――――――――――――――")

        #-------------Choix des cartes à jouer-------------
        print("")
        print("Chaque joueur doit choisir une carte à jouer!")
        cartes_pose = []
        for i in range(nb_joueurs+nb_IA):
            carte = joueurs[i].jouer(series)
            cartes_pose = ajouter_fin(cartes_pose, carte)
            historique_cartes[carte] = joueurs[i]

        trie_cartes_pose= tri_fusion(cartes_pose)

        #--------------Affichage des cartes joués----------
        print("Voici toutes les cartes joués :")
        for c in trie_cartes_pose:
            print(c, " (par", historique_cartes[c].nom+")")
        #---------------------------------------------------
        for c in trie_cartes_pose:
            s = serie_destinee(series, c)

            #Carte trop petite pour toutes les séries
            if s ==-1:
                print("Série destinée pour ", c, "   :  AUCUNE")
                if not historique_cartes[c].estIA:
                    pseudo = historique_cartes[c].nom
                    s = int(input(str(pseudo)+", votre carte ne rentre nulle part! Choisissez une ligne où jouer (entre 1 et 4) :"))-1
                else:
                    s= minimum_tete_boeuf(series, c)
                    print("série aléatoire : ",s+1)

                cpt=0
                i=0
                while not series[s].estVide():
                    cpt+= series[s].queue.valeur.penalite
                    series[s].supprimer_fin()
                    i+=1
                historique_cartes[c].nb_penalite+=cpt
                series[s].ajouter_derriere(c)

            else:
                placement_carte(series, s, c, historique_cartes)


    # Affichage des séries
    print("―――――――――――――――――――――――――――――――――――")
    for i in range(4):
        print("Série ", i+1, " :       avec", len(series[i]), "cartes")
        #print("―――――――――――――――")
        for j in range(len(series[i])):
            print(series[i][j])
        print("―――――――――――――――――――――――――――――――――――")
    print("")
    print("PARTIE TERMINEE ! VOICI LE RESUME DES PENALITES ✔")
    classement_final(joueurs)


jeu_du_6_qui_prend(1,3)





