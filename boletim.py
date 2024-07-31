import streamlit as st 
import utils_vertex as vertex
from fpdf import FPDF

st.header("Gerar boletim")

x = st.button(label="Gerar")

prompt = """
gere um boletim escolar com o seguinte formato e crie dados ficticios para exemplificar um aluno em especifico. preencha todos os campos . 

Dados do Aluno:

Nome Completo: [Nome do Aluno]
Número de Matrícula: [Número da Matrícula]
Série/Ano: 8ª Série (9º Ano)
Turma: [Turma do Aluno]
Escola: [Nome da Escola]
Ano Letivo: 2024
Disciplinas e Notas:
Disciplina1º Bimestre2º Bimestre3º Bimestre4º BimestreMédia FinalResultado FinalPortuguêsMatemáticaCiênciasHistóriaGeografiaInglêsArteEducação Física[Disciplina Eletiva]
Export to Sheets
Frequência:

Total de Faltas:
Observações do Professor:
[Espaço para comentários sobre o desempenho, comportamento e participação do aluno]
Assinaturas:

Professor(a):
Responsável:
Instruções:

Preencha os campos entre colchetes com as informações correspondentes.
Insira as notas de cada bimestre nas respectivas colunas.
Calcule a média final de cada disciplina e preencha a coluna "Média Final".
Indique o resultado final (Aprovado, Reprovado, Recuperação) na coluna "Resultado Final".
Preencha o total de faltas.
Adicione as observações do professor no espaço designado.
Inclua a assinatura do professor e do responsável.


"""

def gerar_pdf(texto):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, texto)
    pdf.output("boletim.pdf")  

if x: 
    texto_boletim = vertex.sendPrompt(prompt, vertex.model_gemini_pro)
    st.write(texto_boletim)
    gerar_pdf(texto_boletim)
    with open("boletim.pdf", "rb") as pdf_file:
        st.download_button(
            label="Baixar Boletim",
            data=pdf_file,
            file_name="boletim.pdf",
            mime="application/pdf",
        )
