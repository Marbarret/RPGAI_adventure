# RPG AI Adventure
Este documento detalha a arquitetura, implementação e funcionamento de um RPG AI Adventure, desenvolvido com o objetivo de criar uma experiência de jogo de role-playing game interativa e personalizada, utilizando as tecnologias de Inteligência Artificial (IA) e aprendizado de máquina. O projeto se baseia na plataforma Hugging Face e na linguagem de programação Python.

### Objetivo
O principal objetivo deste projeto é desenvolver um chatbot capaz de:

- Compreender linguagem natural: Processar e interpretar comandos e perguntas do usuário em linguagem natural, simulando uma conversa com um personagem não-jogador (NPC).
- Gerar respostas contextualmente relevantes: Produzir respostas coerentes e contextualmente adequadas, considerando o histórico da conversa e o estado atual do jogo.
- Aprender continuamente: Adaptar-se a diferentes estilos de jogo e preferências do usuário através de um mecanismo de aprendizado contínuo.
- Criar narrativas dinâmicas: Gerar histórias e cenários de forma dinâmica, baseados nas escolhas e ações do usuário.

### Estrutura do Projeto
Estrutura de Pastas e Arquivos
  
```data/```: Contém o dataset (rpg_dataset.json) com os contextos de missões, diálogos e condições.
  
```scripts/```: Contém scripts principais para o treinamento e execução do modelo.
  
```train.py```: Realiza o pré-processamento e treinamento do modelo.
  
```tokenizer.py``` e ```config.py```: Configurações e tokenizações usadas pelo modelo.

```chat_user.py```: Contém a lógica da interface gráfica do usuário, construída usando customtkinter, permitindo interações no chat.

```models/```: Contém o modelo GPT-2 pré-treinado e ajustado para a IA de RPG.

### Interface do Usuário (UI)
A interface foi construída utilizando ```customtkinter``` para oferecer uma experiência visual organizada e funcional.

Componentes da UI:
- ChatBox: Exibe as mensagens trocadas entre o jogador e a IA.
- Entrada de Texto: Permite ao usuário enviar mensagens para a IA.
- Botão de Envio: Envia a mensagem para ser processada.
- Carregar Foto e Exibir Status: Adiciona interatividade e personalização, onde o jogador pode carregar uma foto e ver seu status atual.
- Seleção e Rolagem de Dados: O usuário pode escolher um dado (D4, D6, D8, D10, D12, D20) e realizar uma rolagem, cujo resultado é exibido no chat.

### Tecnologias Utilizadas
- Hugging Face Transformers: Biblioteca de processamento de linguagem natural (NLP) que oferece uma ampla variedade de modelos pré-treinados para tarefas como classificação de texto, geração de texto e compreensão de linguagem natural.
- Python: Linguagem de programação utilizada para implementar a lógica do chatbot, interagir com a biblioteca Hugging Face e outras bibliotecas auxiliares.
- TensorFlow ou PyTorch: Frameworks de deep learning usados ​​para treinar os modelos de linguagem.
- NLTK (Natural Language Toolkit): Biblioteca para processamento de linguagem natural que oferece ferramentas para tokenização, stemming, lematização e outras tarefas de pré-processamento de texto.

### Arquitetura do Sistema
O sistema do chatbot RPG é composto pelos seguintes módulos:

- Interface do usuário: Interface textual ou gráfica que permite ao usuário interagir com o chatbot, inserindo comandos e recebendo respostas.
- Motor de diálogo: Módulo responsável por processar as entradas do usuário, gerar respostas e manter o contexto da conversa.
- Modelo de linguagem: Modelo de linguagem pré-treinado ou fine-tunado para a tarefa específica de geração de texto para RPGs.
- Base de conhecimento: Conjunto de informações sobre o mundo do jogo, personagens, itens e eventos.
- Mecanismo de aprendizado: Módulo responsável por ajustar os parâmetros do modelo de linguagem com base em novas interações com o usuário.

### Funcionamento
- Entrada do usuário: O usuário insere um comando ou pergunta através da interface.
- Pré-processamento: O texto de entrada é pré-processado para remover stop words, realizar stemming ou lematização e converter para um formato adequado para o modelo de linguagem.
- Processamento pelo modelo de linguagem: O texto pré-processado é alimentado ao modelo de linguagem, que gera uma resposta.
- Pós-processamento: A resposta gerada pelo modelo é pós-processada para garantir coerência e fluidez na linguagem.
- Geração da saída: A resposta final é apresentada ao usuário através da interface.
- Aprendizado: O modelo de linguagem é atualizado com base na interação, ajustando seus parâmetros para gerar respostas mais precisas e relevantes no futuro.

### Treinamento do Modelo
O modelo de linguagem é treinado em um grande corpus de texto relacionado a RPGs, como diálogos, descrições de cenários e histórias. O processo de treinamento envolve a otimização dos parâmetros do modelo para minimizar a diferença entre as respostas geradas e as respostas corretas.

### Desafios e Considerações
- Geração de texto coerente e criativo: Garantir que o chatbot gere respostas que sejam não apenas gramaticalmente corretas, mas também criativas e envolventes.
- Manutenção do contexto: Manter o contexto da conversa ao longo de várias interações é fundamental para criar uma experiência de jogo mais realista.
- Escalabilidade: O sistema deve ser capaz de lidar com um grande volume de interações e um mundo de jogo complexo.
- Personalização: Adaptar o comportamento do chatbot às preferências e estilo de jogo de cada usuário.

### Clonagem do Repositório e Instalação de Bibliotecas
1. Clonar o repositório pelo link
   ```
   https://github.com/Marbarret/RPGAI_adventure.git
   ```
2. Recomendado a criação de ambiente virtual
   ```
    python -m venv seu_ambiente
    source venv/bin/activate   # Para Linux/Mac
    .\venv\Scripts\activate    # Para Windows
   ```
3. Instalar as dependências utilizadas no projeto
   ```
   pip install -r requirements.txt
   ```

### Próximos Passos
- Expansão da base de conhecimento: Aumentar a quantidade e a diversidade de informações sobre o mundo do jogo.
- Implementação de diálogos mais complexos: Permitir diálogos mais longos e complexos, com ramificações e múltiplos finais.
- Integração com outras tecnologias: Integrar o chatbot com outras tecnologias, como reconhecimento de voz e realidade virtual.
