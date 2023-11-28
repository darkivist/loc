# Digital Collection Counting

afc_counter.py - script that prompts user for fileList.txt (ideally generated from cts-get_instances.py - example in this repo) or local path, reports extension counts, prints file category counts derived from LC digital format descriptions, then translates those into counts for the four LC reporting categories (manuscript, still-image, moving-image, and sound). If user selects local path, script will include contents of .zip and .tar archives in final report. Requires fdd_extensions_genre.csv (also in this repo) in same directory as script to run.

count_file_types.py - DEPRECATED. script that accepts a text file with list of filepaths (ideally generated from cts-get_instances.py - example in this repo) and reports file extension counts.

count_file_types_on_device.py - DEPRECATED. version of count_file_types.py that operates directly on local filesystem.

ext_genre.py - script that scrapes file extensions and corresponding genre terms from LC digital format description XML.

file_category_counter.py - DEPRECATED. combines some of the work above to print file type counts from user-provided fileList.txt. 
