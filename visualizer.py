import matplotlib.pyplot as plt
import math


def create_graph_visualization(page_connections, limit=15):
    page_scores = []
    for page, connections in page_connections.items():
        count = len(connections)
        page_scores.append((page, count))

    srt_score = sorted(page_scores, key=lambda item: item[1], reverse=True)
    top_pages = srt_score[:limit]
    top_page_urls = [x[0] for x in top_pages]

    filtered_connections = {}
    for page in top_page_urls:
        if page in page_connections:
            all_connections = page_connections[page]
            top_connections = [url for url in all_connections if url in top_page_urls]
            filtered_connections[page] = top_connections

    positions = {}
    num_pages = len(top_page_urls)
    radius = 5

    for i, page in enumerate(top_page_urls):
        angle = (i * 2 * math.pi) / num_pages
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        positions[page] = (x, y)

    plt.figure(figsize=(12, 8))

    x_coords = []
    y_coords = []
    for page in top_page_urls:
        x, y = positions[page]
        x_coords.append(x)
        y_coords.append(y)

    plt.scatter(x_coords, y_coords, s=100, c='blue', alpha=0.7)

    for source_page, target_pages in filtered_connections.items():
        source_x, source_y = positions[source_page]

        for target_page in target_pages:
            target_x, target_y = positions[target_page]
            plt.plot([source_x, target_x], [source_y, target_y], 'k-', alpha=0.3)

    plt.title('Website Connection Graph')
    plt.axis('equal') 
    plt.savefig('connections.png')
    plt.close()

    print("Graph visualization created locally and saved as connections.png for the 15 of the most connected pages.")
