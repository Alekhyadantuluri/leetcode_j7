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
    ListNode* reverse(ListNode *head){
        ListNode* cur = head;
        ListNode* next = NULL;
        ListNode* prev = NULL;
        while(cur){
            next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }
        head = prev;
        return head;
    }
    ListNode* doubleIt(ListNode* head) {
         ListNode* head1 = reverse(head);
        ListNode* temp2 = head1;
        ListNode* prev = NULL;
         int c = 0;
        while(temp2 != NULL){
            int a = temp2->val*2;
            temp2->val = c+(a)%10;
            c = a/10;
            prev = temp2;
            temp2 = temp2->next;
        }
        if (c==0){
            return reverse(head1);
        }
        ListNode *n = new ListNode(c);
        prev->next = n;
        return reverse(head1);
    }
};