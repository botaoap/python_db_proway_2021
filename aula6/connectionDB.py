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

# Get some stuffs on DB
# In this case we get all products
def read_all_products():
    sql = "SELECT p.id, p.nome, p.preco, c.nome as categoria FROM produtos p join categoria c on p.id_categoria = c.id"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)

def read_all_categories():
    sql = "SELECT * FROM categoria"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data)

def insert_data(nome, preco, categoria):
    sql = f"""
        INSERT INTO produtos (id, nome, preco, id_categoria) VALUES (0, %s, %s, %s)
    """
    cursor.execute(sql, (nome, preco, categoria))
    connection.commit()

def delete_data(id, more_equal_then_id = False):
    if (more_equal_then_id == True):
        sql = f"""
        DELETE FROM produtos where id >= '{id}'
    """
    else:
        sql = f"""
            DELETE FROM produtos where id = '{id}' 
        """
    cursor.execute(sql)
    connection.commit()

def update_data(id,nome="", preco="", categoria=""):
    if (nome != ""):
        sql = f"""
            UPDATE produtos
            set nome = '{nome}'
            where id = '{id}'
        """
    if (preco != ""):
        sql = f"""
            UPDATE produtos
            set preco = '{preco}'
            where id = '{id}'
        """
    if (categoria != ""):
        sql = f"""
            UPDATE produtos
            set id_categoria = '{categoria}'
            where id = '{id}'
        """
    cursor.execute(sql)
    connection.commit()

def add_foreign_key_products_to_categories():
    sql = f"""
        ALTER TABLE produtos
        ADD FOREIGN KEY (id_categoria) REFERENCES categoria(id)
    """
    cursor.execute(sql)
    connection.commit()

def search_products_by_name(nome):
    sql = f"""
        SELECT * FROM produtos where nome like '%{nome}%'
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)



# delete_data(id=12, more_equal_then_id=True)
# insert_data(nome="Guarana", preco=10.50, categoria=1)
# update_data(id=11,nome="Vale-Uva")
# read_all_products()
# read_all_categories()
# add_foreign_key_products_to_categories()
# search_products_by_name("gua")
