# Jogo da Adivinhação em Python com Interface Gráfica

Este é um script que impletenta um jogo de adivinhação, o sistema sorteia um número e você tem várias tentativas para tentar adivinhar o número sorteado, a quantidade de chances varia de acordo com a dificuldade.

## Pré-requisitos

- Python 3.x
- Biblioteca Tkinter (normalmente incluída na intalação padrão do Python)
- Biblioteca Random (normalmente incluída na instalação padrão do Python)
- Biblioteca `customtkinter` (é necessário instalá-la)

## Como usar

1. Certifique-se de que os pré-requisitos estejam instalados.

2. Clone o repositório ou copie o código-fonte em um arquivo Python (.py).

3. Execute o arquivo Python.

4. O jogo será executado em uma janela gráfica.

5. Insira seu nome no campo de entrado de texto.

6. Escolha o nível de dificuldade no menu suspenso.

7. Clique no botão "Iniciar Jogo" para começar a partida.

8. O programa irá falar para você adivinhar um número entre 1 e 100.

9. Junto também irá mostrar quantas chances você tem, variando de 5 a 15, dependendo da dificuldade escolhida.

10. Digite o número que você deseja chutar para tentar acertar o número secreto no campo de entrada.

11. O jogo terminará com uma mensagem de vitória ou de derrota.

12. Você pode reiniciar o jogo clicando no botão "Iniciar Jogo" novamente.

## Estrutura do código

- O código é estruturado em classes e métodos para melhor compreensão, manutenção e alteração.

- A classe `JogoAdivinhacao` é a principal e contém toda a lógica do jogo e a interface gráfica.

- O jogo usa a função `randint` da biblioteca `random` que sorteia um número inteiro.

- A interface gráfica é criada usando a biblioteca Customtkinter, com elementos como rótulos, campos de entrada e botões.

- O jogo permite que o jogador insira números e fornece feedbacks sobre números que já foram inseridos e caso insira letras ao invés de números.

- O jogo termina quando o jogador acerta o número secreto ou as chances acabam.

## Personalização

Você pode personalizar o jogo alterando a quantidade de chances na função `iniciarJogo` e também mudando o range de números que o computador pode sortear em `self.numeroSecreto` um pouco abaixo da opção anterior. Basta seguir o formato existente.

## Licença

Este código é disponibilizado sob a licença [MIT](https://opensource.org/licenses/MIT), o que significa que você é livre para usá-lo, modificá-lo e distribuí-lo da maneira que desejar, desde que mantenha o aviso de direitos autorais original e não responsabilize os autores por qualquer dano ou perda relacionada ao uso deste código.
