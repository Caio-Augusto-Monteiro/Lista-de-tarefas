import secrets
import string


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"s", "sim"}:
            return True
        if answer in {"n", "nao", "não"}:
            return False
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def ask_length():
    while True:
        try:
            length = int(
                input("Digite o comprimento desejado da senha (mínimo 8): "))
            if length >= 8:
                return length
            print("O comprimento deve ser pelo menos 8.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def build_charset(include_lower, include_upper, include_digits, include_symbols):
    charset = ""
    groups = []
    if include_lower:
        groups.append(string.ascii_lowercase)
        charset += string.ascii_lowercase
    if include_upper:
        groups.append(string.ascii_uppercase)
        charset += string.ascii_uppercase
    if include_digits:
        groups.append(string.digits)
        charset += string.digits
    if include_symbols:
        groups.append(string.punctuation)
        charset += string.punctuation
    return charset, groups


def generate_password(length, charset, groups):
    if not charset:
        raise ValueError("Nenhum tipo de caractere selecionado para a senha.")

    password_chars = []
    for group in groups:
        password_chars.append(secrets.choice(group))

    remaining = length - len(password_chars)
    password_chars.extend(secrets.choice(charset) for _ in range(remaining))
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("Gerador de senhas")
    print("Responda às opções abaixo para definir as regras da senha.")

    length = ask_length()
    include_lower = ask_yes_no("Incluir letras minúsculas? (s/n): ")
    include_upper = ask_yes_no("Incluir letras maiúsculas? (s/n): ")
    include_digits = ask_yes_no("Incluir números? (s/n): ")
    include_symbols = ask_yes_no("Incluir símbolos especiais? (s/n): ")

    if not any([include_lower, include_upper, include_digits, include_symbols]):
        print("Você deve escolher pelo menos um tipo de caractere.")
        return

    charset, groups = build_charset(
        include_lower,
        include_upper,
        include_digits,
        include_symbols,
    )

    password = generate_password(length, charset, groups)
    print("Sua senha gerada é:", password)


if __name__ == "__main__":
    main()
