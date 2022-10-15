#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

/**
* infinite_while - function that runs an infinite while loop after
* creating the parent process and the zombie
*
* Return: 0 Always success
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
* main - function that creates five zombie processes
*
* Return: 0 Always success
*/
int main(void)
{
	pid_t pid;
	char count;

	for (count = 0; count <= 4; count++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
			exit(0);
	}
	infinite_while();

	return (EXIT_SUCCESS);
}
