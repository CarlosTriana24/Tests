from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime, Float, Boolean, Text, select, and_

class DataBase:
    def __init__(self, db_name):
        self.engine = create_engine(f'sqlite:///{db_name}')
        self.metadata = MetaData()
        self.users = Table('users', self.metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('name', String(50)),
            Column('email', String(50), unique=True),
            Column('password', String(50)),
            Column('created_at', DateTime),
            Column('updated_at', DateTime),
            Column('is_active', Boolean),
            Column('is_admin', Boolean),            
        )
        self.posts = Table('posts', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('title', String(100)),
            Column('content', Text),
            Column('user_id', Integer, ForeignKey('users.id')),
            Column('created_at', DateTime),
            Column('updated_at', DateTime),
        )
        self.comments = Table('comments', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('content', Text),
            Column('post_id', Integer, ForeignKey('posts.id')),
            Column('user_id', Integer, ForeignKey('users.id')),
            Column('created_at', DateTime),            
        )
        self.metadata.create_all(self.engine)

    def insert_user(self, name, email, password, created_at, updated_at, is_active, is_admin):
        with self.engine.connect() as conn:
            conn.execute(self.users.insert(), {
                'name': name,
                'email': email,
                'password': password,
                'created_at': created_at,
                'updated_at': updated_at,
                'is_active': is_active,
                'is_admin': is_admin,
            })

    def insert_post(self, title, content, user_id, created_at, updated_at):
        with self.engine.connect() as conn:
            conn.execute(self.posts.insert(), {
                'title': title,
                'content': content,
                'user_id': user_id,
                'created_at': created_at,
                'updated_at': updated_at,
            })

    def insert_comment(self, content, post_id, user_id, created_at):
        with self.engine.connect() as conn:
            conn.execute(self.comments.insert(), {
                'content': content,
                'post_id': post_id,
                'user_id': user_id,
                'created_at': created_at,
            })

    def get_user_by_email(self, email):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.users]).where(self.users.c.email == email)).first()
            if result:
                return {
                    'id': result[0],
                    'name': result[1],
                    'email': result[2],
                    'password': result[3],
                    'created_at': result[4],
                    'updated_at': result[5],
                    'is_active': result[6],
                    'is_admin': result[7],
                }
            else:
                return None

    def get_user_by_id(self, id):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.users]).where(self.users.c.id == id)).first()
            if result:
                return {
                    'id': result[0],
                    'name': result[1],
                    'email': result[2],
                    'password': result[3],
                    'created_at': result[4],
                    'updated_at': result[5],
                    'is_active': result[6],
                    'is_admin': result[7],
                }
            else:
                return None

    def get_post_by_id(self, id):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.posts]).where(self.posts.c.id == id)).first()
            if result:
                return {
                    'id': result[0],
                    'title': result[1],
                    'content': result[2],
                    'user_id': result[3],
                    'created_at': result[4],
                    'updated_at': result[5],
                }
            else:
                return None

    def get_comment_by_id(self, id):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.comments]).where(self.comments.c.id == id)).first()
            if result:
                return {
                    'id': result[0],
                    'content': result[1],
                    'post_id': result[2],
                    'user_id': result[3],
                    'created_at': result[4],
                }
            else:
                return None

    def get_all_users(self):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.users])).all()
            if result:
                return [
                    {
                        'id': row[0],
                        'name': row[1],
                        'email': row[2],
                        'password': row[3],
                        'created_at': row[4],
                        'updated_at': row[5],
                        'is_active': row[6],
                        'is_admin': row[7],
                    } for row in result
                ]
            else:
                return []

    def get_all_posts(self):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.posts])).all()
            if result:
                return [
                    {
                        'id': row[0],
                        'title': row[1],
                        'content': row[2],
                        'user_id': row[3],
                        'created_at': row[4],
                        'updated_at': row[5],
                    } for row in result
                ]
            else:
                return []

    def get_all_comments(self):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.comments])).all()
            if result:
                return [
                    {
                        'id': row[0],
                        'content': row[1],
                        'post_id': row[2],
                        'user_id': row[3],
                        'created_at': row[4],
                    } for row in result
                ]
            else:
                return []

    def get_all_posts_by_user_id(self, user_id):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.posts]).where(self.posts.c.user_id == user_id)).all()
            if result:
                return [
                    {
                        'id': row[0],
                        'title': row[1],
                        'content': row[2],
                        'user_id': row[3],
                        'created_at': row[4],
                        'updated_at': row[5],
                    } for row in result
                ]
            else:
                return []

    def get_all_comments_by_user_id(self, user_id):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.comments]).where(self.comments.c.user_id == user_id)).all()
            if result:
                return [
                    {
                        'id': row[0],
                        'content': row[1],
                        'post_id': row[2],
                        'user_id': row[3],
                        'created_at': row[4],
                    } for row in result
                ]
            else:
                return []

    def get_all_comments_by_post_id(self, post_id):
        with self.engine.connect() as conn:
            result = conn.execute(select([self.comments]).where(self.comments.c.post_id == post_id)).all()
            if result:
                return [
                    {
                        'id': row[0],
                        'content': row[1],
                        'post_id': row[2],
                        'user_id': row[3],
                        'created_at': row[4],
                    } for row in result
                ]
            else:
                return []

    def update_user(self, id, name, email, password, created_at, updated_at, is_active, is_admin):
        with self.engine.connect() as conn:
            conn.execute(self.users.update().where(self.users.c.id == id), {
                'name': name,
                'email': email,
                'password': password,
                'created_at': created_at,
                'updated_at': updated_at,
                'is_active': is_active,
                'is_admin': is_admin,
            })

    def update_post(self, id, title, content, user_id, created_at, updated_at):
        with self.engine.connect() as conn:
            conn.execute(self.posts.update().where(self.posts.c.id == id), {
                'title': title,
                'content': content,
                'user_id': user_id,
                'created_at': created_at,
                'updated_at': updated_at,
            })

    def update_comment(self, id, content, post_id, user_id, created_at):
        with self.engine.connect() as conn:
            conn.execute(self.comments.update().where(self.comments.c.id == id), {
                'content': content,
                'post_id': post_id,
                'user_id': user_id,
                'created_at': created_at,
            })

    def delete_user(self, id):
        with self.engine.connect() as conn:
            conn.execute(self.users.delete().where(self.users.c.id == id))

    def delete_post(self, id):
        with self.engine.connect() as conn:
            conn.execute(self.posts.delete().where(self.posts.c.id == id))

    def delete_comment(self, id):
        with self.engine.connect() as conn:
            conn.execute(self.comments.delete().where(self.comments.c.id == id))

    def delete_all_users(self):
        with self.engine.connect() as conn:
            conn.execute(self.users.delete())

    def delete_all_posts(self):
        with self.engine.connect() as conn:
            conn.execute(self.posts.delete())

    def delete_all_comments(self):
        with self.engine.connect() as conn:
            conn.execute(self.comments.delete())

  