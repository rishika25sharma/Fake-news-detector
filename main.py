def detect_fake_news(text):
    fake_keywords = ["shocking", "click here", "breaking", "viral", "urgent"]
    
    for word in fake_keywords:
        if word in text.lower():
            return "⚠️ Likely Fake News"
    
    return "✅ Likely Real News"


user_input = input("Enter news text: ")
print(detect_fake_news(user_input))