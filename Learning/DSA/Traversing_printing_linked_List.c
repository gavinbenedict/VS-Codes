
#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *link;
};
void countnode(struct node *head)
{
    int count=0;
    if(head==NULL)
    {
        printf("Linked List Empty!");
        //exit();
    }
    else{
        struct node *ptr=NULL;
        ptr=head;
        while(ptr!=NULL)
        {
            count++;
            printf("In node %d =%d\n",count,ptr->data);
            ptr=ptr->link;
        }
        printf("Totoal nodes=%d",count);
    }
}



int main() 
{
    struct node *head=NULL;
    head=(struct node*)malloc(sizeof(struct node));
    head->data=45;
    head->link=NULL;
    
    struct node *ptr=NULL;
    ptr=(struct node*)malloc(sizeof(struct node));
    ptr->data=98;
    ptr->link=NULL;
    
    head->link=ptr;
    
    ptr=malloc(sizeof(struct node));
    ptr->data=3;
    ptr->link=NULL;

    head->link->link=ptr;
        
    countnode(head);
    return 0;
    
}