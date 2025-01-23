import argparse
from get_paper.fetch_papers import PubMedFetcher

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument('query', type=str, help='Search query for PubMed.')
    parser.add_argument('-d', '--debug', action='store_true', help='Print debug information.')
    parser.add_argument('-f', '--file', type=str, help='Filename to save the results as CSV.')
    
    args = parser.parse_args()
    
    fetcher = PubMedFetcher(args.query)
    
    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    papers = fetcher.fetch_papers()
    filtered_papers = fetcher.filter_non_academic_authors(papers)
    
    if args.file:
        fetcher.to_csv(filtered_papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in filtered_papers:
            print(paper)

if __name__ == "__main__":
    main()
