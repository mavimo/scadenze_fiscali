# Scadenze fiscali

Create a scraper to generate a parsable output (CSV, XML,JSON, ..) of tax deadline in Italy.

## Install

Install [scrapy](http://scrapy.org/) using PIP:

```bash
sudo pip install scrapy
```

clone this repo:

```bash
git clone git@github.com:mavimo/scadenze_fiscali.git
```

## Run it

Open a terminal and go in the project folder

```bash
cd scadenze_fiscali
```

Choise the exporter, you can use ```JSON```, ```XML``` and ```CSV``` format (you can also use other exporter from scrapy, now you can run scraper using:

```bash
scrapy crawl scadenze_fiscali -o result/items.xml -t xml
```

 * ```-o```: parameter define the generated result file
 * ```-t```: pameter define the export format

## Generated data

Generated file have the following structure:

 * ```items```
   * ```item```
     * ```when```: day of deadline
     * ```who```: who need to respect this deadline
     * ```what```: the deadline description
     * ```how```: how user can "resolve" the deadline
     * ```code```: code of this deadline type
     * ```type```: type of responsability
     * ```category```: Category of user that must rquire to respect the deadline

You can find more info in the wiki (Work In Progres)

## Know issues

 * This tool grab data for the specified year information. This data is wired in code, so if you require information for a different year is required to change this information directlry in the 
spider file.
 * Exported JSON data generate have text encoding error. Is required for you to re-convert generated file.

## Disclaimer

All information will be grabbed directly from [Inland Revenue](http://www1.agenziaentrate.gov.it/documentazione/scadenzefiscali/index.htm). I don't assume responsability for data or damange that 
this data can causate.
