def safe_input(t):
    while True:
        cmd = input("> ").strip().lower()
        if cmd in ("", "q", "r"):
            return cmd
        else:
            print(t["wrong_key"])
            print(t["controls_hint"])