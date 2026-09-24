from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1: King ถูก Pawn โจมตี
    print("--- Test Case 1 ---")
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1) # คาดหวัง: Success

    # ตัวอย่างที่ 2: King ไม่ถูกโจมตี (Pawn อยู่ผิดตำแหน่ง)
    print("\n--- Test Case 2 ---")
    board2 = """\
..P.
.K..
....
...."""
    checkmate(board2) # คาดหวัง: Fail

    # ตัวอย่างที่ 3: Queen ถูก Bishop บล็อกไว้ ทำให้โจมตี Kingไม่ได้
    print("\n--- Test Case 3 ---")
    board3 = """\
..Q.
..B.
..K.
...."""
    checkmate(board3) # คาดหวัง: Fail

    # ตัวอย่างที่ 4: King ถูก Bishop โจมตี
    print("\n--- Test Case 4 ---")
    board4 = """\
B.......
........
........
...K....
........
........
........
........"""
    checkmate(board4) # คาดหวัง: Success

    # ตัวอย่างที่ 5: King ถูก Rook โจมตี
    print("\n--- Test Case 5 ---")
    board5 = """\
....
.K..
....
.R.."""
    checkmate(board5) # คาดหวัง: Success
    
    # ตัวอย่างที่ 6: กระดานที่ใช้ตัวอักษรอื่นเป็นช่องว่าง (เช่น Space)
    print("\n--- Test Case 6 (Spaces as Empty Squares) ---")
    board6 = """\
R   
 K  
  P 
    """
    checkmate(board6) # คาดหวัง: Success

    # ตัวอย่างที่ 7: Undefined (ไม่มี King)
    print("\n--- Test Case 7 (Undefined: No King) ---")
    board7 = """\
R...
....
..P.
...."""
    checkmate(board7) # คาดหวัง: ไม่แสดงผล

    # ตัวอย่างที่ 8: Undefined (กระดานไม่เป็นสี่เหลี่ยมจัตุรัส)
    print("\n--- Test Case 8 (Undefined: Not Square) ---")
    board8 = """\
R..
.K.
..P.
...."""
    checkmate(board8) # คาดหวัง: ไม่แสดงผล

    # ตัวอย่างที่ 9: มี King หลายตัว
    print("\n--- Test Case 9 (Undefined: Multiple Kings) ---")
    board9 = """\
R...
.K..
..K.
...."""
    checkmate(board9) # คาดหวัง: ไม่แสดงผล

if __name__ == "__main__":
    main()