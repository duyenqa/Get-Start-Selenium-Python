# Get starting Selenium
[Refer Document Selenium](https://www.selenium.dev/documentation/webdriver/)

# Get starting Pytest
[Refer Document Pytest](https://docs.pytest.org/en/stable/getting-started.html)

## Find element

| Method                                          | Description                                                                        |
|-------------------------------------------------|------------------------------------------------------------------------------------|
|find_element(By.XPATH, "string xpath")           |Finds the first element matching the given XPath expression.                        |
|find_element(By.ID, "string id")                 |Finds the element with the specified ID attribute.                                  |
|find_element(By.NAME, "name of attribute")       |Finds the element with the specified name attribute.                                |
|find_element(By.CLASS_NAME, "string class")      |Finds the element with the specified class attribute.                               |
|find_element(By.TAG_NAME, "string tag")          |Finds the element with the specified tag name.                                      |
|find_element(By.CSS_SELECTOR, ".name_attribute") |Finds the element with the specified CSS Selector.                                  |
|find_element(By.LINK_TEXT, "string text")        |Finds the anchor element with the specified exact text.                             |
|find_element(By.PARTIAL_LINK_TEXT, "string text")|Finds the element with the specified partial text.                                  |
|send_keys(value)                                 |It simulates typing the specified value into the element                            |
|clear()                                          |Clears the text if it’s a text entry element.                                       |
|click()                                          |It simulates clicking on the element.                                               |
|text                                             |Retrieves the text content of the element.                                          |
|get_attribute(name)                              |Retrieves the value of the specified attribute of the element.                      |
|is_displayed()                                   |Returns True if the element is visible on the page, False otherwise.                |
|is_enabled()                                     |Returns True if the element is enabled for interaction, False otherwise.            |
|is_selected()                                    |Returns True if the element (checkbox or radio button) is selected, False otherwise.|

## Author:
Ngô Thị Kim Duyên
