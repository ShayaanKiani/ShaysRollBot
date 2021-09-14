def create_bar(percentage):
    if percentage < 10:
        return "[⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜]"
    elif percentage >= 10 and percentage < 20:
        return "[🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜]"
    elif percentage >= 20 and percentage < 30:
        return "[🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜]"
    elif percentage >= 30 and percentage < 40:
        return "[🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜]"
    elif percentage >= 40 and percentage < 50:
        return "[🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜]"
    elif percentage >= 50 and percentage < 60:
        return "[🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜]"
    elif percentage >= 60 and percentage < 70:
        return "[🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜]"
    elif percentage >= 70 and percentage < 80:
        return "[🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜]"
    elif percentage >= 80 and percentage < 90:
        return "[🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜]"
    elif percentage >= 90 and percentage < 100:
        return "[🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜]"
    else:
        return "[🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩]"
