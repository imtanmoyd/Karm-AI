from verse_engine import get_shloka
from response_gen import generate_reflection, guiding_question, ai_response
from memory import save_prompt
from utils import detect_intent
from rich import print

def karm_response(user_input):
    print("\n[bold blue]🔍 Detecting your concern...[/bold blue]")

    intent = detect_intent(user_input)

    # === Always show the Offline Wisdom First ===
    print("\n🧘‍♂️ [bold magenta]KARM Wisdom (Offline Solution):[/bold magenta]")

    shloka = get_shloka(intent)
    if shloka:
        print(f"\n📘 [bold cyan]Gita Insight:[/bold cyan] Chapter {shloka['chapter']}, Verse {shloka['verse']}")
        print(f"[italic yellow]{shloka['shloka']}[/italic yellow]")
        print(f"🌐 Translation: {shloka['translation']}")
        print(f"🧠 Theme: [bold magenta]{shloka['theme']}[/bold magenta]")
    else:
        print("[bold red]⚠️ No direct shloka match found.[/bold red]")
        print(f"📿 [bold green]Advice:[/bold green] {generate_reflection(intent)}")

    print(f"\n💭 [bold cyan]Ask Yourself:[/bold cyan] [italic]{guiding_question(intent)}[/italic]")

    # === Try Deep AI Advice after that ===
    print("\n🤖 [bold bright_blue]AI Reflection (Deep Thinking Advice):[/bold bright_blue]")
    ai_thought = ai_response(user_input)
    print(f"[italic]{ai_thought}[/italic]")

    save_prompt(user_input)

if __name__ == "__main__":
    print("[bold bright_magenta]Welcome to KARM 💫 – Your Krishna-Inspired AI Guide.[/bold bright_magenta]")
    print("[bold cyan]Ask what’s on your mind.[/bold cyan]")

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit", "bye"]:
            print("🙏 [bold yellow]May your path be guided by wisdom. Karm Karo![/bold yellow]")
            break
        karm_response(query)
