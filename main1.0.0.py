# Import the required modules
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import os
import asyncio
from sydney import SydneyClient
import emoji
os.environ["BING_U_COOKIE"]="1I1MDR_bVj9QxhIIJU5HowZOsYtzCvkOMcdwsRstJzpXkxzjpjjEd29O0NioO0fzAvSH0uTQGuFoIj3b8WBgppXhB_ds8EwWARjhbc0nk01UBV1EYhlWsi64-0odyf3LNKUfNz9tF6MyXrntBIF-AErX--3P_AsCV5buyC4R0IrS7Iw_fPRTiqhBR-w1GWe_sIDhGZ4fgupstGYnvNLSgqplclDJ9zNbnPmsSWuAjoho"

async def main() -> None:
    async with SydneyClient() as sydney:
        
            print(text)
            prompt = text.replace("/bing","")

            if prompt == "!reset":
                await sydney.reset_conversation()

            print("Bing: ", end="", flush=True)
            async with SydneyClient() as sydney:
                responses = []
                async for response in sydney.ask_stream(prompt):
                    responses.append(response)

            responses_text = "".join(responses)
            chunks = [responses_text[i:i + 100] for i in range(0, len(responses_text), 100)] # split the text into chunks of 100 characters

            input_box = driver.find_element(By.XPATH, "//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
            input_box.click()

            for chunk in chunks:
                input_box.send_keys(emoji.replace_emoji(chunk))

            input_box.send_keys(Keys.RETURN)
                 

driver = webdriver.Chrome()
# Whatsappi ac
driver.get("https://web.whatsapp.com/")
# Scan Qr
input("Press enter after scanning QR code")


# Kontakti bul
contact = "Aslıcık"
contact_element = driver.find_element(By.XPATH,f"//span[@title='{contact}']")
contact_element.click()


# Loop through the messages and print them
while True:
    time.sleep(10)
  # Get the HTML of the chat window
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
  # Find all the messages in the chat window
    messages = soup.find_all("div", {"class": "copyable-text"})  
    
    for message in messages:
      # Convert emojis to plain text
        for emoji in message.find_all("img", {"class": "emoji"}):
            emoji.replace_with(emoji["alt"])
      # Get the message text and sender
        text = message.span.text.strip()
        #sender = message["data-pre-plain-text"].split()[-1].strip(":")
      # Print the message text and sender
        #print(f"{sender}: {text}")
    print("-----------------------------------------------------------------------")
    
    if "/bing" in text:
        asyncio.run(main())

            
    
            
      

    
