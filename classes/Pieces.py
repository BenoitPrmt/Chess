class Piece:
    """A class to represent a chess piece."""

    def __init__(self: object, color: str, x: int, y: int, value: str) -> None:
        """Constructeur de la classe Piece

        Args:
            self (object): Piece
            color (str): Couleur de la pièce
            x (int): Coordonnée x de la pièce
            y (int): Coordonnée y de la pièce
            value (str): Valeur de la pièce (P, R, N, B, Q, K)
        """        
        self.color = color
        self.x = x
        self.y = y
        self.value = value

    def __str__(self: object) -> str:
        return self.color + self.value

    def __repr__(self: object) -> str:
        return self.color + self.value

    def move(self: object, x: int, y: int)-> None:
        """Déplacer une pièce

        Args:
            self (object): Piece
            x (int): Nouvelle coordonnée x de la pièce
            y (int): Nouvelle coordonnée y de la pièce
        """        
        self.x = x
        self.y = y

    def getPos(self: object)-> tuple:
        """Obtenir la position de la pièce

        Args:
            self (object): Piece

        Returns:
            tuple: (x, y)
        """        
        return (self.x, self.y)

    def getColor(self: object)-> str:
        """Obtenir la couleur de la pièce

        Args:
            self (object): Piece

        Returns:
            str: Couleur (white, black)
        """        
        return self.color

    def getValue(self: object)-> str:
        """Obtenir la valeur de la pièce

        Args:
            self (object): Piece

        Returns:
            str: Valeur (P, R, N, B, Q, K)
        """        
        return self.value

    def clone(self: object)-> object:
        """Cloner une pièce

        Args:
            self (object): Piece

        Returns:
            object: Piece
        """        
        return Piece(self.color, self.x, self.y, self.value)