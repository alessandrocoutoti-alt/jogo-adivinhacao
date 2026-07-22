# 🎮 Jogo de Adivinhação

Um jogo simples e divertido de adivinhação de números desenvolvido em Python. O computador escolhe um número aleatório entre 1 e 100, e você tem até **10 tentativas** para adivinhar qual é o número secreto!

---

## 🚀 Como Funciona?

1. O jogo escolhe um número secreto entre `1` e `100`.
2. A cada rodada, você digita o seu palpite.
3. O jogo te dá dicas:
   - **"Mais alto!"** se o número secreto for maior que o seu palpite.
   - **"Mais baixo!"** se o número secreto for menor que o seu palpite.
4. O jogo termina quando:
   - Você descobre o número secreto (Parabéns! 🎉).
   - Suas 10 tentativas se esgotam.

---

## 🛠️ Pré-requisitos

Para rodar o jogo, você só precisa ter o **Python 3** instalado em sua máquina.

---

## 💻 Como Rodar o Jogo

1. Abra o terminal ou prompt de comando na pasta do projeto.
2. Execute o seguinte comando:

```bash
python jogo.py
```

3. Divirta-se jogando!

---

## ⚙️ Tecnologias Utilizadas

- **Python 3**
- Biblioteca nativa `random` para geração de números aleatórios.
- Tratamento de exceções com `try/except` para garantir que o jogo não trave caso você digite uma letra ou caractere inválido.