Ionic Framework Extended Autocomplete
============================

This is the most complete ST2/ST3 plugin to auto complete Ionic Framework directives, services and **elements**. 

This plugins has a different approach from other plugins. It aims to be the most handful tool to help you to build great apps with Ionic, however it does not intends to overcome your mandatory knowledge over the framework. 

If you wants to create a list of items, for instance, you must know what elements are part of a "Ionic List", because **Ionic Framework Extended AutoComplete only will help you with the elements**:
```HTML
<!-- Element generated separately -->
<ion-list> 
	<!-- Element generated separately -->
	<ion-item href="#"></ion-item>
</ion-list>
``` 
```HTML
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

```HTML
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

<h2 id="Reference">Reference</h2>

First, you can easily find out how this plugin works in ST2/ST3 with the following tips:
 - In HTML you can type "<" followed by "ion" and all the directives will show up for you;
 - Still in HTML for CSS Components, just type "ionic-" and the snippets will popup for you;
 - In a JS script, most of snippets are services. So just type "$" followed by "ionic" and the services will be there for you;
   - Exception are from Utility snippets, such as "ionic.Platform" ou "ionic.DomUtil". You will find this snippets typing "ionic" and following the capital letter case, looking for "ionicPlatform" and "ionicDomUtil" respectively. 

But still the whole reference are put below in case of any doubts. Have fun. :)

