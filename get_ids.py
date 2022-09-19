import json
import datetime

def import_runs():
  runs_file = 'runs.response'
  f = open(runs_file)
  data = json.load(f)

def get_runs(from_date, to_date):
  runs = []
  for run in data['value']:
    run_date = datetime.fromisoformat(run.createdDate)
    if run_date >= from_date && run_date <= to_date && run.result == "succeeded":
      runs.append(run.id)
  return runs

runs_file = 'runs.response'
f = open(runs_file)
data = json.load(f)
from_date = datetime.date(2022, 9, 17)
to_date = datetime.date(2022, 9, 18)
runs = get_runs(from_date, to_date)
return runs
f.close()