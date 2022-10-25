### Bag-O-Rama Notebook

Jupter Notebook to efficiently bag content according to the BagIt specification, designed for non-coders. Requires Jupyter Notebook, as well as BagIt python (https://github.com/LibraryOfCongress/bagit-python) and the Grabbags library (https://github.com/amiaopensource/grabbags).

Note that running this notebook requires increasing the default data rate limit of Jupyter Notebook. To do this, open Anaconda Prompt and enter ```jupyter notebook –generate-config``` and open the generated config file. Locate the text that reads ```#c.NotebookApp.iopub_data_rate_limit = 1000000```, add a single '0' to '1000000', then save and close.

Experimental - use at your own risk. I cannot speak to the wisdom of kicking off Powershell inside a notebook multiple times.
