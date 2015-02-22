Ionic Framework Extended Autocomplete
============================

This is the most complete ST2/ST3 plugin to auto complete Ionic Framework directives, services and **elements**. 

This plugins has a different approach from other plugins. It aims to be the most handful tool to help you to build great apps with Ionic, however it does not intends to overcome your mandatory knowledge over the framework. 

If you wants to create a list of items, for instance, you must know what elements are part of a "Ionic List", because **Ionic Framework Extended AutoComplete only will help you with the elements**:
```
<!-- Element generated separately -->
<ion-list> 
	<!-- Element generated separately -->
	<ion-item href="#"></ion-item>
</ion-list>
``` 
```
<!-- Element generated separately. You must know that you have to create a div with 'list' class. The plugin won't generate a whole list for you. -->
<div class="list">
<!-- Element generated separately -->
	<a class="item">
	
	</a>
</div>
``` 

So, why use this plugin?
-------
The Ionic Framework Extended AutoComplete has almost all html completions of Ionic directives and has **more than 300 snippets of elements and services, among color and types combinations**! It is based on the most recent version, the [1.0.0-beta.14 "magnesium-mongoose"](https://github.com/driftyco/ionic/releases/tag/v1.0.0-beta.14). 

Let's take a look in another example. If you want a list of thumbnails, just **create a DIV with list class** (or use **ion-list** provided as well) and search for **ionic-item-thumbnail-left** (or right if you want) and done:

```
<div class="list">
	<a class="item item-thumbnail-left" href="#">
		<img src="image_source">
		<h2>title</h2>
		<p>description</p>
	</a>
</div>
```  
Again, this plugin won't generate to you a whole thumbnail list, but will, for certain, help you to build one more quickly, assuming that you know to build one. Got me?

You can see the whole plugin reference [here](#Reference). 

How to contribute?
-------
You can contribute submitting issues, forking and sending pull requests. Attempt to two files: "html_completions.py" and "snippets.py". 

The first one is a basic Sublime Text plugin file that handles the html only autocomplete. To change or add Ionic directives, please refer to **html_completions.py** file.

Last one is a regular python script. It handles all snippets files generation (Do you think that I would create all these file by hand? ;) ). So, if you want to submit a new snippet or a fix to an existent one, please refer to **snippets.py** file.

Contribute and let's make a even better plugin to the awesome Ionic Framework. :D

Finally, how to install this awesome plugin?
-------

 1. First, if you didn't install yet, you must install the Package Control;
 2. Once installed, open the **Command Palette** and search for **Ionic Framework Extended Autocomplete** and install it. 

And you are done. You don't need to configure anything. Just install it, use it and start ASAP a new awesome Ionic app. 

Credits
-------
There are two related plugins for ST2/ST3 that provides snippets and completions for Ionic Framework. They are:

 - [Ionic Snippets - Sublime Plugin](https://github.com/PixelDropInc/ionic-snippets-sublime-plugin)
 - [Ionic - Sublime Plugin](https://github.com/imsingh/ionic-sublime-plugin)

They are far from the covering of this plugin, however they have a different approach. They provide big snippets (the second one, in recent updates has been breaking down some pieces too) instead of parts of elements. If you are interested in generate whole stuff like tabs, list (with pre established items), etc. please refer to them.

I must say that [Ionic - Sublime Plugin](https://github.com/imsingh/ionic-sublime-plugin) was my inspiration. In early releases I even contribute to the plugin. But I wanted more control over the what would be generated, so I developed this plugin.

Reference
---------

First, you can easily find out how this plugin works in ST2/ST3 with the following tips:
 - In HTML you can type "<" followed by "ion" and all the directives will show up for you;
 - Still in HTML for CSS Components, just type "ionic-" and the snippets will popup for you;
 - In a JS script, most of snippets are services. So just type "$" followed by "ionic" and the services will be there for you;
   - Exception are from Utility snippets, such as "ionic.Platform" ou "ionic.DomUtil". You will find this snippets typing "ionic" and following the capital letter case, looking for "ionicPlatform" and "ionicDomUtil" respectively. 

But still the whole reference are put below in case of any doubts. Have fun. :)

**CSS Components**
 - [Header](#Header)
 - Content
 - Footer
 - Buttons
 - List
 - Cards
 - Forms
 - Toggle
 - Checkbox
 - Radio Buttons
 - Range
 - Select
 - Tabs
 - Utility

**JavaScript**
 - Action Sheet
 - Backdrop
 - Content
 - Form Inputs
 - Gesture
 - Headers/Footers
 - Lists
 - Loading
 - Modal
 - Navigation
 - Platform
 - Popover
 - Popup
 - Scroll
 - Side Menus
 - Slide Box
 - Tabs
 - Tap & Click
 - Utility
 
**CSS Components**
-------

Header
-------
Trigger -  **ionic-header-assertive:** 
```
<div class="bar bar-header bar-assertive"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-balanced:** 
```
<div class="bar bar-header bar-balanced"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-calm:** 
```
<div class="bar bar-header bar-calm"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-dark:** 
```
<div class="bar bar-header bar-dark"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-energized:** 
```
<div class="bar bar-header bar-energized"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-light:** 
```
<div class="bar bar-header bar-light"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-positive:** 
```
<div class="bar bar-header bar-positive"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-royal:** 
```
<div class="bar bar-header bar-royal"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-stable:** 
```
<div class="bar bar-header bar-stable"> 
	 <h1 class="title"></h1> 
</div>

