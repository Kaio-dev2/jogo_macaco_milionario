import random
import time

# Taxa de vitória fixa
taxa_de_vitoria = 0.25  # 25% de chance de vitória

def dep_cre(wallet):
    while wallet < 5:
        try:
            deposito = int(input("Quanto deseja depositar? (mínimo 5₢): "))
            if deposito >= 5:
                wallet += deposito
                print(f"✅ Depósito de {deposito}₢ realizado! Saldo atual: {wallet}₢")
            else:
                print("❌ O valor mínimo de depósito é 5₢.")
        except ValueError:
            print("❌ Por favor, insira um número válido.")
    return wallet

def escolher_aposta(wallet):
    while True:
        try:
            aposta = int(input("Quanto deseja apostar por rodada? (mínimo 5₢): "))
            if aposta < 5:
                print("❌ A aposta mínima por rodada é 5₢.")
            elif aposta > wallet:
                print(f"❌ Saldo insuficiente! Você tem {wallet}₢.")
            else:
                return aposta
        except ValueError:
            print("❌ Por favor, insira um número válido.")

def gerar_matriz_controlada(num_rodadas):
    tem_vitoria = random.random() < taxa_de_vitoria
    matriz = []

    for i in range(num_rodadas):
        if tem_vitoria and i == 0:
            num = random.randint(1, 9)
            linha = [num, num, num]
            tem_vitoria = False
        else:
            linha = [random.randint(1, 9) for _ in range(3)]
            while linha[0] == linha[1] == linha[2]:
                linha = [random.randint(1, 9) for _ in range(3)]
        matriz.append(linha)

    return matriz

def verificar_premio(matriz, num_rodadas, vlr_aposta):
    premios_por_rodada = {1: 1.2, 2: 1.3, 3: 1.4}
    multiplicador = premios_por_rodada[num_rodadas]

    vitorias = 0
    for linha in matriz:
        if linha[0] == linha[1] == linha[2]:
            vitorias += 1

    if vitorias > 0:
        premio_base = vitorias * vlr_aposta
        premio_total = int(premio_base * multiplicador)
        print(f"🎉 {vitorias} linha(s) vencedora(s)! Prêmio multiplicado por {multiplicador}x!")
        return premio_total
    else:
        return 0

def mapear_emojis_tematicos(numero):
    mapeamento = [
         "🐅", "💎", "💰", "🍒", "🫎", "🍀", "🔥", "🐴", "🐺"
    ]
    return f"{mapeamento[numero - 1]}"

def interface_animada(matriz):
    print("--- Raspando as rodadas... 🎰 Fortune Scratch ---")
    time.sleep(1)

    for i, linha in enumerate(matriz):
        print(f"🎮 Rodada {i+1}:", end="  ", flush=True)
        time.sleep(0.5)
        for num in linha:
            time.sleep(0.4)
            emoji = mapear_emojis_tematicos(num)
            print(emoji, end=" ")
            time.sleep(0.4)
        print("")
    print("----------------------------------------")
    print("🎉 Raspagem concluída! Boa sorte! 🍀")

def ler_sim_nao(mensagem):
    while True:
        escolha = input(mensagem).strip().lower()
        if escolha in ['s', 'sim']:
            return True
        elif escolha in ['n', 'não', 'nao', 'no']:
            return False
        else:
            print("❌ Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")

def inicio(wallet, custo_temporario):
    print("💰 === Boas-vindas ao 'Macaco Milionário'! === 💰")
    print(f"Saldo atual: {wallet}₢")

    aposta_atual = custo_temporario if custo_temporario else None

    if wallet < 5:
        print("💳 Você precisa de créditos para jogar.")
        wallet = dep_cre(wallet)

    if aposta_atual:
        usar_oferta = input(f"Oferta ativa: apostar por {aposta_atual}₢ nesta rodada? (s/n): ").strip().lower()
        if usar_oferta == 's':
            vlr_aposta = aposta_atual
            print(f"✅ Aposta definida para {vlr_aposta}₢ (oferta especial).")
        else:
            vlr_aposta = escolher_aposta(wallet)
    else:
        vlr_aposta = escolher_aposta(wallet)

    while True:
        try:
            num_rodadas_input = input("Quantas rodadas deseja apostar? (1 a 3): ").strip()
            if not num_rodadas_input.isdigit():
                print("❌ Por favor, insira um número válido.")
                continue
            num_rodadas = int(num_rodadas_input)
            if num_rodadas < 1 or num_rodadas > 3:
                print("❌ Escolha entre 1 e 3 rodadas.")
                continue

            custo_total = num_rodadas * vlr_aposta
            if custo_total > wallet:
                print(f"❌ Saldo insuficiente! Custo: {custo_total}₢ | Saldo: {wallet}₢.")
                if ler_sim_nao("Deseja fazer um depósito? (s/n): "):
                    wallet = dep_cre(wallet)
                    if wallet < custo_total:
                        print("Depósito insuficiente. Tente apostar menos.")
                        continue
                    else:
                        break
                else:
                    continue
            else:
                break

        except ValueError:
            print("❌ Por favor, insira um número válido.")

    wallet -= custo_total
    print(f"🎟️ Apostas realizadas! {num_rodadas} rodada(s). Custo: {custo_total}₢. Saldo restante: {wallet}₢")

    matriz = gerar_matriz_controlada(num_rodadas)
    interface_animada(matriz)

    premio = verificar_premio(matriz, num_rodadas, vlr_aposta)
    if premio > 0:
        wallet += premio
        print(f"💰 Você ganhou {premio}₢! Novo saldo: {wallet}₢")
    else:
        print("❌ Nenhuma linha vencedora. Tente novamente!")

    if custo_temporario and aposta_atual and usar_oferta == 's':
        print(f"➡️ Oferta usada. Aposta voltou ao valor normal a partir da próxima.")
        custo_temporario = None

    return wallet, custo_temporario

if __name__ == "__main__":
    wallet = 0
    custo_temporario = None

    if wallet == 0:
        print("💳 Para começar, faça seu primeiro depósito!")
        wallet = dep_cre(wallet)

    while True:
        wallet, custo_temporario = inicio(wallet, custo_temporario)

        if not ler_sim_nao("Deseja jogar novamente? (s/n): "):
            if ler_sim_nao("Você está desistindo? Que tal tentar por 2₢ na próxima rodada? (s/n):"):
                if wallet >= 2:
                    custo_temporario = 2
                    print("✅ Ótimo! Próxima rodada custará apenas 2₢. Boa sorte! 🍀")
                else:
                    print("❌ Saldo insuficiente. Vamos te ajudar.")
                    wallet = dep_cre(wallet)
                    if wallet >= 2:
                        custo_temporario = 2
                        print("✅ Oferta ativada! Próxima aposta por 2₢.")
                    else:
                        print("➡️ Depósito insuficiente. Tente novamente mais tarde.")
                        print("Obrigado por jogar! Até a próxima! 🐵")
                        break
            else:
                print("Obrigado por jogar! Até a próxima! 🐵")
                break
