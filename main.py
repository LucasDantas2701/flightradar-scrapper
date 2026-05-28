from modules.scrappy.main import run
from playwright.sync_api import (Playwright,sync_playwright)


def main():
    with sync_playwright() as playwright:
        run(playwright)

if __name__ == "__main__":
    main()