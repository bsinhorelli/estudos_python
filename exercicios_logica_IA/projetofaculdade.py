import os

def limpar_tela():
    """Limpa o terminal para manter a organização visual."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_nota_valida(bimestre):
    """Garante que o usuário digite um número válido entre 0 e 10."""
    while True:
        try:
            nota = float(input(f"  > Nota do {bimestre}º Bimestre: "))
            if 0 <= nota <= 10:
                return nota
            print("    ⚠️  A nota deve ser entre 0 e 10. Tente novamente.")
        except ValueError:
            print("    ❌ Erro: Digite apenas números (use ponto em vez de vírgula).")

def exibir_cabecalho():
    print("=" * 40)
    print(f"{'BOLETIM ESCOLAR':^40}")
    print("=" * 40)

def main():
    limpar_tela() 
    exibir_cabecalho()
    
    nome_aluno = input("\nNome do Aluno: ").strip()
    notas = []

    print(f"\nDigite as notas de {nome_aluno}:")
    for i in range(1, 5):
        nota = obter_nota_valida(i)
        notas.append(nota)

    media = sum(notas) / len(notas)
    situacao = "APROVADO(A) ✅" if media >= 6.0 else "REPROVADO(A) ❌"

    
    print("\n" + "-" * 40)
    print(f"ALUNO: {nome_aluno.upper()}")
    print(f"MÉDIA FINAL: {media:.1f}")
    print(f"STATUS: {situacao}")
    print("-" * 40)

    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()