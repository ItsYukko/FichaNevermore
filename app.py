import streamlit as st
import random
import json

st.set_page_config(page_title="Ficha Nevermore", page_icon="📜", layout="wide")
st.title("📜 Ficha de Personagem - Nevermore")

# ------------------ DADOS BÁSICOS ------------------
st.header("Informações do Personagem")
nome = st.text_input("Nome")
tropo = st.text_input("Tropo")
vida = st.number_input("Vida", min_value=0, step=1)
mana = st.number_input("Mana", min_value=0, step=1)
sanidade = st.number_input("Sanidade", min_value=0, step=1)

# ------------------ TABS PRINCIPAIS ------------------
tabs = st.tabs(["Atributos", "Sanidade", "Armas", "Inventário", "Glifos", "Artefatos", "Livro"])

# ------------------ ATRIBUTOS ------------------
with tabs[0]:
    st.subheader("Atributos")
    col1, col2, col3 = st.columns(3)

    with col1:
        reacao = st.number_input("Reação (d6)", min_value=0)
        percepcao = st.number_input("Percepção (d6)", min_value=0)
        sagacidade = st.number_input("Sagacidade (d6)", min_value=0)
        potencia = st.number_input("Potência (d6)", min_value=0)
        influencia = st.number_input("Influência (d6)", min_value=0)
        resolucao = st.number_input("Resolução (d6)", min_value=0)

    with col2:
        ocultismo = st.number_input("Ocultismo (d10)", min_value=0)
        biologico = st.number_input("Biológico (d10)", min_value=0)
        exato = st.number_input("Exato (d10)", min_value=0)
        saude = st.number_input("Saúde (d10)", min_value=0)
        social = st.number_input("Social (d10)", min_value=0)
        artistico = st.number_input("Artístico (d10)", min_value=0)

    with col3:
        esportivas = st.number_input("Esportivas (d12)", min_value=0)
        ferramentas = st.number_input("Ferramentas (d12)", min_value=0)
        oficios = st.number_input("Ofícios (d12)", min_value=0)
        armas_attr = st.number_input("Armas (d12)", min_value=0)
        veiculos = st.number_input("Veículos (d12)", min_value=0)
        infiltracao = st.number_input("Infiltração (d12)", min_value=0)

    # Rolagem de dados de atributo
    if st.button("🎲 Rolar dado de atributo aleatório"):
        dado = random.choice([6, 10, 12])
        valor = random.randint(1, dado)
        st.info(f"Você rolou um d{dado} e tirou **{valor}**!")

# ------------------ SANIDADE ------------------
with tabs[1]:
    st.subheader("Sanidade")
    fardos = st.text_area("Fardos")
    gatilhos = st.text_area("Gatilhos")
    conforto = st.text_area("Conforto")
    falso_controle = st.text_area("Falso Controle")

# ------------------ ARMAS ------------------
with tabs[2]:
    st.subheader("Armas")
    armas_list = st.text_area("Lista de Armas (Nome | Dano | Crítico | Tipo)")

# ------------------ INVENTÁRIO ------------------
with tabs[3]:
    st.subheader("Inventário")
    dinheiro = st.text_input("Dinheiro")
    itens = st.text_area("Itens do inventário")

# ------------------ GLIFOS ------------------
with tabs[4]:
    st.subheader("Glifos")
    glifos = st.text_area("Glifos conhecidos")

# ------------------ ARTEFATOS ------------------
with tabs[5]:
    st.subheader("Artefatos")
    artefatos = st.text_area("Artefatos mágicos conhecidos")

# ------------------ LIVRO ------------------
with tabs[6]:
    st.subheader("Livro Mágico")
    nome_livro = st.text_input("Nome do Livro")
    sinopse = st.text_area("Sinopse (máx. 10 linhas)")
    habilidade = st.text_area("Habilidade do Livro")
    deterioracao = st.text_area("Deterioração")

# ------------------ SALVAR FICHA ------------------
if st.button("💾 Salvar Ficha"):
    ficha = {
        "nome": nome,
        "tropo": tropo,
        "vida": vida,
        "mana": mana,
        "sanidade": sanidade,
        "inventario": itens,
        "dinheiro": dinheiro,
        "glifos": glifos,
        "artefatos": artefatos,
        "livro": {
            "nome": nome_livro,
            "sinopse": sinopse,
            "habilidade": habilidade,
            "deterioracao": deterioracao
        }
    }
    with open("ficha_personagem.json", "w", encoding="utf-8") as f:
        json.dump(ficha, f, ensure_ascii=False, indent=4)
    st.success("Ficha salva como ficha_personagem.json!")
