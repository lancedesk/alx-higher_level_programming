#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints basic information about Python list objects.
 * @p: A pointer to a Python list object.
 *
 * This function prints the size, allocated space, and elements' types of
 * the Python list object.
 */

void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);

		if (item == NULL)
		{
			fprintf(stderr, "[ERROR] Invalid List Object\n");
			return;
		}
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic information about Python byte objects.
 * @p: A pointer to a Python byte object.
 *
 * This function prints the size, string representation, and first 10 bytes
 * of the Python byte object.
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	Py_ssize_t size, i;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; ++i)
	{
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints basic information about Python float objects.
 * @p: A pointer to a Python float object.
 *
 * This function prints the value of the Python float object.
 */

void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	float_obj = (PyFloatObject *)p;

	printf("[.] float object info\n");
	printf("  value: %f\n", float_obj->ob_fval);
}

