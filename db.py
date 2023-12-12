import sqlalchemy as db


class DataBase():
  def __init__(self):
    self.engine = db.create_engine('sqlite:///dentists.db')
    self.connection = self.engine.connect()
    self.metadata = db.MetaData()

  def create_table(self, name_table, *args):
    table = db.Table(name_table, self.metadata,
                     db.Column('id_', db.Integer(), autoincrement=True, primary_key=True),
                     *[db.Column(arg, db.String()) for arg in args]
                     )
    table.create(self.engine)
    print(f'Table {name_table} created')

  def read_table(self, name_table, return_keys=False):
    table = db.Table(name_table, self.metadata, autoload=True, autoload_with=self.engine)
    if return_keys:
      table.columns.keys()
    else:
      return table

  def add_row(self, name_table, **kwargs):
    # Read the table definition
    name_table = self.read_table(name_table)

    # Check if a row with the same name already exists
    select_stmt = db.select([name_table]).where(name_table.c.name == kwargs['name'])
    result = self.connection.execute(select_stmt)
    if result.fetchone():
      print(f"Row with name '{kwargs['name']}' already exists. No new row added.")
      return

    # Insert the new row since it doesn't exist
    insert_stmt = db.insert(name_table).values(**kwargs)
    self.connection.execute(insert_stmt)
    print('New row added.')

  def delete_row_by_id(self, table, id_):
    name_table = self.read_table(table)

    stmt = (
      db.delete(name_table).
      where(name_table.columns.id_ == id_)
    )
    self.connection.execute(stmt)
    print(f'Row id {id_} deleted')

  def select_table(self, name_table):
    name_table = self.read_table(name_table)
    stm = db.select([name_table])
    return self.connection.execute(stm).fetchall()
