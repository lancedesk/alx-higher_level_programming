#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic information about Python list objects.
 * @p: A pointer to a Python list object.
 *
 * This function prints the size, allocated space, and elements' types of
 * the Python list object.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocation, i;
	PyListObject *list = (PyListObject *)p;
	const char *type;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocation = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");

		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocation);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;

		printf("Element %ld: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
		else if (strcmp(type, "float") == 0)
		{
			print_python_float(list->ob_item[i]);
		}
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
	Py_ssize_t size, i;
	PyBytesObject *bytes_number = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes_number->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
	{
		size = 10;
	}
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}

	printf("  first %ld bytes: ", size);

	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes_number->ob_sval[i]);
		if (i == (size - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
	}
}

/**
 * print_python_float - Prints basic information about Python float objects.
 * @p: A pointer to a Python float object.
 *
 * This function prints the value of the Python float object.
 */

void print_python_float(PyObject *p)
{
	char *memory = NULL;

	PyFloatObject *float_object = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");

		return;
	}

	memory = PyOS_double_to_string(float_object->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", memory);

	PyMem_Free(memory);
}

