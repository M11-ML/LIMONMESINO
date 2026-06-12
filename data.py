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
    0: (130, 345),   # CD Cartago (junto al cantón Cartago)
    1: (140, 350),   # Cartago
    2: (250, 250),   # Paraíso
    3: (70, 410),    # La Unión
    4: (350, 290),   # Jiménez
    5: (470, 420),   # Turrialba
    6: (245, 430),   # Alvarado
    7: (205, 530),   # Oreamuno
    8: (90, 280),    # El Guarco
}

# Alias por compatibilidad con código existente
COORDS = CENTERS

CAPACITY = 24  # pallets por camión

# Tamaño del "lienzo" del mapa (ancho, alto), en las mismas unidades que CENTERS / CANTON_POLY
MAP_SIZE = (640, 600)

# Polígonos (contornos aproximados) de cada cantón, calcados sobre el mapa de
# referencia del IGN/atlas cantonal de Cartago. Coordenadas (x, y) con eje Y hacia arriba.
CANTON_POLY = {
    # Oreamuno (norte)
    7: [
        (90, 585), (230, 590), (330, 510), (300, 460), (250, 435),
        (200, 450), (160, 470), (120, 490), (95, 530),
    ],
    # Alvarado (centro-norte)
    6: [
        (195, 485), (260, 495), (295, 450), (290, 390), (250, 365),
        (210, 380), (190, 420), (185, 455),
    ],
    # La Unión (noroeste)
    3: [
        (35, 450), (95, 460), (115, 425), (105, 385), (70, 370),
        (35, 390), (20, 420),
    ],
    # Cartago (centro-oeste, debajo de La Unión)
    1: [
        (85, 385), (150, 395), (195, 375), (195, 340), (160, 310),
        (110, 315), (80, 345),
    ],
    # El Guarco (suroeste)
    8: [
        (10, 350), (85, 350), (110, 315), (160, 310), (190, 270),
        (180, 220), (120, 200), (50, 230), (10, 280),
    ],
    # Paraíso (centro)
    2: [
        (160, 310), (195, 340), (195, 375), (250, 365), (290, 340),
        (330, 310), (340, 240), (310, 170), (250, 130), (180, 160),
        (150, 240),
    ],
    # Jiménez (centro-este)
    4: [
        (290, 340), (340, 350), (400, 320), (410, 260), (370, 230),
        (330, 240), (340, 310),
    ],
    # Turrialba (este — el más grande)
    5: [
        (250, 365), (290, 390), (295, 450), (330, 510), (420, 540),
        (520, 520), (615, 450), (560, 400), (490, 320), (440, 310),
        (410, 260), (400, 320), (340, 350), (290, 340),
    ],
}

# Contorno general (silueta) de toda la provincia, para dibujar el borde
# exterior tipo "mapa con contorno" (similar al mapa de Costa Rica de referencia).
PROVINCE_OUTLINE = [
    (90, 585), (230, 590), (330, 510), (420, 540), (520, 520),
    (615, 450), (560, 400), (490, 320), (440, 310), (410, 260),
    (400, 320), (340, 350), (330, 310), (340, 240), (310, 170),
    (250, 130), (180, 160), (150, 240), (120, 200), (50, 230),
    (10, 280), (10, 350), (20, 420), (35, 450), (95, 530),
]

# Colores por cantón (paleta inspirada en el mapa oficial de cantones)
CANTON_COLOR = {
    1: "#e8d9a0",  # Cartago
    2: "#f5ecc8",  # Paraíso
    3: "#d8c98a",  # La Unión
    4: "#e3d4a3",  # Jiménez
    5: "#f0e3ad",  # Turrialba
    6: "#b6a06f",  # Alvarado - tono oscuro distintivo
    7: "#f6e7ad",  # Oreamuno
    8: "#ead9a3",  # El Guarco
}
