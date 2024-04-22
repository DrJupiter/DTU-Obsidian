def distance_matrix_noloop(p1, p2):
    p1 = cp.radians(p1)
    p2 = cp.radians(p2)
    dsin2 = cp.sin(0.5 * (p1[:, None, :] - p2[None, :, :])) ** 2
    cosprod = cp.cos(p1[:, None, 0]) * cp.cos(p2[None, :, 0])
    D = 2 * cp.arcsin(cp.sqrt(dsin2[:, :, 0] + cosprod * dsin2[:, :, 1]))
    D *= 6371  # Earth radius in km
    return D