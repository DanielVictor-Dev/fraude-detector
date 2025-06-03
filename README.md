🧠 Machine Learning Pipeline para Classificação de Dados Transacionais

🚀 Descrição do Projeto
Este projeto demonstra a construção de um pipeline completo de Machine Learning aplicado à classificação de dados transacionais. Desde a geração de dados sintéticos, passando por pré-processamento, engenharia de atributos, treinamento de modelos, avaliação de performance e até a simulação de deploy via API, o projeto reflete as principais etapas enfrentadas no ciclo de vida de projetos em Ciência de Dados.

O objetivo é apresentar uma abordagem robusta, modular e escalável, capaz de ser aplicada a diversos contextos de negócios que demandam classificação de eventos, tomada de decisão em tempo real e modelos interpretáveis.

🏛️ Contexto e Objetivo
Área de Aplicação: Ciência de Dados / Machine Learning aplicado a negócios.

Cenário Simulado: Classificação de transações digitais (aplicável a setores como finanças, e-commerce, telecom, seguros, entre outros).

Objetivo: Construção de um pipeline end-to-end com foco em boas práticas de:

Engenharia de Dados

Modelagem Supervisionada

Avaliação de Modelos

Interpretabilidade

Simulação de Deploy (API)

🔧 Funcionalidades e Etapas
✔️ Geração de dados sintéticos representando transações digitais.

✔️ Pipeline de pré-processamento de dados (scaling, encoding e feature engineering).

✔️ Construção de variáveis derivadas para potencializar o modelo.

✔️ Modelagem supervisionada utilizando algoritmos de Gradient Boosting.

✔️ Avaliação do modelo com métricas robustas.

✔️ Análise de interpretabilidade utilizando Explainable AI (SHAP).

✔️ Simulação de uma API para consumo do modelo em produção.

🗂️ Estrutura do Projeto
bash
Copiar
Editar
├── data/               # Dados brutos e processados
├── notebooks/          # Notebooks de desenvolvimento
├── models/             # Modelos e pipelines serializados
├── outputs/            # Resultados, gráficos e análises
├── src/                # Código fonte do pipeline
│   ├── data/           # Scripts de geração e transformação de dados
│   ├── features/       # Engenharia de atributos
│   ├── models/         # Treinamento e avaliação de modelos
│   └── api/            # Simulação de API para deploy
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
🛠️ Tecnologias e Ferramentas Utilizadas
Linguagem: Python

Bibliotecas Principais:

Manipulação de dados: pandas, numpy

Modelagem: scikit-learn, xgboost

Interpretabilidade: shap

Visualização: matplotlib, seaborn

Persistência de modelos: joblib

Simulação de API: Python (JSON + pipeline carregado)

Arquitetura: Projeto estruturado em módulos para escalabilidade e boas práticas de Engenharia de Dados e MLOps.

🧠 Pipeline de Machine Learning

1️⃣ Geração de Dados Sintéticos
Simula 10.000 transações digitais com variáveis como:

usuario_id, idade, renda_mensal, valor_transacao, canal (app, web, atm), dispositivo, hora_transacao, pais, localizacao_ip_diferente.

Dados rotulados binariamente (0 e 1) para simular eventos de interesse.

2️⃣ Pré-Processamento e Engenharia de Atributos
Transformações aplicadas:

Log Transform: para variáveis como valor_transacao e renda_mensal.

Feature Ratio: relação entre valor da transação e renda (valor_transacao/renda_mensal).

Pipeline de dados com:

Escalonamento de variáveis numéricas (StandardScaler).

Codificação de variáveis categóricas (OneHotEncoder).

Booleanos tratados como passthrough.

Pipeline construído com ColumnTransformer e Pipeline do scikit-learn garantindo reprodutibilidade.

3️⃣ Modelagem Preditiva
Algoritmo utilizado: XGBoost Classifier (modelo baseado em Gradient Boosting).

Divisão dos dados:

70% treino

30% teste

Avaliação com:

classification_report (precision, recall, f1-score)

roc_auc_score

Curvas ROC e matriz de confusão

4️⃣ Análise de Interpretabilidade
Utilização de SHAP (SHapley Additive exPlanations) para:

Avaliar impacto de cada variável nas decisões do modelo.

Geração de gráficos summary_plot e force_plot para entender o comportamento do modelo.

5️⃣ Simulação de Deploy via API
Pipeline e modelo serializados (.joblib).

API simulada em Python:

Recebe dados no formato JSON.

Executa o pipeline de pré-processamento.

Faz a previsão da classe (0 ou 1) e retorna a probabilidade associada.

Resposta estruturada em JSON.

🔍 Principais Competências Demonstradas
✔️ Manipulação e preparação de dados tabulares.

✔️ Construção de pipelines escaláveis e reutilizáveis.

✔️ Técnicas de engenharia de atributos para aumento de performance.

✔️ Modelagem supervisionada com algoritmos de alta performance.

✔️ Avaliação de modelos com múltiplas métricas.

✔️ Aplicação de técnicas de interpretabilidade (Explainable AI).

✔️ Simulação de deploy de modelo via API, seguindo práticas de MLOps iniciais.

🏆 Resultados Técnicos
Métrica AUC-ROC: Superior a 0,95.

Recall: Acima de 92%.

Modelo balanceado: Trade-off entre precisão e recall otimizado.

Pipeline modular: Reutilizável tanto no treino quanto em produção.

🚀 Próximos Passos / Evoluções Possíveis
Deploy real via Flask, FastAPI ou Streamlit.

Integração com ambientes de nuvem (AWS, Google Cloud, Azure).

Monitoramento de modelos em produção.

Implementação de versionamento de dados e modelos.

👨‍💻 Sobre o Autor
Daniel Victor Simões Neves

Cientista de Dados com foco em construção de pipelines, modelagem supervisionada, interpretação de modelos e deploy de soluções de Machine Learning. Apaixonado por transformar dados em soluções inteligentes e escaláveis.

🔗 LinkedIn

💻 GitHub



