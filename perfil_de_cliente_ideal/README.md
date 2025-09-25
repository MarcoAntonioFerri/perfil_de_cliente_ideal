# 🎯 Projeto: Perfil de Cliente Ideal
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
## 📖 Descrição
Este projeto tem como objetivo analisar dados de clientes e identificar padrões que ajudem a prever o **perfil de cliente ideal** para campanhas de marketing.  
A ideia é entender quais fatores mais influenciam a aceitação de uma campanha e como podemos usar Machine Learning para apoiar decisões de negócio.  

Este trabalho foi desenvolvido como parte do meu portfólio em Data Science, aplicando **boas práticas de Engenharia de Machine Learning** (estrutura modular, Cookiecutter Data Science, automação com Makefile e logging estruturado).

---

## 📊 Dataset
- Fonte: [Customer Personality Analysis – Kaggle](https://www.kaggle.com/datasets/whenamancodes/customer-personality-analysis/code)  
- Arquivo principal: `marketing_campaign.csv`  
- O dataset contém informações demográficas, educacionais, estado civil, renda e comportamento de compra.  
- Target do modelo: `AcceptedCmp1` (se o cliente aceitou ou não a campanha).  

---

## 📂 Estrutura do Repositório:
```bash
├── LICENSE              # Licença MIT
├── Makefile             # Makefile com comandos convenientes como `make train`
├── README.md            # Intruções de como um desenvolvedor instalar e rodar o projeto.
├── pyproject.toml       # Configurações do projeto 
├── data/
│   ├── processed/       # Dados tratados, pronto para modelagem.
│   └── raw/             # Dataset Original, com dado bruto.
│       └── marketing_campaign.csv
│
├── notebooks/           # Jupyter Notebooks com exploração e protótipo
├── perfil_de_cliente_ideal/
│   ├── dataset.py       # Carregamento e salvamento de dados
│   ├── features.py      # Tratamento e engenharia de features
│   ├── config.py        # Configurações globais do projeto
│   └── modeling/ 
│       └── model.py     # Script de treino e predição
│        
├── reports/             # Resultados e predições
├── run.py               # Orquestrador (treino e predição via CLI)
├── requirements.txt     # Dependências principais
├── requirements-dev.txt # Dependências extras para devs (exploração/notebooks)
└── Makefile             # Automação de tarefas
```
---
## ⚙️ Tecnologias Utilizadas:

- **Linguagem**: Python 3.13.3
- **Análise & ML**: pandas, scikit-learn, imbalanced-learn
- **Visualização**: matplotlib, seaborn
- **Outros**: joblib (serialização), loguru (logging), Makefile (automação), Cookiecutter Data Science (estrutura)

---

## 🚀 Instruções de Instalação:
```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/perfil-de-cliente-ideal.git
cd perfil-de-cliente-ideal

# Crie o ambiente virtual
make create_environment

# Instale dependências principais
make requirements

# Instale dependências de desenvolvimento (opcional)
make requirements_dev
```
---

## 🛠️ Instruções para rodar o projeto:

### Treinar o modelo:
Após o treino, o modelo é salvo no diretório `/models`.
```bash
make train
```
### Treinar o modelo:
É obrigatório "Inputar" um arquivo `.csv` para fazer a predição. Caso não preencha o campo "OUTPUT", será salvo automaticamente em `/reports` com o nome de `predição_dataatual.csv`.
```bash
make predict INPUT=arquivo.csv
make predict INPUT=data/processed/clean_dataset.csv OUTPUT=reports/predictions/minhas_preds.csv
```
---
## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.  
Isso significa que você pode usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do software, desde que mantenha o aviso de copyright e a permissão incluídos.  

Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).

---

## 📬 Contato

- 👤 Autor: **Marco Antônio Ferri**
- 📧 Email: [marco.ferri.profissional@gmail.com](mailto:seuemail@email.com)
- 🔗 LinkedIn: [link_do_linkedin](https://www.linkedin.com/in/link_do_linkedin)