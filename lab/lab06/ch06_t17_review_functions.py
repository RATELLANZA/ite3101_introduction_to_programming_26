def shut_down(s: str) -> str:
    if s == "yes":
        return "Shutting down"
    if s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"
