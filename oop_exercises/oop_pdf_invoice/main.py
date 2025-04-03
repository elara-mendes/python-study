from fpdf import FPDF
import pandas as pd

df = pd.read_csv("articles.csv", dtype={"id":str})
print(df)

class PDF:

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)

        for i, row in df.iterrows():
            print(row["name"])
            print(row["id"])
            print(row["price"])
            content = f"""
            ID: {row["id"]}\n
            Name: {row["name"]}\n
            Price: {row["price"]}
            """

            pdf.add_page()

            pdf.set_font(family="Times", size=24, style="B")
            pdf.set_text_color(100, 100, 100)
            pdf.multi_cell(w=0, h=12, txt=content, align="L")

            pdf.output("test.pdf")



class Article:

    def __init__(self, id_article):
        self.id_article = id_article

    def available(self):
        name = df.loc[df["id"] == self.id_article, "name"]
        return not name.empty

    def quantity(self):
        df.loc[df["id"] == self.id_article, "in stock"] -= 1
        df.to_csv("articles.csv", index=False)


article_ask = input("Choose an article to buy: ")
article = Article(article_ask)
pdf = PDF()
if article.available():
    print("Yes")
    article.quantity()
    pdf.generate()
else:
    print("No")

