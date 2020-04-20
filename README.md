# CovidCombate

## Objetivos
A ideia central é servir como um ambiente em que a Prefeitura, em conjunto com as respectivas entidades de saúde podem montar uma base de informações sólidas e em tempo real, em que é possível além de armazenar as mesmas, fazer o processamento de dados e obter arquivos para análises mais complexas.

#### [Clique para acessar o projeto](https://covidcombate.com.br)

## Como funciona ?
É possível concluir o cadastro na ferramenta de duas formas distintas:
* Criando uma nova base de dados como administrador
* Utilizando o código de colaboração de uma base já existente

Criando uma nova base como administrador, é possível:
* Inserir novos dados
* Editar/Excluir qualquer dado colocado por você ou qualquer colaborador
* Processar os dados
* Gerar arquivos .csv e .shp da base de dados
* Visualizar todas as informações da base de dados

Por fim, quem finalize o cadastro utilizando um código de colaboração poderá:
* Inserir novos dados para a base de colaboração
* Editar/Excluir apenas os dados colocados por ele mesmo

O processamento dos dados é possível devido a API Geocoding da Google, além de posteriores análises de resultado para mitigar possíveis incongruências. Este processamento transforma endereços em coordenadas e após isso é possível gerar um arquivo Shapefile.

A partir destas coordenadas podemos mapear os doentes e fazer análises com filtros diversos em Softwares como [QGis](https://qgis.org/en/site/) além disso é possível verificar a concentração de doentes numa determinada área de modo a tomar ações mais efetivas e direcionadas.

#### ATENÇÃO: A aplicação gera coordenadas com base na API da Google, com base em testes já foi verificado que certos resultados, principalmente em regiões mais remotas podem apresentar erros.

| rua                 | numero_casa  |cidade       |cep|latitude       |longitude      |
| ------------------- | ------------ |------------ | ----|---------------|---------------|
|  Rua Barreto Leme   |  35          | Campinas    | 13010200 |Gerado no Processamento|Gerado no Processamento|

## Imagens

###### Página de Login
![login](https://user-images.githubusercontent.com/56345369/79779697-b1094680-8332-11ea-8ac0-eccd7825d243.png)

###### Inserção/Edição/Remoção de dados
![dados](https://user-images.githubusercontent.com/56345369/79779800-db5b0400-8332-11ea-8b61-8af429bad88a.png)

###### Ferramenta de processamento de dados
![processamento](https://user-images.githubusercontent.com/56345369/79779862-f7f73c00-8332-11ea-90a4-3cde93483106.png)

###### Gestão de colaboradores
![colab](https://user-images.githubusercontent.com/56345369/79780938-9d5edf80-8334-11ea-8926-df7dbe2d5ce3.png)

###### Visualização das entradas de forma espacializada
![mapa com shapefile gerado](https://user-images.githubusercontent.com/56345369/79780022-342a9c80-8333-11ea-9c47-67bc4f33702e.png)

## Limitações

No momento a ferramenta já se encontra funcional, porém com algumas limitações:

  * Em localizações mais remotas como cidades pequenas o resultado gerado não se provou satisfatório.
  
  * Ainda existem pequenos problemas a serem corrigidos para lidar com todas as possíveis exceções que um usuário pode gerar
 
  * Ainda não foi feita uma versão mobile.

# CovidCombate - FERRAMENTA ANTERIOR (DESATUALIZADO)

O uso recomendado seria que entidades responsáveis por cidades (Prefeituras, etc) criassem uma planilha e a configurassem, fornecendo a chave específica para centros de saúde, hospitais entre outros que pudessem atualizar a base com novas entradas de doentes.
Ao processar os dados o campo da planilha de rua, número da casa e cidade são utilizadas junto ao [API Geocoding da Google](https://developers.google.com/maps/documentation/geocoding/intro) para gerar coordenadas. (Um endereço é transformado em latitude e longitude e então a planilha é atualizada em tempo real e os arquivos gerados). 

A partir destas coordenadas podemos mapear os doentes e fazer análises com filtros diversos em Softwares como [QuantumGis](https://qgis.org/en/site/) além disso é possível verificar a concentração de doentes numa determinada área de modo a tomar ações mais efetivas e direcionadas.

#### ATENÇÃO: A aplicação gera coordenadas com base na API da Google, com base em testes já foi verificado que certos resultados, principalmente em regiões mais remotas não possuem tanta eficiência.

| rua                 | numero_casa  |cidade       |cep|latitude       |longitude      |
| ------------------- | ------------ |------------ | ----|---------------|---------------|
|  Rua Barreto Leme   |  35          | Campinas    | 13010200 |Gerado no Processamento|Gerado no Processamento|

Para a geração das coordenadas, estas quatro colunas contém as informações necessárias. O resto das colunas e as que possam ser adicionadas pelos usuários são para outras avaliações que podem ser interessantes também. É possível fazer o download de  uma tabela base [aqui](https://covidcombate.com.br/escolhaprocessamento.html), novas colunas podem ser adicionadas de acordo com a necessidade.

## Como funciona ?
Pode ser utilizada uma planilha específica na nuvem (plataforma Google Sheets) em que é possível realizar a inserção de dados pelo [formulário web](https://covidcombate.com.br/avisoFormulario.html) utilizado a chave da base de dados para identificar a planilha correta. Esta ferramenta possibilita grande escalabilidade após criar e configurar a planilha, pois qualquer entidade responsável pode enviar dados diretamente para a planilha apenas com a chave, sem maiores complicações. Entretanto, o armazenamento de dados na nuvem pode não ser da vontade dos órgãos públicos.

Devido isso é possível utiizar planilhas locais para atualização local, sem armazenamento na nuvem. Desta forma a inserção de novos dados fica a critério dos órgãos responsáveis. 

Em ambos os casos existem respectivas [aplicações WEB](https://covidcombate.com.br/escolhaprocessamento.html) que processam os arquivos.

* Ao processar arquivos na nuvem (Google Sheets) os dados são atualizados em tempo real na planilha online e os arquivos shapefile gerados para download.

* Ao processar arquivos localmente além do shapefile também é devolvida uma nova planilha com os dados atualizados.

## Imagens

###### Aplicação para processamento de dados na nuvem
![Captura de ecrã 2020-04-04, às 19 57 00](https://user-images.githubusercontent.com/56345369/78459084-78b90580-76ae-11ea-9d59-d2b22d0a363b.png)

###### Aplicação para processamento de dados locais
![Captura de ecrã 2020-04-04, às 19 58 25](https://user-images.githubusercontent.com/56345369/78459115-ac942b00-76ae-11ea-8c8c-36e32d202aae.png)

###### Dados dispostos no software QuantumGis utilizando sinalizações diferentes para o estado da doença: Em análise, positivo e negativo
![IMG_2509](https://user-images.githubusercontent.com/56345369/78459169-17ddfd00-76af-11ea-93c2-420281d159a5.JPG)

###### .zip de teste sendo visualizado no mapa disponível no site. (O mapa é apenas para ilustração, não é possível fazer maiores análises)
![Captura de ecrã 2020-04-04, às 20 05 04](https://user-images.githubusercontent.com/56345369/78459263-bbc7a880-76af-11ea-90f4-4051979ff39f.png)

## Como foi feito?

Toda a aplicação WEB de processamento foi construída em Python utilizando diversas bibliotecas, foi também utilizado o [framework flask](https://flask.palletsprojects.com/en/1.1.x/) assim como HTML, CSS e JS para o desenvolvimento destas e todas as outras páginas WEB.

Para o formulário de inserção foi utilizado Javascript e jquery além de uma planilha previamente configurada com o editor de script para aceitar entradas.

As aplicações WEB de processamento estão hospedadas numa VM da Google e utilizando tmux para rodar em tempo integral. O servidor utiliza [Gunicorn](https://gunicorn.org) já que pela própria documentação oficial, Flask não se mostra adequado para tal.







