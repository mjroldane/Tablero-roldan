import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuracion de la pagina limpia y ancha
st.set_page_config(page_title="Tablero de Dibujo", layout="wide")

st.title("Tablero de Dibujo")
st.markdown("---")

# --- SIDEBAR: CONFIGURACION ---
with st.sidebar:
    st.header("Configuracion")
    
    with st.expander("Dimensiones del Lienzo", expanded=True):
        canvas_width = st.slider("Ancho", 300, 1000, 800, 50)
        canvas_height = st.slider("Alto", 200, 800, 400, 50)

    with st.expander("Herramientas de Estilo", expanded=True):
        drawing_mode = st.selectbox(
            "Herramienta:",
            ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
            index=0
        )
        
        stroke_width = st.slider('Grosor de linea', 1, 50, 5)
        
        col1, col2 = st.columns(2)
        with col1:
            stroke_color = st.color_picker("Trazo", "#FFFFFF")
        with col2:
            bg_color = st.color_picker("Fondo", "#262730")

    st.info("Tip: Use 'Transform' para mover objetos ya dibujados.")

# --- CUERPO PRINCIPAL ---
main_col, side_info = st.columns([3, 1])

with main_col:
    st.subheader("Lienzo")
    # Correccion del error: eliminamos el parametro inexistente
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}"
    )

with side_info:
    st.subheader("Informacion")
    if canvas_result.json_data is not None:
        objetos_count = len(canvas_result.json_data["objects"])
        st.metric("Objetos", objetos_count)
        
        if st.button("Reiniciar Aplicacion"):
            st.rerun()
            
    st.markdown("""
    **Controles:**
    * Click y arrastrar para dibujar.
    * Seleccione herramientas en el menu lateral.
    * Los cambios de tamaño limpian el lienzo.
    """)

st.caption("Aplicacion de Dibujo Profesional")
