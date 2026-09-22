'''
332. Reconstruct Itinerary

You are given a list of airline tickets where tickets[i] = [fromi, toi]
represent the departure and arrival airports.

Reconstruct the itinerary in order and return it.

Rules:
    - Begin the itinerary with "JFK".
    - Use all tickets exactly once.
    - If multiple valid itineraries exist, return the itinerary with the
      smallest lexical order.

Example 1:
    Input:
        tickets = [
            ["MUC","LHR"],
            ["JFK","MUC"],
            ["SFO","SJC"],
            ["LHR","SFO"]
        ]

    Output:
        ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
    Input:
        tickets = [
            ["JFK","SFO"],
            ["JFK","ATL"],
            ["SFO","ATL"],
            ["ATL","JFK"],
            ["ATL","SFO"]
        ]

    Output:
        ["JFK","ATL","JFK","SFO","ATL","SFO"]

Constraints:
    1 <= tickets.length <= 300
    tickets[i].length == 2
    fromi.length == 3
    toi.length == 3
    fromi and toi consist of uppercase English letters.
'''

# Eulerian Path + Hierholzer's Algorithm

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Min-heap preserves lexical order.
        for source, destination in tickets:
            heapq.heappush(graph[source], destination)

        itinerary = []

        def dfs(airport: str) -> None:
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)

            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]


# Example usage
solution = Solution()

# Example 1
tickets1 = [
    ["MUC","LHR"],
    ["JFK","MUC"],
    ["SFO","SJC"],
    ["LHR","SFO"]
]

print(solution.findItinerary(tickets1))
# Output: ['JFK','MUC','LHR','SFO','SJC']

# Example 2
tickets2 = [
    ["JFK","SFO"],
    ["JFK","ATL"],
    ["SFO","ATL"],
    ["ATL","JFK"],
    ["ATL","SFO"]
]

print(solution.findItinerary(tickets2))
# Output: ['JFK','ATL','JFK','SFO','ATL','SFO']

# Example 3
tickets3 = [
    ["JFK","KUL"],
    ["JFK","NRT"],
    ["NRT","JFK"]
]

print(solution.findItinerary(tickets3))
# Output: ['JFK','NRT','JFK','KUL']

# Example 4
tickets4 = [
    ["JFK","A"],
    ["A","B"],
    ["B","JFK"],
    ["JFK","C"]
]

print(solution.findItinerary(tickets4))
# Output: ['JFK','A','B','JFK','C']

# Example 5
tickets5 = [
    ["JFK","AAA"],
    ["AAA","BBB"],
    ["BBB","CCC"],
    ["CCC","JFK"]
]

print(solution.findItinerary(tickets5))
# Output: ['JFK','AAA','BBB','CCC','JFK']

# Example 6
tickets6 = [
    ["JFK","ATL"],
    ["ATL","SFO"],
    ["SFO","JFK"]
]

print(solution.findItinerary(tickets6))
# Output: ['JFK','ATL','SFO','JFK']
