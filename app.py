def greet(name: str = "Vishal") -> str:
	"""Return a greeting message for the given name."""
	return f"Hello {name} Welcome to CI/CD workflow"


if __name__ == "__main__":
	print(greet())


