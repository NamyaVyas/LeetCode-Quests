class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        # Build sweep events
        for x, y, l in squares:
            events.append((y, 1, x, x + l))       # square enters
            events.append((y + l, -1, x, x + l))  # square leaves
            xs.add(x)
            xs.add(x + l)

        # Coordinate compression on x
        xs = sorted(xs)
        x_id = {x: i for i, x in enumerate(xs)}

        events.sort()
        n = len(xs) - 1

        # Segment tree arrays
        cover = [0] * (4 * n)
        length = [0] * (4 * n)

        def push_up(node, l, r):
            if cover[node] > 0:
                length[node] = xs[r] - xs[l]
            elif l + 1 == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(node, l, r, ql, qr, val):
            if ql >= r or qr <= l:
                return
            if ql <= l and r <= qr:
                cover[node] += val
                push_up(node, l, r)
                return
            mid = (l + r) // 2
            update(node * 2, l, mid, ql, qr, val)
            update(node * 2 + 1, mid, r, ql, qr, val)
            push_up(node, l, r)

        # First pass: compute total union area
        total_area = 0
        prev_y = events[0][0]

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            total_area += length[1] * dy
            update(1, 0, n, x_id[x1], x_id[x2], typ)
            prev_y = y

        half = total_area / 2

        # Reset tree for second pass
        cover = [0] * (4 * n)
        length = [0] * (4 * n)

        area = 0
        prev_y = events[0][0]

        # Second pass: find minimal y where area reaches half
        for y, typ, x1, x2 in events:
            dy = y - prev_y
            slab = length[1] * dy

            if area + slab >= half:
                if length[1] == 0:
                    return float(prev_y)
                return prev_y + (half - area) / length[1]

            area += slab
            update(1, 0, n, x_id[x1], x_id[x2], typ)
            prev_y = y

        return float(prev_y)