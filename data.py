"""
Datos base del problema — Florida Bebidas, Provincia de Cartago
Fuente: hoja de datos del Caso (8 cantones + CD Cartago)
"""

# Nombres de los nodos (0 = Centro de Distribución)
NAMES = {
    0: "CD Cartago",
    1: "Cartago",
    2: "Paraíso",
    3: "La Unión",
    4: "Jiménez",
    5: "Turrialba",
    6: "Alvarado",
    7: "Oreamuno",
    8: "El Guarco",
}

# Matriz de distancias por carretera (km) — nodo 0..8
DIST = [
    [0,  0,  9, 10, 34, 34, 20, 6,  6],
    [0,  0,  9, 10, 34, 34, 20, 6,  6],
    [9,  9,  0, 19, 26, 28, 13, 7, 12],
    [10, 10, 19, 0, 45, 43, 29, 14, 11],
    [34, 34, 26, 45, 0, 20, 21, 31, 37],
    [34, 34, 28, 43, 20, 0, 15, 29, 40],
    [20, 20, 13, 29, 21, 15, 0, 14, 25],
    [6,  6,  7, 14, 31, 29, 14, 0, 12],
    [6,  6, 12, 11, 37, 40, 25, 12, 0],
]

# Demanda semanal total (pallets) por cantón — valores por defecto
DEFAULT_DEMAND = {
    1: 124,  # Cartago
    2: 48,   # Paraíso
    3: 75,   # La Unión
    4: 15,   # Jiménez
    5: 61,   # Turrialba
    6: 12,   # Alvarado
    7: 36,   # Oreamuno
    8: 35,   # El Guarco
}

# Split de productos (Imperial / Pilsen / Tropical)
PRODUCT_SPLIT = {"Imperial": 0.50, "Pilsen": 0.25, "Tropical": 0.25}

# Posición (x, y) del centro de cada cantón / CD, en un sistema de coordenadas
# "de pantalla" (0-500 horizontal, 0-426 vertical, eje Y hacia arriba), inspirado
# en el mapa oficial de cantones de la provincia de Cartago.
CENTERS = {
    0: (108, 245),   # CD Cartago (depósito) — junto al cantón Cartago
    1: (112, 240),   # Cartago
    2: (190, 145),   # Paraíso
    3: (65, 285),    # La Unión
    4: (262, 195),   # Jiménez
    5: (385, 215),   # Turrialba
    6: (188, 315),   # Alvarado
    7: (143, 340),   # Oreamuno
    8: (88, 145),    # El Guarco
}

# Alias por compatibilidad con código existente
COORDS = CENTERS

CAPACITY = 24  # pallets por camión

# Tamaño del "lienzo" del mapa (ancho, alto), en las mismas unidades que CENTERS / CANTON_POLY
MAP_SIZE = (500, 426)

# Polígonos (contornos aproximados) de cada cantón, inspirados en el mapa oficial
# de cantones de la provincia de Cartago. Coordenadas (x, y) con eje Y hacia arriba.
CANTON_POLY = {
    # Oreamuno (amarillo, norte)
    7: [
        (95, 416), (160, 418), (200, 381), (205, 331), (185, 281),
        (160, 251), (135, 266), (115, 291), (95, 316), (82, 356), (80, 391),
    ],
    # Alvarado (oliva, centro-norte)
    6: [
        (160, 351), (205, 361), (228, 326), (222, 271), (190, 246),
        (160, 261), (150, 296), (150, 331),
    ],
    # La Unión (azul claro, noroeste, arriba de Cartago)
    3: [
        (28, 308), (75, 321), (112, 308), (118, 271), (95, 244),
        (52, 238), (20, 266), (15, 288),
    ],
    # Cartago (verde, centro-oeste, debajo de La Unión)
    1: [
        (75, 261), (130, 266), (150, 256), (155, 226), (135, 201),
        (100, 201), (75, 221), (65, 241),
    ],
    # El Guarco (naranja, suroeste, abajo)
    8: [
        (10, 221), (75, 226), (135, 201), (165, 166), (175, 116),
        (150, 71), (95, 51), (40, 81), (10, 136), (0, 181),
    ],
    # Paraíso (morado, centro)
    2: [
        (135, 266), (160, 251), (190, 246), (225, 231), (245, 196),
        (250, 136), (235, 81), (215, 41), (180, 31), (150, 66),
        (140, 116), (120, 156), (125, 201), (135, 231),
    ],
    # Jiménez (durazno, centro-este)
    4: [
        (225, 276), (265, 286), (295, 256), (310, 206), (305, 151),
        (280, 106), (250, 96), (225, 131), (220, 176), (225, 226),
    ],
    # Turrialba (turquesa, este — el más grande)
    5: [
        (230, 326), (310, 346), (400, 356), (480, 366), (498, 276),
        (498, 6), (380, 1), (290, 26), (250, 96), (280, 106),
        (305, 151), (310, 206), (295, 256), (265, 286), (225, 276),
    ],
}

# Colores por cantón (paleta inspirada en el mapa oficial de cantones)
CANTON_COLOR = {
    1: "#a9d18e",  # Cartago - verde
    2: "#c8a2d6",  # Paraíso - morado
    3: "#9dc3e6",  # La Unión - azul claro
    4: "#f4b183",  # Jiménez - naranja
    5: "#7fd1c8",  # Turrialba - turquesa
    6: "#bfbfa0",  # Alvarado - oliva
    7: "#ffd966",  # Oreamuno - amarillo
    8: "#f6a96b",  # El Guarco - naranja oscuro
}
