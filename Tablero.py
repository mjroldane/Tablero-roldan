import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de página limpia
st.set_page_config(page_title="Editor de Dibujo", layout="wide")

# Estilo personalizado para el título y márgenes
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        margin-top: -50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL: HERRAMIENTAS ---
with st.sidebar:
    st.title("Configuración")
    
    with st.expander("Dimensiones del Lienzo", expanded=False):
        canvas_width = st.slider("Ancho", 300, 1200, 800, 50)
        canvas_height = st.slider("Alto", 200, 800, 450, 50)

    st.markdown("---")
    
    drawing_mode = st.selectbox(
        "Herramienta de dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )
    
    stroke_width = st.slider("Grosor del trazo", 1, 50, 4)
    
    c1, c2 = st.columns(2)
    with c1:
        stroke_color = st.color_picker("Color", "#000000")
    with c2:
        bg_color = st.color_picker("Fondo", "#EEEEEE")

# --- CUERPO PRINCIPAL ---
col_canvas, col_info = st.columns([4, 1])

with col_canvas:
    st.subheader("Área de Trabajo")
    
    # Contenedor para el lienzo
    with st.container():
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color=bg_color,
            height=canvas_height,
            width=canvas_width,
            drawing_mode=drawing_mode,
            key=f"canvas_{canvas_width}_{canvas_height}",
        )

with col_info:
    # Panel de información plegable (Meter y Sacar)
    with st.expander("Panel de Información", expanded=True):
        if canvas_result.json_data is not None:
            n_objetos = len(canvas_result.json_data["objects"])
            st.metric("Objetos en escena", n_objetos)
        
        st.markdown("---")
        st.write("**Atajos:**")
        st.caption("- Shift: Bloquear ángulos")
        st.caption("- Supr: Borrar seleccionado")
        
        if st.button("Limpiar todo", use_container_width=True):
            st.rerun()

# Pie de página simple
st.markdown("---")
st.caption("Editor de Gráficos Vectoriales | Prototipo v2.0")
