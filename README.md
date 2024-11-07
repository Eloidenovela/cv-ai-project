## Inar-2024

Este projeto é um componente de um **sistema de gestão de recursos humanos**, com foco na **marcação de presenças** dos funcionários utilizando **reconhecimento facial**. A aplicação utiliza **visão computacional**, especificamente a biblioteca **OpenCV**, para realizar a identificação dos funcionários através de suas características faciais.

### Funcionalidade Principal

- **Marcação de Presença**: O sistema permite registrar a presença de funcionários por meio de reconhecimento facial. Quando um funcionário se apresenta à câmera, o sistema utiliza a tecnologia de visão computacional para identificar e registrar sua entrada, evitando a necessidade de sistemas tradicionais como crachás ou senhas.
  
- **Reconhecimento Facial**: Utilizando a biblioteca OpenCV, o sistema captura as imagens faciais, as processa e compara com um banco de dados de imagens previamente cadastradas para realizar a identificação. O processo de reconhecimento é rápido e eficiente, garantindo uma experiência fluída no ponto de entrada.

- **Integração com Sistema de Gestão**: Este componente de marcação de presenças pode ser integrado a um sistema de gestão de recursos humanos mais amplo, possibilitando o acompanhamento de horários, controle de faltas e outras informações relacionadas ao desempenho dos funcionários.

### Tecnologias Utilizadas

- **FastAPI**: Framework moderno para construir APIs rápidas e de alto desempenho.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **OpenCV**: Biblioteca de visão computacional usada para captura, processamento e reconhecimento facial.
- **Python**: Linguagem de programação utilizada para o desenvolvimento da aplicação.
  
### Funcionalidades Esperadas

- **Cadastro de Funcionários**: Funcionários podem ser cadastrados no sistema com suas imagens faciais.
- **Reconhecimento em Tempo Real**: Ao se aproximar da câmera, o sistema automaticamente identifica o funcionário e registra sua presença.
- **Relatórios de Presença**: O sistema gera relatórios com informações sobre as marcações de presença realizadas.

Este componente visa trazer maior precisão, agilidade e segurança no processo de registro de presença dos funcionários, reduzindo erros humanos e aumentando a eficiência no ambiente corporativo.

--- 

### Passos para Clonar um Repositório

1. **Obtenha o link do repositório**:
   - Copie o link de clonagem (`https://github.com/Eloidenovela/cv-ai-project.git`).

2. **Abra o terminal ou prompt de comando**:
   - No Windows, você pode usar o **Prompt de Comando** ou o **PowerShell**.
   - No macOS ou Linux, use o **Terminal**.

3. **Vá até o diretório onde deseja clonar o repositório**:
   Se voce quiser clonar em uma pasta específica, navegue até ela usando o comando `cd` (exemplo: `cd ~/Projetos` no Linux/macOS ou `cd C:\Users\SeuUsuario\Projetos` no Windows).

4. **Clone o repositório**:
   Execute o comando `git clone` seguido do link do repositório:
   ```bash
   git clone `https://github.com/eloidenovela/cv-ai-project.git`.

   ```
   Isso irá baixar todos os arquivos do repositório para o diretório atual.

5. **Acesse o diretório do repositório clonado**:
   Após o clone, entre no diretório do projeto:
   ```bash
   cd repositorio
   ```

---

### Passos para Rodar a API e Instalar Dependências

#### 1. Criação de um Ambiente Virtual

Primeiro, é recomendado criar um ambiente virtual para isolar as dependências do seu projeto. Para isso, siga os passos abaixo:

1. **Crie o ambiente virtual**:
   No terminal, navegue até o diretório do seu projeto e execute:
   ```bash
   python -m venv venv
   ```
   Isso criará uma pasta chamada `venv` dentro do seu projeto, que conterá o ambiente virtual.

2. **Ative o ambiente virtual**:
   - **No Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **No macOS ou Linux**:
     ```bash
     source venv/bin/activate
     ```

   Quando o ambiente virtual estiver ativado, o nome do ambiente (`venv`) aparecerá antes do prompt de comando.

#### 2. Instalar as Dependências

Agora, que o ambiente virtual está ativado, instale as dependências do seu projeto.

1. **Instale as dependências**:
   Se o seu projeto já tiver um arquivo `requirements.txt`, basta executar o seguinte comando para instalar todas as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

#### 3. Rodar o Servidor Uvicorn

Com as dependências instaladas, você pode rodar o servidor para iniciar a API.

1. **Execute a API com Uvicorn**:
   No terminal, ainda com o ambiente virtual ativado, execute o seguinte comando para iniciar o servidor:
   ```bash
   uvicorn main:app --reload
   ```

   - **`main`**: Refere-se ao arquivo Python onde o FastAPI está configurado (por exemplo, `main.py`).
   - **`app`**: Nome da instância do FastAPI dentro do arquivo.
   - **`--reload`**: Faz com que a aplicação seja recarregada automaticamente sempre que houver alterações no código.

   O servidor será iniciado e estará disponível no endereço:
   ```
   http://127.0.0.1:8000
   ```

#### 4. Acessar a Documentação Interativa

Com o servidor rodando, você pode acessar a documentação interativa da API:

- **Swagger UI** (para testar e visualizar os endpoints):
  ```
  http://127.0.0.1:8000/docs
  ```