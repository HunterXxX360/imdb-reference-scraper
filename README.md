# IMDB Reference Scraper

#### release-milestones
- [x] creating a scraper for any imdb movieconnections-page
- [x] getting the scraper to identify explicitly "Referenced in"-connections
- [x] creating a crawler to automatize data-collecting
- [x] writing the collected data into a .csv
- [x] accessing the scraper via argparse
- [x] rudimentary error-handling
- [ ] compiling a stable binary
- [ ] advanced error-handling
- [ ] creating an analyzer for collected data

#### documentation (for v0.2-alpha)
1. download and unzip the source-code into a path of choice
2. open the terminal and navigate to the chosen path
3. run the scraper by `$python3 imdbRefScraper.py [-args, ...]`
  * `$python 3 imdbRefScraper.py -h` shows the documentation

##### list of arguments

condition | argument (short) | argument (long) | comment
--------- | ---------------- | --------------- | -------
optional | `-h`| `--help` | show documentary
mandatory | `-d`| `--levelDepth`| how deep should the crawler follow the link-tree? (exponantial!)
optional | `-iL` | `--initialLink`| seed-link, from which the crawler starts scraping format: `'title/tt0000000'` (Default: Matrix)
optional | `-t` | `--time` | how many seconds should the scraper wait between every request? (Default: 5)
