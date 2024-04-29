from  statistic import *

def main():
    # crée le pavage
    pavage = Pavage(Pentagone(pygame.Vector2(screen.get_width()//2,screen.get_height()//2), size=40))
    pavage.create_pavage()

    # demande à l'utilisateur un nombre de couleur
    correct_input = False
    while not correct_input:
        try:
            nb_color: int = int(input("Saisir un nombre de couleur: "))
            # colore le pavage
            coloring_pavage(pavage, nb_color)
            correct_input = True
        except:
            print("Erreur de saisie\n")

    # affiche le pavage
    running: bool = True
    while running:
        
        for event in pygame.event.get():
            # permet de fermer la fenetre
            if event.type == pygame.QUIT:
                running = False
            
            # recolore le pavage en apuyant sur la souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                coloring_pavage(pavage, nb_color)
        
        # rafréchi la fenêtre
        pygame.display.flip()

main()
