from classes.Pieces import Piece
from classes.Board import Board


class Game:
    """Classe du jeu
    """

    def __init__(self: object) -> None:
        """Constructeur de la classe Game

        Args:
            self (object): Game
        """
        self.pieces = self.createPieces()
        self.board = Board(self.pieces)

        self.turn = "white"
        self.turnState = "choosePiece"
        self.possibleMoves = []
        self.backUpCoord = {}
        self.movingPiece = None

        self.check = False
        self.checkmate = False
        self.isOver = False

    def createPieces(self: object) -> list:
        """Créer les pièces du jeu

        Args:
            self (object): Game

        Returns:
            list: Liste des pièces
        """
        pieces = []
        for i in range(8):
            pieces.append(Piece("white", i, 1, "P"))
            pieces.append(Piece("black", i, 6, "P"))

        pieces.append(Piece("white", 0, 0, "R"))
        pieces.append(Piece("white", 7, 0, "R"))
        pieces.append(Piece("white", 1, 0, "N"))
        pieces.append(Piece("white", 6, 0, "N"))
        pieces.append(Piece("white", 2, 0, "B"))
        pieces.append(Piece("white", 5, 0, "B"))
        pieces.append(Piece("white", 4, 0, "Q"))
        pieces.append(Piece("white", 3, 0, "K"))

        pieces.append(Piece("black", 0, 7, "R"))
        pieces.append(Piece("black", 7, 7, "R"))
        pieces.append(Piece("black", 1, 7, "N"))
        pieces.append(Piece("black", 6, 7, "N"))
        pieces.append(Piece("black", 2, 7, "B"))
        pieces.append(Piece("black", 5, 7, "B"))
        pieces.append(Piece("black", 4, 7, "Q"))
        pieces.append(Piece("black", 3, 7, "K"))

        for p in pieces:
            if p.getValue() == "K":
                if p.getColor() == "white":
                    self.whiteKing = p
                else:
                    self.blackKing = p

        return pieces

    def getBoard(self: object) -> Board:
        """Obtenir le plateau

        Args:
            self (object): Game

        Returns:
            Board: Board
        """
        return self.board

    def getTurn(self: object) -> str:
        """Obtenir le tour actuel

        Args:
            self (object): Game

        Returns:
            str: tour actuel (white / black)
        """
        return self.turn

    def changeTurn(self: object) -> str:
        """Changer le tour

        Args:
            self (object): Game

        Returns:
            str: nouveau tour (white/black)
        """
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

        return self.turn

    def setCheck(self: object, check: bool) -> None:
        """Définir un échec

        Args:
            self (object): Game
            check (bool): Nouvel état de l'échec
        """
        self.check = check

    def setCheckmate(self: object, checkmate: bool) -> None:
        """Définir un échec et mat

        Args:
            self (object): Game
            checkmate (bool): Nouvel état de l'échec et mat
        """        
        self.checkmate = checkmate

    def movePiece(self: object, piece: Piece, x: int, y: int) -> None:
        """Déplacer une pièce

        Args:
            self (object): Game
            piece (Piece): Piece
            x (int): coordonnée x de la case de destination
            y (int): _description_
        """        
        self.board.movePiece(piece, x, y)
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def getPossibleMoves(self: object, piece: Piece) -> list:
        """Obtenir les mouvements possibles d'une pièce

        Args:
            self (object): Game
            piece (Piece): Piece

        Returns:
            list: Liste des mouvements possibles (tuples x y)
        """        
        val = piece.getValue()
        if val == "P":
            return self.getPawnMoves(piece)
        elif val == "R":
            return self.getRookMoves(piece)
        elif val == "N":
            return self.getKnightMoves(piece)
        elif val == "B":
            return self.getBishopMoves(piece)
        elif val == "Q":
            return self.getQueenMoves(piece)
        elif val == "K":
            return self.getKingMoves(piece)

    # White start y lines : 0, 1 | Black start y lines : 6, 7

    def getRookMoves(self: object, piece: Piece) -> list:
        """Obtenir les mouvements possibles d'une tour

        Args:
            self (object): Game
            piece (Piece): Piece

        Returns:
            list: Liste des mouvements possibles (tuples x y)
        """        
        moves = []

        # Check up
        for i in range(piece.y - 1, -1, -1):
            if self.board.checkMove(piece, piece.x, i) == 1:
                moves.append((piece.x, i))
            elif self.board.checkMove(piece, piece.x, i) == 2:
                moves.append((piece.x, i))
                break
            else:
                break

        # Check down
        for i in range(piece.y + 1, 8):
            if self.board.checkMove(piece, piece.x, i) == 1:
                moves.append((piece.x, i))
            elif self.board.checkMove(piece, piece.x, i) == 2:
                moves.append((piece.x, i))
                break
            else:
                break

        # Check left
        for i in range(piece.x - 1, -1, -1):
            if self.board.checkMove(piece, i, piece.y) == 1:
                moves.append((i, piece.y))
            elif self.board.checkMove(piece, i, piece.y) == 2:
                moves.append((i, piece.y))
                break
            else:
                break

        # Check right
        for i in range(piece.x + 1, 8):
            if self.board.checkMove(piece, i, piece.y) == 1:
                moves.append((i, piece.y))
            elif self.board.checkMove(piece, i, piece.y) == 2:
                moves.append((i, piece.y))
                break
            else:
                break

        return moves

    def getKnightMoves(self: object, piece: Piece) -> list:
        """Obtenir les mouvements possibles d'un cavalier

        Args:
            self (object): Game
            piece (Piece): Piece

        Returns:
            list: Liste des mouvements possibles (tuples x y)
        """        
        moves = []
        if piece.getColor() == "white":
            if piece.x > 0:
                if piece.y > 1:
                    if self.board.checkMove(piece, piece.x - 1, piece.y - 2) != 0:
                        moves.append((piece.x - 1, piece.y - 2))
                if piece.y < 6:
                    if self.board.checkMove(piece, piece.x - 1, piece.y + 2) != 0:
                        moves.append((piece.x - 1, piece.y + 2))
            if piece.x > 1:
                if piece.y > 0:
                    if self.board.checkMove(piece, piece.x - 2, piece.y - 1) != 0:
                        moves.append((piece.x - 2, piece.y - 1))
                if piece.y < 7:
                    if self.board.checkMove(piece, piece.x - 2, piece.y + 1) != 0:
                        moves.append((piece.x - 2, piece.y + 1))
            if piece.x < 7:
                if piece.y > 1:
                    if self.board.checkMove(piece, piece.x + 1, piece.y - 2) != 0:
                        moves.append((piece.x + 1, piece.y - 2))
                if piece.y < 6:
                    if self.board.checkMove(piece, piece.x + 1, piece.y + 2) != 0:
                        moves.append((piece.x + 1, piece.y + 2))
            if piece.x < 6:
                if piece.y > 0:
                    if self.board.checkMove(piece, piece.x + 2, piece.y - 1) != 0:
                        moves.append((piece.x + 2, piece.y - 1))
                if piece.y < 7:
                    if self.board.checkMove(piece, piece.x + 2, piece.y + 1) != 0:
                        moves.append((piece.x + 2, piece.y + 1))
        else:

            if piece.x > 0:
                if piece.y > 1:
                    if self.board.checkMove(piece, piece.x - 1, piece.y - 2) != 0:
                        moves.append((piece.x - 1, piece.y - 2))
                if piece.y < 6:
                    if self.board.checkMove(piece, piece.x - 1, piece.y + 2) != 0:
                        moves.append((piece.x - 1, piece.y + 2))
            if piece.x > 1:
                if piece.y > 0:
                    if self.board.checkMove(piece, piece.x - 2, piece.y - 1) != 0:
                        moves.append((piece.x - 2, piece.y - 1))
                if piece.y < 7:
                    if self.board.checkMove(piece, piece.x - 2, piece.y + 1) != 0:
                        moves.append((piece.x - 2, piece.y + 1))
            if piece.x < 7:
                if piece.y > 1:
                    if self.board.checkMove(piece, piece.x + 1, piece.y - 2) != 0:
                        moves.append((piece.x + 1, piece.y - 2))
                if piece.y < 6:
                    if self.board.checkMove(piece, piece.x + 1, piece.y + 2) != 0:
                        moves.append((piece.x + 1, piece.y + 2))
            if piece.x < 6:
                if piece.y > 0:
                    if self.board.checkMove(piece, piece.x + 2, piece.y - 1) != 0:
                        moves.append((piece.x + 2, piece.y - 1))
                if piece.y < 7:
                    if self.board.checkMove(piece, piece.x + 2, piece.y + 1) != 0:
                        moves.append((piece.x + 2, piece.y + 1))

        return moves

    def getPawnMoves(self: object, piece: Piece) -> list:
        """Obtenir les mouvements possibles d'un pion

        Args:
            self (object): Game
            piece (Piece): Piece

        Returns:
            list: Liste des mouvements possibles (tuples x y)
        """        
        moves = []

        if piece.getColor() == "black":
            if piece.y > 0:
                if self.board.checkMove(piece, piece.x, piece.y - 1) == 1:
                    moves.append((piece.x, piece.y - 1))
                if piece.y == 6:
                    if self.board.checkMove(piece, piece.x, piece.y - 2) == 1:
                        moves.append((piece.x, piece.y - 2))
                if piece.x > 0:
                    if self.board.checkMove(piece, piece.x - 1, piece.y - 1) == 2:
                        moves.append((piece.x - 1, piece.y - 1))
                if piece.x < 7:
                    if self.board.checkMove(piece, piece.x + 1, piece.y - 1) == 2:
                        moves.append((piece.x + 1, piece.y - 1))
        else:
            if piece.y < 7:
                if self.board.checkMove(piece, piece.x, piece.y + 1) == 1:
                    moves.append((piece.x, piece.y + 1))
                if piece.y == 1:
                    if self.board.checkMove(piece, piece.x, piece.y + 2) == 1:
                        moves.append((piece.x, piece.y + 2))
                if piece.x > 0:
                    if self.board.checkMove(piece, piece.x - 1, piece.y + 1) == 2:
                        moves.append((piece.x - 1, piece.y + 1))
                if piece.x < 7:
                    if self.board.checkMove(piece, piece.x + 1, piece.y + 1) == 2:
                        moves.append((piece.x + 1, piece.y + 1))

        return moves

    def getBishopMoves(self: object, piece: Piece) -> list:
        """Obtenir les mouvements possibles d'un fou

        Args:
            self (object): Game
            piece (Piece): Piece

        Returns:
            list: Liste des mouvements possibles (tuples x y)
        """        
        moves = []

        # Check up left
        for i in range(1, 8):
            if piece.x - i >= 0 and piece.y - i >= 0:
                if self.board.checkMove(piece, piece.x - i, piece.y - i) == 1:
                    moves.append((piece.x - i, piece.y - i))
                elif self.board.checkMove(piece, piece.x - i, piece.y - i) == 2:
                    moves.append((piece.x - i, piece.y - i))
                    break
                else:
                    break

        # Check up right
        for i in range(1, 8):
            if piece.x + i <= 7 and piece.y - i >= 0:
                if self.board.checkMove(piece, piece.x + i, piece.y - i) == 1:
                    moves.append((piece.x + i, piece.y - i))
                elif self.board.checkMove(piece, piece.x + i, piece.y - i) == 2:
                    moves.append((piece.x + i, piece.y - i))
                    break
                else:
                    break

        # Check down left
        for i in range(1, 8):
            if piece.x - i >= 0 and piece.y + i <= 7:
                if self.board.checkMove(piece, piece.x - i, piece.y + i) == 1:
                    moves.append((piece.x - i, piece.y + i))
                elif self.board.checkMove(piece, piece.x - i, piece.y + i) == 2:
                    moves.append((piece.x - i, piece.y + i))
                    break
                else:
                    break

        # Check down right
        for i in range(1, 8):
            if piece.x + i <= 7 and piece.y + i <= 7:
                if self.board.checkMove(piece, piece.x + i, piece.y + i) == 1:
                    moves.append((piece.x + i, piece.y + i))
                elif self.board.checkMove(piece, piece.x + i, piece.y + i) == 2:
                    moves.append((piece.x + i, piece.y + i))
                    break
                else:
                    break

        return moves

    def getQueenMoves(self: object, piece: Piece) -> list:
        """Obtenir les mouvements possibles d'une reine

        Args:
            self (object): Game
            piece (Piece): Piece

        Returns:
            list: Liste des mouvements possibles (tuples x y)
        """        
        moves = []

        # Check up
        for i in range(piece.y - 1, -1, -1):
            if self.board.checkMove(piece, piece.x, i) == 1:
                moves.append((piece.x, i))
            elif self.board.checkMove(piece, piece.x, i) == 2:
                moves.append((piece.x, i))
                break
            else:
                break

        # Check down
        for i in range(piece.y + 1, 8):
            if self.board.checkMove(piece, piece.x, i) == 1:
                moves.append((piece.x, i))
            elif self.board.checkMove(piece, piece.x, i) == 2:
                moves.append((piece.x, i))
                break
            else:
                break

        # Check left
        for i in range(piece.x - 1, -1, -1):
            if self.board.checkMove(piece, i, piece.y) == 1:
                moves.append((i, piece.y))
            elif self.board.checkMove(piece, i, piece.y) == 2:
                moves.append((i, piece.y))
                break
            else:
                break

        # Check right
        for i in range(piece.x + 1, 8):
            if self.board.checkMove(piece, i, piece.y) == 1:
                moves.append((i, piece.y))
            elif self.board.checkMove(piece, i, piece.y) == 2:
                moves.append((i, piece.y))
                break
            else:
                break

        # Check diagonals
        for i in range(8):
            if i != piece.x:
                if self.board.checkMove(piece, i, piece.y + (piece.x - i)) == 1:
                    moves.append((i, piece.y + (piece.x - i)))
                elif self.board.checkMove(piece, i, piece.y + (piece.x - i)) == 2:
                    moves.append((i, piece.y + (piece.x - i)))
                    break
                else:
                    break

        for i in range(8):
            if i != piece.x:
                if self.board.checkMove(piece, i, piece.y - (piece.x - i)) == 1:
                    moves.append((i, piece.y - (piece.x - i)))
                elif self.board.checkMove(piece, i, piece.y - (piece.x - i)) == 2:
                    moves.append((i, piece.y - (piece.x - i)))
                    break
                else:
                    break
        return moves

    def getKingMoves(self: object, piece: Piece) -> list:
        """Obtenir les mouvements possibles d'un roi

        Args:
            self (object): Game
            piece (Piece): Piece

        Returns:
            list: Liste des mouvements possibles (tuples x y)
        """        
        moves = []

        if piece.x > 0:
            if self.board.checkMove(piece, piece.x - 1, piece.y) != 0:
                moves.append((piece.x - 1, piece.y))
            if piece.y > 0:
                if self.board.checkMove(piece, piece.x - 1, piece.y - 1) != 0:
                    moves.append((piece.x - 1, piece.y - 1))
            if piece.y < 7:
                if self.board.checkMove(piece, piece.x - 1, piece.y + 1) != 0:
                    moves.append((piece.x - 1, piece.y + 1))

        if piece.x < 7:
            if self.board.checkMove(piece, piece.x + 1, piece.y) != 0:
                moves.append((piece.x + 1, piece.y))
            if piece.y > 0:
                if self.board.checkMove(piece, piece.x + 1, piece.y - 1) != 0:
                    moves.append((piece.x + 1, piece.y - 1))
            if piece.y < 7:
                if self.board.checkMove(piece, piece.x + 1, piece.y + 1) != 0:
                    moves.append((piece.x + 1, piece.y + 1))

        if piece.y > 0:
            if self.board.checkMove(piece, piece.x, piece.y - 1) != 0:
                moves.append((piece.x, piece.y - 1))
        if piece.y < 7:
            if self.board.checkMove(piece, piece.x, piece.y + 1) != 0:
                moves.append((piece.x, piece.y + 1))

        return moves

    def checkIfCheck(self: object, color: str) -> bool:
        """Vérifier si le roi est en échec

        Args:
            self (object): Game
            color (str): Couleur du roi (white ou black)

        Returns:
            bool: True si le roi est en échec, False sinon
        """        
        if color == "white":
            king = self.whiteKing
        else:
            king = self.blackKing

        for piece in self.pieces:
            if piece.color != king.color:
                if self.getPossibleMoves(piece) == []:
                    continue
                if (king.x, king.y) in self.getPossibleMoves(piece):
                    self.setCheck(True)
                    return True
        return False

    def checkIfCheckmate(self: object, color: str) -> bool:
        """Vérifier si le roi est en échec et mat

        Args:
            self (object): Game
            color (str): Couleur du roi (white ou black)

        Returns:
            bool: True si le roi est en échec et mat, False sinon
        """        
        # Checkmate = check + king can't move + no piece can block the check or capture the piece putting the king in check

        if color == "white":
            king = self.whiteKing
        else:
            king = self.blackKing

        # Check if king can move to a safe square (not in check)
        for move in self.getKingMoves(king):
            if not self.checkIfMoveIsCheck(king, move[0], move[1]):
                return False

        # Check if any piece can block or capture the piece putting the king in check
        for piece in self.pieces:
            if piece.color == king.color:
                for move in self.getPossibleMoves(piece):
                    if not self.checkIfMoveIsCheck(piece, move[0], move[1]):
                        return False

        self.setCheckmate(True)
        self.isOver = True
        return True

    def checkIfMoveIsCheck(self: object, piece: Piece, x: int, y: int) -> bool:
        """Vérifier si un mouvement met le roi en échec

        Args:
            self (object): Game
            piece (Piece): Piece
            x (int): coordonnée x de la case de destination du mouvement
            y (int): coordonnée y de la case de destination du mouvement

        Returns:
            bool: True si le mouvement met le roi en échec, False sinon
        """        
        clone = self.clone()
        clone.getBoard().movePiece(piece, x, y)
        return not clone.checkIfCheck(self.getTurn())

    def clone(self: object)-> object:
        """Cloner le plateau de jeu et les pièces qui s'y trouvent

        Args:
            self (object): Game

        Returns:
            object: Clone du plateau de jeu et des pièces qui s'y trouvent
        """        

        clone_game = Game()
        clone_board = clone_game.getBoard()

        for piece in self.pieces:
            clone_board.setPiece(piece.x, piece.y, piece)

        clone_board.whiteKing = clone_board.getPiece(
            self.whiteKing.x, self.whiteKing.y)
        clone_board.blackKing = clone_board.getPiece(
            self.blackKing.x, self.blackKing.y)

        return clone_game


if __name__ == "__main__":
    partie = Game()
    partie.getBoard().printBoard()

    partie.getBoard().movePiece(partie.getBoard().getPiece(0, 1), 0, 3)
    partie.getBoard().printBoard()

    partie.getBoard().movePiece(partie.getBoard().getPiece(0, 6), 0, 4)
    partie.getBoard().printBoard()

    partie.getBoard().movePiece(partie.getBoard().getPiece(0, 0), 0, 4)
    partie.getBoard().printBoard()
