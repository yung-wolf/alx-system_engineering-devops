#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - runs an infinite while loop
 * Return: 0 on success
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - runs main code
 * Return: 0 on success
 */
int main(void)
{
	pid_t child_pid;
	int i;

	i = 0;

	while (i < 5)
	{
		child_pid = fork();

		if (child_pid == 0)
			exit(0);
		else if (child_pid > 0)
			printf("Zombie process created, PID:%d\n", (int)child_pid);
		else
		{
			perror("fork");
			exit(1);
		}
		i++;
	}

	return (infinite_while());
}
