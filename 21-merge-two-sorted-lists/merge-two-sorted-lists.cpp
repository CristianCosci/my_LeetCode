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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* newNode = new ListNode(-1);
        ListNode* temp = newNode;
        ListNode* head1 = list1;
        ListNode* head2 = list2;

        if(head1 == NULL){
            return head2;
        } 
        if(head2 == NULL){
            return head1;
        }

        while(head1 != NULL && head2 != NULL){
            if(head1->val <= head2->val){
                temp->next = head1;
                temp = head1;
                head1 = head1->next;
            }else{
                temp->next = head2;
                temp = head2;
                head2 = head2->next;
            }
        }
        
        if(head1 != NULL){
            temp->next = head1;
        }
        if(head2 != NULL){
            temp->next = head2;
        }

        return newNode->next;
        
    }
};