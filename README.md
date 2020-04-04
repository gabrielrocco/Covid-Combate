# Covid-Combate

## Objetivos
O projeto tem como objetivo contribuir com os gestores dos municípios que não possuem base de dados de endereços, disponibilizando aplicação para o processamento de planilhas específicas (utilizadas como base de dados) e inclusão de novos dados por hospitais e centros de saúde. Como produto final é gerado um .zip com arquivo .shp (shapefile), possibilitando  aplicações na área de geotecnologias dando abertura para serem traçadas estratégias e ações para o bloqueio do COVID19, com a finalidade de minimizar a contaminação.

#### [Clique para acessar o projeto](covidcombate.com.br)

O uso recomendado seria que entidades responsáveis por cidades (Prefeituras, etc) criassem uma planilha e a configurassem, fornecendo a chave específica para centros de saúde, hospitais entre outros que pudessem atualizar a base com novas entradas de doentes.
Ao processar os dados o campo da planilha de rua, número da casa e cidade são utilizadas junto ao [API Geocoding da Google](https://developers.google.com/maps/documentation/geocoding/intro) para gerar coordenadas. (Um endereço é transformado em latitude e longitude e então a planilha é atualizada em tempo real e os arquivos gerados). 

A partir destas coordenadas podemos mapear os doentes e fazer análises com filtros diversos em Softwares como [QuantumGis](https://qgis.org/en/site/) além disso é possível verificar a concentração de doentes numa determinada área de modo a tomar ações mais efetivas e direcionadas.

#### ATENÇÃO: A aplicação gera coordenadas com base na API da Google, com base em testes já foi verificado que certos resultados, principalmente em regiões mais remotas não possuem tanta eficiência.

| rua                 | numero_casa  |cidade       |cep|latitude       |longitude      |
| ------------------- | ------------ |------------ | ----|---------------|---------------|
|  Rua Barreto Leme   |  35          | Campinas    | 13010200 |Gerado no Processamento|Gerado no Processamento|

Para a geração das coordenadas, estas quatro colunas contém as informações necessárias. O resto das colunas e as que possam ser adicionadas pelos usuários são para outras avaliações que podem ser interessantes também. É possível fazer o download de  uma tabela base [aqui](https://covidcombate.com.br/escolhaprocessamento.html), novas colunas podem ser adicionadas de acordo com a necessidade.

## Como funciona ?
Pode ser utilizada uma planilha específica na nuvem (plataforma Google Sheets) em que é possível realizar a inserção de dados pelo [formulário web](http://covidcombate.com.br/avisoFormulario.html) utilizado a chave da base de dados para identificar a planilha correta. Esta ferramenta possibilita grande escalabilidade após criar e configurar a planilha, pois qualquer entidade responsável pode enviar dados diretamente para a planilha apenas com a chave, sem maiores complicações. Entretanto, o armazenamento de dados na nuvem pode não ser da vontade dos órgãos públicos.

Devido isso é possível utiizar planilhas locais para atualização local, sem armazenamento na nuvem. Desta forma a inserção de novos dados fica a critério dos órgãos responsáveis. 

Em ambos os casos existem respectivas [aplicações WEB](https://covidcombate.com.br/escolhaprocessamento.html) que processam os arquivos.

* Ao processar arquivos na nuvem (Google Sheets) os dados são atualizados em tempo real na planilha online e os arquivos shapefile gerados para download.

* Ao processar arquivos localmente além do shapefile também é devolvida uma nova planilha com os dados atualizados.

## Como foi feito?

Toda a aplicação WEB de processamento foi construída em Python utilizando diversas bibliotecas, foi também utilizado o [framework flask](https://flask.palletsprojects.com/en/1.1.x/) assim como HTML, CSS e JS para o desenvolvimento destas e todas as outras páginas WEB.

