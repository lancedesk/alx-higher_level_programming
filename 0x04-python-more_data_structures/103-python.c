#include <Python.h>
#include <stdio.h>

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
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %ld\n", PyBytes_Size(p));
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first 10 bytes: ");
		unsigned long size = PyBytes_Size(p);
		unsigned long i;
		for (i = 0; i < size && i < 10; ++i)
			printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Prints information about a Python list object.
 * @p: Python list object to print information about.
 *
 * This function prints the size, allocated memory,
 * and the type name of each element in the list @p.
 * If an element is a bytes object, it calls the print_python_byte
 * function to print information about the bytes object.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
