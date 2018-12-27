import os
import random
import copy


class KargerMinCut:
    KARGER_TXT = os.path.abspath("") + "/files/kargerMin.txt"
    KARGER_TEST = os.path.abspath("") + "/files/karger_test.txt"
    KARGER_SIMPLE = os.path.abspath("") + "/files/karger_simplest.txt"
    KARGER_N = 100

    def __init__(self):
        self.all_node_objs_list = self.process_raw_file()

    def run(self):
        return self.compute_by_N(self.KARGER_N)

    @classmethod
    def process_raw_file(cls):
        all_node_objs_list = list()
        with open(cls.KARGER_TXT, encoding="utf-8") as f:
            for raw_node_info in f.readlines():
                # append 'Node' object
                all_node_objs_list.append(cls.to_node_obj(raw_node_info))
        return all_node_objs_list

    def compute_by_N(self, karger_n):
        min_cut = None
        count = 1
        while count <= karger_n:
            print(f"----- count: {count} -----")
            if min_cut is None:
                min_cut = self.compute_min_karger_algo()
                count += 1
                continue
            cut_num = self.compute_min_karger_algo()
            if cut_num < min_cut:
                min_cut = cut_num
            count += 1
        return min_cut

    def compute_min_karger_algo(self):
        # stop when two Nodes remain
        all_nodes_obj_list_copy = copy.deepcopy(self.all_node_objs_list)
        while len(all_nodes_obj_list_copy) > 2:
            # random pick of Nodes
            random_nodes: ['Node'] = random.choices(all_nodes_obj_list_copy, k=2)
            if random_nodes[0].num == random_nodes[1].num:
                continue

            random_nodes[0].contract(random_nodes[1], all_nodes_obj_list_copy)

        last_node_1 = all_nodes_obj_list_copy[0]
        last_node_2 = all_nodes_obj_list_copy[1]
        return max(len(last_node_1.edge_vertexes), len(last_node_2.edge_vertexes))

    @staticmethod
    def to_node_obj(raw_node_info: str):
        processed = list(map(int, raw_node_info.strip("\t").split()))
        # create each Node obj
        node_obj = Node()
        node_obj.num = processed[0]
        node_obj.edge_vertexes = processed[1:]
        return node_obj


class Node:
    def __init__(self):
        self._num: int = None
        self._edged_vertexes: list = None

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @property
    def edge_vertexes(self):
        return self._edged_vertexes

    @edge_vertexes.setter
    def edge_vertexes(self, value):
        self._edged_vertexes = value

    def contract(self, other: 'Node', node_objs_list: list):
        # check if able to contract
        if self.num not in other.edge_vertexes or other.num not in self.edge_vertexes:
            return

        # check size of Node.num
        if self.num < other.num:
            to_survive = self
            to_die = other
        else:
            to_survive = other
            to_die = self

        # extract sharing/distinct edges from 'to_die'
        to_survive.edge_vertexes = self.remove_all_occurence([to_die.num], to_survive.edge_vertexes)
        nodes_to_be_contracted = self.remove_all_occurence([to_survive.num, to_die.num], to_die.edge_vertexes)
        to_survive.edge_vertexes.extend(nodes_to_be_contracted)
        node_objs_list.remove(to_die)

        # apply Nodes that was attached to 'to_die' to 'to_survive'
        for node_obj in node_objs_list:  # type: Node
            if node_obj.num in nodes_to_be_contracted:
                # count to_die in current node_obj
                occur_num = node_obj.edge_vertexes.count(to_die.num)

                node_obj.edge_vertexes = self.remove_all_occurence([to_die.num], node_obj.edge_vertexes)
                node_obj.edge_vertexes.extend([to_survive.num] * occur_num)

    @staticmethod
    def remove_all_occurence(filter_num_list: [int], target_list: list):
        def dulplicate_checker(compare: int):
            for filter_num in filter_num_list:
                if filter_num.__eq__(compare):
                    return False
            return True
        return list(filter(dulplicate_checker, target_list))


karger = KargerMinCut()
print(karger.run())
