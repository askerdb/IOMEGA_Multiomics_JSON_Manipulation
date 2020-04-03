#!usr/bin/env python
import json
import urllib2 as ul
import shutil


def get_large_file(url, file, length=16*1024):
    req = ul.urlopen(url)
    with open(file, 'wb') as fp:
        shutil.copyfileobj(req, fp, length)

jsonfile = "paired_datarecord_50f9540c-9c9c-44e6-956c-87eabc960d7b.2.json"
url_template = "https://www.ebi.ac.uk/ena/data/warehouse/filereport?accession=%s&result=read_run&fields=fastq_ftp,"
output_base = "../../data/"

jo = json.load(open(jsonfile, 'r'))
for genome in jo["genomes"]:
    name = output_base + genome['genome_label'] + "_" +genome['genome_ID']['ENA_NCBI_accession'] + "fastq.gz"
    response = ul.urlopen(url_template % (genome['genome_ID']['ENA_NCBI_accession']))
    html = response.read()
    file_url = (html.split("\n")[1])
    print(file_url)
    get_large_file('ftp://'+file_url, name)

