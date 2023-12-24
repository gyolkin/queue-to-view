from rich import print


def print_success_finish(message: str):
    print(f"[bold green]Выполнение завершено.[/bold green] {message}.")


def print_error(message: str):
    print(f"[bold red]Ошибка![/bold red] {message}.")


def print_success(message: str):
    print(f"[bold green]Успех![/bold green] {message}.")


def print_warning(message: str):
    print(f"[bold yellow]Внимание![/bold yellow] {message}.")
