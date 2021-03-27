from chaos_game import *

def run_chaos_game():
    canvas = initialize(800)

    triangle = draw_triangle(canvas)

    p = random_point(canvas)

    for i in range(10000):
        corner = random_corner(triangle)
        p_new = get_halfway_point(p, corner)
        draw_point(p_new, canvas)

        p = p_new


if __name__ == "__main__":
    run_chaos_game()

    # wait until user closes application
    mainloop()
