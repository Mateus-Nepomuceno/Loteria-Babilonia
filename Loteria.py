import streamlit as st
import random as rd

def novo_sorteio():
    if st.button("Novo Sorteio"):
            st.session_state.sorteio = rd.randint(1,15)
            st.session_state.chances = 3
            st.session_state.usuario = None

def numero_certo():
    st.success("Parabéns, você acertou o número!")
    st.balloons()

st.title("Loteria da Babilônia")

if "sorteio" not in st.session_state:
    st.session_state.sorteio = rd.randint(1,15)

if "chances" not in st.session_state:
    st.session_state.chances = 3
st.write(f"Você tem {st.session_state.chances} chances para acertar o número.")

if "usuario" not in st.session_state:
    st.session_state.usuario = None 
st.session_state.usuario = st.number_input(
    "Entre com um valor de 1 até 15:",
    min_value=1,
    max_value=15,
    value=None
)

if st.session_state.chances == 3:
    st.session_state.chances -=1

elif 1 <= st.session_state.chances <= 2:
     if st.session_state.usuario != None:
        if st.session_state.usuario == st.session_state.sorteio:
            numero_certo()
            novo_sorteio()
            st.session_state.chances = 0
        elif st.session_state.usuario > st.session_state.sorteio:
            st.warning("O número é menor.")
            st.session_state.chances -=1
        else:
            st.warning("O número é maior.")
            st.session_state.chances -=1

else:
    if st.session_state.usuario == st.session_state.sorteio:
            numero_certo()
            novo_sorteio()
    else:
        st.error(f"Suas tentativas acabaram! O número era {st.session_state.sorteio}")
        novo_sorteio()