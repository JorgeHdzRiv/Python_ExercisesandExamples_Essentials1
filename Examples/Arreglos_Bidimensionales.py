"""
El acceso al campo seleccionado del tablero requiere dos índices: el primero selecciona la fila;
el segundo: el número del campo dentro de la fila, el cual es un número de columna.
"""
EMPTY = "-"
PAWN = "PEON"
ROOK = "TORRE"
KNIGHT = "CABALLO"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

#Agregamos todas las torres del tablero
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

#Agregando un caballo en C4 ejemplo
board[4][2] = KNIGHT

#Agregando un peon a E5
board[3][4] = PAWN

print(board)
