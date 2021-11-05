# LS 190: Song Recommender bot

## Training

To train the model:

1. Run `csv_to_spacy.py` on an updated copy of `classify.csv` to create `train.spacy`
2. Run the following command to train the spaCy classifier

```bash
python -m spacy train config/base.cfg --output ./data --paths.train ./train.spacy --paths.dev ./train.spacy
```

## Running the bot

* To run the bot, `python main.py`
* When finished running the script for testing `CTRL + C` the process to kill it
* Further automation of the bot as a "daemon" (long-running, independent process) is possible via a `crontab` "job"
  * This isn't possible without administrator consent on the JupyterHub

## "Publishing" the bot

1. Obtain a bot account from [dev.twitter.com](https://dev.twitter.com)
2. Create the aforementioned `crontab` "job"

