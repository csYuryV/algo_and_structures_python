"""
2019-12-12 Sikorskiy Yuriy
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""


# класс бнарного дерева
class Btree:
    def __init(self):
        self._root = None  # ссылка на корневой узел
        self._current_node = None  # выбранный узел
        self._nodes = list()  # список узлов  составляющих дерево

    def create_node(self):
        new_node = Bnode()
        self._nodes.append(new_node)
        return new_node

    def set_root_node(self, node):
        self._root = node

    def get_root_node(self):
        return self._root


class Bnode:
    def __init___(self):
        self._owner = None
        self._children = dict(left=None, right=None)

    def set_left_child(self, node):
        self._children['left'] = node

    def get_left_child(self):
        return self._children['left']

    def set_right_child(self, node):
        self._children['right'] = node

    def get_right_child(self):
        return self._children['right']

    def set_owner(self, owner):
        self._owner = owner

    def get_owner(self, owner):
        return self._owner

class

# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)
#
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
#
# from sqlalchemy import Column, Integer, String
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     nickname = Column(String)
#
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (
#                              self.name, self.fullname, self.nickname)
#
#
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
#
# Base.metadata.create_all(engine)
#
# ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# print(f'ed_user.name = {ed_user.name}')
# print(f'ed_user.id = {ed_user.id}')
#
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(ed_user)
# print(f'ed_user.id = {ed_user.id}')
# our_user = session.query(User).filter_by(name='ed').first()
# print(f'our_user.id = {our_user.id}')
# print(f'our_user = {our_user}')
# our_user2 = session.query(User).filter_by(id=1).first()
# print(f'our_user2 is our_user = {our_user2 is our_user}')
# print(f'our_user2 is ed_user = {our_user2 is ed_user}')
#
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', nickname='windy'),
#     User(name='mary', fullname='Mary Contrary', nickname='mary'),
#     User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
#
# ed_user.nickname = 'eddie'
#
# print(session.dirty)
# print(session.new)
#
# session.commit()
# print(f'ed_user.id  = {ed_user.id}')
#
# ed_user.name = 'Edwardo'
# fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
# session.add(fake_user)
#
# print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())
#
# print(f'ed_user.name = {ed_user.name}')
# print('session.rollback()')
# session.rollback()
# print(f'ed_user.name = {ed_user.name}')
# print(f'fake_user in session = {fake_user in session}')
