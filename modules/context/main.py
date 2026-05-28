from shared.constants import URL, STATE_PATH

def create_context(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)
    try:
        page.get_by_role("button",name="Agree and close").click(timeout=3000)
    except:
        pass
    try:
        page.get_by_role("button",name="Close").click(timeout=3000)
    except:
        pass
    context.storage_state(path=STATE_PATH)
    context.close()