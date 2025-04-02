import datetime
import logging
import subprocess
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info('Timer function triggered at %s', datetime.datetime.utcnow())

    try:
        result = subprocess.run(["Rscript", "-e" "epiverse.scraper::get_universe_docs(destdir = 'sources')"], check=True, capture_output=True, text=True)
        logging.info("R script output:\n" + result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("Error running R script:\n" + e.stderr)
