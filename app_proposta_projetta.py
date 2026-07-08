import streamlit as st
from datetime import datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# 1. Configuração da página e identidade visual
st.set_page_config(
    page_title="Orçamento Interativo | Projetta Educação & Inovação",
    page_icon="💼",
    layout="centered"
)

# --- CONTROLE DE TEMA (LIGHT / DARK) ---
if 'tema_escuro' not in st.session_state:
    st.session_state.tema_escuro = False

with st.sidebar:
    st.markdown("### 🌗 Preferências Visuais")
    if st.button("Alternar Modo Claro / Escuro", use_container_width=True):
        st.session_state.tema_escuro = not st.session_state.tema_escuro
        st.rerun()

# Paleta de cores dinâmica baseada no estado do tema
if st.session_state.tema_escuro:
    cor_fundo_app = "#0f172a"
    cor_texto_principal = "#f8fafc"
    cor_texto_label = "#cbd5e1"
    cor_card = "#1e293b"
    cor_borda = "#334155"
else:
    cor_fundo_app = "#ffffff"
    cor_texto_principal = "#0f172a"
    cor_texto_label = "#1e293b"
    cor_card = "#f8fafc"
    cor_borda = "#e2e8f0"

# Injeção de CSS Premium
st.markdown(f"""
    <style>
    .stApp {{ background-color: {cor_fundo_app} !important; color: {cor_texto_principal} !important; }}
    label, p, span, .stMarkdown p {{ color: {cor_texto_label} !important; font-weight: 500 !important; }}
    h1, h2, h3, h4 {{ color: {cor_texto_principal} !important; font-family: Arial, sans-serif; font-weight: 700; }}

    .pricing-card {{
        background-color: {cor_card};
        border: 1px solid {cor_borda};
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }}

    button, .stButton>button {{
        background-color: #0f172a !important; color: #c5a880 !important;
        border: 1px solid #c5a880 !important; font-weight: 600 !important;
        transition: all 0.3s ease;
    }}
    button p, button span {{ color: #c5a880 !important; }}
    button:hover {{ background-color: #c5a880 !important; color: #0f172a !important; }}
    button:hover p, button:hover span {{ color: #0f172a !important; }}

    .proposta-header {{ border-left: 5px solid #c5a880; padding-left: 15px; margin-bottom: 25px; }}

    .total-box {{
        background-color: #0f172a; color: #c5a880;
        padding: 20px; border-radius: 8px; text-align: center;
        border: 2px solid #c5a880; margin-top: 20px;
    }}

    .stCheckbox, div[role="checkbox"], .stRadio, div[role="radiogroup"] label, button {{
        cursor: pointer !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 2. Cabeçalho Institucional
try:
    st.image("logo.png", width=320)
except:
    st.markdown("<h3 style='color: #c5a880; margin: 0;'>PROJETTA EDUCAÇÃO & INOVAÇÃO</h3>", unsafe_allow_html=True)

st.markdown(f"""
    <div class="proposta-header" style="margin-top: 15px;">
        <h1 style="margin: 0; padding: 0; font-size: 30px; color: {cor_texto_principal};">Simulador de Escopo & Proposta Comercial</h1>
        <p style="color: #64748b; margin-top: 5px; font-size: 15px;">Monte a solução digital ideal para o seu momento de investimento</p>
    </div>
""", unsafe_allow_html=True)

# Dados do Cliente
st.markdown("### 🏢 Identificação do Projeto")
col_cli1, col_cli2 = st.columns(2)
with col_cli1:
    nome_cliente = st.text_input("Nome do Cliente / Empresa:", placeholder="Ex: Escola TechMinds")
with col_cli2:
    responsavel = st.text_input("Responsável:")

st.markdown("---")
st.markdown("### 🛠️ Personalize os Módulos do seu Projeto")

total_projeto = 0.0
itens_selecionados = []

# --- MÓDULO 1: ESTRUTURA BASE ---
st.markdown("#### 🌐 1. Estrutura e Design Base (Obrigatório)")
with st.container():
    st.markdown(f"""
    <div class="pricing-card">
        <strong style="color: #c5a880; font-size: 16px;">Core Setup + UI/UX Premium (R$ 950,00)</strong><br>
        <span style="font-size: 13px; color: #64748b;">Inclui: Configuração de servidor na Hostinger, Otimização de Performance, SEO Base, Design Responsivo (Celular/Desktop), e Integração flutuante com WhatsApp.</span>
    </div>
    """, unsafe_allow_html=True)
    total_projeto += 950.0
    itens_selecionados.append("Core Setup + UI/UX Premium (R$ 950.00)")

    try:
        st.image("mockup_home.png", caption="Conceito Visual: Estrutura Base Responsiva", use_container_width=True)
    except:
        pass

# --- MÓDULO 2: MAPA DE PÁGINAS ---
st.markdown("#### 📄 2. Páginas Institucionais Adicionais")
col_pag_dados, col_pag_img = st.columns([1.2, 1.0])

with col_pag_dados:
    p_somos = st.checkbox("Página Quem Somos / Institucional (+ R$ 100,00)", key="pag_somos")
    p_serv = st.checkbox("Página de Serviços / Cursos (+ R$ 120,00)", key="pag_serv")
    p_blog = st.checkbox("Blog estruturado para artigos (+ R$ 200,00)", key="pag_blog")
    p_faq = st.checkbox("Central de Perguntas Frequentes (FAQ) (+ R$ 150,00)", key="pag_faq")

    if p_somos: total_projeto += 100.0; itens_selecionados.append("Página Quem Somos (R$ 100.00)")
    if p_serv: total_projeto += 120.0; itens_selecionados.append("Página de Serviços/Cursos (R$ 120.00)")
    if p_blog: total_projeto += 200.0; itens_selecionados.append("Módulo Blog Estruturado (R$ 200.00)")
    if p_faq: total_projeto += 150.0; itens_selecionados.append("Módulo Central de FAQ (R$ 150.00)")

with col_pag_img:
    if p_faq:
        try:
            st.image("mockup_faq.png", caption="Conceito Visual: Central de Ajuda/FAQ", use_container_width=True)
        except:
            pass
    elif p_blog:
        try:
            st.image("mockup_blog.png", caption="Conceito Visual: Blog de Conteúdo", use_container_width=True)
        except:
            pass

# --- MÓDULO 3: E-COMMERCE / LOJA (ESCALONADO) ---
st.markdown("#### 🛍️ 3. Módulo de Loja Virtual (E-commerce)")
ativou_loja = st.checkbox("Ativar Infraestrutura de Loja Virtual", key="loja_infra")

if ativou_loja:
    col_loja_dados, col_loja_img = st.columns([1.2, 1.0])

    with col_loja_dados:
        st.markdown("<div style='padding-left: 10px;'>", unsafe_allow_html=True)
        porte_loja = st.radio(
            "Selecione o volume estimado de produtos iniciais:",
            [
                "Loja Start (Até 20 produtos) - R$ 650,00",
                "Loja Growth (De 21 a 100 produtos) - R$ 950,00",
                "Loja Enterprise (Acima de 100 produtos) - R$ 1.450,00"
            ],
            key="porte_loja"
        )

        if "Start" in porte_loja:
            preco_loja = 650.0
            nome_escopo_loja = "Loja Virtual Start"
        elif "Growth" in porte_loja:
            preco_loja = 950.0
            nome_escopo_loja = "Loja Virtual Growth"
        else:
            preco_loja = 1450.0
            nome_escopo_loja = "Loja Virtual Enterprise"

        total_projeto += preco_loja
        itens_selecionados.append(f"{nome_escopo_loja} (R$ {preco_loja:.2f})")

        st.markdown("---")
        if st.checkbox("Cálculo de Frete Automatizado (+ R$ 200,00)", key="loja_frete"):
            total_projeto += 200.0;
            itens_selecionados.append("Cálculo de Frete Automatizado (R$ 200.00)")
        if st.checkbox("Gateways de Pagamento (PIX, Cartão Automatizado) (+ R$ 250,00)", key="loja_payment"):
            total_projeto += 250.0;
            itens_selecionados.append("Gateways de Pagamento Integrados (R$ 250.00)")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_loja_img:
        try:
            st.image("mockup_loja.png", caption="Conceito Visual: E-commerce Mobile", use_container_width=True)
        except:
            pass

# --- MÓDULO 4: FUNCIONALIDADES AVANÇADAS ---
st.markdown("#### ⚙️ 4. Funcionalidades Extras & Recursos de Marketing")
col_rec_dados, col_rec_img = st.columns([1.2, 1.0])

with col_rec_dados:
    st.markdown("<div style='padding-left: 5px;'>", unsafe_allow_html=True)
    ativou_membros = st.checkbox("Área de Membros / Login de Clientes (+ R$ 300,00)", key="rec_membros")
    if ativou_membros: total_projeto += 300.0; itens_selecionados.append("Área de Membros (R$ 300.00)")

    if st.checkbox("Sistema de Cupons de Desconto e Ofertas (+ R$ 100,00)", key="rec_cupons"):
        total_projeto += 100.0;
        itens_selecionados.append("Sistema de Cupons (R$ 100.00)")

    if st.checkbox("Automação de E-mail Marketing / Captação (+ R$ 450,00)", key="rec_email"):
        total_projeto += 450.0;
        itens_selecionados.append("Automação de E-mail Marketing (R$ 450.00)")

    if st.checkbox("Feed do Instagram dinâmico no rodapé (+ R$ 95,00)", key="rec_insta"):
        total_projeto += 95.0;
        itens_selecionados.append("Feed do Instagram (R$ 95.00)")
    st.markdown("</div>", unsafe_allow_html=True)

with col_rec_img:
    if ativou_membros:
        try:
            st.image("mockup_membros.png", caption="Conceito Visual: Dashboard de Alunos", use_container_width=True)
        except:
            pass

# --- RESUMO FINANCEIRO ---
st.markdown("---")
st.markdown("### 📊 Resumo do Escopo Customizado")

st.markdown(f"""
    <div class="total-box">
        <span style="font-size: 14px; text-transform: uppercase; letter-spacing: 1px; color: #ffffff;">Investimento Total Estimado</span>
        <h2 style="margin: 5px 0 0 0; font-size: 36px; color: #c5a880;">R$ {total_projeto:,.2f}</h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("#### 💳 Condições Especiais de Pagamento sugeridas pela Projetta:")
st.markdown(f"""
*   **À vista no PIX (5% de Desconto):** R$ {total_projeto * 0.95:,.2f}
*   **Parcelamento de Escopo:** Sinal de 50% (R$ {total_projeto * 0.5:,.2f}) + 50% na homologação final.
*   **Cartão de Crédito:** Em até 6x fixas de R$ {total_projeto / 6:,.2f} sem juros.
""")

st.markdown("---")
st.markdown("### 📑 Confirmar e Enviar Escolha")
st.write("Se o escopo acima atende às suas expectativas e planejamento de investimento, clique no botão abaixo.")

if st.button("📝 ENVIAR CONFIGURAÇÃO E SOLICITAR CONTRATO", use_container_width=True):
    if not nome_cliente:
        st.error("Por favor, preencha o campo 'Nome do Cliente / Empresa' na identificação inicial antes de submeter.")
    else:
        try:
            # Conexão com o Google Sheets especificando a nova aba de propostas
            conn = st.connection("gsheets", type=GSheetsConnection)

            # Estrutura os dados para gravação na planilha
            dados_proposta = {
                "Data/Hora Envio": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "Empresa": nome_cliente,
                "Responsavel": responsavel if responsavel else "Não informado",
                "Valor Total": f"R$ {total_projeto:,.2f}",
                "Itens Selecionados": " | ".join(itens_selecionados)
            }

            df_novo = pd.DataFrame([dados_proposta])

            # Alvo explícito: Grava na aba 'Propostas_Simuladas'
            df_existente = conn.read(worksheet="Propostas_Simuladas")
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
            conn.update(worksheet="Propostas_Simuladas", data=df_final)

            st.balloons()
            st.success(
                f"🎉 Perfeito! As preferências de escopo da empresa '{nome_cliente}' foram registradas com sucesso na central de propostas da Projetta.")
        except Exception as e:
            st.error(
                f"Erro ao salvar na planilha. Verifique se a aba 'Propostas_Simuladas' foi criada com os cabeçalhos. Detalhes: {e}")