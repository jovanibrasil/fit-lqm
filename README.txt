################## Instruções Básicas ###################

# Informações Gerais

		É necessária a instação dos módulos scypy e PIL para o devido
		funcionamento da aplicação.

		Os resultados gerados por mim foram organizados em pastas. Dentro
		de cada pasta estão arquivos com coeficientes e as respectivas
		imagens. Diretórios: 
	
			/adam-results
			/c3po-results
			/monalisa-results
	
		Existem 3 módulos:

			FitLqm.py - Aplica o método de ajuste.
				Entrada: Uma imagem PGM.
				Saída: Um arquivo de coeficientes.

				Observações: O nome do arquivo gerado é:

					nome_extensão_da_imagem + 
					_quantidade_de_níveis + 
					_data.txt
						
					Cada linha do arquivo é uma lista de coeficientes de um
					polinônimo da imagem.					 

			Viz.py - Visualização da imagem aproximada.
				Entrada: Arquivo de coeficientes.
				Saída: Apresenta imagem aproximada e imagem original na tela.
			
				Observações: A imagem original deve estar no mesmo diretório
				do módulo. É possível salvar a imagem aproximada, pasta incluir
				o parâmetro s no final da chamada do módulo.
		
			ConvertoToPGM.py - Converte uma imagem qualquer para PGM.		
				Entrada: Uma imagem quer.
				Saída: Uma imagem PGM.

		O trabalho foi feito no linux. Não posso garantir funcionamento do mesmo em
		outros sistemas.	
	
# Executando o módulo para ajuste de função #

		python FitLqm.py nome_da_imagem.pgm níveis_de_divisões

		Exemplo:

		python FitLqm.py mona.pgm 4

# Executando o módulo de visualização #
	
	# Sem salvar a imagem gerada. 

		python Viz.py nome_do_arquivo_de_coeficientes

		Exemplo:

		python Viz.py mona-pgm_4_data.txt
    
	# Salvando a imagem gerada

		python Viz.py nome_do_arquivo_de_coeficientes s

		Exemplo:

		python Viz.py mona-pgm_4_data.txt s


	# BUG: Dependendo do software default para visualização
	de imagens do sistema a imagem original e aproximadas podem
	não ficar lado a lado. Porém como são janelas separadas,
	basta selecionar uma deles e ajustar a posição.


	
