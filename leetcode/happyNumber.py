def happy(n):
    visited = set()

    def square_sum(n):
        pass

    while n not in visited:
        visited.add(n)
        n = square_sum(n)

        if n == 1:
            return True
    
    return False

happy(19)