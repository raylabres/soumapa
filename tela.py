from tkinter import *
from customtkinter import *
import back
import os

back.baixar_imagem() # Baixa as imagens

cor_roxo = '#4B0082'
cor_branco = '#ffffff'
cor_azulclaro = '#1E90FF'
cor_verde = '#42C40A' 
cor_vermelho = '#FF0000'

diretorio = 'C:/soumapa/'

lista_cep = list()
lista_logradouro = list()
lista_bairro = list()
lista_cidade = list()
lista_estado = list()
lista_dados = list()

def mostrar_tela_inicial():
    tela_inicial.place(x=0, y=0, width=800, height=600)
    back.verifica_diretorio()
    back.apaga_arquivos()

    # Aguarda 1 segundo e depois muda para a tela de carregamento
    janela.after(1000, mostrar_tela_carregamento)


def mostrar_tela_carregamento():
    tela_inicial.place_forget()  # Oculta a tela inicial
    tela_carregamento.place(x=0, y=0, width=800, height=600)

    # Aguarda 3 segundos e depois muda para a tela principal
    janela.after(3000, mostrar_tela_menu)


def mostrar_tela_menu():
    tela_carregamento.place_forget()  # Oculta a tela de carregamento
    tela_menu.place(x=0, y=0, width=800, height=600)
    fonte = CTkFont(family="Arial", size=20)
    botao_iniciar = CTkButton(master=tela_menu, text='Iniciar', corner_radius=32, width=200, height=50, font=fonte, fg_color='#414042', hover_color='#000000', command=mostrar_tela_principal)
    botao_iniciar.place(relx=0.5, rely=0.5, anchor='center')

def mostrar_tela_principal():
    def obter_cep():
        remover_labels_existents()

        cep_desejado = caixa_cep.get()
        dados = back.busca_cep(cep_desejado)

        def mensagem_busca(dado):
            if 'erro' in dado:
                sobreponhe_label_exportacao = CTkLabel(master=tela_principal, text='Arquivo exportado com sucesso!', font=fonte_titulo, text_color=cor_branco)
                sobreponhe_label_exportacao.place(x=430, y=450, anchor='center')
                erro_busca = CTkLabel(master=tela_principal, text='Cep não encontrado!', font=fonte_titulo, text_color=cor_vermelho)
                erro_busca.place(x=430, y=450, anchor='center')
            else:
                infomacoes = CTkLabel(master=campo_dados, text='Informações', font=fonte_titulo)
                campo_cep = CTkLabel(master=campo_dados, text=f'CEP:', font=fonte)
                valor_cep = CTkLabel(master=campo_dados, text=f'{dados["cep"]}', font=fonte)
                campo_logradouro = CTkLabel(master=campo_dados, text=f'Logradouro:', font=fonte)
                valor_logradouro = CTkLabel(master=campo_dados, text=f'{dados["logradouro"]}', font=fonte)
                campo_bairro = CTkLabel(master=campo_dados, text=f'Bairro:', font=fonte)
                valor_bairro = CTkLabel(master=campo_dados, text=f'{dados["bairro"]}', font=fonte)
                campo_cidade = CTkLabel(master=campo_dados, text=f'Cidade:', font=fonte)
                valor_cidade = CTkLabel(master=campo_dados, text=f'{dados["localidade"]}', font=fonte)
                campo_estado = CTkLabel(master=campo_dados, text=f'Estado:', font=fonte)
                valor_estado = CTkLabel(master=campo_dados, text=f'{dados["uf"]}', font=fonte)

                infomacoes.grid(row=0, column=0, columnspan=2, pady=10, padx=30, sticky='nswe')
                campo_cep.grid(row=1, column=0, sticky='nswe')  # 'nswe' significa norte, sul, oeste, leste (north, south, west, east)
                valor_cep.grid(row=1, column=1, sticky='nswe')
                campo_logradouro.grid(row=2, column=0, sticky='nswe')
                valor_logradouro.grid(row=2, column=1, sticky='nswe')
                campo_bairro.grid(row=3, column=0, sticky='nswe')
                valor_bairro.grid(row=3, column=1, sticky='nswe')
                campo_cidade.grid(row=4, column=0, sticky='nswe')
                valor_cidade.grid(row=4, column=1, sticky='nswe')
                campo_estado.grid(row=5, column=0, sticky='nswe')
                valor_estado.grid(row=5, column=1, sticky='nswe')
                
                # Configurar o redimensionamento das colunas e linhas para preencher o espaço disponível
                campo_dados.grid_columnconfigure(0, weight=1)
                campo_dados.grid_columnconfigure(1, weight=1)
                campo_dados.grid_rowconfigure(0, weight=0)  # A linha da informação não deve redimensionar verticalmente
                campo_dados.grid_rowconfigure(1, weight=1)
                campo_dados.grid_rowconfigure(2, weight=1)
                campo_dados.grid_rowconfigure(3, weight=1)
                campo_dados.grid_rowconfigure(4, weight=1)
                campo_dados.grid_rowconfigure(5, weight=1)
                
                sobreponhe_label_exportacao = CTkLabel(master=tela_principal, text='Arquivo exportado com sucesso!', font=fonte_titulo, text_color=cor_branco)
                sobreponhe_label_exportacao.place(x=430, y=450, anchor='center')
                sucesso_busca = CTkLabel(master=tela_principal, text='Cep encontrado!', font=fonte_titulo, text_color=cor_verde)
                sucesso_busca.place(x=430, y=450, anchor='center')

                # Adicionando a lista
                lista_cep.append(dados['cep'])
                lista_logradouro.append(dados['logradouro'])
                lista_bairro.append(dados['bairro'])
                lista_cidade.append(dados['localidade'])
                lista_estado.append(dados['uf'])
                lista_dados = [lista_cep, lista_logradouro, lista_bairro, lista_cidade, lista_estado]

                with open(f'{diretorio}/temp/dados.txt', 'w') as arquivo_txt:
                    arquivo_txt.write(str(lista_dados))

        mensagem_busca(dados)

    def mensagem_exportada():
        arquivos = os.listdir(f'{diretorio}/temp/')
        for arquivo in arquivos:
            if 'dados_exportados' in arquivo:
                sucesso_exportacao = CTkLabel(master=tela_principal, text='Arquivo exportado com sucesso!', font=fonte_titulo, text_color=cor_verde)
                sucesso_exportacao.place(x=430, y=450, anchor='center')

    def remover_labels_existents():
        for widget in campo_dados.winfo_children():
            widget.pack_forget()

    tela_menu.place_forget()  # Oculta a tela de carregamento

    tela_principal.place(x=0, y=0, width=800, height=600)
    fonte = CTkFont(family="Arial", size=20)

    fonte_titulo = CTkFont(family="Arial", size=30)
    campo_dados = CTkScrollableFrame(master=tela_principal, scrollbar_button_color=cor_branco, width=500, corner_radius=16, fg_color="#414042", border_color='#000000', border_width=2)
    campo_dados.place(relx=0.5, rely=0.25, anchor='center')
    caixa_cep = CTkEntry(master=tela_principal, placeholder_text='Digite o CEP...', width=300, border_color='#000000')
    caixa_cep.place(relx=0.5, rely=0.5, anchor='center')
    botao_buscar = CTkButton(master=tela_principal, text='Buscar', width=200, height=50, corner_radius=32, font=fonte, fg_color='#414042', hover_color='#000000', bg_color='transparent', command=obter_cep)
    botao_buscar.place(x=170, y=350)
    botao_exportar = CTkButton(master=tela_principal, text='Exportar Excel', width=200, height=50, corner_radius=32, font=fonte, fg_color='#414042', hover_color='#000000', bg_color='transparent', command=lambda: (back.cria_base(), mensagem_exportada()))
    botao_exportar.place(x=430, y=350)


