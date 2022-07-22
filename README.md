# simplicitas
*ANNOUNCEMENT*: simplicitas alpha will be releasing soon!

*NOTE*: Current version not confirmed to be functional
## 📨 Installing simplicitas
Coming soon:tm:

## ⚙️ Using simplicitas
In its alpha phase simplicitas can be easily used to create some basic CLI programs. All you need is the `simplicitas.setup()` function and a bit of creativity. Besides the simple setup that only takes 2 options (`origin` and `status`, which is set to `False` by default, so you don't need to worry about it). Besides the setup function you will need to create a dictionary which will be passed into the `origin` parameter. A quick sample code would be:
```python
sample = {
  "header": 'This is a header',
  "text": 'This is some text, it's interactable!!',
  "text": 'This is some more text...'
}

simplicitas.setup(origin=sample)
```
...and just like that you have created a very basic, yet functional CLI. 

*NOTE*: Functions *will* be included, they are being worked on as of right now (together with more features, which will be part of the alpha)!

## 🛠️ Troubleshooting
As of right now most troubleshooting consists of simply changing data-types to the correct form (e.g.: `origin` *only* accepts the type `dict`!). However, if a type can be converted easily, it already is. Troubleshooting will be a real issue when there are more complex features in the future.

## ℹ️ Contributing
You better not. Too lazy for that.
