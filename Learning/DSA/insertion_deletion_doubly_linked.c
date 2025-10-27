#include <stdio.h>
#include <stdlib.h>

struct node{
    struct node *prev;
    int data;
    struct node *next;
};

void disp(struct node *head)
{
    struct node *ptr=NULL;
    ptr=head;
    printf("The entire list:");
    while(ptr!=NULL)
    {
        printf(" %d ,",ptr->data);
        ptr=ptr->next;
    }
    printf("\n");
}

void insert(struct node *head, int n)
{
    struct node *ptr=head;
    while(ptr->next!=NULL)
    {
        ptr=ptr->next;
    }

    struct node *newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=n;
    newnode->next=NULL;
    newnode->prev=ptr;

    ptr->next=newnode;
}

int main()
{
    int choice;
    struct node *head=NULL;
    head=(struct node*)malloc(sizeof(struct node));
    head->data=10;
    head->next=NULL;
    head->prev=NULL;

    struct node *ptr=NULL;
    ptr=malloc(sizeof(struct node));
    ptr->data=20;
    ptr->next=NULL;
    ptr->prev=head;

    head->next=ptr;

    ptr=malloc(sizeof(struct node));
    ptr->data=30;
    ptr->next=NULL;
    ptr->prev=head->next;

    head->next->next=ptr;

    while(1)
    {
        printf("Choices:\n1.insert\n2.delete\n3.display\n4.end\n\nYour Choice:");
        scanf("%d",&choice);

        if(choice == 1)
        {
            int n;
            printf("Enter value to insert: ");
            scanf("%d", &n);
            insert(head, n);
        }
        else if(choice == 2)
        {
            printf("Delete not implemented.\n");
        }
        else if(choice == 3)
        {
            disp(head);
        }
        else if(choice == 4)
        {
            break;
        }
        else
        {
            printf("Invalid choice.\n");
        }
    }

    return 0;
}
