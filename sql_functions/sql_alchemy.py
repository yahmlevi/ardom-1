import sqlalchemy as db
from sqlalchemy.pool import NullPool

#engine = create_engine('sqlite://D:\\projects\\ardom-1\\sql_functions\\testdatabase.db',pool_size=NullPool, max_overflow=0)
engine = db.create_engine('sqlite:///D:\\projects\\ardom-1\\sql_functions\\testdatabase.db', poolclass=NullPool)

# connection = engine.connect()
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)