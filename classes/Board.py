class Board:
    """Chess board class"""

    def __init__(self: object, pieces: list) -> None:
        """Constructeur de la classe Board
        """        
        self.pieces = pieces
        self.board = self.createBoard()

    def createBoard(self: object) -> list:
        """Création du plateau de jeu

        Args:
            self (object): Board

        Returns:
            list: board
        """
        board = []
        for i in range(8):
            board.append([None] * 8)
        for piece in self.pieces:
            board[piece.x][piece.y] = piece
        return board

    def getPiece(self: object, x: int, y: int) -> object:
        """Obtenir la pièce avec les coordonnées

        Args:
            self (object): Board
            x (int): coordonnée x de la pièce
            y (int): coordonnée y de la pièce

        Returns:
            object: Piece
        """
        return self.board[x][y]

    def setPiece(self: object, x: int, y: int, piece: object) -> None:
        """Définir une pièce à certaines coordonnées

        Args:
            self (object): Board
            x (int): coordonnée x où placer la pièce
            y (int): coordonnée y où placer la pièce
            piece (object): Piece
        """
        self.board[x][y] = piece

    def movePiece(self: object, piece: object, x: int, y: int) -> None:
        """Déplacer une pièce

        Args:
            self (object): Board
            piece (object): Piece
            x (int): nouvelle coordonnée x de la Piece
            y (int): nouvelle coordonnée y de la Piece
        """
        self.board[piece.x][piece.y] = None
        self.board[x][y] = piece
        piece.move(x, y)

    def getBoard(self: object) -> list:
        """Obtenir le plateau

        Args:
            self (object): Board

        Returns:
            list: Board
        """
        return self.board

    def printBoard(self: object) -> None:
        """Afficher le plateau dans le terminal

        Args:
            self (object): Board
        """
        print("\t\t 0 \t 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7")

        for row in self.board:
            l = "\t"
            l += str(self.board.index(row)) + " \t"
            for piece in row:
                if piece == None:
                    l += "----- \t"
                else:
                    l += str(piece) + " \t"
            print(l)

    def checkMove(self: object, piece: object, x: int, y: int) -> int:
        """Savoir si un déplacement est possible

        Args:
            self (object): Board
            piece (object): Piece
            x (int): Coordonnée x de la case à vérifier
            y (int): Coordonnée y de la case à vérifier

        Returns:
            int: 0 si impossible / 1 si possible / 2 si possible et capture
        """
        if x < 0 or x > 7 or y < 0 or y > 7:
            return 0
        if self.board[x][y] == None:
            return 1
        elif self.board[x][y].getColor() != piece.getColor():
            return 2
        else:
            return 0
