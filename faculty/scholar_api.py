from scholarly import scholarly
from .models import ScholarCache, Faculty
from datetime import timedelta
from django.utils import timezone


def get_or_cache_best_papers(google_scholar_url, limit=8, paper_update_interval=180, citation_update_interval=20):
    if not google_scholar_url:
        return []

    try:
        cache_entry = ScholarCache.objects.get(scholar_url=google_scholar_url)
    except ScholarCache.DoesNotExist:
        cache_entry = ScholarCache(scholar_url=google_scholar_url)

    now = timezone.now()
    if cache_entry.last_updated is None:
        time_since_update = timedelta(days=180)
    else:
        time_since_update = now - cache_entry.last_updated

    papers = cache_entry.papers if time_since_update < timedelta(days=paper_update_interval) else get_best_papers(google_scholar_url, limit)

    # Update cache only if papers were re-fetched
    if time_since_update >= timedelta(days=paper_update_interval):
        cache_entry.papers = papers
        cache_entry.save()

    # Update citation count if older than citation_update_interval
    if time_since_update >= timedelta(days=citation_update_interval):
        try:
            if "user=" in google_scholar_url:
                author_id = google_scholar_url.split("user=")[1].split("&")[0]
                author = scholarly.search_author_id(author_id)
                scholarly.fill(author, sections=[])
                citation_count = author.get("citedby", 0)

                faculty_obj = Faculty.objects.get(google_scholar_url=google_scholar_url)
                faculty_obj.citation = citation_count
                faculty_obj.save()
        except Exception as e:
            print(f"Error updating citation count: {e}")

    return papers


def get_best_papers(google_scholar_url, limit=5):

    try:
        if not google_scholar_url:
            return []

        # Extracting the author ID from the URL
        if "user=" in google_scholar_url:
            author_id = google_scholar_url.split("user=")[1].split("&")[0]
        else:
            return []

        author = scholarly.search_author_id(author_id)
        scholarly.fill(author, sections=['publications'])

        publications = sorted(
            author['publications'],
            key=lambda x: x['num_citations'] if 'num_citations' in x else 0,
            reverse=True
        )

        top_papers = []
        for pub in publications[:limit]:
            scholarly.fill(pub)

            # Trying to get URL from various possible locations
            paper_url = None

            # Check common URL fields
            for url_field in ['pub_url', 'url_scholarbib', 'eprint_url']:
                if url_field in pub and pub[url_field]:
                    paper_url = pub[url_field]
                    break

            # If no URL was found, check in the bib dictionary
            if not paper_url and 'bib' in pub:
                if 'url' in pub['bib'] and pub['bib']['url']:
                    paper_url = pub['bib']['url']

            # If still no URL, create a Google Scholar search URL
            if not paper_url and 'bib' in pub and 'title' in pub['bib']:
                encoded_title = pub['bib']['title'].replace(' ', '+')
                paper_url = f"https://scholar.google.com/scholar?q={encoded_title}"

            paper_info = {
                'title': pub['bib']['title'],
                'url': paper_url or "",
                'citations': pub.get('num_citations', 0),
                'year': pub['bib'].get('pub_year', 'N/A')
            }
            top_papers.append(paper_info)

        return top_papers
    except Exception as e:
        print(f"Error fetching papers: {e}")
        return []