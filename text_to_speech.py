
from gtts import gTTS
import os

# create the output directory if it doesn't exist
os.makedirs("Text To Speech", exist_ok=True)


def text_to_speech(
    text,
    lang="en",
    tld="com",
    slow=False,
    lang_check=True,
    pre_processor_funcs=None,
    tokenizer_func=None,
    timeout=None,
    output_file="output.mp3",
):
    """
    Convert the provided text to speech and save it as an audio file.
    (Full docstring kept unchanged.)
    """

    # Use default pre‑processor functions if not provided
    if pre_processor_funcs is None:
        pre_processor_funcs = [
            lambda txt: txt.replace(".", ""),  # simple example
        ]

    # Use default tokenizer if not provided
    if tokenizer_func is None:
        tokenizer_func = lambda txt: txt.split()

    try:
        # Create the gTTS object with the provided arguments
        tts = gTTS(
            text=text,
            lang=lang,
            tld=tld,
            slow=slow,
            lang_check=lang_check,
            pre_processor_funcs=pre_processor_funcs,
            tokenizer_func=tokenizer_func,
            timeout=timeout,
        )

        # Save the audio file
        output_path = os.path.join("Text To Speech", output_file)
        tts.save(output_path)
        print(f"Audio saved at {output_path}")

    except AssertionError as ae:
        print(f"Assertion Error: {ae}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")


if __name__ == "__main__":
    # Basic example (English, default options)
    sample_text = "Hello, welcome to the gTTS Python tutorial."
    text_to_speech(sample_text)
