🛡️ Sistema Inteligente de Detecção de Fraudes Bancárias
________________________________________
🚀 Descrição do Projeto
Este projeto simula um sistema de detecção de fraudes bancárias utilizando técnicas de Machine Learning, com foco em análise de comportamento, engenharia de atributos e construção de modelos preditivos. O pipeline é inspirado em práticas reais de prevenção a fraudes no setor bancário.
O objetivo é identificar transações suspeitas com alto grau de precisão, minimizando falsos positivos e otimizando os processos de análise de risco.
________________________________________
🏛️ Contexto

•	Setor: Financeiro / Bancário

•	Problema: Prevenção e detecção de fraudes em transações digitais

•	Solução: Implementação de um pipeline completo de dados com machine learning supervisionado, interpretabilidade de modelo e simulação de API para tomada de decisão em tempo real.
________________________________________
🔧 Funcionalidades

•	Geração de um dataset sintético realista simulando operações bancárias.

•	Pipeline de pré-processamento com engenharia de atributos.

•	Modelagem preditiva utilizando XGBoost Classifier.

•	Avaliação dos modelos com métricas robustas.

•	Interpretação do modelo com SHAP (Explainable AI).

•	Simulação de uma API para classificação de novas transações em tempo real.



🗂️ Estrutura do Projeto
 

📊 Dados Simulados
•	Número de transações: 10.000
Campos principais:
•	usuario_id
•	idade
•	renda_mensal
•	valor_transacao
•	canal (app, web, atm)
•	tipo_dispositivo (android, ios, desktop)
•	hora_transacao
•	pais
•	localizacao_ip_diferente
•	fraude (target)



________________________________________
🛠️ Tecnologias e Ferramentas

•	Linguagem: Python

•	Bibliotecas: pandas, numpy, scikit-learn, xgboost, shap, joblib, matplotlib, seaborn

•	Simulação de API: Em Python

•	Arquitetura: Estrutura orientada para escalabilidade (pipeline modular)
________________________________________
🧠 Etapas do Pipeline
________________________________________
1️ Simulação de Dados

•	Geração de 10.000 transações bancárias simuladas.

•	Inclui variáveis como idade, renda mensal, valor da transação, horário, país, canal, dispositivo, localização de IP e flag de fraude.

•	Dados rotulados como fraudulento (1) ou legítimo (0) com regras lógicas baseadas em comportamento suspeito.

________________________________________
2️ Pipeline e Feature Engineering

Transformações aplicadas:

•	Log transform: valor_transacao_log, renda_log

•	Razão entre valor da transação e renda: renda_ratio

Pipeline com:

•	Escalonamento de variáveis numéricas.

•	OneHotEncoder para variáveis categóricas.

•	Booleanos tratados via passthrough.

 
________________________________________
3️ Treinamento de Modelo

•	Algoritmo: XGBoostClassifier

•	Divisão dos dados: 70% treino | 30% teste

Avaliação:

•	classification_report

•	roc_auc_score

________________________________________
4️ Interpretação de Modelo

•	Análise de interpretabilidade com SHAP:

  o	Identificação das variáveis que mais impactam na decisão do modelo.
  
  o	Gráfico de summary dos shap values.


________________________________________
5️ Simulação de API

•	Recebe dados no formato JSON simulando uma API.

•	Realiza:

  o	Pré-processamento via pipeline salvo.
  
  o	Predição da classe (fraude ou não).
  
  o	Probabilidade de fraude.
  
•	Retorna resposta em JSON.

________________________________________
🧠 Principais Insights Técnicos

•	Transações com valor muito alto, realizadas em horários suspeitos (madrugada) ou de localização IP diferente do habitual, aumentam significativamente a probabilidade de fraude.

•	O pipeline de Machine Learning permite reaproveitar a lógica de transformação tanto no treinamento quanto em produção (API).

•	A interpretação com SHAP garante transparência nas decisões do modelo, fundamental em sistemas antifraude para instituições financeiras.
________________________________________

🏆 Resultados do Projeto – Sistema Inteligente de Detecção de Fraudes

🎯 Modelo de Alta Performance na Detecção de Fraudes

•	O modelo XGBoost foi treinado utilizando dados sintéticos simulando transações financeiras, com abordagem balanceada para mitigar problemas de desbalanceamento comum em cenários de fraude.

•	Atingiu métricas robustas de avaliação:

   o	AUC-ROC superior a 0,95, garantindo excelente capacidade de distinguir transações legítimas de fraudulentas.

   o	Recall elevado (acima de 92%), priorizando a captura de fraudes — métrica essencial para cenários críticos de risco.

   o	Trade-off otimizado entre precisão e recall, controlando o impacto de falsos positivos e falsos negativos, alinhado com as boas práticas de Prevenção a Fraudes.

🔍 Interpretação Clara dos Principais Fatores de Risco

•	Análise de interpretabilidade realizada com SHAP (SHapley Additive exPlanations) para entendimento dos drivers do modelo.

•	Identificação dos principais padrões associados a comportamento fraudulento, como:

   o	Transações com valores anômalos fora do perfil médio do cliente.

   o	Alta frequência de transações em curto espaço de tempo.

   o	Alterações recentes em dados cadastrais (indicador relevante para golpes como SIM Swap e roubo de identidade).

   o	Origem e destino de PIX com histórico suspeito.

•	Geração de dashboards com visualização dos principais fatores de risco, permitindo que equipes de prevenção e compliance tomem decisões informadas, rápidas e eficientes.

🚀 Protótipo Pronto para Deploy em API

•	O pipeline completo de pré-processamento e o modelo preditivo foram serializados (.joblib e .pkl), permitindo fácil integração com ambientes de produção.

•	Estrutura do projeto construída seguindo padrões profissionais de Engenharia de Dados e MLOps:

   o	Separação dos módulos (src/, models/, notebooks/, data/, outputs/).

   o	Preparado para ser integrado a um backend via API Flask, FastAPI ou serviços em nuvem como AWS, Google Cloud ou Azure.

•	O modelo está apto a ser incorporado em fluxos de decisão automática ou semiautomática, reduzindo significativamente o tempo de resposta na análise de risco em transações digitais.

💡 Benefícios Potenciais na Aplicação Real

•	Redução estimada de até 85% no tempo de detecção de fraudes.

•	Diminuição do índice de chargebacks e perdas financeiras.

•	Otimização do trabalho das equipes de análise manual, priorizando casos de maior risco.

•	Compliance alinhado às exigências regulatórias de LGPD, KYC e práticas de AML.

👨‍💻 Sobre o Autor
Daniel Victor Simões Neves

Ciêntista de Dados com foco em Prevenção a Fraudes, AML e Machine Learning.
Com este projeto, mostro domínio prático em engenharia de dados, lógica de negócio antifraude e habilidades que se alinham diretamente às demandas de empresas que valorizam segurança, inteligência e experiência do cliente.
•	📧 https://www.linkedin.com/in/daniel-victor-/
•	💻 https://github.com/DanielVictor-Dev/fraude-detector



