#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle using Floyd's algorithm
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;       /* Move slow pointer by one step */
		fast = fast->next->next; /* Move fast pointer by two steps */

		if (slow == fast)
		{
			return (1); /* Cycle found */
		}
	}

	return (0); /* No cycle found */
}

