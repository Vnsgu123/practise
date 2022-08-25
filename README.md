/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node* next;
};

struct node* r;
struct node* f;

struct node* head=NULL;
void insert()
{
    int w;
    printf("enter the value ");
    scanf("%d",&w);
    struct node* ptr=(struct node*)malloc(sizeof(struct node));
    ptr->data=w;
    ptr->next=NULL;
    
    if(r==NULL)
    {
        r=f=ptr;
    }
    else
    {
        r->next=ptr;
        r=ptr;
    }
}

void delete()
{
    struct node* ptr=f;
    
    if(ptr==NULL)
    {
        printf("queue is empty");
    }
    else
    {
        printf("deleted element is %d ",ptr->data);
        f=f->next;
        free(ptr);
    }
}

void display(struct node* p)
{
    while(p->next!=NULL)
    {
        printf("%d",p->data);
        p=p->next;
    }
            printf("%d",p->data);


}
int main()
{
    int p,m;
    
    while(p)
    {
        printf("press 1 for insert\n");
        printf("press 2 for delete\n");
        printf("press 3 for display\n");
        printf("press 4 for exit\n");
        
        scanf("%d",&p);
        
        switch(p)
        {
            case 1:
            insert();
            break;
            
            case 2:
            delete();
            break;
            
            case 3:
            display(f);
            break;
            
            case 4:
            exit;
            break;
            
            default :
            break;
        }


    }

    return 0;
}

