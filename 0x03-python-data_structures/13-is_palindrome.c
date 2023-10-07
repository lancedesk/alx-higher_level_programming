#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head node of the list.
 * Return: 1 if palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	/* Find the middle of the list using slow and fast pointers */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	/* If the list has an odd number of nodes, skip the middle one */
	if (fast != NULL)
	{
		slow = slow->next;
	}

	/* Compare the first half and reversed second half of the list */
	while (slow != NULL)
	{
		if (slow->n != prev->n)
		{
			return (0);
		}
		slow = slow->next;
		prev = prev->next;
	}

	return (1);
}
