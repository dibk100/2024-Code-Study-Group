from collections import deque
import copy

class Solution:
    def curriculum(self):
        N = int(input())
        indegree = [0] * (N + 1)      # 진입차수 (선행강의 개수)
        graph = [[] for i in range(N + 1)]
        time = [0] * (N + 1)         # 강의 시간

        for i in range(1, N + 1):
            info = list(map(int, input().split()))
            time[i] = info[0]

            for x in info[1:-1]:
                indegree[i] += 1
                graph[x].append(i)

        # 위상 정렬 함수
        def topology_sort():
            result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
            q = deque() # 큐 기능을 위한 deque 라이브러리 사용

            # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
            for i in range(1, N + 1):
                if indegree[i] == 0:
                    q.append(i)

            # 큐가 빌 때까지 반복
            while q:
                # 큐에서 원소 꺼내기
                now = q.popleft()
                
                # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
                for i in graph[now]:
                    result[i] = max(result[i], result[now] + time[i])
                    indegree[i] -= 1
                    # 진입차수가 0이 되는 노드를 큐에 삽입
                    if indegree[i] == 0:
                        q.append(i)

            for i in range(1, N + 1):
                print(result[i])

        topology_sort()
s = Solution()
s.curriculum()