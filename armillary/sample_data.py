import numpy as np
from hypatie import sph2car, unit

def big_dipper():
    stars = [('alf UMa', 165.9319646738126, 61.751034687818226),
             ('bet UMa', 165.46033229797294, 56.382433649496384),
             ('del UMa', 183.85650263625, 57.03261544611111),
             ('eps UMa', 193.5072899675, 55.95982295694445),
             ('eta UMa', 206.88515734206297, 49.31326672942533),
             ('gam UMa', 178.45769715249997, 53.69475972916666),
             ('zet UMa', 200.98141866666666, 54.92535197222222)]

    pos = np.zeros((7,3))
    pos[:, 0] = [i[1] for i in stars]
    pos[:, 1] = [i[2] for i in stars]
    pos[:, 2] = 7 * [1e100]

    star_positions = np.array([unit(sph2car(i)) for i in pos])
    return star_positions
