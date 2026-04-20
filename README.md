# 🖼️ Image to BMP Converter

Um programa simples em Python para converter imagens `.jpg` e `.png` para o formato `.bmp`.
---
## 🚀 Como funciona

O programa:
1. Pede o nome do arquivo
2. Verifica se o arquivo existe
3. Valida se é uma imagem
4. Converte automaticamente para `.bmp`
---
## 📦 Requisitos
* Python 3
* Biblioteca Pillow

Instale com:

```bash
pip install pillow
```

---

## ▶️ Como usar

1. Execute o script:

```bash
python main.py
```

2. Digite o nome da imagem:

```bash
Digite o nome do seu arquivo: imagem.png
```

3. O arquivo será convertido automaticamente:

```bash
Convertido: imagem.png para imagem.bmp
```

---

## ⚠️ Observações

* Arquivos `.png` com transparência serão convertidos para RGB (sem transparência)
* O arquivo `.bmp` gerado pode ser maior que o original

---

## 📁 Estrutura esperada

```
/projeto
 ├── main.py
 ├── input.png
 └── output.bmp
```

---

## 💡 Exemplo

Entrada:

```
foto.jpg
```

Saída:

```
foto.bmp
```

---

## 📄 Licença

Projeto simples para estudos 🚀
