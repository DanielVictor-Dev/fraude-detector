🛡️ Sistema Inteligente de Detecção de Fraudes Bancárias
🚀 Descrição do Projeto
Este projeto simula um sistema de detecção de fraudes bancárias utilizando técnicas de Machine Learning, com foco em análise de comportamento, engenharia de atributos e construção de modelos preditivos. O pipeline é inspirado em práticas reais de prevenção a fraudes no setor bancário.

O objetivo é identificar transações suspeitas com alto grau de precisão, minimizando falsos positivos e otimizando os processos de análise de risco.

🏛️ Contexto
Setor: Financeiro / Bancário

Problema: Prevenção e detecção de fraudes em transações digitais

Solução: Implementação de um pipeline completo de dados com machine learning supervisionado, interpretabilidade de modelo e simulação de API para tomada de decisão em tempo real.

🔧 Funcionalidades
🔹 Geração de um dataset sintético realista simulando operações bancárias
🔹 Pipeline de pré-processamento com engenharia de atributos
🔹 Modelagem preditiva utilizando XGBoost Classifier
🔹 Avaliação dos modelos com métricas robustas
🔹 Interpretação do modelo com SHAP (Explainable AI)
🔹 Simulação de uma API para classificação de novas transações em tempo real

📁 Estrutura do Projeto
bash
Copiar
Editar
📦 detecao-fraudes-bancarias
├── data/                # Dados brutos e processados
│   └── dados_brutos.csv
├── modelos/             # Modelos treinados e pipeline
│   ├── pipeline_preprocess.joblib
│   └── xgb_model.joblib
├── notebooks/           # Notebooks exploratórios (opcional)
├── src/                 # Scripts principais
│   └── pipeline_modelagem.py
├── README.md            # Documentação do projeto
└── requirements.txt     # Dependências do projeto
📊 Dados Simulados
Número de transações: 10.000

Campos principais:
usuario_id
idade
renda_mensal
valor_transacao
canal (app, web, atm)
tipo_dispositivo (android, ios, desktop)
hora_transacao
pais
localizacao_ip_diferente
fraude (target)

🛠️ Tecnologias e Ferramentas
🐍 Python

📦 Bibliotecas:
pandas, numpy
scikit-learn
xgboost
shap
joblib
matplotlib, seaborn

💻 Simulação de API (em Python)

☁️ Estrutura orientada para escalabilidade (pipeline modular)

🧠 Etapas do Pipeline
---

### 1️⃣ Simulação de Dados
- Geração de 10.000 transações bancárias simuladas.
- Inclui variáveis como:
  - idade, renda mensal, valor da transação, horário, país, canal, dispositivo, localização de IP e flag de fraude.
- Dados rotulados como **fraudulento (1)** ou **legítimo (0)** com regras lógicas baseadas em comportamento suspeito.

---

### 2️⃣ Pipeline e Feature Engineering
- Transformações aplicadas:
  - Log transform (`valor_transacao_log`, `renda_log`)
  - Razão entre valor da transação e renda (`renda_ratio`)
- Pipeline com:
  - Escalonamento de variáveis numéricas
  - OneHotEncoder para variáveis categóricas
  - Booleanos tratados via passthrough
- Pipeline salvo como objeto (`pipeline_preprocess.joblib`)

---

### 3️⃣ Treinamento de Modelo
- Algoritmo: **XGBoostClassifier**
- Divisão dos dados: 70% treino | 30% teste
- Avaliação:
  - `classification_report`
  - `roc_auc_score`
- Modelo salvo em: `xgb_model.joblib`

---

### 4️⃣ Interpretação de Modelo
- Análise de interpretabilidade com **SHAP**:
  - Quais variáveis mais impactam na decisão do modelo.
  - Gráfico de summary dos shap values.

---

### 5️⃣ Simulação de API
- Recebe dados no formato JSON simulando uma API.
- Realiza:
  - Pré-processamento via pipeline salvo
  - Predição da classe (fraude ou não)
  - Probabilidade de fraude
- Retorna resposta em JSON:

```json
{
  "fraude": true,
  "probabilidade_fraude": 0.873
}

🧠 Principais Insights Técnicos

🔍 Transações com valor muito alto, realizadas em horários suspeitos (madrugada) ou de localização IP diferente do habitual, aumentam significativamente a probabilidade de fraude.
🔗 O pipeline de Machine Learning permite reaproveitar a lógica de transformação tanto no treinamento quanto em produção (API).
💡 A interpretação com SHAP garante transparência nas decisões do modelo, fundamental em sistemas antifraude para instituições financeiras.

🏆 Resultados

🎯 Modelo treinado com alta performance na detecção de fraudes
🔍 Interpretação clara dos principais fatores de risco
🚀 Pronto para ser integrado como protótipo de API

📌 Exemplo de Resposta da API
json
Copiar
Editar
{
  "fraude": true,
  "probabilidade_fraude": 0.912
}
🚀 Como Executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/detecao-fraudes-bancarias.git
cd detecao-fraudes-bancarias
Crie e ative um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o script principal:

bash
Copiar
Editar
python src/pipeline_modelagem.py

📜 Licença
Este projeto é de código aberto para fins educacionais e demonstração. Sinta-se livre para utilizar, estudar e adaptar, dando os devidos créditos.

💻 Como Executar Localmente
1️⃣ Clone o repositório:
bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2️⃣ Crie um ambiente virtual:
bash
Copiar
Editar
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Instale as dependências:
bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Execute os scripts:
Simular dados e treinar modelo:

bash
Copiar
Editar
python simulacao_pipeline.py
Simular predição via API:

bash
Copiar
Editar
python simulacao_api.py

📜 Licença
Este projeto é de código aberto para fins educacionais e demonstração. Sinta-se livre para utilizar, estudar e adaptar, dando os devidos créditos.

🧠 Autor
Desenvolvido por DANIEL VICTOR SIMÕES NEVES  — Apaixonado por Ciência de Dados, Machine Learning e Prevenção de Fraudes.

🔗 https://www.linkedin.com/in/daniel-victor-/
📧 nevesdatascience@gmail.com


