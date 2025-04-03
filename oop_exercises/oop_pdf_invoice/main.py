from fpdf import FPDF
import pandas as pd

df = pd.read_csv("articles.csv", dtype={"id":str})
print(df)

class Article:

    def __init__(self, id_article):
        self.id_article = id_article
        self.content = None

    def available(self):
        name = df.loc[df["id"] == self.id_article, "name"]
        return not name.empty

    def row(self):
        article_row = df[df["id"] == self.id_article]
        row = article_row.iloc[0]
        self.content = f"ID: {row['id']}\nName: {row['name']}\nPrice: {row['price']}"
        return self.content

    def quantity(self):
        df.loc[df["id"] == self.id_article, "in stock"] -= 1
        df.to_csv("articles.csv", index=False)

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.add_page()

        pdf.set_font(family="Times", size=24, style="B")
        pdf.set_text_color(100, 100, 100)
        pdf.multi_cell(w=0, h=12, txt=self.content, align="L")

        pdf.output("test.pdf")


article_ask = input("Choose an article to buy: ")
article = Article(article_ask)
pdf = Article(article_ask)
if article.available():
    print("Yes")
    article.quantity()
    pdf.row()
    pdf.generate()
else:
    print("No")

