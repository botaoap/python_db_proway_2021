# Teste do Exerc 1
from typing import Union
from pymysql import cursors, connect

# Connection with DB
connection = connect(
    host = 'localhost',
    port = 3306,
    user = 'botaoap',
    password = 'Abc1234@',
    database = 'loja',
    charset = 'utf8',
    cursorclass = cursors.DictCursor
)
cursor = connection.cursor()

class Categoria:

    nome: str

class Produto:

    nome: str
    preco: float
    fk_categoria: Union[Categoria, int] 

    def __repr__(self) -> str:
        return f"{self.nome} {self.preco} {self.fk_categoria}"

class DataBaseProducts:
    def create_table_produtos(self):
        sql = f"""
            CREATE TABLE produtos(
                id int not null primary key auto_increment,
                nome varchar(100) not null,
                preco decimal(5,2),
                fk_categoria int,
                CONSTRAINT fk_produtos_catrgoria FOREIGN KEY (fk_categoria)
                REFERENCES categoria(id)
            )
        """
        cursor.execute(sql)
        connection.commit()
    
    def insert_into_products(self,nome, preco, fk_categoria):
        sql = f"""
            INSERT INTO produtos (id, nome, preco, fk_categoria)
            values (0, '{nome}', '{preco}', '{fk_categoria}')
        """
        cursor.execute(sql)
        connection.commit()

    def read_all_products(self):
        sql = f"""
            SELECT p.id, p.nome, p.preco, c.nome as categoria FROM produtos p JOIN categoria c on p.fk_categoria = c.id
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data)

    def update_products_by_field(self, id, valor_do_campo, nome_do_campo):
        sql = f"""
            UPDATE produtos
            SET {nome_do_campo} = '{valor_do_campo}'
            WHERE id = '{id}'
        """
        cursor.execute(sql)
        connection.commit()
    
    def update_products_by_kwargs(self, id:int,**kwargs:Produto) -> None:
        for key, value in kwargs.items():
            sql = f"""
                UPDATE produtos
                SET {key} = '{value}'
                WHERE id = '{id}'
            """
            cursor.execute(sql)
            
        connection.commit()


    def delete_product_by_id(self,id):
        sql = f"""
            DELETE FROM produtos
            WHERE id = '{id}'
        """
        cursor.execute(sql)
        connection.commit()

class DataBaseCategory:
    def create_table_category(self):
        sql = f"""
            CREATE TABLE categoria(
                id int not null primary key auto_increment,
                nome varchar(100) not null
            )
        """
        cursor.execute(sql)
        connection.commit()

    def insert_into_category(self, nome):
        sql = f"""
            INSERT INTO categoria (id, nome)
            values (0, '{nome}')
        """
        cursor.execute(sql)
        connection.commit()

    def read_all_category(self):
        sql = f"""
            SELECT * FROM categoria
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data)

    def update_category(self,id, **kwargs):
        for key, value in kwargs.items():
            print(key, value)
            sql = f"""
                UPDATE categoria
                SET {key}='{value}'
                WHERE id = '{id}'
            """
        cursor.execute(sql)
        connection.commit()
        
    def delete_category_by_id(self,id):
        sql = f"""
            DELETE FROM categoria
            WHERE id = '{id}'
        """
        cursor.execute(sql)
        connection.commit()

# DataBaseCategory.create_table_category()
# DataBaseProducts.create_table_produtos()
# DataBaseCategory.insert_into_category(nome="Refrigerante")
# DataBaseCategory.insert_into_category(nome="Comida")
# DataBaseProducts.insert_into_products(nome="Guanara", preco= 10.00, fk_categoria= 1)
# DataBaseProducts.insert_into_products(nome="Coca", preco= 12.00, fk_categoria= 1)
# DataBaseProducts.insert_into_products(nome="Arroz", preco= 15.00, fk_categoria= 2)
# DataBaseCategory.read_all_category()
# DataBaseProducts.read_all_products()
# DataBaseCategory.update_category(id=3, nome="Limpeza")
# DataBaseCategory.read_all_category()
# DataBaseProducts.insert_into_products(nome="Limpa Vidro", preco=30.00, fk_categoria=3)
# DataBaseProducts.update_products_by_field(4,valor_do_campo="Limpa Móveis", nome_do_campo="nome")
# DataBaseProducts.update_products_by_field(4,valor_do_campo=10.00, nome_do_campo="preco")
# DataBaseProducts.delete_product_by_id(2)
# DataBaseProducts.read_all_products()
# DataBaseCategory.delete_category_by_id(4)
# DataBaseCategory.read_all_category()

# DataBaseCategory().update_category(1, nome="Teste")
# DataBaseCategory().read_all_category()

DataBaseProducts().update_products_by_kwargs(1, )

DataBaseProducts().read_all_products()