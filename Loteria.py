import streamlit as st
import random as rd

def novo_sorteio():
            st.session_state.sorteio = rd.randint(1,15)
            st.session_state.chances = 3

def verificar_sorteio():
    usuario = st.session_state.get("usuario", 0)

    if usuario is None:
        st.error("Por favor, insira um número válido!")
        return
    
    if 1 <= usuario <=15:
        if usuario == st.session_state.sorteio:
            st.success("Parabéns, você acertou o número!")
            st.balloons()
            st.session_state.chances = 0

        elif usuario > st.session_state.sorteio:
            st.session_state.chances -=1
            if st.session_state.chances > 0:
                st.warning("O número é menor.")
            else:
                st.error(f"Suas tentativas acabaram! O número era {st.session_state.sorteio}")
        else:
            st.session_state.chances -=1
            if st.session_state.chances > 0:
                st.warning("O número é maior.")
            else:
                st.error(f"Suas tentativas acabaram! O número era {st.session_state.sorteio}")

if 'sorteio' not in st.session_state:
    novo_sorteio() 

st.title("Loteria da Babilônia")
st.write(f"Você tem {st.session_state.chances} chances para acertar o número.")

desativar = st.session_state.chances == 0

st.number_input(
    "Entre com um valor de 1 até 15:",
    min_value=1,
    max_value=15,
    value=None,
    disabled=desativar,
    key="usuario"
)    

a, b,_ = st.columns([1.5, 2, 8])

with a:
    st.button(
        "Verificar",
        on_click=verificar_sorteio,
        disabled=desativar
    )
        
     
with b:
    st.button(
        "Novo sorteio",
        type="primary",
        on_click=novo_sorteio
    )