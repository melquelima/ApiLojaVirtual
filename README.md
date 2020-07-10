# ApiLojaVirtual
Projeto desenvolvido com finalidade de demonstração de habilidade em desenvolvimento API em python

<h4>1. Sobre o projeto</h4>
<p>
 &nbsp Foi solicitado pela Capitani, o desenvolvimento de um sistema em REST API simulando uma loja virtual devendo conter: cadastro de clientes, produtos e pedidos, como o intuito não foi o desenvolvimento de fato de um sistema completo, o mesmo nao contem enumeras funções necessarias para um bom funcionamento em ambiente de produção, mas sim uma boa estrutura em backend para a analise de qualidade de código.
</p>
 
 <h4>2. Ferramentas utilizadas</h4>
 <p>&nbsp
  O sistema é constituido de ferramentas que funcionam em conjunto e torna a aplicação funcional:
  <ul>
    <li>Banco de dados
      <ul>
        <li>SQLite3</li>  
      </ul>
    </li>
    <li>FrameWork/Linguagem
      <ul>
        <li>Python</li>  
        <li>Flask</li>
      </ul>
    </li>
    <li>Outros
      <ul>
        <li>SQLAlchemy</li>
        <li>Autenticação JWT</li>
      </ul>
    </li>
  </ul>
</p>  
  
<h4>3. Banco de dados</h4>
<p>&nbsp
  A escolha do <b>SQLite3</b> foi apenas em quesito praticidade aplicada ao tamanho do projeto, em uma escala maior o mais indicado seria migrar para um banco de dados profissional no qual se comporta de melhor maneira quando se trata de larga escala em volume de dados e multiprocessos como SQL Server, Oracle, Postgree entre outros.
&nbsp Para a comunicação e mapemento dos dados com o sistema em si foi utilizado <b>SQLAlchemy</b> que é uma biblioteca de mapeamento objeto-relacional, torna a interação mais organizada alem de gerir melhor os dados manipulados a fim de melhorar o desenpenho do sistema.
</p>

<h4>4. Segurança</h4>
<p>&nbsp
  A fim de manter a segurança fez-se necessario a utilização de um método de autenticação tornando o sistema mais seguro, sendo assim, optei pela autenticação de dois pontos utilizando o <b>JWT Token</b>, com isto o usuario deve solicitar o token por uma autenticação básica com login e senha para obter assim seu token válido por <b>60 minutos</b> que por sua vez é utilizado em todas as interações da API, alem disto, senhas do sistema são todas encriptadas no banco de dados.
</p>

<h4>5. Sobre o sistema</h4>
<p>&nbsp
 O sistema foi projetado para ser utilizado em varias LOJAS e CLIENTES, para que possa usar o sistema primeiramente deve-se criar o seu usuário, lembrando que:
 <ul>
   <li>Perfis
     <ul>
       <li>LOJA
         <ul>
           <li>Cadastro de Produtos</li>
           <li>Listar produtos</li>
         </ul>
       </li>
      <li>CLIENTE
         <ul>
           <li>Fazer pedido</li>
           <li>Listar pedidos</li>
         </ul>
       </li>
     </ul>
   </li>
 </ul>
 
 <b>OBS:</b> As rotas de exclusão de clientes, produtos e pedidos nao foram implementadas.
 </p>
 
 <h4>5.1. Criação de Usuario</h4>
 <p>&nbsp
   Conforme informado no ultimo tópico é necessária a criação do seu usario, para isto é utilizadas as configurações abaixo: 
 
  <ul>
    <li>Rota <br/><b>"/createUser"</b></li>
    <li>Metodo <br/><b>"POST"</b></li>
    <li>Headers
      <ul>
        <li>Content Type: <b>application/json</b></li>
      </ul>
    </li>
    <li>Body</li>
  </ul>

```json
{
	"userName": "melque",
	"password": "123",
	"perfil": "LOJA"
}
```

Resposta:
```json
{
    "message": "User created successfully!",
    "status": true
}
```
 
 <b>OBS:</b> ja existe um usuario criado para teste, caso prefira nao criar um, basta utilizar as credenciais informadas acima no campo <b>Body</b>
</p>

 <h4>5.2. Token</h4>
 <p>&nbsp
	Com o usuario criado temos que adquirir o token no qual vai nos permitir fazer todas as interações, para isto utilizamos as configurações abaixo:
<ul>
    <li>Rota <br/><b>"/getToken"</b></li>
    <li>Metodo <br/><b>"GET"</b></li>
    <li>Authorization
      <ul>
        <li>Type: <b>Basic Auth</b></li>
        <li>User: <b>{{usuario}}</b></li>
        <li>Pwd: <b>{{senha}}</b></li>
      </ul>
    </li>
  </ul>

Resposta:
```json
{
    "message": "Your token is valid through the next 60 minutes!",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNJZCI6IjNhNjlkNzlmLTYzNDEtNDMzMC1iNmNkLTIwYzIyMTE0ZTliOSIsImV4cCI6MTU5NDQwMjE0N30.iUQEh0FdCv7NzIi-t-6hw8xnXEhPOO7XhRzA-zYfnEs"
}
```

Basta utilizar o token informado nas operações seguintes.

 <h4>5.3. Envio de produtos - LOJA</h4>
 <p>&nbsp o usuário uma vez cadastrado podemos cadastrar produtos e atribuilos ao perfil, lembrando que apenas perfis do tipo "LOJA" podem cadastrar produtos, para cadastrar um ou "n" produtos utilizamos as configurações abaixo:
	
  <ul>
    <li>Rota <br/><b>"/uploadPoducts"</b></li>
    <li>Metodo <br/><b>"POST"</b></li>
    <li>Headers
      <ul>
        <li>Content Type: <b>application/json</b></li>
	<li>x-access-token: <b>{{TOKEN}}</b></li>
      </ul>
    </li>
    <li>Body</li>
  </ul>

```json
[
	{"name":"bola de futebol","description":"feita de couro sintetico","price":12.5},
	{"name":"chuteira","description":"chuteira de campo","price":50.24}
]	
```
Resposta:
```json
{
    "message": "products uploaded successfully!",
    "status": true
}
```

<h4>5.4. Listar produtos - LOJA</h4>
 <p>&nbsp Com os produtos uma vez cadastrados voce tem a opção de lista-los do sistema utilizando as configurações abaixo:

  <ul>
    <li>Rota <br/><b>"/getPoducts"</b></li>
    <li>Metodo <br/><b>"GET"</b></li>
    <li>Headers
      <ul>
	<li>x-access-token: <b>{{TOKEN}}</b></li>
      </ul>
    </li>
  </ul>
Resposta:

```json
{
    "message": "OK",
    "products": [
        {
            "description": "feita de couro sintetico",
            "name": "bola de futebol",
            "price": 12.5,
            "publicId": "998e7544-47db-43e0-b113-cbaae74dfde4"
        },
        {
            "description": "chuteira de campo",
            "name": "chuteira",
            "price": 50.24,
            "publicId": "25fd4f5e-98b7-47be-9328-bd3e0fd3386d"
        }
    ],
    "status": true
}
```
