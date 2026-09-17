import os
import streamlit as st

st.set_page_config(
    page_title="Alexa Soluções - Central de Vendas",
    page_icon="🌐",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #0b0714; color: #ffffff; }
    .brand-container { text-align: center; padding: 10px 0; }
    .brand-title { font-size: 26px; font-weight: 800; color: #ffffff; letter-spacing: 2px; margin-bottom: 0px; }
    .brand-title span { color: #b057f5; }
    .brand-subtitle { font-size: 12px; color: #d4af37; letter-spacing: 3px; text-transform: uppercase; margin-top: 3px; font-weight: 600; }
    .custom-cta { display: block; background: linear-gradient(135deg, #8a2be2, #4b0082); color: #ffffff; text-align: center; padding: 12px 20px; border-radius: 30px; font-weight: bold; text-decoration: none; box-shadow: 0 4px 15px rgba(138, 43, 226, 0.4); margin: 15px auto; width: 80%; max-width: 300px; }
    div[data-testid="stForm"] { background-color: #130d22; padding: 20px; border-radius: 16px; border: 1px solid #2d1b4e; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5); }
    h3, h4 { color: #d4af37 !important; text-align: center; }
    .stTextInput label, .stSelectbox label { color: #e0d0ff !important; font-weight: 500; }
    </style>
""",
    unsafe_allow_html=True,
)

# Cabeçalho
st.markdown(
    """
    <div class="brand-container">
        <div class="brand-title">ALEXA <span>SOLUÇÕES</span></div>
        <div class="brand-subtitle">Central de Vendas e Atendimento</div>
    </div>
""",
    unsafe_allow_html=True,
)

# Botão WhatsApp
st.markdown(
    '<a href="https://wa.me/5566999536712" target="_blank" class="custom-cta">💬 Fale com a Alexa (66) 99953-6712</a>',
    unsafe_allow_html=True,
)

st.markdown("---")

# Exibição da Foto Real da Alexa e Bloco de Autoridade
col_p1, col_p2, col_p3 = st.columns([1, 2, 1])
with col_p2:
    if os.path.exists("alexa.jpg"):
        st.image(
            "alexa.jpg",
            caption= " Alexa Soluções",
            use_container_width=True,
        )
    else:
        st.info(
            "💡 Dica: Salve sua foto na pasta do projeto com o nome 'alexa.jpg' para ela aparecer aqui automaticamente!"
        )

    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #1f1335, #130d22); padding: 15px; border-radius: 12px; border: 1px solid #d4af37; text-align: center; margin-top: 10px;">
            <p style="color: #d4af37; font-weight: bold; font-size: 15px; margin-bottom: 3px;">Atendimento Exclusivo</p>
            <p style="color: #ffffff; font-size: 12px;">"É conexão, é confiança, é resultado!"</p>
            <p style="color: #b057f5; font-weight: bold; font-size: 13px; margin-top: 5px;">📲 (66) 99953-6712</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# Seleção de Provedores e Planos Personalizados
st.markdown("### **Selecione o Provedor e o Plano Desejado**", unsafe_allow_html=True)

provedor = st.selectbox(
    "Escolha a Operadora / Provedor:",
    [
        "Pedranet - Fibra Óptica",
        "Amigo Internet",
        "Vivo - Planos Residenciais e Móvel",
        "Federal Associados - Sem Fidelidade"
    ]
)

# 1. Pedranet
if "Pedranet" in provedor:
    tipo_plano = st.selectbox(
        "Escolha o Plano da Pedranet (Sem Fidelidade / Sem Consulta):",
        [
            "600 Megas + 60 Canais de TV (R$ 99,90/mês)",
            "700 Megas + 60 Canais de TV (R$ 109,90/mês)",
            "800 Megas + 80 Canais de TV (R$ 129,90/mês)",
            "900 Megas + 80 Canais de TV (R$ 149,90/mês)",
            "1000 Megas + 80 Canais de TV (R$ 199,90/mês)",
            "1000 Megas + Upload + IP Fixo + 80 Canais (R$ 299,90/mês)"
        ]
    )
    plano_escolhido = f"Pedranet - {tipo_plano}"

# 2. Amigo Internet
elif "Amigo Internet" in provedor:
    tipo_plano = st.selectbox(
        "Escolha o Plano da Amigo Internet:",
        [
            "700 Mega + Amigo TV Sky+ (R$ 119,90/mês)",
            "700 Mega + HBO Max (R$ 129,90/mês)",
            "700 Mega + Champions League + HBO Max (R$ 129,90/mês)",
            "600 Mega + TV Box + HBO Max + Disney+ (R$ 144,60/mês)",
            "700 Mega + Rede Mesh (R$ 139,90/mês)",
            "500 Mega (R$ 99,90/mês)",
            "600 Mega + Apps (Deezer, Paramount, TV Sky) (R$ 109,90/mês)",
            "Plano Gamer Pro - 700 Mega + ExitLag + IP Fixo (R$ 169,80/mês)",
            "Plano Gamer Ultra - 1GB + ExitLag + IP Fixo + Mesh (R$ 229,80/mês)",
            "700 Mega + 15GB Móvel (R$ 152,90/mês)",
            "Kit Segurança: 600 Mega + 2 Câm. Internas (R$ 139,80/mês)",
            "Kit Segurança: 600 Mega + 1 Int. e 1 Ext. (R$ 159,70/mês)",
            "Kit Segurança: 600 Mega + 2 Int. e 2 Ext. (R$ 199,70/mês)"
        ]
    )
    plano_escolhido = f"Amigo Internet - {tipo_plano}"

# 3. Vivo
elif "Vivo" in provedor:
    categoria_vivo = st.selectbox(
        "Escolha a Categoria da Vivo:",
        [
            "Planos Controle (Com Fidelidade)",
            "Planos Pós e Família (Com Fidelidade)",
            "Planos Fibra e Outros"
        ]
    )

    if categoria_vivo == "Planos Controle (Com Fidelidade)":
        lista_vivo = [
            "Franquia 10GB + Bônus (R$ 54,90/mês)",
            "Franquia 11GB + Bônus (R$ 64,90/mês)",
            "Franquia 15GB + Bônus (R$ 89,90/mês)"
        ]
    elif categoria_vivo == "Planos Pós e Família (Com Fidelidade)":
        lista_vivo = [
            "Vivo Pós (Franquia + Apps inclusos) - A partir de R$ 150,00/mês",
            "Vivo Família 2 Linhas - R$ 270,00/mês",
            "Vivo Família 3 Linhas - R$ 340,00/mês",
            "Vivo Família 4 Linhas - R$ 430,00/mês",
            "Vivo Família 5 Linhas - R$ 530,00/mês"
        ]
    else:
        lista_vivo = [
            "Vivo Fibra 500 Mega + Apps - A partir de R$ 140,00/mês",
            "Vivo Fibra 700 Mega / 1GB + Apps - A partir de R$ 160,00/mês",
            "Vivo Total Ultra - R$ 100,00/mês (Cidades SPI)"
        ]

    plano_selecionado = st.selectbox("Escolha o Plano da Vivo:", lista_vivo)
    plano_escolhido = f"Vivo - {plano_selecionado}"

# 4. Federal Associados
else:
    operadora_fed = st.selectbox(
        "Selecione a Operadora Federal Associados (Sem Fidelidade):",
        ["Vivo", "Claro", "TIM"]
    )

    if operadora_fed == "Vivo":
        lista_fed = [
            "60 GB (Internet e ligações) - R$ 69,90/mês",
            "100 GB (Internet e ligações) - R$ 99,90/mês",
            "300 GB (Apenas Internet) - R$ 189,90/mês",
            "500 GB (Apenas Internet) - R$ 299,90/mês"
        ]
    elif operadora_fed == "Claro":
        lista_fed = [
            "80 GB (Internet e ligações) - R$ 69,90/mês",
            "160 GB (Internet e ligações) - R$ 99,90/mês"
        ]
    else: # TIM
        lista_fed = [
            "100 GB (Internet e ligações) - R$ 69,90/mês",
            "500 GB (Só Internet) - R$ 189,90/mês"
        ]

    plano_selecionado = st.selectbox("Escolha o Plano Federal:", lista_fed)
    plano_escolhido = f"Federal Associados - {operadora_fed} - {plano_selecionado} (Sem Fidelidade)"

st.markdown("<br>", unsafe_allow_html=True)

# Formulário com digitação 100% livre corrigida
st.markdown("### **Formulário de Cadastro**", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #b8b8b8; font-size: 12px;'>Preencha os campos abaixo livremente.</p>",
    unsafe_allow_html=True,
)

with st.form("form_oficial_alexa"):
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome Completo / Razão Social")
        # Campo de texto livre para CPF/CNPJ sem travar
        cpf_cnpj = st.text_input("CPF ou CNPJ", placeholder="Digite os números")
        data_nascimento = st.text_input("Data de Nascimento", placeholder="DD/MM/AAAA")
        email = st.text_input("E-mail")

    with col2:
        # Campos de texto livres para telefones sem formatação restritiva
        telefone_principal = st.text_input(
            "Telefone Principal (WhatsApp)", placeholder="(66) 99999-9999"
        )
        telefone_recado = st.text_input(
            "Telefone para Recado", placeholder="(66) 99999-9999"
        )
        perfil = st.selectbox("Perfil", ["Residencial", "Empresarial"])
        vencimento = st.selectbox(
            "Vencimento", ["Dia 10", "Dia 5", "Outra data"]
        )

    st.markdown("---")
    st.markdown("#### **Endereço de Instalação**")

    cep = st.text_input("CEP", placeholder="78850-000")
    endereco = st.text_input("Endereço Completo (Rua, Número, Bairro, Cidade)")
    ponto_referencia = st.text_area("Ponto de Referência")

    st.info(
        "⚠️ **Atenção:** Para finalizar a ativação, será necessário o envio de documento com foto (RG/CNH) e selfie."
    )

import os
import pandas as pd
from datetime import datetime

# Cria a pasta para guardar os documentos se ela não existir
os.makedirs("uploads_clientes", exist_ok=True)

st.markdown("---")
st.markdown("### **Documentação Obrigatória para Ativação**")
st.markdown("Envie a foto do seu documento (RG ou CNH) e uma selfie para validação do cadastro:")

arquivo_doc = st.file_uploader("1. Foto do Documento (RG ou CNH)", type=["jpg", "jpeg", "png"])
arquivo_selfie = st.file_uploader("2. Selfie do Cliente (com ou sem o documento)", type=["jpg", "jpeg", "png"])

st.markdown("<br>", unsafe_allow_html=True)

# Botão de Envio Principal
if st.button("Enviar Solicitação para a Central", use_container_width=True):
    # Verifica se preencheu os campos obrigatórios E anexou os arquivos
    if nome and telefone_principal and endereco and arquivo_doc and arquivo_selfie:
        # Pega a data e hora exata do pedido
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Limpa o CPF para usar no nome do arquivo (remove pontos e traços se houver)
        cpf_limpo = ''.join(filter(str.isdigit, str(cpf))) if 'cpf' in locals() and cpf else "cliente"

        # Define os caminhos onde os arquivos serão salvos na pasta do projeto
        doc_path = os.path.join("uploads_clientes", f"{cpf_limpo}_doc_{arquivo_doc.name}")
        selfie_path = os.path.join("uploads_clientes", f"{cpf_limpo}_selfie_{arquivo_selfie.name}")

        # Salva os arquivos de imagem fisicamente na pasta
        with open(doc_path, "wb") as f:
            f.write(arquivo_doc.getbuffer())

        with open(selfie_path, "wb") as f:
            f.write(arquivo_selfie.getbuffer())

        # Organiza os dados para salvar na planilha de histórico
        novo_pedido = {
            "Data/Hora": [data_atual],
            "Nome": [nome],
            "Telefone": [telefone_principal],
            "Endereço": [endereco],
            "Plano Escolhido": [plano_escolhido],
            "Arquivo Doc": [doc_path],
            "Arquivo Selfie": [selfie_path]
        }

        df_pedido = pd.DataFrame(novo_pedido)

        # Grava os dados no arquivo CSV de vendas de forma acumulativa
        arquivo_existe = os.path.exists("historico_vendas.csv")
        df_pedido.to_csv("historico_vendas.csv", mode='a', index=False, header=not arquivo_existe, encoding="utf-8-sig")

        # Mensagens de sucesso na tela
        st.success(f"Perfeito, {nome}! Sua solicitação do plano **{plano_escolhido}** (`{provedor}`) e seus documentos foram enviados com sucesso!")
        st.balloons()
        st.info("A central entrará em contato via WhatsApp para concluir a ativação com base na documentação enviada.")
    else:
        st.error("Atenção: Por favor, preencha todos os campos obrigatórios (Nome, Telefone e Endereço) e **anexe a foto do documento e a selfie** para prosseguir!")

# Rodapé
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #888888; font-size: 11px; padding: 15px;">
        <p style="color: #d4af37; font-weight: bold; font-size: 13px;">É conexão, é confiança, é resultado!</p>
        <p>Instagram: @alexa.solucoes | Central: (66) 99953-6712</p>
        <p>© 2026 Alexa Soluções. Todos os direitos reservados.</p>
    </div>
""",
    unsafe_allow_html=True,
)
