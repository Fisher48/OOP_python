def conquest_campaign(N, M, L, battalion):
    start_positions = set()
    for i in range(L):
        x = battalion[2 * i]
        y = battalion[2 * i + 1]
        # Проверка, что координаты в пределах поля
        if 1 <= x <= N and 1 <= y <= M:
            start_positions.add((x, y))

    # Если уже всё захвачено
    if len(start_positions) == N * M:
        return 1

    # Внутренняя рекурсивная функция
    def simulate(captured, day):
        # Проверка все ли клетки захвачены
        if len(captured) == N * M:
            return day

        # Находим всех соседей текущих захваченных клеток
        neighbors = set()
        for (x, y) in captured:
            # Четыре направления
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx = x + dx
                ny = y + dy
                if 1 <= nx <= N and 1 <= ny <= M:
                    neighbors.add((nx, ny))

        # Объединяем текущие и новые
        new_captured = captured | neighbors

        # Рекурсивный вызов на следующий день
        return simulate(new_captured, day + 1)

    return simulate(start_positions, 1)


result = conquest_campaign(3, 4, 2, [2,2, 3,4])
print(f"День полного захвата: {result}")  # 3


