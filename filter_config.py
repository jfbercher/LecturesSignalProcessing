c = get_config()

c.NbConvertApp.export_format = 'notebook'
c.Exporter.preprocessors = ['filters.RemoveCellWithNbInitIpy']

# Usage: jupyter nbconvert --inplace --config filter_config.py FILE.ipynb
