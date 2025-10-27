#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *link;
};
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
    
    
    printf("%d",ptr->data);
    return 0;
    
}