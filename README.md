# Prototipo
### Código e Vídeo Demonstrativo do Protótipo construído em aula

## Vídeo

[Link do Vídeo - Salvo no Drive](https://drive.google.com/file/d/1lhhnx3zMxAkAlVme-dePC1AkiypwPwvb/view?usp=drive_link)

### Descrição do Código

O código foi produzido em Python 3.0, instalando bibliotecas, como: `custmomtkinter`, `time` e `threading`.

#### Biblioteca:

- `customtkinter`: Utilizado para criar a janela e elementos do nosso código.
- `time`: Utilizado para a função do timer.
- `threading`: Utilizado para realizar funções assíncronas.

#### O código foi divido nas seguintes partes:

- Configuração: Define algumas opções de aparência e a abertura da janela.

- Funções: É a parte onde estarão o backend da nossa janela, são os comandos que podem ser executados ao utilizar de objetos dos ELEMENTOS.

- Elementos: Parte visual da janela, onde o CTk mais age. Os seguintes elementos estão presentes: Label (texto), Button (botão) e Entry (entrada).

- Iniciar: Código de inicialização.

### Funcionamento do Código

#### O código sempre abrirá nessa primeira janela.

![image](https://github.com/user-attachments/assets/e4a64c19-9aec-45c2-b6d1-b7d4f9fcf401)

Os botões, "Tarefas", "Horário" e "Terminal", são apenas absratos, para representar a área de trabalho do usuário.

#### O botão "DARKNESS", ao ser pressionado, executará um código que leva o usuário para a nossa tela de economia de energia, chamada: "BlackOut".

![image](https://github.com/user-attachments/assets/5c687fe1-e80b-4aa9-8488-12d3394fdee8)

#### Clicando em "VOLTAR", votará à área de trabalho.

![image](https://github.com/user-attachments/assets/e4a64c19-9aec-45c2-b6d1-b7d4f9fcf401)

#### O botão "CONFIGURAÇÕES", ao ser pressionado, executará um outro código que leva o usuário, ao Timer, onde pode ser definido um tempo.
#### Na caixa pode ser definido um tempo em minutos, digitando algum número da preferência do usuário; após digitar, pressionando em "Definir Timer", o tempo desejado já estará correndo.

![image](https://github.com/user-attachments/assets/c8ab65b2-a436-4efe-8122-9abc618dd16d)

Obs: Se caso, haja alguma atividade para usuário fazer nesse meio tempo, ele poderá executar sem problemas até o tempo acabar.

#### Ao término do tempo, a aplicação irá jogar o usuário de volta a tela de economia de energia, "BlackOut".

![image](https://github.com/user-attachments/assets/5c687fe1-e80b-4aa9-8488-12d3394fdee8)
