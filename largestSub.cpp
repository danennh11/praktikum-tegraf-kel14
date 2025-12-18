#include <bits/stdc++.h>
using namespace std;

struct Node {
    int value;
    vector<Node*> children;
    
    Node(int val) : value(val) {}
};

class Tree {
private:
    Node* root;
    vector<int> longestPath;
    int maxLength;
    
    void buildTree(Node* node, vector<int>& arr, int startIdx) {
        for (int i = startIdx; i < arr.size(); i++) {
            if (arr[i] > node->value) {
                Node* child = new Node(arr[i]);
                node->children.push_back(child);
                buildTree(child, arr, i + 1);
            }
        }
    }
    
    void findLongestPath(Node* node, vector<int>& currentPath) {
        currentPath.push_back(node->value);
        
        if (currentPath.size() > maxLength) {
            maxLength = currentPath.size();
            longestPath = currentPath;
        }
        
        for (Node* child : node->children) {
            findLongestPath(child, currentPath);
        }
        
        currentPath.pop_back();
    }
    
public:
    Tree() : root(nullptr), maxLength(0) {}
    
    void build(vector<int>& arr) {
        root = new Node(INT_MIN);
        buildTree(root, arr, 0);
    }
    
    vector<int> findLIS() {
        vector<int> currentPath;
        longestPath.clear();
        maxLength = 0;
        
        for (Node* child : root->children) {
            findLongestPath(child, currentPath);
        }
        
        return longestPath;
    }
};

int main() {
    vector<int> arr = {4, 1, 13, 7, 0, 2, 8, 11, 3};
    
    Tree tree;
    tree.build(arr);
    
    vector<int> lis = tree.findLIS();
    
    for (int i = 0; i < lis.size(); i++) {
        cout << lis[i];
        if (i < lis.size() - 1) cout << " ";
    }
    cout << endl;
    
    
    return 0;
}