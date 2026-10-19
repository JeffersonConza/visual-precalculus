"""
Paletas de colores y constantes de diseño visual para las animaciones.
"""

THEME = {
    # Fondos y neutros (inspirados en el tejido del poncho)
    "bg_color": "#151212",         # Carbón noche andino (base oscura cálida)
    "statement_text": "#fdfbf7",   # Blanco lana de alpaca / marfil suave
    
    # Identidad Editorial Amarun (verdes azulados y pizarras)
    "amarun_teal": "#7da3a1",      # Turquesa pizarra distintivo del logo Amarun
    "header_color": "#8ec3c0",     # Turquesa claro Amarun para títulos
    "axes": "#5d7876",             # Pizarra Amarun para ejes matemáticos
    "curve": "#5ce1e6",            # Turquesa luminoso para curvas de funciones

    # Identidad Poncho Yachay Tech (rojo carmesí, terracota y dorado)
    "poncho_red": "#9e2a2b",       # Rojo granate / carmesí del poncho
    "statement_box": "#a32f30",    # Recuadro de enunciado en rojo poncho
    "highlight": "#f6b840",        # Oro andino / maíz para fórmulas matemáticas clave
    "secondary": "#db5a38",        # Terracota cálido para transiciones intermedias
    
    # Estados y utilidades
    "success": "#48bb78",          # Verde esmeralda andino para resultado final
    "error": "#e53e3e",            # Rojo de advertencia
}

# Constantes de tiempo estándar (segundos)
TIMINGS = {
    "header_appear": 0.8,
    "statement_write": 1.5,
    "statement_read_base": 4.0,
    "statement_minimize": 1.0,
    "step_transition": 1.2,
    "highlight_answer": 0.8,
    "final_pause": 4.0,
}
