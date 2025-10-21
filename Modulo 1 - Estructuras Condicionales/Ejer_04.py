# =========================================
# SISTEMA DE RECOMENDACIÓN SIMPLE
# =========================================

# Historial de compras y productos recomendados
historial = ["cuaderno", "lapicero", "borrador"]

# Diccionario con productos relacionados
recomendaciones = {
    "cuaderno": ["papel bond", "carpeta", "resaltador"],
    "lapicero": ["tinta", "marcador", "portaminas"],
    "borrador": ["sacapuntas", "corrector", "lápiz"]
}

# Sistema de recomendación
for producto in historial:
    if producto in recomendaciones:
        print(f"\nSi compraste {producto}, también podrías querer: {', '.join(recomendaciones[producto])}")
