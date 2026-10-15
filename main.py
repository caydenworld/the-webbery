import streamlit as st


def main():

    if "bg_color" not in st.session_state:
        st.session_state.bg_color = "#ffffff11"

    st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)
    st.header("Hi There! I'm C98!")
    st.write(
        "This is a place where I might post what I'm working on, and keeping it as a portfolio... That's kinda it..."
    )
    st.subheader("This is the code for the website so far:")
    st.code("""st.header("Hi There! I'm C98!")
        st.write("This is a place where I might post what I'm working on, and keeping it as a portfolio... That's kinda it...")
        st.subheader("This is the code for the website so far:")""")


    st.session_state.bg_color = st.color_picker("Pick a color", key=1)

    if "bg_color" not in st.session_state:
        st.session_state.bg_color = "#ffffff11"

    st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {st.session_state.bg_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)
    


if __name__ == "__main__":
    main()
