// Including necessary libraries
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Type-defining our node.
typedef struct Node
{
    struct Node *back;
    int content;
    struct Node *ahead;
    struct Node *start;
}
Node;

// Starting main() function.
int main(void)
{
    // Initializing necessary variables
    int status = 0;
    int total = 0;
    char *tmp = malloc(sizeof(char) * 20);
    Node *start = malloc(sizeof(Node));
    Node *node = start;

    // Getting input and adding to node
    printf("Enter the numbers(Type stop to stop the loop):-\n");
    while (1)
    {
        printf("Enter a number or type 'stop' if added all the numbers: ");
        scanf("%s", tmp);
        if (strcasecmp(tmp, "stop") == 0)
        {
            node->ahead = NULL;
            break;
        }
        node->ahead = malloc(sizeof(Node));
        node->ahead->back = node;
        node->ahead->content = atoi(tmp);
        node = node->ahead;
    }

    // Printing out the result
    int j = 0;
    node = start->ahead;
    printf("Node is:-\n");
    while (node != NULL)
    {
        printf("%i\n", node->content);
        node = node->ahead;
    }
}