# ✈️ FlightRadar Scraper Automation

Automação web desenvolvida em Python que acessa o site do FlightRadar, identifica aeronaves na tela usando `PyAutoGUI`, coleta informações de voo via `Playwright` e salva capturas de tela automaticamente.

---

## 🚀 Funcionalidades

- Abre o site do FlightRadar automaticamente
- Detecta ícones de aeronaves na tela com `PyAutoGUI`
- Clica nos aviões encontrados
- Coleta dados do voo:
  - Código do voo
  - Aeroporto de partida
  - Aeroporto de chegada
- Captura screenshot do voo selecionado
- Evita duplicação de registros
- Limita a captura a um número definido de aviões

---

## 🧰 Tecnologias utilizadas

- Python 3.10+
- Playwright
- PyAutoGUI
- Time
- OS

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/flightradar-scrapper.git
cd flightradar-scrapper
````

### 2. Crie um ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Instale o Playwright

```bash
playwright install
```

---

## ▶️ Como executar

```bash
python main.py
```

---

## ⚙️ Como funciona

1. O Playwright abre o site do FlightRadar
2. O PyAutoGUI procura os ícones de aeronaves na tela
3. Quando encontra, clica automaticamente
4. O Playwright coleta os dados do painel do voo
5. Uma screenshot do voo é salva na pasta:

```
assets/img/screenshots/
```

---

## 📁 Estrutura do projeto

```
flightradar-scrapper/
│
├── assets/
│   ├── img/
│   │   └── screenshots/
│   └── json/
│       └── auth.json
│
├── main.py
├── shared/
│   └── constants.py
├── requirements.txt
└── README.md
```

---

## ⚠️ Observações

* O reconhecimento de imagem depende da resolução da tela
* Recomenda-se manter o zoom do navegador em 100%
* O desempenho do PyAutoGUI pode variar conforme o sistema
* Evite alterar o layout do site durante a execução

---

## 📌 Melhorias futuras

* Substituir PyAutoGUI por detecção via DOM (Playwright puro)
* Adicionar banco de dados para armazenar voos
* Criar interface gráfica
* Exportar dados em CSV/Excel
* Melhorar detecção de aeronaves

---

## 🧑‍💻 Autor

Desenvolvido para fins de automação e estudo de scraping com Python.

```

