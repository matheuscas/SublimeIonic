import os

current_path = os.path.dirname(os.path.abspath(__file__))
header = False
sub_header = False
footer = False
buttons = False
lists = True

def create_snippet_string(tabTrigger,content,scope,description):
	tabTrigger_tag = "<tabTrigger>"+tabTrigger+"</tabTrigger>"
	content_tag = "<content><![CDATA["+content+"]]></content>"
	scope_tag = "<scope>"+scope+"</scope>"
	if len(description) == 0:
		description_tag = "<description>...</description>"
	else:
		description_tag = "<description>"+description+"</description>"
	snippet_string = "<snippet>\n\t"+content_tag+"\n\t"+tabTrigger_tag+\
						"\n\t"+scope_tag+"\n\t"+description_tag+"\n"+"</snippet>"
	return snippet_string	

if header:
	output_folder = current_path + '/Header/'
	css_bars = ['bar-light','bar-stable','bar-positive',
				'bar-calm','bar-balanced','bar-energized',
				'bar-assertive','bar-royal','bar-dark']

	for bar in css_bars:
		header_str = '<div class="bar bar-header ' + bar + '"> \n' + '\t <h1 class="title">${1:' + bar + '}</h1> \n' + '</div>'
		snippet_str = create_snippet_string('ionic-header-'+bar[4:],header_str,'text.html','ionic-header-'+bar[4:]) 
		print snippet_str
		print '----------'
		output_file = open(output_folder+'ionic-header-'+bar[4:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()	

if sub_header:
	output_folder = current_path + '/SubHeader/'
	css_bars = ['bar-subheader']

	for bar in css_bars:
		strr = '<div class="bar ' + bar + '"> \n' + '\t <h2 class="title">${1:' + bar + '}</h2> \n' + '</div>'
		snippet_str = create_snippet_string('ionic-subheader',strr,'text.html',bar + ' snippet') 
		print snippet_str
		print '----------'
		output_file = open(output_folder+'ionic-subheader'+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()	
	

if footer:
	output_folder = current_path + '/Footer/'
	css_bars = ['bar-light','bar-stable','bar-positive',
				'bar-calm','bar-balanced','bar-energized',
				'bar-assertive','bar-royal','bar-dark']

	for bar in css_bars:
		strr = '<div class="bar bar-footer ' + bar + '"> \n' + '\t <div class="title">${1:' + bar + '}</div> \n' + '</div>'
		snippet_str = create_snippet_string('ionic-footer-'+bar[4:],strr,'text.html','ionic-footer-'+bar[4:]) 
		print snippet_str
		print '----------'
		output_file = open(output_folder+'ionic-footer-'+bar[4:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()
	

if buttons:
	output_folder = current_path + '/Buttons/'
	css_buttons = ['button-light', 'button-stable', 'button-positive', 'button-calm',
							'button-balanced', 'button-energized','button-assertive', 'button-royal', 'button-dark']

	for button_color in css_buttons:
		regular_button = '<button class="button ' + button_color + '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
		block_button = '<button class="button button-block ' + button_color + '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
		full_button = '<button class="button button-full ' + button_color + '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
		small_button = '<button class="button button-small ' + button_color + '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
		large_button = '<button class="button button-large ' + button_color + '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
		outline_button = '<button class="button button-outline ' + button_color + '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
		clear_button = '<button class="button button-clear ' + button_color + '"> \n' + '\t ${1:' + button_color + '}\n' + '</button>'
		icon_left_button = '<button class="button icon-left ${1:ionicon} ' + button_color + '"> \n' + '\t ${2:' + button_color + '}\n' + '</button>'
		icon_right_button = '<button class="button icon-right ${1:ionicon} ' + button_color + '"> \n' + '\t ${2:' + button_color + '}\n' + '</button>'
		button_bar = '<div class="button-bar bar-' + button_color[7:] + '">$0</div>'

		snippet_str = create_snippet_string('ionic-button-'+button_color[7:],regular_button,'text.html','ionic-button-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-block-'+button_color[7:],block_button,'text.html','ionic-button-block-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-block-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-full-'+button_color[7:],full_button,'text.html','ionic-button-full-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-full-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-small-'+button_color[7:],small_button,'text.html','ionic-button-small-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-small-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-large-'+button_color[7:],large_button,'text.html','ionic-button-large-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-large-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-outline-'+button_color[7:],outline_button,'text.html','ionic-button-outline-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-outline-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-clear-'+button_color[7:],clear_button,'text.html','ionic-button-clear-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-clear-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-icon-left-'+button_color[7:],icon_left_button,'text.html','ionic-button-icon-left-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-icon-left-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-icon-right-'+button_color[7:],icon_right_button,'text.html','ionic-button-icon-right-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-icon-right-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

		snippet_str = create_snippet_string('ionic-button-bar-'+button_color[7:],button_bar,'text.html','ionic-button-bar-'+button_color[7:]) 
		output_file = open(output_folder+'ionic-button-bar-'+button_color[7:]+".sublime-snippet","w+")
		output_file.write(snippet_str)
		output_file.close()

if lists:

	output_folder = current_path + '/Lists/'
	item_divider = '<div class="item item-divider">$0</div>'
	item_icon_left = '<a class="item item-icon-left" href="#">$0</a>'
	item_icon_right = '<a class="item item-icon-right" href="#">$0</a>'
	item_icon_left_right = '<a class="item item-icon-left item-icon-right" href="#">$0</a>'
	item_button_right = '<a class="item item-button-right" href="#">$0</a>'
	item_button_left= '<a class="item item-button-left" href="#">$0</a>'
	item_avatar= '<a class="item item-avatar" href="#">\n' + '\t<img src="${1:image_source}">\n' + '\t<h2>${2:title}</h2>\n' + '\t<p>${3:description}</p>\n' + '</a>'
	item_thumbnail_left= '<a class="item item-thumbnail-left" href="#">\n' + '\t<img src="${1:image_source}">\n' + '\t<h2>${2:title}</h2>\n' + '\t<p>${3:description}</p>\n' + '</a>'
	item_thumbnail_right= '<a class="item item-thumbnail-right" href="#">\n' + '\t<img src="${1:image_source}">\n' + '\t<h2>${2:title}</h2>\n' + '\t<p>${3:description}</p>\n' + '</a>'
	list_inset = '<div class="list list-inset">$0</div>'
	collection_repeat = '<div class="item ${1:your_item_css_class}"\n' + '\tcollection-repeat="${2:item in items}"\n' + '\tcollection-item-width="${3:\'100%\'}"\n' + '\tcollection-item-height="${4:getItemHeight(item, \$index)}"\n' + '\tng-style="${5:{height: getItemHeight(item, \$index)}\}">$0\n' + '</div>'

	ionicListDelegate_showReorder = '\$ionicListDelegate.showReorder(${1:true});'
	ionicListDelegate_showDelete = '\$ionicListDelegate.showDelete(${1:true});'
	ionicListDelegate_canSwipeItems = '\$ionicListDelegate.canSwipeItems(${1:true});'
	ionicListDelegate_closeOptionButtons = '\$ionicListDelegate.closeOptionButtons();'

	snippet_str = create_snippet_string('item-divider',item_divider,'text.html','item-divider')
	output_file = open(output_folder+'item-divider'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('item-icon-left',item_icon_left,'text.html','item-icon-left')
	output_file = open(output_folder+'item-icon-left'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('item-icon-right',item_icon_right,'text.html','item-icon-right')
	output_file = open(output_folder+'item-icon-right'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('item-icon-left-right',item_icon_left_right,'text.html','item-icon-left-right')
	output_file = open(output_folder+'item-icon-left-right'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('item-button-right',item_button_right,'text.html','item-button-right')
	output_file = open(output_folder+'item-button-right'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('item-button-left',item_button_left,'text.html','item-button-left')
	output_file = open(output_folder+'item-button-left'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('item-avatar',item_avatar,'text.html','item-avatar')
	output_file = open(output_folder+'item-avatar'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('item-thumbnail-left',item_thumbnail_left,'text.html','item-thumbnail-left')
	output_file = open(output_folder+'item-thumbnail-left'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('item-thumbnail-right',item_thumbnail_right,'text.html','item-thumbnail-right')
	output_file = open(output_folder+'item-thumbnail-right'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('list-inset',list_inset,'text.html','list-inset')
	output_file = open(output_folder+'list-inset'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('collection-repeat',collection_repeat,'text.html','collection-repeat')
	output_file = open(output_folder+'collection-repeat'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('ionicListDelegate.showReorder',ionicListDelegate_showReorder,'source.js','ionicListDelegate.showReorder')
	output_file = open(output_folder+'ionicListDelegate.showReorder'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('ionicListDelegate.showDelete',ionicListDelegate_showDelete,'source.js','ionicListDelegate.showDelete')
	output_file = open(output_folder+'ionicListDelegate.showDelete'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('ionicListDelegate.canSwipeItems',ionicListDelegate_canSwipeItems,'source.js','ionicListDelegate.canSwipeItems')
	output_file = open(output_folder+'ionicListDelegate.canSwipeItems'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

	snippet_str = create_snippet_string('ionicListDelegate.closeOptionButtons',ionicListDelegate_closeOptionButtons,'source.js','ionicListDelegate.closeOptionButtons')
	output_file = open(output_folder+'ionicListDelegate.closeOptionButtons'+".sublime-snippet","w+")
	output_file.write(snippet_str)
	output_file.close()

