import streamlit as st

def calculate_energy_level(n, l):
    m = 9.109383702 * 10**-31  # kg, electron mass
    h = 6.63 * 10**-34  # J.s constant

    energy = (n ** 2 * h ** 2) / (8 * m * l ** 2)
    return energy

st.title("Energy Level Calculator")

n = st.number_input("Enter the value of n", value=1.0, step=0.1)
x = st.number_input("Enter the value of x (in Ångstrom)", value=1.0, step=0.1)
l = x * 10**-10

if st.button("Calculate Energy Level"):
    energy_level = calculate_energy_level(n, l)
    st.write("Energy Level:", energy_level)
    ev = energy_level / (1.6 * 10**-19)
    st.write("Energy level in eV:", ev, "eV")
