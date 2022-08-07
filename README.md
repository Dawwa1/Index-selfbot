# Foxxy Discord Bot

Foxxy is a discord bot that I am making, designed to make have a ton of features while also being minimalistic and easy to use!

## Installation

Download the folder, and install everything in the requirments.txt file

```bash
pip install -r requirements.txt
```

Configuring the bot is pretty self explanatory

```json
{
    "token":"",
    "keywords": ["This Spawn Contains a Wishlisted Servant", "Has triggered a Server spawn"],
    "send_channel":"",
    "ping_OnAlert": false
}
```

Token: your discord ACCOUNT token

keywords: the keywords that the bot will look for

send_channel: the channel that the bot will send the alert to

ping_OnAlert: whether or not you want the bot to ping @everyone on an alert

To start the bot, either double click on main.py or open it with command prompt

```bash
python main.py
```

## Contributing
If you want to contribute to this project, be welcome to open a pull request!

## License
MIT License

Copyright (c) 2022 Dawwa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
