import os

text_file_name = 'scratches/ionicListDelegate.txt'
output_folder = os.path.dirname(os.path.abspath(__file__)) + "/services/"
text_input_file = open(text_file_name)


def create_snippet_string(tabTrigger,content,source,description):
	tabTrigger_tag = "<tabTrigger>"+tabTrigger+"</tabTrigger>"
	content_tag = "<content><![CDATA["+content+"]]></content>"
	source_tag = "<source>"+source+"</source>"
	if len(description) == 0:
		description_tag = "<description>...</description>"
	else:
		description_tag = "<description>"+description+"</description>"
	snippet_string = "<snippet>\n\t"+content_tag+"\n\t"+tabTrigger_tag+\
						"\n\t"+source_tag+"\n\t"+description_tag+"\n"+"</snippet>"
	return snippet_string					


for line in text_input_file.readlines():
	if line[0] != '#' and len(line) > 0:
		stripped_line = line.strip().split('|')[:len(line.strip().split('|'))-1]
		tabTrigger = stripped_line[0]
		content = stripped_line[1]
		source = stripped_line[2]
		description = stripped_line[3]
		snippet = create_snippet_string(tabTrigger, content, source, description)
		output_file = open(output_folder+tabTrigger+".sublime-snippet","w+")
		output_file.write(snippet)
		output_file.close()