janela = CTk()
janela.iconbitmap(f'{diretorio}templates/icone.ico')
janela.title('Soumapa')
janela.geometry('800x600')
janela.resizable(width=False, height=False)

# Tela inicial
tela_inicial = Frame(janela, bg=cor_branco)


# Tela de carregamento
tela_carregamento = Frame(janela, bg=cor_branco)

# Carregar a imagem
imagem_carregamento = PhotoImage(file=f"{diretorio}templates/carregando.png")

# Criar um Canvas para a imagem
canvas_carregamento = Canvas(tela_carregamento, width=imagem_carregamento.width(), height=imagem_carregamento.height())
canvas_carregamento.pack()

# Adicionar a imagem ao Canvas
canvas_carregamento.create_image(0, 0, anchor=NW, image=imagem_carregamento)

# Tela de menu
tela_menu = Frame(janela, bg=cor_branco)
# Carregar a imagem
imagem_menu = PhotoImage(file=f"{diretorio}templates/menu.png")

# Criar um Canvas para a imagem
canvas_menu = Canvas(tela_menu, width=imagem_menu.width(), height=imagem_menu.height())
canvas_menu.pack()

# Adicionar a imagem ao Canvas
canvas_menu.create_image(0, 0, anchor=NW, image=imagem_menu)

# Tela principal
tela_principal = Frame(janela, bg=cor_branco)

# Carregar a imagem
imagem_principal = PhotoImage(file=f"{diretorio}templates/fundo_branco.png")

# Criar um Canvas para a imagem
canvas_principal = Canvas(tela_principal, width=imagem_principal.width(), height=imagem_principal.height())
canvas_principal.pack()

# Adicionar a imagem ao Canvas
canvas_principal.create_image(0, 0, anchor=NW, image=imagem_principal)

# Inicialmente, mostra a tela inicial
mostrar_tela_inicial()

janela.mainloop()