import scraper

# getTagImage(), getCelebrity(), getOCR()

def main():
    links = ["example.com", "example.com/2"]
    for link in links:
        print("This is the tag image data")
        print("===========================")
        print(scraper.getTagImage(link))
        print("\n\n\n\n")

        print("This is the celebrity data")
        print("===========================")
        print(scraper.getCelebrity(link))
        print("\n\n\n\n")

        print("This is the OCR data")
        print("===========================")
        print(scraper.getOCR(link))

main()