import sys
import requests
import re
import pandas as pd
from datetime import datetime
from tqdm import tqdm

def check_input(arguments):
    if len(arguments) == 1:
        sys.exit("No word is provided")

def define_word(word):
    if not word:
        return None
    api_key = "2defa2b9-0852-4e37-8112-b6488bd15567"
    response = requests.get("https://www.dictionaryapi.com/api/v3/references/learners/json/" + word+ "?key=" + api_key)
    return response.json()

def parser(raw_input):
    entry = {"word": None, "part_of_speech": None, "definition": None, "eg_sentence_bank":[], "time":datetime.now().isoformat(timespec="hours")}
    word= raw_input[0]["meta"]["app-shortdef"]["hw"]
    entry["word"] = re.sub(r":\d+", "", word)
    entry["part_of_speech"] = raw_input[0]["meta"]["app-shortdef"]["fl"]
    entry["definition"] = raw_input[0]["meta"]["app-shortdef"]["def"][0]
    entry["definition"] = re.sub(r"{.*}", "", entry["definition"])
    sentence_count = 0
    while True:
        try:
            sentence = raw_input[0]["def"][0]["sseq"][0][0][1]["dt"][1][1][sentence_count]["t"]
            sentence = re.sub(r"{/.*}", "", sentence)
            sentence = re.sub(r"{.*}", "", sentence)
            sentence = re.sub(r"\[.*\]", "", sentence)
            entry["eg_sentence_bank"].append(sentence)
            sentence_count += 1
        except:
            break
    if not entry["eg_sentence_bank"]:
        entry["eg_sentence_bank"] = "NIL"
    return entry

def main():
    check_input(sys.argv)
    word_list = []

    pbar = tqdm(sys.argv[1:])
    for undefined_word in pbar:
        try:
            defined_word = define_word(undefined_word)
            parsed_word = parser(defined_word)
            word_list.append(parsed_word)
        except:
            print(f"{undefined_word} is not found")
        finally:
            pbar.set_description(f"Processed {undefined_word}")

    df = pd.DataFrame(word_list)
    print(df[["word","part_of_speech","definition"]].to_markdown())

    if df.empty:
        sys.exit("No words found! Pls try again!")

    create_csv = input("Do you wish to save these words?(y/n) ").lower()
    if create_csv == "y":
      name = input("csv filename: ")
      df.to_csv(name)


if __name__ == "__main__":
    main()