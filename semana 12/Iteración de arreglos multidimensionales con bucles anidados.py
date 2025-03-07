# vamos analizar tres temperaturas de ciudades difrentes
# Definir la matriz de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1 quito
        [   # Semana 1
            {"dia": "Lunes", "temp": 75},
            {"dia": "Martes", "temp": 90},
            {"dia": "Miércoles", "temp": 89},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 85},
            {"dia": "Sábado", "temp": 91},
            {"dia": "Domingo", "temp": 77}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 88},
            {"dia": "Martes", "temp": 87},
            {"dia": "Miércoles", "temp": 83},
            {"dia": "Jueves", "temp": 91},
            {"dia": "Viernes", "temp": 77},
            {"dia": "Sábado", "temp": 89},
            {"dia": "Domingo", "temp": 92}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 88},
            {"dia": "Martes", "temp": 85},
            {"dia": "Miércoles", "temp": 89},
            {"dia": "Jueves", "temp": 77},
            {"dia": "Viernes", "temp": 90},
            {"dia": "Sábado", "temp": 91},
            {"dia": "Domingo", "temp": 89}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 79},
            {"dia": "Martes", "temp": 89},
            {"dia": "Miércoles", "temp": 85},
            {"dia": "Jueves", "temp": 91},
            {"dia": "Viernes", "temp": 91},
            {"dia": "Sábado", "temp": 88},
            {"dia": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2 cuenca
        [   # Semana 1
            {"dia": "Lunes", "temp": 63},
            {"dia": "Martes", "temp": 65},
            {"dia": "Miércoles", "temp": 77},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 89},
            {"dia": "Sábado", "temp": 90},
            {"dia": "Domingo", "temp": 93}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 89},
            {"dia": "Martes", "temp": 63},
            {"dia": "Miércoles", "temp": 76},
            {"dia": "Jueves", "temp": 72},
            {"dia": "Viernes", "temp": 77},
            {"dia": "Sábado", "temp": 90},
            {"dia": "Domingo", "temp": 92}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 65},
            {"dia": "Martes", "temp": 88},
            {"dia": "Miércoles", "temp": 69},
            {"dia": "Jueves", "temp": 61},
            {"dia": "Viernes", "temp": 72},
            {"dia": "Sábado", "temp": 76},
            {"dia": "Domingo", "temp": 93}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 66},
            {"dia": "Martes", "temp": 69},
            {"dia": "Miércoles", "temp": 88},
            {"dia": "Jueves", "temp": 75},
            {"dia": "Viernes", "temp": 90},
            {"dia": "Sábado", "temp": 92},
            {"dia": "Domingo", "temp": 86}
        ]
    ],
    [   # Ciudad 3  Duran
        [   # Semana 1
            {"dia": "Lunes", "temp": 88},
            {"dia": "Martes", "temp": 87},
            {"dia": "Miércoles", "temp": 88},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 90},
            {"dia": "Sábado", "temp": 90},
            {"dia": "Domingo", "temp": 89}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 90},
            {"dia": "Martes", "temp": 88},
            {"dia": "Miércoles", "temp": 87},
            {"dia": "Jueves", "temp": 86},
            {"dia": "Viernes", "temp": 89},
            {"dia": "Sábado", "temp": 84},
            {"dia": "Domingo", "temp": 89}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 91},
            {"dia": "Martes", "temp": 83},
            {"dia": "Miércoles", "temp":90 },
            {"dia": "Jueves", "temp": 88},
            {"dia": "Viernes", "temp": 89},
            {"dia": "Sábado", "temp": 85},
            {"dia": "Domingo", "temp": 82}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 81},
            {"dia": "Martes", "temp": 78},
            {"dia": "Miércoles", "temp": 92},
            {"dia": "Jueves", "temp": 77},
            {"dia": "Viernes", "temp": 86},
            {"dia": "Sábado", "temp": 88},
            {"dia": "Domingo", "temp": 93}
        ]
    ]
]

ciudades = ["Quito", "Cuenca", "Duran"]

for i, ciudad in enumerate(temperaturas):
    for j, semana in enumerate(ciudad):
        suma_temperaturas = 0
        total_dias = 0
        for dia in semana:
            suma_temperaturas += dia["temp"]
            total_dias += 1
        promedio = suma_temperaturas / total_dias
        print(f"Promedio en {ciudades[i]}, Semana {j + 1}: {promedio:.2f}°C")