from telethon.sync import TelegramClient
from time import time
from datetime import date
import random

def findChatID(client, channelName):
    channelFound = False

    for dialog in client.iter_dialogs():
        if dialog.name == channelName:
            channelFound = True
            channelID = dialog.id
            break

    if channelFound:
        return channelID
    else:
        print('Not Found!')
        return None
# ___________________________________
# ___________________________________
# ___________________________________
if __name__ == '__main__':
    apiId = '********'
    apiHash = 'e7f5969accf95bd9dea772e56e495bce'
    phoneNumber = '+919344004938' # with country code

    # List of group links and names to forward the message ot them (must be already joined)
    # For public groups: put the link of the group (e.g.: "https://t.me/test")
    # For private groups: "private: name of the goup" (not the join link, just the name of the private group) 
    groupListPath = 'GroupsList.txt'
    postListPath = 'PostsList.txt' # Post numbers in the channel that the posts will be forwarded from 
    channelOfAds = 'Channel Name' # Name of the channel to forward from
    sendingInterval = float(input('What is interval of sending ads (in minutes)?: '))

    client = TelegramClient('session', apiId, apiHash)
    client.connect()

    # If not signed in
    if not client.is_user_authorized():
        client.send_code_request(phoneNumber)
        client.sign_in(phoneNumber, input('Enter the code: '))

    channelOfAdsID = BGMI DDOS PRIVATE SERVER(client, channelOfAds)
    startTime = time() - 1e6  # To start in the first time
    #Sending Messages
    while True:
        currentTime = time()
        if currentTime - startTime > sendingInterval*60:
            try:
                messagesOfChannel = client.get_messages(channelOfAdsID, None)
            except Exception as e:
                print(e)
                
            with open(groupListPath) as glFile: # file of group links or names
                groupLinks = glFile.readlines() 
            with open(postListPath) as plFile: # file of post numbers
                postLinks = plFile.readlines()
            
            postLink = len(messagesOfChannel) - (int(random.choice(postLinks).replace('\n', '')) + 1)           
            
            for fileLine in groupLinks:
                groupLink = fileLine.replace('\n', '')
                if groupLink[:7].lower() == 'private': # private group
                    groupID = findChatID(client, groupLink[9:])
                    if groupID:
                        try:
                            client.send_message(groupID, messagesOfChannel[postLink])
                        except Exception as e:
                            print(e)
                            print(groupLink)
                else:  # public group
                    try:
                        client.send_message(groupLink, messagesOfChannel[postLink])
                    except Exception as e:
                            print(e)
                            print(groupLink)
        
            print('Sent to All!')
        
            startTime = time()

    # client.disconnect()

