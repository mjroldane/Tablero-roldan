import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de la página (esto le da un look más profesional)
st.set_page_config(page_title="Magic Canvas", page_icon="🎨", layout="wide")

st.title("🎨 Magic Drawing Board")
st.markdown("---")

# --- SIDEBAR: CONFIGURACIÓN ---
with st.sidebar:
    st.header("🛠️ Configuración")
    
    with st.expander("📐 Dimensiones del Lienzo", expanded=True):
        canvas_width = st.slider("Ancho", 300, 1000, 800, 50)
        canvas_height = st.slider("Alto", 200, 800, 400, 50)

    with st.expander("🖌️ Herramientas de Estilo", expanded=True):
        drawing_mode = st.selectbox(
            "Herramienta:",
            ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
            index=0
        )
        
        stroke_width = st.slider('Grosor de línea', 1, 50, 5)
        
        # Columnas para los selectores de color (se ve más limpio)
        col1, col2 = st.columns(2)
        with col1:
            stroke_color = st.color_picker("Trazo", "#FFFFFF")
        with col2:
            bg_color = st.color_picker("Fondo", "#262730")

    st.info("💡 **Tip:** Usa 'Transform' para mover objetos ya dibujados.")

# --- CUERPO PRINCIPAL ---
# Centramos el canvas usando columnas
main_col, side_info = st.columns([3, 1])

with main_col:
    st.subheader("🖼️ Lienzo")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}",
        update_穩定=True,
    )

with side_info:
    st.subheader("📊 Datos del Dibujo")
    if canvas_result.json_data is not None:
        # Mostramos cuántos objetos hay en el canvas
        objects = canvas_result.json_data["objects"]
        st.metric("Objetos dibujados", len(objects))
        
        if st.button("🗑️ Limpiar Consola"):
            st.rerun()
            
    st.markdown("""
    **Controles rápidos:**
    * **Mouse:** Dibujar
    * **Transform:** Escalar/Mover
    * **Colores:** Cambia el look al instante
    """)

# Pie de página sutil
st.caption("Hecho con ❤️ usando Streamlit y Drawable Canvas")
