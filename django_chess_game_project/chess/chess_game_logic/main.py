from .app.board import *
from .app.moves import *

def main(board = Board()):
        
    while True:
        
        start = [int(element) for element in input('\n Enter coordinates of first piece x,y \n').split(',')]
        end = [int(element) for element in input('\n Enter coordinates of target position x,y \n').split(',')]
        piece = board.get_board_piece(start)
        color = lambda x: 'White' if piece.color else 'Black'
        
        if piece:
            print(f'Selected a {color(piece)} {piece.__class__.__name__}')
            if piece.__class__.__name__ == 'Rook':
                possible_moves = RookMoves(board,piece)
                
            elif piece.__class__.__name__ == 'Knight':
                possible_moves = KnightMoves(board,piece)
                
            elif piece.__class__.__name__ == 'Bishop':
                possible_moves = BishopMoves(board,piece)
                
            elif piece.__class__.__name__ == 'Queen':
                possible_moves = QueenMoves(board,piece)
                
            elif piece.__class__.__name__ == 'Knight':
                possible_moves = KnightMoves(board,piece)
                
            elif piece.__class__.__name__ == 'King':
                possible_moves = KingMoves(board,piece)
                
            elif piece.__class__.__name__ == 'Pawn':
                possible_moves = PawnMoves(board,piece)
        
        
            possible_moves.check_possible_moves()
            print(possible_moves.possible_moves)


def start():
    board = Board()
    return board 
    