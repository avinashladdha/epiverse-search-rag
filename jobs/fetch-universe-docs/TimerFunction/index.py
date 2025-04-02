import datetime
import logging
import subprocess
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="fetch-universe-docs")
@app.route(route="file")
@app.blob_output(arg_name="outputblob",
                 path="sources.tar.gz",
                 connection="<BLOB_CONNECTION_SETTING>")

def main(mytimer: func.TimerRequest) -> None:
    logging.info('Timer function triggered at %s', datetime.datetime.utcnow())

    try:
        result = subprocess.run(["Rscript", "-e" "epiverse.scraper::get_universe_docs(destdir = 'sources')"], check=True, capture_output=True, text=True)
        outputblob.set()
        logging.info("R script output:\n" + result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("Error running R script:\n" + e.stderr)
