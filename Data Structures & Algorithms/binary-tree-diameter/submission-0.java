/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int diameter = 0; // Stores the maximum diameter found so far

    public int diameterOfBinaryTree(TreeNode root) {
        height(root); // Call a helper function to calculate heights and update diameter
        return diameter;
    }

    private int height(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int leftHeight = height(node.left);
        int rightHeight = height(node.right);

        // Update the global diameter if the path through the current node is longer
        diameter = Math.max(diameter, leftHeight + rightHeight); 

        // Return the height of the current subtree
        return 1 + Math.max(leftHeight, rightHeight);
    }
}
