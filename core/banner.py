from rich.console import Console

console = Console()

def show_banner():
    console.print()
    console.print("=" * 60, style="cyan")
    console.print("               DevAgent", style="bold green")
    console.print("=" * 60, style="cyan")
    console.print()
