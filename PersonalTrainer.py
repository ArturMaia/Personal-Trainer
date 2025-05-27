import tkinter as tk
from tkinter import messagebox
import random
import datetime

cafe_da_manha = {
    "proteína": ["Ovo Cozido","Ovo Mexido","Leite Integral"],
    "carboidrato": ["Pão francês", "Mingau de aveia", "Cuzcuz","Bolacha gágua e sal","Batata Doce"],
    "fruta": ["Banana", "Tangerina", "Meio mamão","Goiaba"],
    "bebida": ["Café preto","Água com limão","Suco","Leite","Chá"]
}

almoco = {
    "proteína": ["Frango","Fígado","Carne","Porco","Peixe"],
    "carboidrato": ["Arroz branco", "Macarrão com molho", "Feijão com arroz","Farinha","Purê de batata"],
    "legume/vegetal": ["Cenoura", "Chuchu", "Abóbora", "Repolho"],
    "gordura boa": ["Sementes de abóbora", "Azeite","Castanha do Pará"]
}

jantar = {
    "proteína": ["Ovo", "Frango","Sardinha"],
    "carboidrato leve": ["Pão francês", "Tapioca","Purê de batata","Arroz branco","Cuzcuz"],
    "legume": ["Couve refogada", "Alface", "Tomate"],
    "suplemento leve": ["Chá", "Água com limão","Suco"]
}

# Exercícios 
agenda_exercicios = {
    "Segunda": [
        "Ponte de glúteo no chão (3x10)", 
        "Elevação de perna deitado (3x10)", 
        "Alongamento leve de quadríceps e glúteos"
    ],
    "Terça": [
        "Flexão de braço contra a parede (3x10)", 
        "Elevação lateral dos braços sem peso (3x10)", 
        "Alongamento de ombros"
    ],
    "Quarta": [
        "Remada com toalha (3x10)", 
        "Caminhada leve no lugar (5 minutos)", 
        "Movimento de pular corda sem corda (3 minutos)"
    ],
    "Quinta": [
        "Abdominal infra leve (3x10)", 
        "Prancha apoiada nos joelhos (3x15 segundos)", 
        "Elevação de joelhos sentado (3x10)"
    ],
    "Sexta": [
        "Agachamento com apoio na parede (3x8)", 
        "Avanço com apoio (3x6 por perna)", 
        "Stiff leve com garrafas de água (3x10)", 
        "Alongamento de posterior e panturrilha"
    ],
    "Sábado": [
        "Caminhada leve no quarteirão (30 minutos)"
    ],
    "Domingo": []
}

def montar_refeicao(refeicao_dict):
    return [random.choice(v) for v in refeicao_dict.values()]

def roleta_dieta():
    refeicoes = {
        "Café da Manhã": montar_refeicao(cafe_da_manha),
        "Almoço": montar_refeicao(almoco),
        "Jantar": montar_refeicao(jantar)
    }
    texto = "Plano de Refeições:\n\n"
    for nome, itens in refeicoes.items():
        texto += f"{nome}:\n  - " + "\n  - ".join(itens) + "\n\n"
    messagebox.showinfo("Dieta do Dia", texto)

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())
        imc = peso / (altura ** 2)
        if imc < 18.5:
            status = "Abaixo do peso"
        elif imc < 25:
            status = "Peso normal"
        elif imc < 30:
            status = "Sobrepeso"
        else:
            status = "Obesidade"
        resultado = f"IMC: {imc:.1f} - {status}"
        messagebox.showinfo("Resultado IMC", resultado)
    except:
        messagebox.showerror("Erro", "Insira peso e altura válidos.")

def mostrar_treino_dia():
    dia_semana = datetime.datetime.now().strftime("%A")
    traduzido = {
        "Monday": "Segunda",
        "Tuesday": "Terça",
        "Wednesday": "Quarta",
        "Thursday": "Quinta",
        "Friday": "Sexta",
        "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    dia = traduzido.get(dia_semana, "Domingo")
    exercicios = agenda_exercicios.get(dia, [])

    if not exercicios:
        texto = "Hoje é domingo! Dia de descanso."
    else:
        texto = f"Treino para {dia}:\n\n" + "\n".join(f"- {ex}" for ex in exercicios)

    label_status.config(text=texto)

janela = tk.Tk()
janela.title("Corpo e Saúde")
janela.geometry("320x640")

tk.Label(janela, text="Guia de Saúde e Corpo", font=("Helvetica", 14, "bold")).pack(pady=5)

tk.Label(janela, text="Calcular IMC", font=("Helvetica", 10, "bold")).pack()
tk.Label(janela, text="Peso (kg):").pack()
entrada_peso = tk.Entry(janela)
entrada_peso.pack()
tk.Label(janela, text="Altura (m):").pack()
entrada_altura = tk.Entry(janela)
entrada_altura.pack()
tk.Button(janela, text="Calcular IMC", command=calcular_imc, bg="lightblue").pack(pady=5)


tk.Button(janela, text="Sortear Refeições do Dia", command=roleta_dieta, bg="lightgreen").pack(pady=10)

btn_treino = tk.Button(janela, text="Mostrar Treino do Dia", command=mostrar_treino_dia, bg="orange")
btn_treino.pack(pady=10)

label_status = tk.Label(janela, text="", font=("Helvetica", 10), fg="darkgreen", wraplength=300, justify="left")
label_status.pack(pady=10)

tk.Label(janela, text="Beba pelo menos 2L de água por dia!", font=("Helvetica", 10, "bold"), fg="red").pack(pady=10)

janela.mainloop()
