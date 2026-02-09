/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void inorder(TreeNode* root, vector<TreeNode*>& nodes) {
        if (!root) return;
        inorder(root->left, nodes);
        nodes.push_back(root);
        inorder(root->right, nodes);
    }

    TreeNode* buildBalanced(int l, int r, vector<TreeNode*>& nodes) {
        if (l > r) return nullptr;

        int mid = l + (r - l) / 2;
        TreeNode* root = nodes[mid];

        root->left = buildBalanced(l, mid - 1, nodes);
        root->right = buildBalanced(mid + 1, r, nodes);

        return root;
    }

    TreeNode* balanceBST(TreeNode* root) {
        vector<TreeNode*> nodes;
        inorder(root, nodes);
        return buildBalanced(0, nodes.size() - 1, nodes);
    }
};
