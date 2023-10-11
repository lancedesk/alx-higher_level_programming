#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Python bytes object to print information about.
 *
 * This function checks if the input object @p
 * is a valid Python bytes object.
 * If it is, it prints the size, trying string,
 * and the first 10 bytes of the bytes object.
 * If it's not a valid bytes object, it prints an error message.
 */

void print_python_bytes(PyObject *p)
{
	unsigned char i, object_size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
	{
		object_size = 10;
	}
	else
	{
		object_size = ((PyVarObject *)p)->ob_size + 1;
	}

	printf("  first %d bytes: ", object_size);

	for (i = 0; i < object_size; i++)
	{
		printf("%02hhx%s", bytes->ob_sval[i], i == object_size - 1 ? "\n" : " ");
	}
}

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Python list object to print information about.
 *
 * This function prints the size, allocated memory,
 * and the type name of each element in the list @p.
 * If an element is a bytes object, it calls the print_python_bytes
 * function to print information about the bytes object.
*/

void print_python_list(PyObject *p)
{
	int allocated, i, object_size;
	PyVarObject *var = (PyVarObject *)p;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	object_size = var->ob_size;
	allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", object_size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < object_size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);

		if (!strcmp(type, "bytes"))
		{
			print_python_bytes(list->ob_item[i]);
		}
	}
}

