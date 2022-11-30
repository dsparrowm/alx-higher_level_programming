#include "lists.h"
/**
 * insert_node - function that adds a number at the end of a list
 * @head: pointer to the first node
 * @number: the number to be added to the singly linked list
 *
 * Return: the address of the new node or Null if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}
	return (new);
}

