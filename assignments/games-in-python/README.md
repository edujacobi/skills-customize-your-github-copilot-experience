
# 📘 Assignment: Hangman (Forca)

## 🎯 Objetivo

Construa uma versão do jogo da Forca (Hangman) para terminal em Python. O estudante praticará manipulação de strings, estruturas de repetição, condicionais e entrada do usuário.

## 📝 Tarefas

### 🛠️ Hangman Game

#### Description

Implemente um jogo da Forca jogável via linha de comando. O programa deve escolher aleatoriamente uma palavra de uma lista pré-definida, aceitar palpites de letras do jogador, atualizar e mostrar o estado atual da palavra (formato: `_ _ _`), e controlar o número de tentativas restantes até vitória ou derrota.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list in the program.
- Accept single-letter guesses and update the displayed progress in `_ _ _` format.
- Track and display the number of incorrect guesses remaining (e.g., 6 attempts).
- Avoid counting the same incorrect guess multiple times.
- End the game when the word is fully guessed or attempts are exhausted, showing a clear win or lose message.
- Include a short `starter-code.py` file in the same folder to help students get started (see `assignments/games-in-python/starter-code.py`).

#### Example

```
Palavra: _ _ _ _ _
Chute: a
Palavra: a _ _ _ _
Tentativas restantes: 6
```
