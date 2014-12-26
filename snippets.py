import os

current_path = os.path.dirname(os.path.abspath(__file__))
header = False
sub_header = False
footer = False
buttons = True

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

