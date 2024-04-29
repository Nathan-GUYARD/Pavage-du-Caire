from window import *
from utilities import *

class Pentagone:

    def __init__(self, position: pygame.Vector2, select_point: int = 0, rotation: float = 0, color: str|list[float] = "red", size: float = 100) -> None:
        """ Initialise le pentagone """
        
        # enregistre les infos utiles
        self.points: list[pygame.Vector2] = [None,None,None,None,None]
        self.size: float = size
        self.color: str|list[float] = color
        self.rotation = rotation%360
        
        self.create_pentagone(select_point, position, rotation)


    def draw(self) -> None:
        """ Dessine le pentagone """

        # crée le pentagone
        pygame.draw.polygon(screen,self.color,self.points)
        # crée la bordure du pentagone
        pygame.draw.polygon(screen,"black",self.points,3)


    def create_pentagone(self, point: int, position: pygame.Vector2, rotation: float) -> None:
        """ Crée le pentagone """

        self.points[point] = position
        rotation -= 30
        
        nb_point: int = 1
        i: int = 0
        while nb_point<5:
            # tourne d'un certain angle
            if i%5==1 or i%5==4:
                rotation += 90
            else:
                rotation += 60
            
            # crée le point
            if self.points[i] != None:
                if i%5==2:
                    self.create_point(i,(i+1)%5, rotation, 2*self.size*math.sqrt(1-math.cos(deg_to_rad(30))))
                else:
                    self.create_point(i,(i+1)%5, rotation, self.size)
                
                nb_point += 1
            
            # garde des valeur entre 0 et 4
            i = (i+1)%5


    def create_point(self, prepoint: int, postpoint: int, angle: float, size: int) -> None:
        """ Crée un point du pentagone """
        
        angle = deg_to_rad(angle)
        # enregistre le point
        self.points[postpoint] = self.points[prepoint] + size * pygame.Vector2(math.cos(angle),math.sin(angle))


    def change_color(self, new_color: str|list[float]) -> None:
        """ Change la couleur du pentagone """
        
        self.color = new_color
        self.draw()

    def commun_point(self, pentagone) -> int:
        """ Compte le nombre de point en commun entre 2 Pentagone """
        
        nb_connect: int = 0

        for point in pentagone.points:
            if point in self.points:
                nb_connect += 1
        
        return nb_connect

#-------------------------------------------------------------
# TEST
#-------------------------------------------------------------
if __name__ == "__main__":
    # le pentagone
    penta = Pentagone(pygame.Vector2(250,100), 0, 0,size=200)
    penta.change_color("white")
    
    running: bool = True
    while running:

        # permet de fermer la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # rafréchi la fenêtre
        pygame.display.flip()