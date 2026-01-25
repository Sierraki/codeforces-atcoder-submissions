import sys
import math

# 增加递归深度，虽然这里主要用迭代，但作为保险
sys.setrecursionlimit(300000)

class Vector:
    __slots__ = ('x', 'y', 'orig_idx')
    
    def __init__(self, x, y):
        # 归一化：除以最大公约数
        if x == 0 and y == 0:
            # 题目保证不为(0,0)，但为了代码健壮性保留
            g = 1
        else:
            g = math.gcd(x, y)
        
        self.x = x // g
        self.y = y // g
        
    def __lt__(self, other):
        # 1. 判断半平面 (Half-plane)
        # Upper: y >= 0 (对应 0 到 pi)
        # Lower: y < 0  (对应 -pi 到 0)
        # 排序顺序: Lower -> Upper (即 -pi -> pi)
        
        is_lower_self = self.y < 0
        is_lower_other = other.y < 0
        
        if is_lower_self != is_lower_other:
            # Lower 排在 Upper 前面
            return is_lower_self
        
        # 2. 如果在同一个半平面，使用叉积判断相对顺序
        # Cross Product = x1*y2 - x2*y1
        # cp > 0 => self 在 other 的顺时针侧 (self 角度更小)
        cp = self.x * other.y - other.x * self.y
        
        if cp != 0:
            return cp > 0
            
        # 3. 极度边缘情况：叉积为0 (共线)
        # 因为我们已经做了 GCD 归一化，如果叉积为0且同在一个半平面：
        # 只有一种可能：它们是完全相同的向量，或者相反向量。
        # 但在 Upper 半平面，(1, 0) 和 (-1, 0) 是相反的且 y 都是 0。
        # (1, 0) 是 0度 (Start of Upper)，(-1, 0) 是 180度 (End of Upper)。
        # 因此，x 较大的排在前面。
        return self.x > other.x
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

def solve():
    # 使用最高效的输入读取方式
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        Q = int(next(iterator))
    except StopIteration:
        return

    # 1. 读取坐标，转换为 Vector 对象
    monsters_vecs = []
    vec_counts = {}

    for _ in range(N):
        x = int(next(iterator))
        y = int(next(iterator))
        
        v = Vector(x, y)
        monsters_vecs.append(v)
        
        if v in vec_counts:
            vec_counts[v] += 1
        else:
            vec_counts[v] = 1

    # 2. 对唯一向量进行排序
    unique_vecs = sorted(vec_counts.keys())
    
    # 3. 建立索引映射和前缀和
    total_unique = len(unique_vecs)
    vec_to_idx = {v: i for i, v in enumerate(unique_vecs)}
    
    P = [0] * (total_unique + 1)
    for i, v in enumerate(unique_vecs):
        P[i+1] = P[i] + vec_counts[v]

    # 4. 处理查询
    results = []
    for _ in range(Q):
        a_id = int(next(iterator)) - 1
        b_id = int(next(iterator)) - 1

        v_a = monsters_vecs[a_id]
        v_b = monsters_vecs[b_id]
        
        # 获取排序后的排名
        idx_a = vec_to_idx[v_a]
        idx_b = vec_to_idx[v_b]

        if idx_a == idx_b:
            # 方向完全相同
            ans = vec_counts[v_a]
        elif idx_a > idx_b:
            # 顺时针旋转：大索引 -> 小索引
            # 覆盖区间 [idx_b, idx_a]
            ans = P[idx_a + 1] - P[idx_b]
        else:
            # 顺时针旋转：跨越了 -pi/pi 切口
            # 覆盖区间 [0, idx_a] 和 [idx_b, end]
            part1 = P[idx_a + 1]
            part2 = P[total_unique] - P[idx_b]
            ans = part1 + part2
            
        results.append(str(ans))

    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()