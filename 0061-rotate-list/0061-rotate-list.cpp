/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;

        // Step 1: Find length and last node
        ListNode* tail = head;
        int length = 1;
        while (tail->next) {
            tail = tail->next;
            length++;
        }

        // Step 2: Reduce k
        k = k % length;
        if (k == 0) return head;

        // Step 3: Make circular
        tail->next = head;

        // Step 4: Find new tail (length - k - 1 steps)
        int steps = length - k - 1;
        ListNode* newTail = head;
        while (steps--) {
            newTail = newTail->next;
        }

        // Step 5: Set new head
        ListNode* newHead = newTail->next;

        // Step 6: Break the cycle
        newTail->next = nullptr;

        return newHead;
    }
};