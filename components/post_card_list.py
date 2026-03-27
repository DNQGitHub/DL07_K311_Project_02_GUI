import components.post_card as post_card

def display(posts):
    for index, row in posts.iterrows():
        post_card.display(row, index)