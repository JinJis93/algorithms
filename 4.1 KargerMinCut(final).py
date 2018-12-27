import os
import random
from collections import Counter
import copy


class KargerMinCounter:
    KARGER_TXT = os.path.abspath("") + "/files/kargerMin.txt"
    KARGER_N = 10

    @classmethod
    def run(cls) -> int:
        graph_dict = cls.process_raw_file(cls.KARGER_TXT)

        count = 0
        min_cut = None
        while count < cls.KARGER_N:
            count += 1
            copied_graph = copy.deepcopy(graph_dict)
            if min_cut is None:
                min_cut = cls.compute_contraction(copied_graph)
                continue
            cur_cut = cls.compute_contraction(copied_graph)
            if cur_cut < min_cut:
                min_cut = cur_cut
        return min_cut

    @staticmethod
    def process_raw_file(file: str) -> dict:
        """
        :return Counter(
            {'Node1': Counter(edged vertexes of 'Node1')})
        :example
        Counter({1: Counter({2: 1, 3: 1, 4: 1}), 2: Counter({1: 1, 3: 1, 4: 1})...)

        """
        graph = {}
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                parsed = list(map(int, line.strip("\t").split()))
                graph[parsed[0]] = Counter(parsed[1:])
        return graph

    @classmethod
    def compute_contraction(cls, g: dict) -> int:
        # randomly pick 2 from Counter.keys
        if len(g) <= 2:
            return int(g[g.__iter__().__next__()].most_common(1)[0][1])

        # Home node
        home: int = random.choice(list(g.keys()))
        ghome: Counter = g[home]

        # Away node
        away: int = ghome.most_common(1)[0][0]
        gaway: Counter = copy.deepcopy(g[away])

        # delete away from graph
        del g[away]

        # delete self loops
        del ghome[away]
        del gaway[home]

        # merge
        ghome.update(gaway.elements())
        for r in gaway.keys():  # type: int
            gref = g[r]
            gref[home] += gref[away]
            del gref[away]

        return cls.compute_contraction(g)


min_cut = KargerMinCounter.run()
print(min_cut)
