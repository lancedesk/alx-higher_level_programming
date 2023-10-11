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
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		Py_ssize_t size;
		char *data = PyBytes_AsStringAndSize(p, &size);
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", data);
		printf("  first 10 bytes: ");
		Py_ssize_t i;
		for (i = 0; i < size && i < 10; ++i)
			printf("%02x ", (unsigned char)data[i]);
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
	PyObject *item, *iterator;

	size = PyList_Size(p);
	iterator = PyObject_GetIter(p);

	if (iterator == NULL) {
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	while ((item = PyIter_Next(iterator)) != NULL) {
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		Py_XDECREF(item);
		++i;
	}

	Py_DECREF(iterator);
}

