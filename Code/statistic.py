from coloring import *


def pentagone_color_stat(pavage: Pavage) -> dict:
    """ Recupère les stats du nombre de pentagone collé de même couleur """

    colors_stat: dict = {}
    # liste des pentagone à visiter
    next_visit: list[Pavage] = pavage.neighbours.copy()
    same_color: list[Pavage] = []
    # liste des pentagone déjà visité
    all_visit: list = []

    while len(next_visit) > 0:
        visit = next_visit.pop(0)
        
        if not(visit in all_visit):
            
            same_color.append(visit)
            nb_same_color = 0
            while len(same_color) > 0:
                visit = same_color.pop(0)
                
                for neighbour in visit.neighbours:
                    # ajoute les vosins à la list voisin à visitier
                    if neighbour.penta.color == visit.penta.color and not(neighbour in same_color) and not(neighbour in all_visit):
                        same_color.append(neighbour)

                    elif not(neighbour in all_visit):
                        next_visit.append(neighbour)

                all_visit.append(visit)
                nb_same_color += 1
            

            if visit.penta.color in colors_stat.keys():
                colors_stat[visit.penta.color].append(nb_same_color)

            else:
                # si la couleur n'est pas encore dans les stats 
                colors_stat[visit.penta.color] = [nb_same_color]

    return colors_stat


def new_color(pavage: Pavage, nb_color: int) -> dict:
    """ Recolore le pavage aléatoirement et recupère les stats """

    coloring_pavage(pavage, nb_color)
    return pentagone_color_stat(pavage)


#-------------------------------------------------------------
# TEST
#-------------------------------------------------------------
if __name__ == "__main__":
    # le pentagone
    pav = Pavage(Pentagone(pygame.Vector2(screen.get_width()//2,screen.get_height()//2), size=50))
    pav.create_pavage()
    
    print(len(pav))
    
    # color le pavage et récupère les stats
    nb_color = 5
    nb=0
    color_group = new_color(pav,nb_color)
    for group in color_group.keys():
        for elem in color_group[group]:
            nb += elem
    print(nb)

    running: bool = True
    while running:
        
        for event in pygame.event.get():
            # permet de fermer la fenetre
            if event.type == pygame.QUIT:
                running = False
            
            # recolorz le pavage en apuyant sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(new_color(pav,nb_color))
                nb=0
                color_group = new_color(pav,nb_color)
                for group in color_group.keys():
                    for elem in color_group[group]:
                        nb += elem
                print(nb)
        
        # rafréchi la fenêtre
        pygame.display.flip()