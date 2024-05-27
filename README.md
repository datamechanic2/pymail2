# pymail2
This library helps you send email with just an import


## How to Install

```
through PyPI
pip install pymail2
```

## How to Use

```
from pymail2 import PyMail

email_obj = PyMail(server_type = 'GMAIL', 
                    user = 'abc@example.com',
                    password = '***', 
                    from_email = 'abc@example.com',
                    to_email = 'xyz@example.com', 
                    subject = 'Your Wish',
                    template_path = 'path_for_the_html_template'
                 )

email_obj.send()

```

## Need Help

Please add Issues through which I can help you in improving the library. 

