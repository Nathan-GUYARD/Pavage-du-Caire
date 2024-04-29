from pavage import *
import random


def coloring_pavage(pavage: Pavage, nb_color: str|list) -> None:
    """ Colore le pavage """
    
    random_coloring(pavage, nb_color)
    color_corection(pavage)


def random_coloring(pavage: Pavage, nb_color: str|list) -> None:
    """ Colore de façcon alétoire le pavage """
    assert nb_color > 0

    colors = ["red","blue","green","magenta","cyan","yellow","pink","purple","brown","aquamarine","orange","greenyellow"]
    # clamp la valeur
    if nb_color > len(colors):
        nb_color = len(colors)
    
    # liste des pentagone à visiter
    next_visit: list[Pavage] = pavage.neighbours.copy()
    # liste des pentagone déjà visité
    all_visit: list = []

    while len(next_visit) > 0:
        visit = next_visit.pop(0)
        
        # ajoute les vosins à la list voisin à visitier
        if not(visit in all_visit):
            for neighbour in visit.neighbours:
                if not (neighbour in all_visit):
                    next_visit.append(neighbour)
            
            # change la couleur aléatoirements
            visit.penta.change_color(colors[random.randint(0,nb_color-1)])
            
            all_visit.append(visit)
    


def color_corection(pavage) -> None:
    """ Modifie la couleur des pentagones pour avoir 2 couleurs côte à côte """

    # liste des pentagone à visiter
    next_visit: list[Pavage] = pavage.neighbours.copy()
    # liste des pentagone déjà visité
    all_visit: list = []

    while len(next_visit) > 0:
        visit = next_visit.pop(0)
        
        if not(visit in all_visit):
            # ajoute les vosins à la list voisin à visitier
            for neighbour in visit.neighbours:
                if not (neighbour in all_visit):
                    next_visit.append(neighbour)
            
            # vérifie si un voisin est de la même couleurs
            can_correct_color: bool = True
            for neighbour in visit.neighbours:
                if neighbour.penta.color == visit.penta.color:
                    can_correct_color = False
            
            if can_correct_color:
                # prend une couleur d'un voisin aléatoirement
                visit.penta.change_color(visit.neighbours[random.randint(0,len(visit.neighbours)-1)].penta.color)
                
            all_visit.append(visit)


#-------------------------------------------------------------
# TEST
#-------------------------------------------------------------
if __name__ == "__main__":
    # le pentagone
    pav = Pavage(Pentagone(pygame.Vector2(screen.get_width()//2,screen.get_height()//2), size=50))
    pav.create_pavage()
    
    # color le pavage
    nb_colors = 4
    random_coloring(pav, nb_colors)

    running: bool = True
    while running:
        
        for event in pygame.event.get():
            # permet de fermer la fenetre
            if event.type == pygame.QUIT:
                running = False
            
            # recolor le pavage en apuyant sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                color_corection(pav)
        
        # rafréchi la fenêtre
        pygame.display.flip()