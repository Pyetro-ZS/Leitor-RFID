# 📡 RFID Attendance System  

## 🧩 Sobre o projeto  
Este sistema lê um **dispositivo de teclado HID (RFID)** e envia automaticamente os dados capturados para um **banco de dados** assim que o computador é ligado.  

O programa é iniciado de forma **automática** através do **Agendador de Tarefas do Google (Google Task Scheduler)**, garantindo funcionamento contínuo e **sem interferir na digitação do usuário**.  

O objetivo principal é permitir a **chamada automática de alunos** por meio do **leitor RFID**, tornando o processo de presença mais rápido, preciso e moderno.  

---

## ⚙️ Funcionalidades  
- 📲 Leitura automática de **dispositivo HID (RFID)**  
- 💾 Envio dos dados para um **banco de dados remoto ou local**  
- 🔁 Inicialização automática ao ligar o computador (via Google Task Scheduler)  
- 🧠 Execução em segundo plano, **sem interferir na digitação**  
- 🧾 Registro automático da presença de alunos  

---

## 🏗️ Tecnologias utilizadas  
- **Linguagem:** Python
- **Banco de dados:** MySQL, SQLite ou PostgreSQL 
- **Integração:** Google Task Scheduler  
- **Hardware:** Leitor RFID com interface HID  

---

## 🚀 Como funciona  
1. O programa é executado automaticamente na inicialização do sistema.  
2. Quando um cartão RFID é aproximado, o leitor envia o código como se fosse uma entrada de teclado.  
3. O sistema captura essa entrada, identifica o código RFID e envia para o banco de dados.  
4. O registro é vinculado ao aluno correspondente, marcando sua presença automaticamente.  

---
