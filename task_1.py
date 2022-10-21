from collections import deque

def check_relation(net, first, second):
    # create graph from net data
    graph = {}
    for x, y in net:
        if x not in graph:
            graph[x] = [y]
        if y not in graph:
            graph[y] = [x]
            if y not in graph[x]:
                graph[x].append(y)
        else:
            if x not in graph[y]:
                graph[y].append(x)
    # check relation using breadth-first search
    search_queue = deque()
    search_queue += graph[first]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == second:
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша"))


    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
