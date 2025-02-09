import spacy
from googletrans import Translator

class HinglishConverter:
    """A class to convert English text to Hinglish (Hindi-English hybrid) text."""
    
    def __init__(self):
        """Initialize the converter with spaCy model and Google translator."""
        # Load English language model
        self.nlp = spacy.load("en_core_web_sm")
        self.translator = Translator()
        
    def _extract_nouns(self, text):
        """Extract nouns from the given English text using spaCy."""
        doc = self.nlp(text)
        return [token.text for token in doc if token.pos_ == "NOUN"]
    
    def _translate_text(self, text, src='en', dest='hi'):
        """Translate text using Google Translate."""
        try:
            translation = self.translator.translate(text, src=src, dest=dest)
            return translation.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text
            
    def convert(self, english_text):
        """Convert English text to Hinglish by keeping nouns in English."""
        try:
            # Extract nouns from input text
            english_nouns = self._extract_nouns(english_text)
            
            # Translate full text to Hindi
            hinglish = self._translate_text(english_text)
            
            # Replace translated nouns with original English nouns
            for noun in english_nouns:
                hindi_noun = self._translate_text(noun)
                hinglish = hinglish.replace(hindi_noun, noun)
                
            return hinglish
            
        except Exception as e:
            print(f"Conversion error: {e}")
            return english_text

def main():
    """Example usage of the HinglishConverter class."""
    converter = HinglishConverter()
    
    # Example sentences
    examples = [
        "I had about a 30 minute demo just using this new headset.",
        "Definitely share your feedback in the comment section.",
        "So even if it's a big video, I will clearly mention all the products.",
        "I was waiting for my bag."
    ]
    
    # Process each example
    print("English to Hinglish Conversion Examples:\n")
    for text in examples:
        hinglish = converter.convert(text)
        print(f"English: {text}")
        print(f"Hinglish: {hinglish}\n")

if __name__ == "__main__":
    main()