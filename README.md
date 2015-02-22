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
 - [Header](#css_header)
 - [Footer](#css_footer)
 - [Buttons](#css_buttons)
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

<h2 id="css_header">Header</h2>

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
```

<h2 id="css_footer">Footer</h2>

Trigger -  **ionic-footer-assertive:** 
```
<div class="bar bar-footer bar-assertive"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-balanced:** 
```
<div class="bar bar-footer bar-balanced"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-calm:** 
```
<div class="bar bar-footer bar-calm"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-dark:** 
```
<div class="bar bar-footer bar-dark"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-energized:** 
```
<div class="bar bar-footer bar-energized"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-light:** 
```
<div class="bar bar-footer bar-light"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-positive:** 
```
<div class="bar bar-footer bar-positive"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-royal:** 
```
<div class="bar bar-footer bar-royal"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-stable:** 
```
<div class="bar bar-footer bar-stable"> 
	 <div class="title"></div> 
</div>
```

<h2 id="css_buttons">Buttons</h2>

Trigger -  **ionic-button-assertive:** 
```
<button class="button button-assertive"></button>
```
Trigger -  **ionic-button-balanced:** 
```
<button class="button button-balanced"></button>
```
Trigger -  **ionic-button-bar-assertive:** 
```
<div class="button-bar bar-assertive"></div>
```
Trigger -  **ionic-button-bar-balanced:** 
```
<div class="button-bar bar-balanced"></div>
```
Trigger -  **ionic-button-bar-calm:** 
```
<div class="button-bar bar-calm"></div>
```
Trigger -  **ionic-button-bar-dark:** 
```
<div class="button-bar bar-dark"></div>
```
Trigger -  **ionic-button-bar-energized:** 
```
<div class="button-bar bar-energized"></div>
```
Trigger -  **ionic-button-bar-light:** 
```
<div class="button-bar bar-light"></div>
```
Trigger -  **ionic-button-bar-positive:** 
```
<div class="button-bar bar-positive"></div>
```
Trigger -  **ionic-button-bar-royal:** 
```
<div class="button-bar bar-royal"></div>
```
Trigger -  **ionic-button-bar-stable:** 
```
<div class="button-bar bar-stable"></div>
```
Trigger -  **ionic-button-block-assertive:** 
```
<button class="button button-block button-assertive"></button>
```
Trigger -  **ionic-button-block-balanced:** 
```
<button class="button button-block button-balanced"></button>
```
Trigger -  **ionic-button-block-calm:** 
```
<button class="button button-block button-calm"></button>
```
Trigger -  **ionic-button-block-dark:** 
```
<button class="button button-block button-dark"></button>
```
Trigger -  **ionic-button-block-energized:** 
```
<button class="button button-block button-energized"></button>
```
Trigger -  **ionic-button-block-light:** 
```
<button class="button button-block button-light"></button>
```
Trigger -  **ionic-button-block-positive:** 
```
<button class="button button-block button-positive"></button>
```
Trigger -  **ionic-button-block-royal:** 
```
<button class="button button-block button-royal"></button>
```
Trigger -  **ionic-button-block-stable:** 
```
<button class="button button-block button-stable"></button>
```
Trigger -  **ionic-button-calm:** 
```
<button class="button button-calm"></button>
```
Trigger -  **ionic-button-clear-assertive:** 
```
<button class="button button-clear button-assertive"></button>
```
Trigger -  **ionic-button-clear-balanced:** 
```
<button class="button button-clear button-balanced"></button>
```
Trigger -  **ionic-button-clear-calm:** 
```
<button class="button button-clear button-calm"></button>
```
Trigger -  **ionic-button-clear-dark:** 
```
<button class="button button-clear button-dark"></button>
```
Trigger -  **ionic-button-clear-energized:** 
```
<button class="button button-clear button-energized"></button>
```
Trigger -  **ionic-button-clear-light:** 
```
<button class="button button-clear button-light"></button>
```
Trigger -  **ionic-button-clear-positive:** 
```
<button class="button button-clear button-positive"></button>
```
Trigger -  **ionic-button-clear-royal:** 
```
<button class="button button-clear button-royal"></button>
```
Trigger -  **ionic-button-clear-stable:** 
```
<button class="button button-clear button-stable"></button>
```
Trigger -  **ionic-button-dark:** 
```
<button class="button button-dark"></button>
```
Trigger -  **ionic-button-energized:** 
```
<button class="button button-energized"></button>
```
Trigger -  **ionic-button-full-assertive:** 
```
<button class="button button-full button-assertive"></button>
```
Trigger -  **ionic-button-full-balanced:** 
```
<button class="button button-full button-balanced"></button>
```
Trigger -  **ionic-button-full-calm:** 
```
<button class="button button-full button-calm"></button>
```
Trigger -  **ionic-button-full-dark:** 
```
<button class="button button-full button-dark"></button>
```
Trigger -  **ionic-button-full-energized:** 
```
<button class="button button-full button-energized"></button>
```
Trigger -  **ionic-button-full-light:** 
```
<button class="button button-full button-light"></button>
```
Trigger -  **ionic-button-full-positive:** 
```
<button class="button button-full button-positive"></button>
```
Trigger -  **ionic-button-full-royal:** 
```
<button class="button button-full button-royal"></button>
```
Trigger -  **ionic-button-full-stable:** 
```
<button class="button button-full button-stable"></button>
```
Trigger -  **ionic-button-icon-left-assertive:** 
```
<button class="button icon-left ionicon button-assertive"></button>
```
Trigger -  **ionic-button-icon-left-balanced:** 
```
<button class="button icon-left ionicon button-balanced"></button>
```
Trigger -  **ionic-button-icon-left-calm:** 
```
<button class="button icon-left ionicon button-calm"></button>
```
Trigger -  **ionic-button-icon-left-dark:** 
```
<button class="button icon-left ionicon button-dark"></button>
```
Trigger -  **ionic-button-icon-left-energized:** 
```
<button class="button icon-left ionicon button-energized"></button>
```
Trigger -  **ionic-button-icon-left-light:** 
```
<button class="button icon-left ionicon button-light"></button>
```
Trigger -  **ionic-button-icon-left-positive:** 
```
<button class="button icon-left ionicon button-positive"></button>
```
Trigger -  **ionic-button-icon-left-royal:** 
```
<button class="button icon-left ionicon button-royal"></button>
```
Trigger -  **ionic-button-icon-left-stable:** 
```
<button class="button icon-left ionicon button-stable"></button>
```
Trigger -  **ionic-button-icon-right-assertive:** 
```
<button class="button icon-right ionicon button-assertive"></button>
```
Trigger -  **ionic-button-icon-right-balanced:** 
```
<button class="button icon-right ionicon button-balanced"></button>
```
Trigger -  **ionic-button-icon-right-calm:** 
```
<button class="button icon-right ionicon button-calm"></button>
```
Trigger -  **ionic-button-icon-right-dark:** 
```
<button class="button icon-right ionicon button-dark"></button>
```
Trigger -  **ionic-button-icon-right-energized:** 
```
<button class="button icon-right ionicon button-energized"></button>
```
Trigger -  **ionic-button-icon-right-light:** 
```
<button class="button icon-right ionicon button-light"></button>
```
Trigger -  **ionic-button-icon-right-positive:** 
```
<button class="button icon-right ionicon button-positive"></button>
```
Trigger -  **ionic-button-icon-right-royal:** 
```
<button class="button icon-right ionicon button-royal"></button>
```
Trigger -  **ionic-button-icon-right-stable:** 
```
<button class="button icon-right ionicon button-stable"></button>
```
Trigger -  **ionic-button-large-assertive:** 
```
<button class="button button-large button-assertive"></button>
```
Trigger -  **ionic-button-large-balanced:** 
```
<button class="button button-large button-balanced"></button>
```
Trigger -  **ionic-button-large-calm:** 
```
<button class="button button-large button-calm"></button>
```
Trigger -  **ionic-button-large-dark:** 
```
<button class="button button-large button-dark"></button>
```
Trigger -  **ionic-button-large-energized:** 
```
<button class="button button-large button-energized"></button>
```
Trigger -  **ionic-button-large-light:** 
```
<button class="button button-large button-light"></button>
```
Trigger -  **ionic-button-large-positive:** 
```
<button class="button button-large button-positive"></button>
```
Trigger -  **ionic-button-large-royal:** 
```
<button class="button button-large button-royal"></button>
```
Trigger -  **ionic-button-large-stable:** 
```
<button class="button button-large button-stable"></button>
```
Trigger -  **ionic-button-light:** 
```
<button class="button button-light"></button>
```
Trigger -  **ionic-button-outline-assertive:** 
```
<button class="button button-outline button-assertive"></button>
```
Trigger -  **ionic-button-outline-balanced:** 
```
<button class="button button-outline button-balanced"></button>
```
Trigger -  **ionic-button-outline-calm:** 
```
<button class="button button-outline button-calm"></button>
```
Trigger -  **ionic-button-outline-dark:** 
```
<button class="button button-outline button-dark"></button>
```
Trigger -  **ionic-button-outline-energized:** 
```
<button class="button button-outline button-energized"></button>
```
Trigger -  **ionic-button-outline-light:** 
```
<button class="button button-outline button-light"></button>
```
Trigger -  **ionic-button-outline-positive:** 
```
<button class="button button-outline button-positive"></button>
```
Trigger -  **ionic-button-outline-royal:** 
```
<button class="button button-outline button-royal"></button>
```
Trigger -  **ionic-button-outline-stable:** 
```
<button class="button button-outline button-stable"></button>
```
Trigger -  **ionic-button-positive:** 
```
<button class="button button-positive"></button>
```
Trigger -  **ionic-button-royal:** 
```
<button class="button button-royal"></button>
```
Trigger -  **ionic-button-small-assertive:** 
```
<button class="button button-small button-assertive"></button>
```
Trigger -  **ionic-button-small-balanced:** 
```
<button class="button button-small button-balanced"></button>
```
Trigger -  **ionic-button-small-calm:** 
```
<button class="button button-small button-calm"></button>
```
Trigger -  **ionic-button-small-dark:** 
```
<button class="button button-small button-dark"></button>
```
Trigger -  **ionic-button-small-energized:** 
```
<button class="button button-small button-energized"></button>
```
Trigger -  **ionic-button-small-light:** 
```
<button class="button button-small button-light"></button>
```
Trigger -  **ionic-button-small-positive:** 
```
<button class="button button-small button-positive"></button>
```
Trigger -  **ionic-button-small-royal:** 
```
<button class="button button-small button-royal"></button>
```
Trigger -  **ionic-button-small-stable:** 
```
<button class="button button-small button-stable"></button>
```
Trigger -  **ionic-button-stable:** 
```
<button class="button button-stable"></button>
```
