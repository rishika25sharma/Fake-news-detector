def detect_fake_news(text):
    fake_keywords = ["shocking", "click here", "breaking", "viral", "urgent"]
    emotional_words = ["fear", "danger", "alert", "warning", "panic"]

    score = 0
    reasons = []

    # Check fake keywords
    for word in fake_keywords:
        if word in text.lower():
            score += 1
            reasons.append(f"Keyword detected: {word}")

    # Check emotional words
    for word in emotional_words:
        if word in text.lower():
            score += 1
            reasons.append(f"Emotional word detected: {word}")

    # Check excessive capital words
    words = text.split()
    caps_count = sum(1 for w in words if w.isupper())
    if caps_count > 2:
        score += 1
        reasons.append("Too many capital words")

    # Final decision
    if score >= 3:
        result = "Likely Fake News"
    else:
        result = "Likely Real News"

    return score, result, reasons


if __name__ == "__main__":
    user_input = input("Enter news text: ")

    score, result, reasons = detect_fake_news(user_input)

    print("\nScore:", score)
    print("Result:", result)
    print("Reasons:")
    for r in reasons:
        print("-", r)
