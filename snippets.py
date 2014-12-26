import os

current_path = os.path.dirname(os.path.abspath(__file__))
header = True
sub_header = True
footer = True

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
		header_str = '<div class="bar ' + bar + '"> \n' + '\t <h2 class="title">${1:' + bar + '}</h2> \n' + '</div>'
		snippet_str = create_snippet_string('ionic-subheader',header_str,'text.html',bar + ' snippet') 
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
		header_str = '<div class="bar bar-footer ' + bar + '"> \n' + '\t <div class="title">${1:' + bar + '}</div> \n' + '</div>'
		snippet_str = create_snippet_string('ionic-footer-'+bar[4:],header_str,'text.html','ionic-footer-'+bar[4:]) 
		print snippet_str
		print '----------'
		output_file = open(output_folder+'ionic-footer-'+bar[4:]+".sublime-snippet","w+")
		output_file.write(snippet_str)

	output_file.close()		