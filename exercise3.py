import heapq

def dijkstra(graph, start):
    """
    Алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі
    з використанням бінарної купи (heapq).
    
    :param graph: Представлення графа у вигляді списку суміжності {вершина: [(сусід, вага)]}.
    :param start: Початкова вершина.
    :return: Словник найкоротших відстаней від start до всіх вершин.
    """
    # Ініціалізація
    shortest_paths = {vertex: float('inf') for vertex in graph}  # Всі відстані - нескінченність
    shortest_paths[start] = 0  # Відстань до стартової вершини - 0
    priority_queue = [(0, start)]  # Куча для вибору мінімальної вершини
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)  # Виймаємо вершину з мінімальною відстанню
        
        # Якщо знайдений шлях вже не актуальний - пропускаємо
        if current_distance > shortest_paths[current_vertex]:
            continue
        
        # Оновлюємо сусідів поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях - оновлюємо
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

# Приклад графа (список суміжності)
graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}

# Виконання алгоритму
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

# Виведення результатів
for vertex, distance in shortest_paths.items():
    print(f"Найкоротший шлях від {start_vertex} до {vertex}: {distance}")