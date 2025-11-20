import streamlit as st
from PIL import Image, ImageDraw
import helper_functions as hf
from forward_checking import forward_checking
# from backtracking import backtracking
# from mac import mac


# ------------------- Draw Chessboard -------------------
def draw_board(assignment, N):
    square_size = 40  # pixels per square
    board_size = N * square_size

    img = Image.new("RGB", (board_size, board_size), "white")
    draw = ImageDraw.Draw(img)

    for row in range(N):
        for col in range(N):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            # color squares
            if (row + col) % 2 == 0:
                draw.rectangle([x1, y1, x2, y2], fill="#EEE")
            else:
                draw.rectangle([x1, y1, x2, y2], fill="#999")

            # draw queen if present
            queen_col = assignment.get(row + 1)
            if queen_col == col + 1:
                draw.text(
                    (x1 + 10, y1 + 5),
                    "♕",
                    fill="red"
                )

    return img


# ------------------- Streamlit UI -------------------
st.title("♕ N-Queens Solver")
st.write("Choose an algorithm and N value, then click Solve.")

algo = st.selectbox("Algorithm:", ["Forward Checking", "Backtracking", "MAC"])
N = st.number_input("Enter N:", min_value=4, value=8, step=1)

if st.button("Solve"):

    if algo == "Forward Checking":
        solution, t, checks = forward_checking(N)

    elif algo == "Backtracking":
        st.write("Backtracking not connected yet.")
        st.stop()

    elif algo == "MAC":
        st.write("MAC not connected yet.")
        st.stop()

    # show results
    st.write("### Solution (row : col):")
    st.write(solution)

    st.write(f"**Time:** {t:.6f} seconds")
    st.write(f"**Checks:** {checks}")

    # draw and show the board
    st.write("### Board Visualization:")
    img = draw_board(solution, N)
    st.image(img)
