int	main(void)
{
	char	*p;
	int		n;

	n = 2;
	p = malloc((1) * sizeof(*p));
	p = malloc((n + 1) * sizeof(*p));
	return (0);
}
> cat test2.c
int	main(void)
{
	char	*p;
	int		n;

	n = 2;
	p = malloc((1) *sizeof(*p));
	p = malloc((n + 1) *sizeof(*p));
	return (0);
}

//issue 14