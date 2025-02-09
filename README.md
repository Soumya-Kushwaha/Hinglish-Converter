# Hinglish Converter 🔤

A Python tool that converts English text to Hinglish (Hindi-English hybrid) while preserving English nouns. This creates more natural-sounding translations for bilingual Hindi-English speakers.

## Features

- Converts English text to Hinglish while keeping nouns in English
- Uses spaCy for accurate noun detection
- Leverages Google Translate API for Hindi translation
- Simple and easy-to-use interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hinglish-converter.git
cd hinglish-converter
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Download the spaCy English model:
```bash
python -m spacy download en_core_web_sm
```

## Dependencies

```
spacy>=3.0.0
googletrans>=3.1.0a0
```

## Usage

### As a Module

```python
from hinglish_converter import HinglishConverter

# Initialize converter
converter = HinglishConverter()

# Convert text
english_text = "Share your feedback in the comment section."
hinglish_text = converter.convert(english_text)
print(hinglish_text)
```

### Command Line

```bash
python hinglish_converter.py
```

## Example Outputs

```
English: I had about a 30 minute demo just using this new headset.
Hinglish: मेरे पास इस नए headset का उपयोग करके लगभग 30 minute का demo था।

English: Definitely share your feedback in the comment section.
Hinglish: निश्चित रूप से comment section में अपनी feedback साझा करें।
```

## How It Works

1. Uses spaCy to identify nouns in the English text
2. Translates the full text to Hindi using Google Translate
3. Replaces the translated Hindi nouns with their original English versions
4. Returns the hybrid Hinglish text

## Limitations

- Relies on internet connection for Google Translate
- Accuracy depends on spaCy's noun detection
- May not catch all context-specific terms
- Google Translate API may have rate limits

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [spaCy](https://spacy.io/)
- Translation powered by [Google Translate](https://translate.google.com/)