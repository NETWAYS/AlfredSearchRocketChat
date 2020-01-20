# Search Rocket.Chat Alfred Workflow

A simple approach to search Rocket.Chat contacts and channels.

## Alfred Search Keyword

![alfred search keyword][screenshot3]

![alfred search user][screenshot1]

![alfred search channel][screenshot2]

### Modifier

You can use prefixes like **@** or **#** for browsing users or chanels. Also
simple regular expressions are allowed.

## Configuration

Create a file named ***.search_rocket_chat.alfred*** in your home directory:

```bash
cat ~/.search_rocket_chat.alfred
[Rocket.Chat]
url=https://url.to.rocket.chat
user=<token_user_id>
auth=<token>
```

Add a personal access token to it:

![personal access token][token]

## License

```
MIT License

Copyright (c) 2020 NETWAYS GmbH

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
```

[screenshot1]: screenshot1.png
[screenshot2]: screenshot2.png
[screenshot3]: screenshot3.png
[token]: token.png