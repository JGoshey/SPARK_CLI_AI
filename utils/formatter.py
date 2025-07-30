def format_output(response, use_rich):
    if not use_rich:
        return response

    try:
        from rich import print as rprint
        rprint(f"\n[bold green]Assistant:[/bold green] {response}")
        return ""
    except:
        return response