import csv


def print_report(pages, base_url, external_domains):
    report_text = ""
    report_text = f"""
=============================
  REPORT for {base_url}
=============================
"""
    nr_of_urls = []
    for url, count in pages.items():
        nr_of_urls.append((url, count))
    srtd_lst = sorted(nr_of_urls, key=lambda item: (item[1] * -1, item[0]))

    for url, count in srtd_lst:
        report_text += f"Found {count} internal links to {url}\n"

    nr_of_external = []
    for domain, count in external_domains.items():
        nr_of_external.append((domain, count))
    external_srtd_lst = sorted(nr_of_external, key=lambda item: (item[1] * -1, item[0]))

    report_text += "\nExternal Domains:\n"

    for domain, count in external_srtd_lst:
        report_text += f"Referenced {domain} {count} times\n"

    with open('internal_links.csv', 'w', newline='') as csv_internals:
        internal_writer = csv.writer(csv_internals, delimiter= ',')
        internal_writer.writerow(['URL', 'Count'])

        for url, count in pages.items():
            internal_writer.writerow([url, count])

    with open('external_domains.csv', 'w', newline='') as csv_externals:
        external_writer = csv.writer(csv_externals, delimiter= ',')
        external_writer.writerow(['Domain', 'Count'])

        for domain, count in external_domains.items():
            external_writer.writerow([domain, count])

    print("CSV files internal_links and external_domains generated locally.")

    return report_text
