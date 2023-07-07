import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Energy level of electron", page_icon="🕴️", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_6ft9bypa.json")
lottie_1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_B8jZujnF4h.json")


# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.subheader(" :wave:")
        st.title(

     """
     What is energy level of electron?
     In quantum mechanics, the energy levels of electrons in an atom or a quantum system are described by the Schrödinger equation. The Schrödinger equation is a fundamental equation in quantum mechanics that describes the behavior of quantum particles, including electrons.
     The energy levels of electrons in a quantum system are quantized, meaning they can only have certain discrete values rather than any arbitrary value. These discrete energy levels are represented by the principal quantum number (n) and other quantum numbers such as the angular momentum quantum number (l) and the magnetic quantum number (m).
    """)
    with right_column:
        st_lottie(lottie, height=300, key="Title")
    
# ---- Formula ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("Formula:")
        #st.write("##")
        st.write(
            """
          energy = (n ** 2 * h ** 2) / (8 * m * l ** 2)

In this formula:

n represents the principal quantum number. It can take on positive integer values greater than zero (1, 2, 3, etc.). Higher values of n correspond to higher energy levels or orbitals.

l represents the length scale. x is the user input for the length scale in Ångstrom. The length scale (l) is converted to meters (l = x * 10**-10) before using it in the energy calculation. The length scale is related to the size or radius of the electron's orbital.

h represents Planck's constant, which is a fundamental constant in quantum mechanics. It is approximately equal to 6.63 * 10**-34 J·s.

m represents the mass of the electron. In the code, the mass of the electron is approximately 9.109383702 * 10**-31 kg


            """
        )
    with right_column:
        st_lottie(lottie_1, height=300, key="Education")
        
