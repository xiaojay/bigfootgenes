from wikitools import wiki
from wikitools import category

def save_snps():
    """save snps from snpedia"""
    site = wiki.Wiki("http://bots.snpedia.com/api.php")                  # open snpedia
    snps = category.Category(site, "Is_a_snp")
    snpedia = []
    for article in snps.getAllMembersGen(namespaces=[0]):   # get all snp-names as list and print them
        snpedia.append(article.title.lower())
        print article.title


