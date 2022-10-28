# <center> >> Aplicação NIP <<
Aplicação para consultas de clientes de um Provedor ISP regional.<br>
<img alt="GitHub" src="https://img.shields.io/github/license/RodrigoTAbreu/App-NIP">

## -- Sobre o Projeto -- 
Disponibilizar para os analistas de TI N1, a consulta de dados dos clientes que haviam se perdido com uma atualização interna. Com isso dificultava identificar se o cliente que estava entrando em contato, informando falta de conectividade, estava ou não dentro de uma região onde estaria ocorrendo uma indisponibilidade.<br>
![nipra.png](https://github.com/RodrigoTAbreu/App-NIP/blob/main/assest/nipra.png)

## -- Coleta de Dados --
Como tratava-se de uma urgência para que os analistas em questão pudessem realizar um atendimento mais eficaz, foi utilizado duas planilhas em .XLS e exportados para .CSV, em que os dados foram cruzados.<br>
![bco_sql.png](https://github.com/RodrigoTAbreu/App-NIP/blob/main/assest/bco_sql.png)


## -- Sobre a Base de Dados --
A empresa utlizava controles em paralelos, para ativação de clientes na rede e para consulta de clientes em um determinado POP de atendimento. Essa base, gerada em .XLS foi captada e identificada que ambas haviam campos em comum, possiblilitando então o cruzamento de informações.

Com isso foi gerado em SQL local, tendo em vista que o banco não ficaria muito grande e conteria somente as informações necessárias.

## -- Interface --
Como a equipe precisa de algo mais rápido e usual, e não haveria a necessidade, em primeiro momento, de se desenvolver uma interface. Sendo assim foi obtado por rodar a aplicação diretamente no terminal.

![tela2.png](https://github.com/RodrigoTAbreu/App-NIP/blob/main/assest/tela2.png)

## -- Instruções -- 
Por fim foi disponibilizado um manual intitulado Leia Antes.pdf para que os analistas possam seguir o passo a passo e baizar e utilizar a aplicação até que o problema esteja totalmente resolvido no sistema global pela equipe de TI da empresa.

![Sele%C3%A7%C3%A3o_167.png](https://github.com/RodrigoTAbreu/App-NIP/blob/main/assest/Sele%C3%A7%C3%A3o_167.png)
<br>


## -- Tecnologias Utilizadas --
- Python 3
- SQLite

## -- Como Executar a Aplicação -- 
``` bash
# Salve os arquivos consultas_nip.exe e olt_bco.db na mesma pasta. Em seguida execute o arquivo.
./consultas_nip

```

## -- Considerações Finais -- 
A aplicação teve como objetivo atender uma demanda em carater de urgência, e não desenvolver algo mais sofitsticado, apenas de possibilitar inúmeras outras demandas.

## -- Autor -- 
Rodrigo Telles de Abreu.<br>
rodrigo.telles.abreu@gmail.com
https://www.linkedin.com/in/rodrigo-telles/


