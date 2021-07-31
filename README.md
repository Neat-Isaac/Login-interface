# Login Interface

### Caption

This is an interface programmed using __Python__.

_Attention,it's ***interface,interface,interface!***_

### Usage method

When using,call the `login.login()` function first,and then use the __variable__`login.ID` and `login.PASSWORD`（Int type） to get the user's ID and password.

Such as

```python
import login
login.login()
if login.ID == 4096:
	print("Hello,Administrator!")
else:
	print("Hello,",login.ID)
```

### Features

Since it is a login interface,this interface will judge the correctness of ID and password and pop up a prompt after the user enters ID and password.

__It doesn't need you to program the program to judge the correctness of ID and password!__

In addition,there are some preset ID and passwords in this interface,which can be used directly.

The file that stores the user ID and password is `data.neat`_（Don't ask me why I set the file suffix to `.neat`,look at my name!）_



