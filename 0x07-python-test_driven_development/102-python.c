#include <Python.h>

/**
 * print_python_string - Prints info about Python strings.
 * @p: A pointer to a PyObject representing a Python string object.
 */

void print_python_string(PyObject *p)
{
	long int length;
	char *sting_input;

	fflush(stdout);

	printf("[.] string object info\n");

	string_input = p->ob_type->tp_name;

	if (strcmp(string_input, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact ascii\n");
	}
	else
	{
		printf("  type: compact unicode object\n");
	}

	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
