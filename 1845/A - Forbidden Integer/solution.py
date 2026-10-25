import sys
 
 
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
 
    t = int(data[0])
    idx = 1
    out = []
 
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        x = int(data[idx + 2])
        idx += 3
 
        if x != 1:
            # We can simply take n copies of 1
            out.append("YES")
            out.append(str(n))
            out.append(" ".join(["1"] * n))
        else:
            # x == 1, so we cannot use 1
            if k == 1:
                # No numbers available
                out.append("NO")
            elif n % 2 == 0:
                # n is even, use n // 2 copies of 2
                count = n // 2
                out.append("YES")
                out.append(str(count))
                out.append(" ".join(["2"] * count))
            else:
                # n is odd
                if k >= 3:
                    # Use one 3, and the rest as 2s
                    count_2 = (n - 3) // 2
                    ans = [3] + [2] * count_2
                    out.append("YES")
                    out.append(str(len(ans)))
                    out.append(" ".join(map(str, ans)))
                else:
                    # k < 3 and x == 1 leaves only 2, which cannot sum to an odd n
                    out.append("NO")
 
    sys.stdout.write("
".join(out) + "
")
 
 
if __name__ == "__main__":
    solve()