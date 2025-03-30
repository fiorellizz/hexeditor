# Editor Hexadecimal para Oficinas 🚗🔧

Este projeto é um **editor hexadecimal de arquivos binários**, desenvolvido em **Django**, voltado para oficinas que precisam visualizar e editar bytes de arquivos.

## 📌 Funcionalidades
- **Upload de Arquivos**: Permite o envio de arquivos binários para edição.
- **Visualização Hexadecimal**: Exibe os bytes do arquivo em formato hexadecimal e ASCII.
- **Edição de Bytes Específicos**: Permite modificar bytes individuais do arquivo.
- **Edição de Endereços Específicos**: Possibilita a alteração de valores diretamente em endereços hexadecimais.
- **Download do Arquivo Editado**: Permite baixar o arquivo após as edições.

---

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Django** (Backend Web Framework)
- **HTML, CSS e Bootstrap** (Frontend)

---

## 📜 Instalação e Configuração
### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/fiorellizz/hexeditor.git
cd hexeditor
```

### 2️⃣ Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Execute as Migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Inicie o Servidor
```bash
python manage.py runserver
```

Acesse o sistema no navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎨 Estilização
Os arquivos CSS estão em desenvolvimento e podem ser encontrados no `static/editor/css/style.css`.

---

## 🔧 Melhorias Futuras
- 🔹 Suporte para múltiplos arquivos.
- 🔹 Implementação de usuários e autenticação.
- 🔹 Melhorias na interface gráfica.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
