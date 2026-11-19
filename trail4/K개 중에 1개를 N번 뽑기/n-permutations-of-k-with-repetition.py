import sys

def main():
    K, N = map(int, sys.stdin.readline().split())
    answer = []
    out = []

    def choose(depth):
        if depth == N:
            out.append(' '.join(map(str, answer)))
            return
        for i in range(1, K + 1):
            answer.append(i)
            choose(depth + 1)
            answer.pop()

    choose(0)
    sys.stdout.write('\n'.join(out) + '\n')

main()