# Macaco Milionário 🎰🐵

Jogo simples de aposta estilo “raspadinha” em Python, onde o jogador deposita créditos, escolhe quantas rodadas quer jogar, e aposta para tentar ganhar prêmios multiplicados.

---

## Sobre o jogo

- O jogador começa com saldo zero e precisa fazer um depósito mínimo para jogar.
- Pode apostar de 1 a 3 rodadas por vez, escolhendo o valor da aposta (mínimo 5₢).
- Cada rodada gera uma linha com três números aleatórios.
- O sistema controla a chance de vitória (~30%) para garantir que haja pelo menos uma linha vencedora em algumas rodadas.
- Se a linha tiver três números iguais, o jogador ganha um prêmio com multiplicador baseado na quantidade de rodadas.
- O jogador pode aceitar uma oferta especial para apostar por 2₢ caso queira continuar após desistir.

---

## Funcionalidades principais

- **Controle de saldo (`wallet`) sem variáveis globais:** o saldo é passado entre funções como parâmetro e atualizado de forma explícita.
- **Oferta especial de aposta (`custo_temporario`):** valor temporário para aposta com desconto, também controlado sem variáveis globais.
- Animação simples simulando o ato de "raspar" as linhas.
- Entrada segura e validação para valores e respostas do usuário.

---
![Fluxograma](https://github.com/Kaio-dev2/jogo_macaco_milionario/blob/main/Fluxograma.png)

Grupo: Kaio Richard, Hariel Mohamed, Vitor Lucindo.

## Como usar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/macaco-milionario.git
cd macaco-milionario
Execute o jogo:

Siga as instruções na tela:

Faça seu depósito inicial (mínimo 5₢).

Escolha o valor da aposta por rodada (mínimo 5₢).

Escolha quantas rodadas deseja apostar (1 a 3).

Veja o resultado da rodada e, se ganhar, seu saldo será atualizado.

Decida se quer jogar novamente ou aceitar uma oferta especial.

Estrutura do código
dep_cre(wallet)
Recebe o saldo atual (wallet) e permite que o jogador faça depósitos até ter pelo menos 5₢.

Retorna o saldo atualizado.

escolher_aposta(wallet)
Permite o jogador escolher o valor da aposta, validando o mínimo e se há saldo suficiente.

Retorna o valor da aposta escolhido.

gerar_matriz_controlada(num_rodadas)
Gera uma matriz (lista de listas) com os números de cada rodada.

Controla a chance de vitória para ter pelo menos uma linha vencedora (três números iguais) em cerca de 30% das vezes.

interface_animada(matriz)
Exibe uma animação simulando o ato de "raspar" os números em cada rodada.

verificar_premio(matriz, num_rodadas, vlr_aposta)
Verifica quantas linhas vencedoras existem e calcula o prêmio final com base no multiplicador.

Retorna o valor do prêmio (0 se não houver vitória).

ler_sim_nao(mensagem)
Lê respostas do usuário para perguntas sim/não, aceitando variações (ex: "s", "sim", "n", "não").

inicio(wallet, custo_temporario)
Função principal que gerencia uma rodada completa.

Recebe o saldo atual e o custo temporário da oferta.

Gerencia depósitos, escolha de aposta, número de rodadas, desconta o custo, gera resultados, calcula prêmio e atualiza saldo.

Retorna o saldo e a oferta atualizados.

Boas práticas:
Sem variáveis globais: O estado do jogo (wallet e custo_temporario) é passado explicitamente entre funções, melhorando modularidade e facilitando testes.

Validação: O jogo trata entradas inválidas para evitar erros e garantir boa experiência do usuário.

Mensagens interativas: O usuário é guiado passo a passo e informado do saldo, apostas, resultados e opções.
Transformar o código em uma classe para encapsular estado e comportamentos.

Criar interface gráfica para melhorar experiência visual.

Adicionar suporte a múltiplos jogadores ou modo online.

Implementar sistema de histórico e estatísticas.

![Fluxograma](https://github.com/Kaio-dev2/jogo_macaco_milionario/blob/main/Fluxograma.png)
