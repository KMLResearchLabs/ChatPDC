def quebrar_em_linhas(texto, palavras_por_linha):
    import re
    texto = re.sub(r"\s+", " ", texto.strip())
    palavras = texto.split(" ")

    linhas = []
    for i in range(0, len(palavras), palavras_por_linha):
        linhas.append(" ".join(palavras[i:i + palavras_por_linha]))

    return "\n".join(linhas)


def PDC_Bot(pergunta, prompt):
    import random
    from groq import Groq
    import os
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    frases = [
    "To comendo sofa",
    "Come sofa",
    "Coem ofsa",
    "Safo moec",
    "Cmoe faos",
    "Bora?",
    "Tem que ir pra Russia",
    "Como minera Bitcoin no celular?"
]

    chance = 5  # %

    if random.uniform(0, 100) < chance:
        print(f"\nKoC > {random.choice(frases)}")

    else:
        client = Groq(api_key=api_key)

        try:
            resposta = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": prompt
                    },
                    {
                        "role": "user",
                        "content": pergunta
                    }
                ]
            )

            if resposta.choices and resposta.choices[0].message:
                conteudo = resposta.choices[0].message.content.strip()
                conteudo = quebrar_em_linhas(conteudo, palavras_por_linha=17)
            else:
                conteudo = "Manoel Gomes não quis compartilhar seu conhecimento hoje."

            print(f"\nChatPDC > {conteudo}")

        except Exception as e:
            print(f"\nChatPDC > Alguém fez porpetagem KKKKK: {e}")

