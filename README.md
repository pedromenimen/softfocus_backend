# softfocus_backend

Para usar localmente é necessário a criação de um arquivo com o nome .env e a criação de algumas variáveis de ambiente:

DATABASE_URL=postgresql://{user}:{password}@{host}:{port}/{dbname}

SECRET_KEY=chave segura

Para instalar todas as bibliotecas basta digitar pip install -r requirements.txt, já dentro de um ambiente virtual.

A aplicação consiste em um crud simples de comunicações, segue abaixo a lista de endpoints, bem como verbo http.

- endpoint: api/communication/

método: POST

request: {
	"owner_name": string,
	"owner_email": string,
	"owner_cpf": string,
	"latitude": number,
	"longitude": number,
	"type": string,
	"date": string,
	"event": string
}

A resposta da rota são as informações enviadas além do id e de um campo adicional, informando se a comunicação é suspeita com base nos critérios enviados por email.

- endpoint: api/communication/list/cpf/

método: GET

request: sem corpo de requisição

A resposta da rota são todas as comunicações feitas pelo usuário cujo CPF começa com o que foi passado na url, podendo ser quantos caracteres precisa, seja 000 ou 000.000.000-00.

- endpoint: api/communication/id/

método: GET

request: sem corpo de requisição

A resposta da rota é a comuncação cujo id é igual as passado na url.

- endpoint: api/communication/

método: GET

request: sem corpo de requisição

A resposta da rota são todas as comunicações feitas registradas no banco de dados.

- endpoint: api/communication/id/

método: PATCH

request: request: {
	"owner_name": string,
	"owner_email": string,
	"owner_cpf": string,
	"latitude": number,
	"longitude": number,
	"type": string,
	"date": string,
	"event": string
}

A rota serve para atualizar informações referentes a comunicação cujo id for igual ao da url.

- endpoint: api/communication/id/

método: DELETE

request: sem corpo de requisição

A rota serve para deletar a comunicação cujo id for igual ao da url.
