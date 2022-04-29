#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert a node in a sorted list
 * @head: pointer to head of list
 * @number: number to add and sort in the list
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *aux;

	if (!number || !head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	aux = *head;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (number < aux->n)
	{
		new->next = aux;
		*head = new;
		return (new);
	}
	while (aux)
	{

		if (!aux->next && number > aux->n)
		{
			aux->next = new;
			new->next = NULL;
			return (new);
		}
		else if (number < (aux->next)->n)
		{
			new->next = aux->next;
			aux->next = new;
			return (new);
		}
		aux = aux->next;
	}
	return (NULL);
}