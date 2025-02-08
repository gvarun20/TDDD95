#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

class BITree {
public:
    vector<int> tree;
    int size;

    BITree(int n) {
        size = n;
        tree.resize(n, 0);
    }

    int getPrefixSum(int idx) {
        int total = 0;
        while (idx >= 0) {
            total += tree[idx];
            idx = (idx & (idx + 1)) - 1;
        }
        return total;
    }

    void addValue(int idx, int value) {
        while (idx < size) {
            tree[idx] += value;
            idx = idx | (idx + 1);
        }
    }
};

vector<int> calculateSwaps(int totalElements, unordered_map<int, int> &elementPosition) {
    vector<int> swapResults;
    int leftPtr = 1, rightPtr = totalElements;
    BITree leftAdjust(totalElements), rightAdjust(totalElements);
    bool moveRight = false;

    while (leftPtr <= rightPtr) {
        if (moveRight) {
            int currentElement = rightPtr;
            int originalIdx = elementPosition[currentElement];
            int adjustedIdx = originalIdx - leftAdjust.getPrefixSum(originalIdx) + rightAdjust.getPrefixSum(totalElements - 1 - originalIdx);
            int swapCount = abs(currentElement - 1 - adjustedIdx);
            swapResults.push_back(swapCount);
            
            if (swapCount > 0) {
                leftAdjust.addValue(originalIdx, 1);
            }
            moveRight = false;
            rightPtr--;
        } else {
            int currentElement = leftPtr;
            int originalIdx = elementPosition[currentElement];
            int adjustedIdx = originalIdx - leftAdjust.getPrefixSum(originalIdx) + rightAdjust.getPrefixSum(totalElements - 1 - originalIdx);
            int swapCount = abs(currentElement - 1 - adjustedIdx);
            swapResults.push_back(swapCount);
            
            if (swapCount > 0) {
                rightAdjust.addValue(totalElements - 1 - originalIdx, 1);
            }
            moveRight = true;
            leftPtr++;
        }
    }
    return swapResults;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int numElements, inputElement;
    while (cin >> numElements) {
        vector<int> dataList(numElements);
        unordered_map<int, int> positionMap;

        for (int i = 0; i < numElements; ++i) {
            cin >> inputElement;
            positionMap[inputElement] = i;
        }

        vector<int> resultSwaps = calculateSwaps(numElements, positionMap);
        for (const int& swaps : resultSwaps) {
            cout << swaps << '\n';
        }
    }
    return 0;
}
