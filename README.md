# >> Aplicação NIP <<
Aplicação para consultas de clientes de um Provedor ISP regional.<br>
<img alt="GitHub" src="https://img.shields.io/github/license/RodrigoTAbreu/App-NIP">

## -- Sobre o Projeto -- 
Disponibilizar para os analistas de TI N1, a consulta de dados dos clientes que haviam se perdido com uma atualização interna. Com isso dificultava identificar se o cliente que estava entrando em contato, informando falta de conectividade, estava ou não dentro de uma região onde estaria ocorrendo uma indisponibilidade.


## -- Coleta de Dados --
Como tratava-se de uma urgência para que os analistas em questão pudessem realizar um atendimento mais eficaz, foi utilizado duas planilhas em .XLS em que os dados foram cruzados.

## -- Sobre a Base de Dados --
A empresa utlizava controles em paralelos, para ativação de clientes na rede e para consulta de clientes em um determinado POP de atendimento. Essa base, gerada em .XLS foi captada e identificada que ambas haviam campos em comum, possiblilitando então o cruzamento de informações.

Com isso foi gerado em SQL local, tendo em vista que o banco não ficaria muito grande e conteria somente as informações necessárias.

## -- Interface --
Como a equipe precisa de algo mais rápido e usual, e não haveria a necessidade, em primeiro momento, de se desenvolver uma interface. Sendo assim foi obtado por rodar a aplicação diretamente no terminal.




