"""

2019-12-12 Sikorskiy Yuriy
cv.yury.v@pm.me

1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

"""

from collections import Counter


# класс бинарного дерева
class Btree:
    def __init__(self):
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
    def __init__(self):
        self._owner = None
        self._children = [None, None]

    def set_left_child(self, node):
        self._children[0] = node
        node._owner = self

    def get_left_child(self):
        return self._children[0]

    def set_right_child(self, node):
        self._children[1] = node
        node._owner = self

    def get_right_child(self):
        return self._children[1]

    def set_owner(self, owner):
        self._owner = owner

    def get_owner(self):
        return self._owner


class Tree_jewish_scholar(Btree):
    def __init__(self, s):  # в s передается строка которую необходиом закодировать
        super().__init__()
        self._s = s
        self._frequency_dict = Counter()  # словарь c символами и их частотами
        self.symbol_repetition_frequency()
        self._list_of_leaf_nodes = list()  # список листовых узлов, упорядоченный по возростанию частот
        self.create_a_list_of_leaf_nodes()
        self.create_grow_a_tree()  # построение дерева еврейского ученого
        self._coding_dict = dict()  # словарь соответствия символа и его двоичного кода
        self.create_coding_dict()
        self._coding_str = ''  # Вид закодированной исходной текстовой строки
        self.create_coding_str()

    # расчет частоты повторения символов в строке
    def symbol_repetition_frequency(self):
        for i in self._s:
            self._frequency_dict[i] += 1

    # наполняю колекцию листовыми узлами упорядеченную по возростанию частот повтерия символов
    def create_a_list_of_leaf_nodes(self):
        list_fd = list(self._frequency_dict.items())
        list_fd.sort(key=lambda i: i[1], reverse=True)
        for i in list_fd:
            self._list_of_leaf_nodes.append(Bnode_jewish_scholar(i[0], i[1]))
        # print(list_fd)
        # for i in self._list_of_leaf_nodes:
        #     print(i)

    def create_grow_a_tree(self):
        if len(self._list_of_leaf_nodes) == 1:
            self._list_of_leaf_nodes[0]._code = 0
            self.set_root_node(self._list_of_leaf_nodes[0])
        if len(self._list_of_leaf_nodes) > 1:
            temp_list_nodes = self._list_of_leaf_nodes.copy()
            while len(temp_list_nodes) > 1:
                left_node = temp_list_nodes.pop()
                right_node = temp_list_nodes.pop()
                characters = left_node.get_characters() + right_node.get_characters()
                frequency = left_node.get_frequency() + right_node.get_frequency()
                owner_node = Bnode_jewish_scholar(characters, frequency)
                owner_node.set_left_child(left_node)
                owner_node.set_right_child(right_node)
                if len(temp_list_nodes) == 0:
                    temp_list_nodes.append(owner_node)
                elif owner_node.get_frequency() >= temp_list_nodes[0].get_frequency():
                    temp_list_nodes.insert(0, owner_node)
                elif owner_node.get_frequency() < temp_list_nodes[-1].get_frequency():
                    temp_list_nodes.append(owner_node)
                else:
                    for i in range(1, len(temp_list_nodes)):
                        if owner_node.get_frequency() >= temp_list_nodes[i].get_frequency():
                            temp_list_nodes.insert(i, owner_node)
                            break
            self.set_root_node(temp_list_nodes[0])

    def create_coding_dict(self):
        for i in self._list_of_leaf_nodes:
            current_node = i
            character_encoding = ''
            while current_node is not self.get_root_node():
                character_encoding += str(current_node.get_code())
                current_node = current_node.get_owner()
            self._coding_dict[i.get_characters()] = ''.join(reversed(character_encoding))

    def get_coding_dict(self):
        for key, value in self._coding_dict.items():
            print(f'{key}: {value}')

    def create_coding_str(self):
        for i in self._s:
            self._coding_str += self._coding_dict[i]

    def get_coding_str(self):
        return self._coding_str


class Bnode_jewish_scholar(Bnode):
    def __init__(self, characters, frequency):
        super().__init__()
        self._code = None  # если по левой ветке к овнеру присоединен то 0 если по правой то 1
        self._characters = characters
        self._frequency = frequency

    def get_characters(self):
        return self._characters

    def get_frequency(self):
        return self._frequency

    def set_right_child(self, node):
        super().set_right_child(node)
        node._code = 1

    def set_left_child(self, node):
        super().set_left_child(node)
        node._code = 0

    def get_code(self):
        return self._code

    def __str__(self):
        return f'<Bnode_jewish_scholar(_code = {self._code} _characters = {self._characters} self._frequencies = {self._frequency})>'


def main():
    test_str = 'папамама ичерт рогатый'
    print(f'Исходная строка: \'{test_str}\'')
    tree_jewish_scholar = Tree_jewish_scholar(test_str)
    print(f'Закодированная исходная строка:\n{tree_jewish_scholar.get_coding_str()}')
    print('Словарь кодировок символов строки')
    tree_jewish_scholar.get_coding_dict()


if __name__ == '__main__':
    main()
