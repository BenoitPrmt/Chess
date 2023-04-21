from tkinter import *
from classes.Game import Game


class App(Tk):
    def __init__(self: object)->None:
        super().__init__()
        self.title("Chess - by @BenoitPrmt")
        self.geometry("800x800")
        self.board = None
        self.mainText = None

    def displayBoard(self: object)->None:
        """Affiche le plateau de jeu
        """

        for i in range(8):
            Label(self, text=i, fg="red", bg="white",
                  width=10, height=5).grid(row=8, column=i)
            for j in range(8):
                Label(self, text=j, fg="red", bg="white",
                      width=10, height=5).grid(row=j, column=8)
                if (i + j) % 2 == 0:
                    color = "white"
                else:
                    color = "black"

                # set a Label for each square of the board, when the user click on it, it will call the function click with the coordinates of the square
                label = Button(self, text=self.board.getBoard()[
                    i][j], fg="red", bg=color, width=10, height=5, command=lambda row=i, col=j: self.click(row, col))
                label.grid(row=j, column=i)

        self.mainText = Label(self, textvariable="Welcome to Chess !",
                              fg="red", bg="white", width=10, height=5)

    def changeMainText(self: object, text: str) -> None:
        """Change le texte principal affiché dans la fenêtre. Ce texte sert à annoncer le tour, si il y a échec ou échec et mat.

        Args:
            text (string): new text
        """
        self.mainText.config(textvariable=text)

    def click(self: object, x: int, y: int) -> None:
        """Se déclenche en cas de clic sur une case du plateau.

        Args:
            x (int): Coordonnée x de la case sur le plateau
            y (int): Coordonnée y de la case sur le plateau
        """

        if game.turnState == "choosePiece":

            piece = game.getBoard().getPiece(x, y)
            game.movingPiece = piece

            # check if user click on a piece
            if piece is not None:
                # check if user click on a piece of the same color
                if piece.getColor() == game.getTurn():

                    # display all possible moves
                    possibMoves = game.getPossibleMoves(piece)

                    for move in possibMoves:
                        if not 0 <= move[0] <= 7 or not 0 <= move[1] <= 7:
                            possibMoves.remove(move)
                            continue
                        game.backUpCoord[move] = game.board.board[move[0]][move[1]]
                        game.board.board[move[0]][move[1]] = "X"

                    if len(possibMoves) == 0:
                        print("No possible moves")
                        return

                    print("Possible moves: " + str(possibMoves))
                    game.turnState = "chooseMove"
                    game.possibleMoves = possibMoves

                    app.displayBoard()

                # check if user click on a piece of the other color
                elif piece.getColor() != game.getTurn():
                    print("This is not your piece, retry")
            else:
                print("No piece here")

        elif game.turnState == "chooseMove":

            possibMoves = game.possibleMoves
            piece = game.movingPiece

            if (x, y) in possibMoves:
                for move in possibMoves:
                    game.board.board[move[0]][move[1]
                                              ] = game.backUpCoord[move]
                # move the piece
                game.board.board[piece.x][piece.y] = None
                game.board.board[x][y] = piece
                piece.move(x, y)
                print("Moved at " + str(x) + ", " + str(y))
                # moved = True

                game.turnState = "choosePiece"
                self.displayBoard()

                # Check if the king is in check
                if game.checkIfCheck(game.getTurn()):
                    if game.checkIfCheckmate(game.getTurn()):
                        print("Checkmate !")
                        print("The winner is " +
                              game.changeTurn() + " !")
                        return
                    else:
                        print("Check !")

                game.changeTurn()

                # Check if the king is in check
                if game.checkIfCheck(game.getTurn()):
                    if game.checkIfCheckmate(game.getTurn()):
                        print("Checkmate !")
                        print("The winner is " +
                              game.changeTurn() + " !")
                        return
                    else:
                        print("Check !")
            else:
                print("Not a possible move")


if __name__ == "__main__":
    app = App()

    game = Game()
    app.board = game.getBoard()

    app.displayBoard()
    app.mainloop()
