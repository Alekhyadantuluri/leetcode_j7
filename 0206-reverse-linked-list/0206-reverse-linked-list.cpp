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
    ListNode* reverseList(ListNode* head) {
        ListNode *prev= NULL,*next = NULL;
        ListNode *c = head;
        while(c!=NULL){
            next = c->next;
            c->next = prev;
            prev = c;
            c = next; 
        }
        head = prev;
        return head;
    }
};