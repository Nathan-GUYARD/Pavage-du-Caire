from pentagone import *

class Pavage:
    
    def __init__(self, pentagone: Pentagone) -> None:
        """ Initialise le pavage """
        
        self.penta: Pentagone = pentagone
        #affiche le pentagone
        self.penta.draw()
        
        self.neighbours: list[Pavage] = []
    

    def new_neighbour(self, pentagone: Pentagone):
        """ Crée un nouveau voisin """

        pavage: Pavage = Pavage(pentagone)
        # crée un lien des 2 cotés 
        self.add_neighbour(pavage)
        pavage.add_neighbour(self)

        return pavage
        
    
    def add_neighbour(self, neighbour) -> None:
        """ Ajoute un voisin """

        assert len(self.neighbours)<5
        self.neighbours.append(neighbour)
    

    def connecting_neighbour(self) -> None:
        """ Connecte les voisins """

        # liste des pentagone à visiter
        next_visit: list[Pavage] = self.neighbours.copy()
        # liste des pentagone déjà visité
        all_visit: list = []

        while len(next_visit) > 0 and len(self.neighbours) < 5:
            visit = next_visit.pop(0)
            
            if not(visit in all_visit):
                # ajoute les vosins à la list voisin à visitier
                for neighbour in visit.neighbours:
                    if not (neighbour in all_visit):
                        next_visit.append(neighbour)
                
                # detecte un voisin
                nb_connect = self.penta.commun_point(visit.penta)
                if nb_connect == 2 and not(visit in self.neighbours):
                    self.add_neighbour(visit)
                    visit.add_neighbour(self)
                
                all_visit.append(visit)
    

    def create_new_pentagone(self, creation_point: int, base_point: int, rotation: float) -> None:
        """ Crée un nouveau pentagone """

        new_pentagone: Pentagone = Pentagone(self.penta.points[creation_point], base_point, self.penta.rotation+rotation, self.penta.color,self.penta.size)
        
        is_valid = self.is_valid_pentagone(new_pentagone)
        
        if is_valid:
            pavage: Pavage = self.new_neighbour(new_pentagone)
            
            # crée le pavage à partir de lui
            pavage.connecting_neighbour()
            pavage.create_pavage()


    def create_pavage(self) -> None:
        """ Crée le pavage """

        self.create_new_pentagone(3,0,90)
        self.create_new_pentagone(0,3,-90)
        self.create_new_pentagone(0,2,90)
        self.create_new_pentagone(2,3,180)
        self.create_new_pentagone(2,0,-90)
        

    def is_valid_pentagone(self, pentagone: Pentagone) -> bool:
        """ Vérifie si le pentagone est valide """
        is_valid: bool = False
        
        # vérifie si il est dans la fenêtre 
        for point in pentagone.points:
            if 0 <= point.x <= screen.get_width() and 0 <= point.y <= screen.get_height():
                is_valid = True
        if not is_valid:
            return is_valid
        
        # vérifie si il existe déjà
        for pavage in self.neighbours:
            if pavage.penta.commun_point(pentagone) == 5:
                return False

            for pavage2 in pavage.neighbours:
                if pavage2.penta.commun_point(pentagone) == 5:
                    return False
                    
                for pavage3 in pavage2.neighbours:
                    if pavage3.penta.commun_point(pentagone) == 5:
                        return False
        
        return is_valid
                
    def __len__(self) -> int:
        """ Récupère le nombre de pentagone du pavage """
        
        # liste des pentagone à visiter
        next_visit: list[Pavage] = self.neighbours.copy()
        # liste des pentagone déjà visité
        all_visit: list = []

        while len(next_visit) > 0:
            visit = next_visit.pop(0)
            
            if not(visit in all_visit):
                # ajoute les vosins à la list voisin à visitier
                for neighbour in visit.neighbours:
                    if not (neighbour in all_visit):
                        next_visit.append(neighbour)
                    
                all_visit.append(visit)
        
        return len(all_visit)

#-------------------------------------------------------------
# TEST
#-------------------------------------------------------------
if __name__ == "__main__":
    # le pentagone
    pav = Pavage(Pentagone(pygame.Vector2(screen.get_width()//2,screen.get_height()//2), size=100,color="red"))
    pav.create_pavage()

    
        
    running: bool = True
    while running:
        
        for event in pygame.event.get():
            # permet de fermer la fenetre
            if event.type == pygame.QUIT:
                running = False

        # rafréchi la fenêtre
        pygame.display.flip()
    
    