<h2 id="css_components">CSS Components</h2>

 - [Header](#css_header)
 - [Footer](#css_footer)
 - [Buttons](#css_buttons)
 - [Lists](#css_lists)
 - [Cards](#css_cards)
 - [Forms](#css_forms)
 - [Toggle](#css_toggle)
 - [Checkbox](#css_checkbox)
 - [Radio Buttons](#css_radio)
 - [Range](#css_range)
 - [Select](#css_select)
 - [Tabs](#css_tabs)

<h2 id="js_snippets">Javascript</h2>

 - [Action Sheet](#js_action_sheet)
 - [Backdrop](#js_backdrop)
 - [Content](#js_content)
 - [Form Inputs](#js_form_input)
 - [Headers/Footers](#js_headers_footers)
 - [Lists](#js_lists)
 - [Loading](#js_loading)
 - [Modal](#js_modal)
 - [Navigation](#js_navigation)
 - [Platform](#js_platform)
 - [Popover](#js_popover)
 - [Popup](#js_popup)
 - [Scroll](#js_scroll)
 - Side Menus
 - Slide Box
 - Tabs
 - Utility
 
**CSS Components**
-------

<h2 id="css_header">Header</h2>

Trigger -  **ionic-header-assertive:** 
```HTML
<div class="bar bar-header bar-assertive"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-balanced:** 
```HTML
<div class="bar bar-header bar-balanced"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-calm:** 
```HTML
<div class="bar bar-header bar-calm"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-dark:** 
```HTML
<div class="bar bar-header bar-dark"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-energized:** 
```HTML
<div class="bar bar-header bar-energized"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-light:** 
```HTML
<div class="bar bar-header bar-light"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-positive:** 
```HTML
<div class="bar bar-header bar-positive"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-royal:** 
```HTML
<div class="bar bar-header bar-royal"> 
	 <h1 class="title"></h1> 
</div>
```
Trigger -  **ionic-header-stable:** 
```HTML
<div class="bar bar-header bar-stable"> 
	 <h1 class="title"></h1> 
</div>
```

<h2 id="css_footer">Footer</h2>

Trigger -  **ionic-footer-assertive:** 
```HTML
<div class="bar bar-footer bar-assertive"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-balanced:** 
```HTML
<div class="bar bar-footer bar-balanced"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-calm:** 
```HTML
<div class="bar bar-footer bar-calm"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-dark:** 
```HTML
<div class="bar bar-footer bar-dark"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-energized:** 
```HTML
<div class="bar bar-footer bar-energized"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-light:** 
```HTML
<div class="bar bar-footer bar-light"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-positive:** 
```HTML
<div class="bar bar-footer bar-positive"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-royal:** 
```HTML
<div class="bar bar-footer bar-royal"> 
	 <div class="title"></div> 
</div>
```
Trigger -  **ionic-footer-stable:** 
```HTML
<div class="bar bar-footer bar-stable"> 
	 <div class="title"></div> 
</div>
```

<h2 id="css_buttons">Buttons</h2>

Trigger -  **ionic-button-assertive:** 
```HTML
<button class="button button-assertive"></button>
```
Trigger -  **ionic-button-balanced:** 
```HTML
<button class="button button-balanced"></button>
```
Trigger -  **ionic-button-bar-assertive:** 
```HTML
<div class="button-bar bar-assertive"></div>
```
Trigger -  **ionic-button-bar-balanced:** 
```HTML
<div class="button-bar bar-balanced"></div>
```
Trigger -  **ionic-button-bar-calm:** 
```HTML
<div class="button-bar bar-calm"></div>
```
Trigger -  **ionic-button-bar-dark:** 
```HTML
<div class="button-bar bar-dark"></div>
```
Trigger -  **ionic-button-bar-energized:** 
```HTML
<div class="button-bar bar-energized"></div>
```
Trigger -  **ionic-button-bar-light:** 
```HTML
<div class="button-bar bar-light"></div>
```
Trigger -  **ionic-button-bar-positive:** 
```HTML
<div class="button-bar bar-positive"></div>
```
Trigger -  **ionic-button-bar-royal:** 
```HTML
<div class="button-bar bar-royal"></div>
```
Trigger -  **ionic-button-bar-stable:** 
```HTML
<div class="button-bar bar-stable"></div>
```
Trigger -  **ionic-button-block-assertive:** 
```HTML
<button class="button button-block button-assertive"></button>
```
Trigger -  **ionic-button-block-balanced:** 
```HTML
<button class="button button-block button-balanced"></button>
```
Trigger -  **ionic-button-block-calm:** 
```HTML
<button class="button button-block button-calm"></button>
```
Trigger -  **ionic-button-block-dark:** 
```HTML
<button class="button button-block button-dark"></button>
```
Trigger -  **ionic-button-block-energized:** 
```HTML
<button class="button button-block button-energized"></button>
```
Trigger -  **ionic-button-block-light:** 
```HTML
<button class="button button-block button-light"></button>
```
Trigger -  **ionic-button-block-positive:** 
```HTML
<button class="button button-block button-positive"></button>
```
Trigger -  **ionic-button-block-royal:** 
```HTML
<button class="button button-block button-royal"></button>
```
Trigger -  **ionic-button-block-stable:** 
```HTML
<button class="button button-block button-stable"></button>
```
Trigger -  **ionic-button-calm:** 
```HTML
<button class="button button-calm"></button>
```
Trigger -  **ionic-button-clear-assertive:** 
```HTML
<button class="button button-clear button-assertive"></button>
```
Trigger -  **ionic-button-clear-balanced:** 
```HTML
<button class="button button-clear button-balanced"></button>
```
Trigger -  **ionic-button-clear-calm:** 
```HTML
<button class="button button-clear button-calm"></button>
```
Trigger -  **ionic-button-clear-dark:** 
```HTML
<button class="button button-clear button-dark"></button>
```
Trigger -  **ionic-button-clear-energized:** 
```HTML
<button class="button button-clear button-energized"></button>
```
Trigger -  **ionic-button-clear-light:** 
```HTML
<button class="button button-clear button-light"></button>
```
Trigger -  **ionic-button-clear-positive:** 
```HTML
<button class="button button-clear button-positive"></button>
```
Trigger -  **ionic-button-clear-royal:** 
```HTML
<button class="button button-clear button-royal"></button>
```
Trigger -  **ionic-button-clear-stable:** 
```HTML
<button class="button button-clear button-stable"></button>
```
Trigger -  **ionic-button-dark:** 
```HTML
<button class="button button-dark"></button>
```
Trigger -  **ionic-button-energized:** 
```HTML
<button class="button button-energized"></button>
```
Trigger -  **ionic-button-full-assertive:** 
```HTML
<button class="button button-full button-assertive"></button>
```
Trigger -  **ionic-button-full-balanced:** 
```HTML
<button class="button button-full button-balanced"></button>
```
Trigger -  **ionic-button-full-calm:** 
```HTML
<button class="button button-full button-calm"></button>
```
Trigger -  **ionic-button-full-dark:** 
```HTML
<button class="button button-full button-dark"></button>
```
Trigger -  **ionic-button-full-energized:** 
```HTML
<button class="button button-full button-energized"></button>
```
Trigger -  **ionic-button-full-light:** 
```HTML
<button class="button button-full button-light"></button>
```
Trigger -  **ionic-button-full-positive:** 
```HTML
<button class="button button-full button-positive"></button>
```
Trigger -  **ionic-button-full-royal:** 
```HTML
<button class="button button-full button-royal"></button>
```
Trigger -  **ionic-button-full-stable:** 
```HTML
<button class="button button-full button-stable"></button>
```
Trigger -  **ionic-button-icon-left-assertive:** 
```HTML
<button class="button icon-left ionicon button-assertive"></button>
```
Trigger -  **ionic-button-icon-left-balanced:** 
```HTML
<button class="button icon-left ionicon button-balanced"></button>
```
Trigger -  **ionic-button-icon-left-calm:** 
```HTML
<button class="button icon-left ionicon button-calm"></button>
```
Trigger -  **ionic-button-icon-left-dark:** 
```HTML
<button class="button icon-left ionicon button-dark"></button>
```
Trigger -  **ionic-button-icon-left-energized:** 
```HTML
<button class="button icon-left ionicon button-energized"></button>
```
Trigger -  **ionic-button-icon-left-light:** 
```HTML
<button class="button icon-left ionicon button-light"></button>
```
Trigger -  **ionic-button-icon-left-positive:** 
```HTML
<button class="button icon-left ionicon button-positive"></button>
```
Trigger -  **ionic-button-icon-left-royal:** 
```HTML
<button class="button icon-left ionicon button-royal"></button>
```
Trigger -  **ionic-button-icon-left-stable:** 
```HTML
<button class="button icon-left ionicon button-stable"></button>
```
Trigger -  **ionic-button-icon-right-assertive:** 
```HTML
<button class="button icon-right ionicon button-assertive"></button>
```
Trigger -  **ionic-button-icon-right-balanced:** 
```HTML
<button class="button icon-right ionicon button-balanced"></button>
```
Trigger -  **ionic-button-icon-right-calm:** 
```HTML
<button class="button icon-right ionicon button-calm"></button>
```
Trigger -  **ionic-button-icon-right-dark:** 
```HTML
<button class="button icon-right ionicon button-dark"></button>
```
Trigger -  **ionic-button-icon-right-energized:** 
```HTML
<button class="button icon-right ionicon button-energized"></button>
```
Trigger -  **ionic-button-icon-right-light:** 
```HTML
<button class="button icon-right ionicon button-light"></button>
```
Trigger -  **ionic-button-icon-right-positive:** 
```HTML
<button class="button icon-right ionicon button-positive"></button>
```
Trigger -  **ionic-button-icon-right-royal:** 
```HTML
<button class="button icon-right ionicon button-royal"></button>
```
Trigger -  **ionic-button-icon-right-stable:** 
```HTML
<button class="button icon-right ionicon button-stable"></button>
```
Trigger -  **ionic-button-large-assertive:** 
```HTML
<button class="button button-large button-assertive"></button>
```
Trigger -  **ionic-button-large-balanced:** 
```HTML
<button class="button button-large button-balanced"></button>
```
Trigger -  **ionic-button-large-calm:** 
```HTML
<button class="button button-large button-calm"></button>
```
Trigger -  **ionic-button-large-dark:** 
```HTML
<button class="button button-large button-dark"></button>
```
Trigger -  **ionic-button-large-energized:** 
```HTML
<button class="button button-large button-energized"></button>
```
Trigger -  **ionic-button-large-light:** 
```HTML
<button class="button button-large button-light"></button>
```
Trigger -  **ionic-button-large-positive:** 
```HTML
<button class="button button-large button-positive"></button>
```
Trigger -  **ionic-button-large-royal:** 
```HTML
<button class="button button-large button-royal"></button>
```
Trigger -  **ionic-button-large-stable:** 
```HTML
<button class="button button-large button-stable"></button>
```
Trigger -  **ionic-button-light:** 
```HTML
<button class="button button-light"></button>
```
Trigger -  **ionic-button-outline-assertive:** 
```HTML
<button class="button button-outline button-assertive"></button>
```
Trigger -  **ionic-button-outline-balanced:** 
```HTML
<button class="button button-outline button-balanced"></button>
```
Trigger -  **ionic-button-outline-calm:** 
```HTML
<button class="button button-outline button-calm"></button>
```
Trigger -  **ionic-button-outline-dark:** 
```HTML
<button class="button button-outline button-dark"></button>
```
Trigger -  **ionic-button-outline-energized:** 
```HTML
<button class="button button-outline button-energized"></button>
```
Trigger -  **ionic-button-outline-light:** 
```HTML
<button class="button button-outline button-light"></button>
```
Trigger -  **ionic-button-outline-positive:** 
```HTML
<button class="button button-outline button-positive"></button>
```
Trigger -  **ionic-button-outline-royal:** 
```HTML
<button class="button button-outline button-royal"></button>
```
Trigger -  **ionic-button-outline-stable:** 
```HTML
<button class="button button-outline button-stable"></button>
```
Trigger -  **ionic-button-positive:** 
```HTML
<button class="button button-positive"></button>
```
Trigger -  **ionic-button-royal:** 
```HTML
<button class="button button-royal"></button>
```
Trigger -  **ionic-button-small-assertive:** 
```HTML
<button class="button button-small button-assertive"></button>
```
Trigger -  **ionic-button-small-balanced:** 
```HTML
<button class="button button-small button-balanced"></button>
```
Trigger -  **ionic-button-small-calm:** 
```HTML
<button class="button button-small button-calm"></button>
```
Trigger -  **ionic-button-small-dark:** 
```HTML
<button class="button button-small button-dark"></button>
```
Trigger -  **ionic-button-small-energized:** 
```HTML
<button class="button button-small button-energized"></button>
```
Trigger -  **ionic-button-small-light:** 
```HTML
<button class="button button-small button-light"></button>
```
Trigger -  **ionic-button-small-positive:** 
```HTML
<button class="button button-small button-positive"></button>
```
Trigger -  **ionic-button-small-royal:** 
```HTML
<button class="button button-small button-royal"></button>
```
Trigger -  **ionic-button-small-stable:** 
```HTML
<button class="button button-small button-stable"></button>
```
Trigger -  **ionic-button-stable:** 
```HTML
<button class="button button-stable"></button>
```

<h2 id="css_lists">Lists</h2>

Trigger -  **ionic-collection-repeat:** 
```HTML
<div class="item your_item_css_class}"
	collection-repeat="item in items"
	collection-item-width="'100%'"
	collection-item-height="getItemHeight(item, $index)"
	ng-style="{height: getItemHeight(item, $index)}\">
</div>
```
Trigger -  **ionic-item-avatar:** 
```HTML
<a class="item item-avatar" href="#">
	<img src="image_source">
	<h2>title</h2>
	<p>description</p>
</a>
```
Trigger -  **ionic-item-button-left:** 
```HTML
<a class="item item-button-left" href="#"></a>
```
Trigger -  **ionic-item-button-right:** 
```HTML
<a class="item item-button-right" href="#"></a>
```
Trigger -  **ionic-item-divider:** 
```HTML
<div class="item item-divider"></div>
```
Trigger -  **ionic-item-icon-left-right:** 
```HTML
<a class="item item-icon-left item-icon-right" href="#"></a>
```
Trigger -  **ionic-item-icon-left:** 
```HTML
<a class="item item-icon-left" href="#"></a>
```
Trigger -  **ionic-item-icon-right:** 
```HTML
<a class="item item-icon-right" href="#"></a>
```
Trigger -  **ionic-item-thumbnail-left:** 
```HTML
<a class="item item-thumbnail-left" href="#">
	<img src="image_source">
	<h2>title</h2>
	<p>description</p>
</a>
```
Trigger -  **ionic-item-thumbnail-right:** 
```HTML
<a class="item item-thumbnail-right" href="#">
	<img src="image_source">
	<h2>title</h2>
	<p>description</p>
</a>
```
Trigger -  **ionic-item:** 
```HTML
<a class="item"></a>
```
Trigger -  **ionic-list-inset:** 
```HTML
<div class="list list-inset"></div>
```

<h2 id="css_cards">Cards</h2>

Trigger -  **ionic-card-footer:** 
```HTML
<div class="card">
	<div class="item item-text-wrap">
		desc
	</div>
	<div class="item item-divider">
		footer
	</div>
</div>
```
Trigger -  **ionic-card-header-footer:** 
```HTML
<div class="card">
	<div class="item item-divider">
		header
	</div>
	<div class="item item-text-wrap">
		desc
	</div>
	<div class="item item-divider">
		footer
	</div>
</div>
```
Trigger -  **ionic-card-header:** 
```HTML
<div class="card">
	<div class="item item-divider">
		header
	</div>
	<div class="item item-text-wrap">
		desc
	</div>
</div>
```
Trigger -  **ionic-card-image:** 
```HTML
<div class="item item-avatar" href="#">
	<img src="image_source">
	<h2>title</h2>
	<p>description</p>
</div>
<div class="item item-image">
	<img src="image_source">
</div>
<a class="item item-icon-left assertive" href="#">
	<i class="icon ionicon"></i>
	text_link
</a>
```
Trigger -  **ionic-card-list-item:** 
```HTML
<a href="#" class="item item-icon-left">
	<i class="icon ionicon"></i>
	desc
</a>
```
Trigger -  **ionic-card-list:** 
```HTML
<div class="list card">
	
</div>
```
Trigger -  **ionic-card-showcase:** 
```HTML
<div class="item item-avatar" href="#">
	<img src="image_source">
	<h2>title</h2>
	<p>description</p>
</div>
<div class="item item-body">
	<img class="full-image" src="image_source">
	<p>description</p>
	<p>
		<a href="#" class="subdued">1 Like</a>
		<a href="#" class="subdued">5 Comments</a>
	</p>
</div>

<div class="item tabs tabs-secondary tabs-icon-left">
	<a class="tab-item" href="#">
		<i class="icon ion-thumbsup"></i>
		Like
	</a>
	<a class="tab-item" href="#">
		<i class="icon ion-chatbox"></i>
		Comments
	</a>
	<a class="tab-item" href="#">
		<i class="icon ion-share"></i>
		Share
	</a>
</div>

```
Trigger -  **ionic-card:** 
```HTML
<div class="card">
	<div class="item item-text-wrap">
		desc
	</div>
</div>
```

<h2 id="css_forms">Forms</h2>

Trigger -  **ionic-input-floating:** 
```HTML
<label class="item item-input item-floating-label">
	<span class="input-label">input_name}</span>
	<input type="text" placeholder="input_placeholder">
</label>
```
Trigger -  **ionic-input-header:** 
```HTML
<div class="bar bar-header item-input-inset">
	<label class="item-input-wrapper">
		<i class="icon ion-ios7-search placeholder-icon"></i>
		<input type="search" placeholder="Search">
	</label>
	<button class="button button-clear">
		Cancel
	</button>
</div>
```
Trigger -  **ionic-input-icon:** 
```HTML
<label class="item item-input">
	<i class="icon ion-search placeholder-icon"></i>
	<input type="text" placeholder="Search">
</label>
```
Trigger -  **ionic-input-inline:** 
```HTML
<label class="item item-input">
	<span class="input-label">input_name</span>
	<input type="text">
</label>
```
Trigger -  **ionic-input-inset:** 
```HTML
<div class="item item-input-inset">
	<label class="item-input-wrapper">
		<input type="text" placeholder="input_placeholder">
	</label>
	<button class="button button-small">
		button_name
	</button>
</div>

```
Trigger -  **ionic-input-placeholder:** 
```HTML
<label class="item item-input">
	<input type="text" placeholder="placeholder_1">
</label>
```
Trigger -  **ionic-input-stacked:** 
```HTML
<label class="item item-input item-stacked-label">
	<span class="input-label">input_name</span>
	<input type="text" placeholder="input_placeholder">
</label>
```

<h2 id="css_toggle">Toggle</h2>

Trigger -  **ionic-toggle-assertive:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-assertive">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```
Trigger -  **ionic-toggle-balanced:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-balanced">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```
Trigger -  **ionic-toggle-calm:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-calm">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```
Trigger -  **ionic-toggle-dark:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-dark">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```
Trigger -  **ionic-toggle-energized:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-energized">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```
Trigger -  **ionic-toggle-light:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-light">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```
Trigger -  **ionic-toggle-positive:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-positive">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```
Trigger -  **ionic-toggle-royal:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-royal">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```
Trigger -  **ionic-toggle-stable:** 
```HTML
<li class="item item-toggle">
	desc
	<label class="toggle toggle-stable">
		<input type="checkbox">
		<div class="track">
			<div class="handle"></div>
		</div>
	</label>
</li>

```

<h2 id="css_checkbox">Checkbox</h2>

Trigger -  **ionic-checkbox-assertive:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-assertive">
		<input type="checkbox">
	</label>
	desc
</li>

```
Trigger -  **ionic-checkbox-balanced:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-balanced">
		<input type="checkbox">
	</label>
	desc
</li>

```
Trigger -  **ionic-checkbox-calm:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-calm">
		<input type="checkbox">
	</label>
	desc
</li>

```
Trigger -  **ionic-checkbox-dark:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-dark">
		<input type="checkbox">
	</label>
	desc
</li>

```
Trigger -  **ionic-checkbox-energized:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-energized">
		<input type="checkbox">
	</label>
	desc
</li>

```
Trigger -  **ionic-checkbox-light:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-light">
		<input type="checkbox">
	</label>
	desc
</li>

```
Trigger -  **ionic-checkbox-positive:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-positive">
		<input type="checkbox">
	</label>
	desc
</li>

```
Trigger -  **ionic-checkbox-royal:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-royal">
		<input type="checkbox">
	</label>
	desc
</li>

```
Trigger -  **ionic-checkbox-stable:** 
```HTML
<li class="item item-checkbox">
	<label class="checkbox checkbox-stable">
		<input type="checkbox">
	</label>
	desc
</li>

```

<h2 id="css_radio">Radio Buttons</h2>

Trigger -  **ionic-radio-button:** 
```HTML
<label class="item item-radio">
	<input type="radio" name="group">
	<div class="item-content">
		desc
	</div>
	<i class="radio-icon ion-checkmark"></i>
</label>
```

<h2 id="css_range">Range</h2>

Trigger -  **ionic-range-assertive:** 
```HTML
<div class="range range-assertive">
	<i class="icon ion-volume-low"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>
</div>

```
Trigger -  **ionic-range-balanced:** 
```HTML
<div class="range range-balanced">
	<i class="icon ion-volume-low"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>
</div>

```
Trigger -  **ionic-range-calm:** 
```HTML
<div class="range range-calm">
	<i class="icon ion-volume-low"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>
</div>

```
Trigger -  **ionic-range-dark:** 
```HTML
<div class="range range-dark">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-energized:** 
```HTML
<div class="range range-energized">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-item-assertive:** 
```HTML
<div class="item range range-assertive">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-item-balanced:** 
```HTML
<div class="item range range-balanced">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-item-calm:** 
```HTML
<div class="item range range-calm">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-item-dark:** 
```HTML
<div class="item range range-dark">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-item-energized:** 
```HTML
<div class="item range range-energized">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-item-light:** 
```HTML
<div class="item range range-light">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>
</div>

```
Trigger -  **ionic-range-item-positive:** 
```HTML
<div class="item range range-positive">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-item-royal:** 
```HTML
<div class="item range range-royal">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-item-stable:** 
```HTML
<div class="item range range-stable">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-light:** 
```HTML
<div class="range range-light">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-positive:** 
```HTML
<div class="range range-positive">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-royal:** 
```HTML
<div class="range range-royal">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```
Trigger -  **ionic-range-stable:** 
```HTML
<div class="range range-stable">
	<i class="icon ion-volume-low}"></i>
	<input type="range" name="volume" min="0" max="100" value="33">
	<i class="icon ion-volume-high"></i>

</div>

```

<h2 id="css_select">Select</h2>

Trigger -  **ionic-select-assertive:** 
```HTML
<label class="item item-input item-select item-assertive">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```
Trigger -  **ionic-select-balanced:** 
```HTML
<label class="item item-input item-select item-balanced">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```
Trigger -  **ionic-select-calm:** 
```HTML
<label class="item item-input item-select item-calm">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```
Trigger -  **ionic-select-dark:** 
```HTML
<label class="item item-input item-select item-dark">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```
Trigger -  **ionic-select-energized:** 
```HTML
<label class="item item-input item-select item-energized">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```
Trigger -  **ionic-select-light:** 
```HTML
<label class="item item-input item-select item-light">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```
Trigger -  **ionic-select-positive:** 
```HTML
<label class="item item-input item-select item-positive">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```
Trigger -  **ionic-select-royal:** 
```HTML
<label class="item item-input item-select item-royal">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```
Trigger -  **ionic-select-stable:** 
```HTML
<label class="item item-input item-select item-stable">
	<div class="input-label">
		desc
	</div>
	<select>
		<option selected>opt1</option>
		<option>opt2</option>
	<select>
</label>

```

<h2 id="css_tabs">Tabs</h2>

Trigger -  **ionic-tabs-assertive:** 
```HTML
<div class="tabs tabs-assertive"></div>

```
Trigger -  **ionic-tabs-balanced:** 
```HTML
<div class="tabs tabs-balanced"></div>

```
Trigger -  **ionic-tabs-calm:** 
```HTML
<div class="tabs tabs-calm"></div>

```
Trigger -  **ionic-tabs-dark:** 
```HTML
<div class="tabs tabs-dark"></div>

```
Trigger -  **ionic-tabs-energized:** 
```HTML
<div class="tabs tabs-energized"></div>

```
Trigger -  **ionic-tabs-icon-left-assertive:** 
```HTML
<div class="tabs tabs-icon-left tabs-assertive"></div>

```
Trigger -  **ionic-tabs-icon-left-balanced:** 
```HTML
<div class="tabs tabs-icon-left tabs-balanced"></div>

```
Trigger -  **ionic-tabs-icon-left-calm:** 
```HTML
<div class="tabs tabs-icon-left tabs-calm"></div>

```
Trigger -  **ionic-tabs-icon-left-dark:** 
```HTML
<div class="tabs tabs-icon-left tabs-dark"></div>

```
Trigger -  **ionic-tabs-icon-left-energized:** 
```HTML
<div class="tabs tabs-icon-left tabs-energized"></div>

```
Trigger -  **ionic-tabs-icon-left-light:** 
```HTML
<div class="tabs tabs-icon-left tabs-light"></div>

```
Trigger -  **ionic-tabs-icon-left-positive:** 
```HTML
<div class="tabs tabs-icon-left tabs-positive"></div>

```
Trigger -  **ionic-tabs-icon-left-royal:** 
```HTML
<div class="tabs tabs-icon-left tabs-royal"></div>

```
Trigger -  **ionic-tabs-icon-left-stable:** 
```HTML
<div class="tabs tabs-icon-left tabs-stable"></div>

```
Trigger -  **ionic-tabs-icon-only-assertive:** 
```HTML
<div class="tabs tabs-icon-only tabs-assertive"></div>

```
Trigger -  **ionic-tabs-icon-only-balanced:** 
```HTML
<div class="tabs tabs-icon-only tabs-balanced"></div>

```
Trigger -  **ionic-tabs-icon-only-calm:** 
```HTML
<div class="tabs tabs-icon-only tabs-calm"></div>

```
Trigger -  **ionic-tabs-icon-only-dark:** 
```HTML
<div class="tabs tabs-icon-only tabs-dark"></div>

```
Trigger -  **ionic-tabs-icon-only-energized:** 
```HTML
<div class="tabs tabs-icon-only tabs-energized"></div>

```
Trigger -  **ionic-tabs-icon-only-light:** 
```HTML
<div class="tabs tabs-icon-only tabs-light"></div>

```
Trigger -  **ionic-tabs-icon-only-positive:** 
```HTML
<div class="tabs tabs-icon-only tabs-positive"></div>

```
Trigger -  **ionic-tabs-icon-only-royal:** 
```HTML
<div class="tabs tabs-icon-only tabs-royal"></div>

```
Trigger -  **ionic-tabs-icon-only-stable:** 
```HTML
<div class="tabs tabs-icon-only tabs-stable"></div>

```
Trigger -  **ionic-tabs-icon-top-assertive:** 
```HTML
<div class="tabs tabs-icon-top tabs-assertive"></div>

```
Trigger -  **ionic-tabs-icon-top-balanced:** 
```HTML
<div class="tabs tabs-icon-top tabs-balanced"></div>

```
Trigger -  **ionic-tabs-icon-top-calm:** 
```HTML
<div class="tabs tabs-icon-top tabs-calm"></div>

```
Trigger -  **ionic-tabs-icon-top-dark:** 
```HTML
<div class="tabs tabs-icon-top tabs-dark"></div>

```
Trigger -  **ionic-tabs-icon-top-energized:** 
```HTML
<div class="tabs tabs-icon-top tabs-energized"></div>

```
Trigger -  **ionic-tabs-icon-top-light:** 
```HTML
<div class="tabs tabs-icon-top tabs-light"></div>

```
Trigger -  **ionic-tabs-icon-top-positive:** 
```HTML
<div class="tabs tabs-icon-top tabs-positive"></div>

```
Trigger -  **ionic-tabs-icon-top-royal:** 
```HTML
<div class="tabs tabs-icon-top tabs-royal"></div>

```
Trigger -  **ionic-tabs-icon-top-stable:** 
```HTML
<div class="tabs tabs-icon-top tabs-stable"></div>

```
Trigger -  **ionic-tabs-item-icon:** 
```HTML
<a class="tab-item" href="#">
	<i class="icon ion-home"></i>
	
</a>

```
Trigger -  **ionic-tabs-item:** 
```HTML
<a class="tab-item" href="#">
	Tab}
</a>

```
Trigger -  **ionic-tabs-light:** 
```HTML
<div class="tabs tabs-light"></div>

```
Trigger -  **ionic-tabs-positive:** 
```HTML
<div class="tabs tabs-positive"></div>

```
Trigger -  **ionic-tabs-royal:** 
```HTML
<div class="tabs tabs-royal"></div>

```
Trigger -  **ionic-tabs-stable:** 
```HTML
<div class="tabs tabs-stable"></div>

```
Trigger -  **ionic-tabs-striped-assertive:** 
```HTML
<div class="tabs-striped tabs-color-assertive"></div>

```
Trigger -  **ionic-tabs-striped-balanced:** 
```HTML
<div class="tabs-striped tabs-color-balanced"></div>

```
Trigger -  **ionic-tabs-striped-calm:** 
```HTML
<div class="tabs-striped tabs-color-calm"></div>

```
Trigger -  **ionic-tabs-striped-dark:** 
```HTML
<div class="tabs-striped tabs-color-dark"></div>

```
Trigger -  **ionic-tabs-striped-energized:** 
```HTML
<div class="tabs-striped tabs-color-energized"></div>

```
Trigger -  **ionic-tabs-striped-light:** 
```HTML
<div class="tabs-striped tabs-color-light"></div>

```
Trigger -  **ionic-tabs-striped-positive:** 
```HTML
<div class="tabs-striped tabs-color-positive"></div>

```
Trigger -  **ionic-tabs-striped-royal:** 
```HTML
<div class="tabs-striped tabs-color-royal"></div>

```
Trigger -  **ionic-tabs-striped-stable:** 
```HTML
<div class="tabs-striped tabs-color-stable"></div>

```

**Javascript**
-------

<h2 id="js_action_sheet">Action Sheet</h2>

Trigger -  **$ionicActionSheet.show:** 
```Javascript
$ionicActionSheet.show({
		buttons: [
			{ text: "Button text 1" },
			{ text: "Move" }
		],
		destructiveText: "Delete",
		titleText: "Title",
		cancelText: "Cancel",
		cancel: function() {
			your code goes here
		},
		buttonClicked: function(index) {
			return true;
		}
});
```

<h2 id="js_backdrop">Backdrop</h2>

Trigger -  **$ionicBackdrop.release:** 
```Javascript
$ionicBackdrop.release();
```
Trigger -  **$ionicBackdrop.retain:** 
```Javascript
$ionicBackdrop.retain();
```

<h2 id="js_content">Content</h2>

Trigger -  **$ionicScrollDelegate.anchorScroll:** 
```Javascript
$ionicScrollDelegate.anchorScroll(shouldAnimate)
```
Trigger -  **$ionicScrollDelegate.getByHandle:** 
```Javascript
$ionicScrollDelegate.$getByHandle(handle)
```
Trigger -  **$ionicScrollDelegate.getScrollPosition:** 
```Javascript
$ionicScrollDelegate.getScrollPosition()
```
Trigger -  **$ionicScrollDelegate.getScrollView:** 
```Javascript
$ionicScrollDelegate.getScrollView()
```
Trigger -  **$ionicScrollDelegate.resize:** 
```Javascript
$ionicScrollDelegate.resize()
```
Trigger -  **$ionicScrollDelegate.scrollBottom:** 
```Javascript
$ionicScrollDelegate.scrollBottom(shouldAnimate)
```
Trigger -  **$ionicScrollDelegate.scrollBy:** 
```Javascript
$ionicScrollDelegate.scrollBy(left, top, shouldAnimate)
```
Trigger -  **$ionicScrollDelegate.scrollTo:** 
```Javascript
$ionicScrollDelegate.scrollTo(left, top, shouldAnimate)
```
Trigger -  **$ionicScrollDelegate.scrollTop:** 
```Javascript
$ionicScrollDelegate.scrollTop(shouldAnimate)
```
Trigger -  **$ionicScrollDelegate.zoomBy:** 
```Javascript
$ionicScrollDelegate.zoomBy(factor, animate, originLeft, originTop)
```
Trigger -  **$ionicScrollDelegate.zoomTo:** 
```Javascript
$ionicScrollDelegate.zoomTo(level, animate, originLeft, originTop)
```
Trigger -  **<ion-content :** 
```HTML
<ion-content has-subheader="false"></ion-content>
```
Trigger -  **<ion-refresher :** 
```HTML
<ion-refresher pulling-text="Pull to refresh..." on-refresh="doRefresh()"></ion-refresher>
```
Trigger -  **<ion-pane :** 
```HTML
<ion-pane></ion-pane>
```

<h2 id="js_form_input">Form Inputs</h2>

Trigger -  **<ion-checkbox :** 
```HTML
<ion-checkbox ng-model="isChecked">Checkbox Label</ion-checkbox>
```
Trigger -  **<ion-radio :** 
```HTML
<ion-radio ng-model="choice" ng-value="\'A\'">Choose A</ion-radio>
```
Trigger -  **<ion-toogle :** 
```HTML
<ion-toggle ng-model="airplaneMode" toggle-class="toggle-calm">Airplane Mode</ion-toggle>
```

<h2 id="js_headers_footers">Headers/Footers</h2>

Trigger -  **<ion-header-bar :** 
```HTML
<ion-header-bar align-title="left" class="bar-positive"></ion-header-bar>
```
Trigger -  **<ion-footer-bar :** 
```HTML
<ion-footer-bar ion-footer-bar align-title="left" class="bar-assertive"></ion-footer-bar>
```

<h2 id="js_lists">Lists</h2>

Trigger -  **$ionicListDelegate.canSwipeItems:** 
```Javascript
$ionicListDelegate.canSwipeItems(true});
```
Trigger -  **$ionicListDelegate.closeOptionButtons:** 
```Javascript
$ionicListDelegate.closeOptionButtons();
```
Trigger -  **$ionicListDelegate.showDelete:** 
```Javascript
$ionicListDelegate.showDelete(true);
```
Trigger -  **$ionicListDelegate.showReorder:** 
```Javascript
$ionicListDelegate.showReorder(true);
```
Trigger -  **<ion-list :** 
```HTML
<ion-list></ion-list>
```
Trigger -  **<ion-item :** 
```HTML
<ion-item href="#"></ion-item>
```
Trigger -  **<ion-delete-button :** 
```HTML
<ion-delete-button class="ion-minus-circled"></ion-delete-button>
```
Trigger -  **<ion-reorder-button :** 
```HTML
<ion-reorder-button class="ion-navicon" on-reorder="moveItem(item, $fromIndex, $toIndex)"></ion-reorder-button>
```
Trigger -  **<ion-option-button :** 
```HTML
<ion-option-button class="button-positive"></ion-option-button>
```

<h2 id="js_loading">Loading</h2>

Trigger -  **$ionicLoading.hide:** 
```Javascript
$ionicLoading.hide()
```
Trigger -  **$ionicLoading.show:** 
```Javascript
$ionicLoading.show({
	template: "Loading..."
});
```

<h2 id="js_modal">Modal</h2>

Trigger -  **$ionicModal.fromTemplate:** 
```Javascript
$ionicModal.fromTemplate(templateString, options)
```
Trigger -  **$ionicModal.fromTemplateUrl:** 
```Javascript
$ionicModal.fromTemplateUrl(templateUrl, options)
```
Trigger -  **<ion-modal-view :** 
```HTML
<ion-modal-view></ion-modal-view>
```

<h2 id="js_navigation">Navigation</h2>

Trigger -  **$ionicHistory.backTitle:** 
```Javascript
$ionicHistory.backTitle()
```
Trigger -  **$ionicHistory.backView:** 
```Javascript
$ionicHistory.backView()
```
Trigger -  **$ionicHistory.clearCache:** 
```Javascript
$ionicHistory.clearCache()
```
Trigger -  **$ionicHistory.clearHistory:** 
```Javascript
$ionicHistory.clearHistory()
```
Trigger -  **$ionicHistory.currentHistoryId:** 
```Javascript
$ionicHistory.currentHistoryId()
```
Trigger -  **$ionicHistory.currentStateName:** 
```Javascript
$ionicHistory.currentStateName()
```
Trigger -  **$ionicHistory.currentTitle:** 
```Javascript
$ionicHistory.currentTitle(val)
```
Trigger -  **$ionicHistory.currentView:** 
```Javascript
$ionicHistory.currentView()
```
Trigger -  **$ionicHistory.forwardView:** 
```Javascript
$ionicHistory.forwardView()
```
Trigger -  **$ionicHistory.goBack:** 
```Javascript
$ionicHistory.goBack()
```
Trigger -  **$ionicHistory.nextViewOptions:** 
```Javascript
$ionicHistory.nextViewOptions(
	disableAnimate: true,
 	disableBack: true
)
```
Trigger -  **$ionicHistory.viewHistory:** 
```Javascript
$ionicHistory.viewHistory()
```
Trigger -  **$ionicNavBarDelegate.align:** 
```Javascript
$ionicNavBarDelegate.align(direction)
```
Trigger -  **$ionicNavBarDelegate.back:** 
```Javascript
$ionicNavBarDelegate.back()
```
Trigger -  **$ionicNavBarDelegate.showBackButton:** 
```Javascript
$ionicNavBarDelegate.showBackButton(show)
```
Trigger -  **$ionicNavBarDelegate.showBar:** 
```Javascript
$ionicNavBarDelegate.showBar(show)
```
Trigger -  **$ionicNavBarDelegate.title:** 
```Javascript
$ionicNavBarDelegate.title(title)
```
Trigger -  **$ionicView.afterEnter:** 
```Javascript
$scope.$on("$ionicView.afterEnter", function () {

});
```
Trigger -  **$ionicView.afterLeave:** 
```Javascript
$scope.$on("$ionicView.afterLeave", function () {

});
```
Trigger -  **$ionicView.beforeEnter:** 
```Javascript
$scope.$on("$ionicView.beforeEnter", function () {

});
```
Trigger -  **$ionicView.beforeLeave:** 
```Javascript
$scope.$on("$ionicView.beforeLeave", function () {

});
```
Trigger -  **$ionicView.enter:** 
```Javascript
$scope.$on("$ionicView.enter", function () {

});
```
Trigger -  **$ionicView.leave:** 
```Javascript
$scope.$on("$ionicView.leave", function () {

});
```
Trigger -  **$ionicView.loaded:** 
```Javascript
$scope.$on("$ionicView.loaded", function () {

});
```
Trigger -  **$ionicView.unloaded:** 
```Javascript
$scope.$on("$ionicView.unloaded", function () {

});
```
Trigger -  **<ion-nav-view :** 
```HTML
<ion-nav-view view-title="Your Title!"></ion-view>
```
Trigger -  **<ion-nav-bar :** 
```HTML
<ion-nav-bar class="bar-positive" align-title="left"></ion-nav-bar>
```
Trigger -  **<ion-nav-buttons :** 
```HTML
<ion-nav-buttons side="primary"></ion-nav-buttons>
```
Trigger -  **<ion-nav-back-button :** 
```HTML
<ion-nav-back-button class="button-clear"></ion-nav-back-button>
```
Trigger -  **<ion-nav-title :** 
```HTML
<ion-nav-title></ion-nav-title>
```

<h2 id="js_platform">Platform</h2>

Trigger -  **$ionicPlatform.offHardwareBackButton:** 
```Javascript
$ionicPlatform.offHardwareBackButton(callback)
```
Trigger -  **$ionicPlatform.on:** 
```Javascript
$ionicPlatform.on(type, callback)
```
Trigger -  **$ionicPlatform.onHardwareBackButton:** 
```Javascript
$ionicPlatform.onHardwareBackButton(callback)
```
Trigger -  **$ionicPlatform.ready:** 
```Javascript
$ionicPlatform.ready()
```
Trigger -  **$ionicPlatform.registerBackButtonAction:** 
```Javascript
$ionicPlatform.registerBackButtonAction(callback, priority)
```

<h2 id="js_popover">Popover</h2>

Trigger -  **$ionicPopover.fromTemplate:** 
```Javascript
$ionicPopover.fromTemplate(templateString, {
 	options
});
```
Trigger -  **$ionicPopover.fromTemplateUrl:** 
```Javascript
$ionicPopover.fromTemplateUrl(templateUrl, {
 	options
})
```

<h2 id="js_popup">Popup</h2>

Trigger -  **$ionicPopup.alert:** 
```Javascript
$ionicPopup.alert({
	title: $1,
	template: $2
});
```
Trigger -  **$ionicPopup.confirm:** 
```Javascript
$ionicPopup.confirm({
	title: $1,
	template: $2
});
```
Trigger -  **$ionicPopup.prompt:** 
```Javascript
$ionicPopup.prompt({
	title: $1,
	template: $2,
	inputType: $3,
	inputPlaceholder: $4
})
```
Trigger -  **$ionicPopup.show:** 
```Javascript
$ionicPopup.show({
	template: $1,
	title: $2,
	subTitle: $3,
	scope: $scope,
	buttons: [$4]
});
```

<h2 id="js_scroll">Scroll</h2>

Trigger -  **<ion-scroll :** 
```HTML
<ion-scroll zooming=\"true\" direction=\"xy\" style=\"width: 500px; height: 500px\"></ion-scroll>
```
Trigger -  **<ion-infinite-scroll :** 
```HTML
<ion-infinite-scroll on-infinite="loadMore()"></ion-infinite-scroll>
```
