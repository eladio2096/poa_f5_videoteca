# ==============================================
# PROBLEMA 4: VIDEOTECA DIGITAL
# Estudiante: [ELADIO RAMIREZ SANCHEZ]
# Curso: Fundamentos de Programación - UNAD
# Fase 5 - Evaluación Final POA
# ==============================================

# --- 1. DATOS INICIALES (Matriz con 8 películas) ---
videoteca = [
    ["Inception", 2010, 8.8, "Ciencia Ficción"],
    ["Parasite", 2019, 9.0, "Drama"],
    ["The Dark Knight", 2008, 9.0, "Acción"],
    ["Spider-Man: Into the Spider-Verse", 2018, 8.4, "Animación"],
    ["Everything Everywhere All at Once", 2022, 8.9, "Ciencia Ficción"],
    ["The Godfather", 1972, 9.2, "Drama"],
    ["Oppenheimer", 2023, 8.5, "Drama"],
    ["Dune: Part Two", 2024, 8.7, "Ciencia Ficción"]
]# --- 2. FUNCIÓN PARA CONTAR TÍTULOS (Módulo solicitado) ---
def contar_titulos_cumplen_criterios(matriz, umbral_calificacion, anio_limite):
    """
    Cuenta cuántas películas tienen calificación >= umbral Y año >= año límite
    """
    contador = 0
    print("\n--- Películas que SÍ cumplen los criterios ---")
    
    for pelicula in matriz:
        titulo = pelicula[0]
        anio = pelicula[1]
        calificacion = pelicula[2]
        # genero = pelicula[3]  # No lo usamos para contar, pero está disponible
        
        # LÓGICA DE NEGOCIO: Ambas condiciones deben ser verdaderas
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador = contador + 1
            print(f"  ✔ {titulo} ({anio}) - Calificación: {calificacion}")
    
    if contador == 0:
        print("  ✖ Ninguna película cumple con los criterios.")
    
    return contador
# --- 3. PROGRAMA PRINCIPAL ---
print("=" * 50)
print("   SISTEMA DE VIDEOTECA DIGITAL")
print("=" * 50)
print(f"Base de datos cargada con {len(videoteca)} películas.\n")

print("--- CRITERIOS DE BÚSQUEDA ---")
try:
    # El usuario ingresa los valores
    umbral = float(input("  › Calificación mínima (0-10): "))
    anio_limite = int(input("  › Año mínimo de lanzamiento: "))
    
    # Validación simple
    if umbral < 0 or umbral > 10:
        print("  ⚠️ Recomendación: La calificación debería estar entre 0 y 10.")
    
    # LLAMAR A LA FUNCIÓN (aquí se ejecuta el conteo)
    total_cumplen = contar_titulos_cumplen_criterios(videoteca, umbral, anio_limite)
    
    # SALIDA FINAL (lo que pide el problema)
    print("\n" + "=" * 50)
    print(">>> INFORME FINAL <<<")
    print(f"Total de títulos que cumplen los criterios: {total_cumplen}")
    print("=" * 50)
    
except ValueError:
    print("\n❌ ERROR: Ingresa números válidos.")
    print("   Usa punto para decimales (ejemplo: 8.5)")