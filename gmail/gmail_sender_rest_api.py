#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
import requests
import json
import sys

# -----------------------------------------------------------------------------------------
def CreateMessage(sender, to, subject, message_text=None, attachment_path=None):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
    attachment_path: Full path for attachment (dir+filename)


  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEMultipart()
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  #message['cc'] = cc
  #message['bcc'] = cc
  #msg.add_header('reply-to', return_addr)

  if message_text != None:
    msg = MIMEText(message_text, 'html')
    message.attach(msg)

  if attachment_path != None:
    content_type, encoding = mimetypes.guess_type(attachment_path)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(attachment_path, 'rb')
        msg = MIMEText(fp.read().decode('utf8'), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(attachment_path, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(attachment_path, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(attachment_path, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()

    msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
    message.attach(msg)

  try:
    return {'raw': base64.urlsafe_b64encode(message.as_string())}
  except:
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('utf8')}

# -----------------------------------------------------------------------------------------
def sendmail(to, subject, message_text_html, attachment=None):
  # Change your access code and account
  access_token = 'ya29.aaaaaaaa'
  user_id = 'your id@gmail.com'

  URL = 'https://www.googleapis.com/gmail/v1/users/'+user_id+'/messages/send'

  request_header = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + access_token,
      "X-GFE-SSL": "yes"
  }

  payload = CreateMessage(user_id, to, subject, message_text_html, attachment)

  # validate payload on https://developers.google.com/gmail/api/v1/reference/users/messages/send
  #print (payload)
  #exit(1)

  response = requests.post(URL, headers=request_header, data=json.dumps(payload))

  print(response)
  print(response.text)

# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    sendmail('receiver@gmail.com', 'subject_test', 'message_test', None)
  