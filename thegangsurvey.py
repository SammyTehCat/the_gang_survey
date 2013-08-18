import easygui

unova_gang_file_path = "C:\\Users\\Logan\\Desktop\\Python Programs\\"
unovaGang = unova_gang_file_path + "unova_gang.jpg"
ash = unova_gang_file_path + "courage.png"
iris = unova_gang_file_path + "irisMad.jpg"
cilan = unova_gang_file_path + "ccilan.jpg"
bianca = unova_gang_file_path + "280.jpg"
stephan = unova_gang_file_path + "stephan.png"

favorite = easygui.buttonbox("Which person in the Unova Gang do you like best?","The Unova Gang Quiz",
['Ash', 'Iris', 'Cilan', 'Bianca', 'Stephan'],unovaGang )
picture_choices = ''
if favorite == 'Ash':
	picture_choices = ash
if favorite == 'Iris':
	picture_choices = iris
if favorite == 'Cilan':
	picture_choices = cilan
if favorite == 'Bianca':
	picture_choices = bianca
if favorite == 'Stephan':
	picture_choices = stephan	

easygui.msgbox("You chose " + favorite,"The Unova Gang Quiz","Excellent choice, my friend.",picture_choices)
 