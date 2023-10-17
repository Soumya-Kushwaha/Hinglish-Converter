# Hinglish Converter

This repository contains the code for a Hinglish converter. The converter uses the spaCy library to identify nouns in English sentences. It then uses the Google Translate API to translate the English sentences to Hindi. Finally, it replaces the translated nouns with the original English nouns.

This converter is useful for translating English sentences to Hinglish in a way that is both accurate and fluent. It is especially useful for translating sentences that contain technical or specialized terms.

To use the converter, simply clone the repository and install the required dependencies:

```
pip install -r requirements.txt
```

Then, run the following command to translate an English sentence to Hinglish:

```
python hinglish_converter.py "English sentence to translate"
```

The converter will print the Hinglish translation of the sentence to the console.

Here is an example of how to use the converter:

```
python hinglish_converter.py "I love the new Google AI Hinglish Converter!"
```

Output:

```
मुझे नया Google AI Hinglish Converter पसंद है!
```

The converter can also be used to translate multiple English sentences to Hinglish at once. Simply pass a list of English sentences to the converter. The converter will return a list of Hinglish translations.

Here is an example of how to translate multiple English sentences to Hinglish:

```
python hinglish_converter.py ["English sentence 1 to translate", "English sentence 2 to translate"]
```

Output:

```
["Hinglish translation of sentence 1", "Hinglish translation of sentence 2"]
```

**Additional notes:**

* The converter is still under development, so there may be some errors in the translations.
* The converter uses the Google Translate API, which is a third-party service. The API may not be available at all times.
* The converter is licensed under the MIT License.
