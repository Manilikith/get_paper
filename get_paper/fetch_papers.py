import requests
import pandas as pd
from typing import List

class PubMedFetcher:
    def __init__(self, query: str):
        self.query = query
        self.base_url = "https://api.ncbi.nlm.nih.gov/lit/ctxp/v1/pubmed/"

    def fetch_papers(self) -> List[dict]:
        response = requests.get(f"{self.base_url}?term={self.query}")
        response.raise_for_status()
        return response.json().get('documents', [])

    def filter_non_academic_authors(self, papers: List[dict]) -> List[dict]:
        filtered_papers = []
        for paper in papers:
            non_academic_authors = []
            company_affiliations = []
            for author in paper.get('authors', []):
                if 'pharma' in author.get('affiliation', '').lower() or 'biotech' in author.get('affiliation', '').lower():
                    non_academic_authors.append(author['name'])
                    company_affiliations.append(author['affiliation'])
            if non_academic_authors:
                paper['non_academic_authors'] = non_academic_authors
                paper['company_affiliations'] = company_affiliations
                filtered_papers.append(paper)
        return filtered_papers

    def to_csv(self, papers: List[dict], file_name: str):
        df = pd.DataFrame([{
            'PubmedID': paper['uid'],
            'Title': paper['title'],
            'Publication Date': paper['pubdate'],
            'Non-academic Author(s)': ', '.join(paper['non_academic_authors']),
            'Company Affiliation(s)': ', '.join(paper['company_affiliations']),
            'Corresponding Author Email': paper.get('corresponding_author', {}).get('email', 'N/A')
        } for paper in papers])
        df.to_csv(file_name, index=False)
