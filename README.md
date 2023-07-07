# Flask CRUD API

Esta é uma API CRUD simples desenvolvida em Flask para gerenciar uma entidade de "usuário". A API permite criar, ler, atualizar e excluir usuários no banco de dados MySQL.

## Configuração

0. tenha xampp e o postman instalado .

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).

2. Crie um ambiente virtual para isolar as dependências:

python -m venv venv

3. Ative o ambiente virtual:
- No Windows:
  ```
  venv\Scripts\activate
  ```
- No macOS e Linux:
  ```
  source venv/bin/activate
  ```

4. Instale as dependências do projeto:

pip install -r requirements.txt

5. Configuração do banco de dados:
- Certifique-se de ter um servidor MySQL em execução localmente.
- Defina a URL do banco de dados no arquivo `app.py`:
  ```
  app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/flask_react_crud"
  ```
  Substitua `"mysql+pymysql://root@localhost/flask_react_crud"` pela URL do seu banco de dados MySQL.

6. Execução da aplicação:

flask --app app run

7. Acesse a API no navegador ou por meio de ferramentas como o Postman usando as seguintes rotas:
- `http://localhost:5000/`: Rota inicial para teste.
- `http://localhost:5000/listadeusuarios`: Rota para listar todos os usuários.
- `http://localhost:5000/detalhedousuario/<id>`: Rota para obter os detalhes de um usuário específico.
  Substitua `<id>` pelo ID real do usuário.
- `http://localhost:5000/atualizarusuario/<id>`: Rota para atualizar um usuário.
  Substitua `<id>` pelo ID real do usuário.
- `http://localhost:5000/deletarusuario/<id>`: Rota para deletar um usuário.
  Substitua `<id>` pelo ID real do usuário.
- `http://localhost:5000/usuarioadd`: Rota para adicionar um novo usuário.




