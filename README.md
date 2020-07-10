# ApiLojaVirtual
Projeto desenvolvido com finalidade de demonstração de habilidade em desenvolvimento backend API em python

<h4>1. Sobre o projeto</h4>
<p>
 &nbsp Foi solicitado pela Capitani o desenvolvimento de um sistema em REST API simulando uma loja virtual a fins de demonstração da qualidade do desenvolvimento em backend utilizando python. O sistema deve conter cadastro de <b><i>clientes, produtos e pedidos</i></b>, como o intuito não foi o desenvolvimento de fato de um sistema completo, o mesmo nao contem enumeras funções necessarias para um bom funcionamento <b><i> em ambiente de produção</i></b>, mas sim uma boa estrutura em backend para a analise de qualidade de código.
</p>
 
 <h4>2. Ferramentas utilizadas</h4>
 <p>&nbsp
  O sistema é constituido de ferramentas que funcionam em conjunto e torna a aplicação funcional, abaixo as ferramentas utilizadas:
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

 
 <b>OBS:</b> ja existe um usuario criado para teste caso prefira nao criar um, basta utilizar as credenciais informadas acima no campo <b>Body</b>

 


</p>


