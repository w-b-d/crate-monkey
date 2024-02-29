from django import forms


class Search(forms.Form):
    genres = [
        ('Random','Random'),
        ('Blues', 'Blues'),
        ('Brass', 'Brass & Military'),
        ('Classical', 'Classical'),
        ('Electronic', 'Electronic'),
        ('Folk', 'Folk, World, & Country'),
        ('Funk / Soul', 'Funk / Soul'),
        ('Jazz', 'Jazz'),
        ('Latin', 'Latin'),
        ('Pop', 'Pop'),
        ('Reggae', 'Reggae'),
        ('Rock', 'Rock'),
    ]





    genre = forms.ChoiceField(label="Genre", choices=genres)

class Rock(forms.Form):
    styles = [
        ('Random', 'Random'),

        ("Pop Rock","Pop Rock"),
        ("Punk", "Punk"),
        ("Indie Rock", "Indie Rock"),
        ("Hard Rock", "Hard Rock"),
        ("Classic Rock", "Classic Rock"),
        ("Psychedelic Rock", "Psychedelic Rock"),
        ("Acoustic", "Acoustic"),
        ("Vocal", "Vocal"),
        ("Country Rock","Country Rock"),
        ("Synth-pop", "Synth-pop"),
        ("Modern Classical", "Modern Classical"),
        ("Instrumental", "Instrumental"),
        ("Gospel","Gospel"),
        ("Experimental", "Experimental"),
        ("Heavy Metal", "Heavy Metal"),



    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)

class Electronic(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("House", "House"),
        ("Synth-pop", "Synth-pop"),
        ("Experimental", "Experimental"),
        ("Techno", "Techno"),
        ("Ambient", "Ambient"),
        ("Electro", "Electro"),
        ("Trance", "Trance"),
        ("Downtempo", "Downtempo"),
        ("Disco", "Disco"),
        ("Tech House", "Tech House"),
        ("Noise", "Noise"),
        ("Deep House", "Deep House"),
        ("Drum n Bass", "Drum n Bass"),
        ("Progressive House", "Progressive House"),
        ("Euro House", "Euro House"),
        ("Industrial", "Industrial"),
        ("Abstract", "Abstract"),
        ("Minimal", "Minimal"),
        ("Hardcore", "Hardcore"),
        ("Pop Rock", "Pop Rock"),
        ("Breakbeat", "Breakbeat"),
        ("Drone", "Drone"),
        ("Progressive Trance", "Progressive Trance"),
        ("IDM", "IDM"),
        ("New Wave", "New Wave"),
        ("Breaks", "Breaks"),
        ("Dark Ambient", "Dark Ambient"),
        ("Hard Trance", "Hard Trance"),
        ("Electro House", "Electro House"),
        ("Dance-pop", "Dance-pop"),
        ("Acid","Acid")



    ]
    style = forms.ChoiceField(label='Style', choices=styles)


class Pop(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("Pop Rock", "Pop Rock"),
        ("Ballad", "Ballad"),
        ("Chanson", "Chanson"),
        ("Schlager", "Schlager"),
        ("Synth-pop", "Synth-pop"),
        ("Europop", "Europop"),
        ("Easy Listening", "Easy Listening"),
        ("Indie Pop", "Indie Pop"),
        ("Disco", "Disco"),
        ("Soft Rock", "Soft Rock"),
        ("Rock & Roll", "Rock & Roll"),
        ("Indie Rock", "Indie Rock"),
        ("Soul", "Soul"),
        ("Soundtrack", "Soundtrack"),
        ("Alternative Rock", "Alternative Rock"),
        ("Folk", "Folk"),
        ("House", "House"),
        ("Dance-pop", "Dance-pop"),
        ("Folk Rock", "Folk Rock"),
        ("New Wave", "New Wave"),
        ("Holiday", "Holiday"),
        ("J-pop", "J-pop"),
        ("Electro", "Electro"),
        ("Country", "Country"),
        ("Euro House", "Euro House"),
        ("Rhythm & Blues", "Rhythm & Blues"),
        ("Beat", "Beat"),
        ("Downtempo", "Downtempo"),
        ("Funk", "Funk"),
        ("Vocal","Vocal"),
        ("Ambient","Ambient")
    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)


class Folk(forms.Form):
    styles = [
        ('Random', 'Random'),
        ('Folk','Folk'),
        ("Country", "Country"),
        ("Folk Rock", "Folk Rock"),
        ("African", "African"),
        ("Vocal", "Vocal"),
        ("Gospel", "Gospel"),
        ("Volksmusik", "Volksmusik"),
        ("Ballad", "Ballad"),
        ("Country Rock", "Country Rock"),
        ("Celtic", "Celtic"),
        ("Bluegrass", "Bluegrass"),
        ("Pop Rock", "Pop Rock"),
        ("Laïkó", "Laïkó"),
        ("Soundtrack", "Soundtrack"),
        ("Chanson", "Chanson"),
        ("Acoustic", "Acoustic"),
        ("Polka", "Polka"),
        ("Religious", "Religious"),
        ("Holiday", "Holiday"),
        ("Schlager", "Schlager"),
        ("Hindustani", "Hindustani"),
        ("Experimental", "Experimental"),
        ("Easy Listening", "Easy Listening"),
        ("Indie Rock", "Indie Rock"),
        ("Flamenco", "Flamenco"),
        ("Bollywood", "Bollywood"),
        ("Alternative Rock", "Alternative Rock"),
        ("Ambient", "Ambient"),
        ("Psychedelic Rock", "Psychedelic Rock"),
        ("Indian Classical", "Indian Classical"),

    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)


class Jazz(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("Easy Listening","Easy Listening"),
        ("Swing", "Swing"),
        ("Big Band", "Big Band"),
        ("Contemporary Jazz", "Contemporary Jazz"),
        ("Vocal", "Vocal"),
        ("Fusion", "Fusion"),
        ("Jazz-Funk", "Jazz-Funk"),
        ("Soul-Jazz", "Soul-Jazz"),
        ("Bop", "Bop"),
        ("Jazz-Rock", "Jazz-Rock"),
        ("Latin Jazz", "Latin Jazz"),
        ("Free Improvisation", "Free Improvisation"),
        ("Hard Bop", "Hard Bop"),
        ("Free Jazz", "Free Jazz"),
        ("Cool Jazz", "Cool Jazz"),
        ("Post Bop", "Post Bop"),
        ("Smooth Jazz", "Smooth Jazz"),
        ("Experimental", "Experimental"),
        ("Dixieland", "Dixieland"),
        ("Soundtrack", "Soundtrack"),
        ("Soul", "Soul"),
        ("Funk", "Funk"),
        ("Bossa Nova", "Bossa Nova"),
        ("Ballad", "Ballad"),
        ("Avant-garde Jazz", "Avant-garde Jazz"),
        ("Pop Rock", "Pop Rock"),
        ("Rhythm & Blues", "Rhythm & Blues"),
        ("Modal", "Modal"),
        ("Prog Rock", "Prog Rock"),
        ("Disco", "Disco")
    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)

class Funk(forms.Form):
    styles= [
    ('Random', 'Random'),
    ('Soul','Soul'),
    ("Disco", "Disco"),
    ("Funk", "Funk"),
    ("Rhythm & Blues", "Rhythm & Blues"),
    ("Contemporary R&B", "Contemporary R&B"),
    ("Pop Rock", "Pop Rock"),
    ("Gospel", "Gospel"),
    ("Synth-pop", "Synth-pop"),
    ("Ballad", "Ballad"),
    ("Jazz-Funk", "Jazz-Funk"),
    ("Vocal", "Vocal"),
    ("House", "House"),
    ("RnB/Swing", "RnB/Swing"),
    ("Soul-Jazz", "Soul-Jazz"),
    ("Rock & Roll", "Rock & Roll"),
    ("Boogie", "Boogie"),
    ("Downtempo", "Downtempo"),
    ("Soundtrack", "Soundtrack"),
    ("Electro", "Electro"),
    ("Neo Soul", "Neo Soul"),
    ("Easy Listening", "Easy Listening"),
    ("Soft Rock", "Soft Rock"),
    ("Afrobeat", "Afrobeat"),
    ("Doo Wop", "Doo Wop"),
    ("Psychedelic", "Psychedelic"),
    ("Pop Rap", "Pop Rap"),
    ("Fusion", "Fusion"),
    ("Alternative Rock", "Alternative Rock"),
    ("Psychedelic Rock", "Psychedelic Rock"),
    ("Blues Rock", "Blues Rock")]
    style = forms.ChoiceField(label = 'Style',choices = styles)



class Classical(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("Romantic","Romantic"),
        ("Classical", "Classical"),
        ("Baroque", "Baroque"),
        ("Modern", "Modern"),
        ("Opera", "Opera"),
        ("Contemporary", "Contemporary"),
        ("Choral", "Choral"),
        ("Renaissance", "Renaissance"),
        ("Neo-Classical", "Neo-Classical"),
        ("Soundtrack", "Soundtrack"),
        ("Religious", "Religious"),
        ("Experimental", "Experimental"),
        ("Vocal", "Vocal"),
        ("Holiday", "Holiday"),
        ("Easy Listening", "Easy Listening"),
        ("Impressionist", "Impressionist"),
        ("Modern Classical", "Modern Classical"),
        ("Operetta", "Operetta"),
        ("Ambient", "Ambient"),
        ("Score", "Score"),
        ("Folk", "Folk"),
        ("Neo-Romantic", "Neo-Romantic"),
        ("Medieval", "Medieval"),



    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)


class Latin(forms.Form):
    styles = [
    ('Random', 'Random'),
    ("Salsa","Salsa"),
    ("Bolero", "Bolero"),
    ("Cumbia", "Cumbia"),
    ("Ballad", "Ballad"),
    ("MPB", "MPB"),
    ("Samba", "Samba"),
    ("Tango", "Tango"),
    ("Latin Jazz", "Latin Jazz"),
    ("Cha-Cha", "Cha-Cha"),
    ("Merengue", "Merengue"),
    ("Vocal", "Vocal"),
    ("Rumba", "Rumba"),
    ("Flamenco", "Flamenco"),
    ("Easy Listening", "Easy Listening"),
    ("Ranchera", "Ranchera"),
    ("Mambo", "Mambo"),
    ("Pop Rock", "Pop Rock"),
    ("Bossanova", "Bossanova"),
    ("Folk", "Folk"),
    ("Afro-Cuban", "Afro-Cuban"),
    ("Guaracha", "Guaracha"),
    ("Son", "Son"),
    ("Bossa Nova", "Bossa Nova"),
    ("Latin", "Latin"),
    ("Guaguancó", "Guaguancó"),
    ("Disco", "Disco"),
    ("Funk", "Funk"),
    ("Chanson", "Chanson"),
    ("Mariachi", "Mariachi"),
    ("House", "House"),
    ("Soul", "Soul")
    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)



class Screen(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("Score", "Score"),
        ("Theme", "Theme"),
        ("Musical", "Musical"),
        ("Vocal", "Vocal"),
        ("Easy Listening", "Easy Listening"),
        ("Pop Rock", "Pop Rock"),
        ("Bollywood", "Bollywood"),
        ("Hindustani", "Hindustani"),
        ("Ballad", "Ballad"),
        ("Ambient", "Ambient"),
        ("Synth-pop", "Synth-pop"),
        ("Video Game Music", "Video Game Music"),
        ("Chanson", "Chanson"),
        ("Experimental", "Experimental"),
        ("Modern Classical", "Modern Classical"),
        ("Disco", "Disco"),
        ("Rock & Roll", "Rock & Roll"),
        ("Contemporary", "Contemporary"),
        ("Comedy", "Comedy"),

    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)


class Reggae(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("Dancehall","Dancehall"),
        ("Reggae", "Reggae"),
        ("Roots Reggae", "Roots Reggae"),
        ("Dub", "Dub"),
        ("Ska", "Ska"),
        ("Reggae-Pop", "Reggae-Pop"),
        ("Rocksteady", "Rocksteady"),
        ("Lovers Rock", "Lovers Rock"),
        ("Calypso", "Calypso"),
        ("Ragga", "Ragga"),
        ("Soca", "Soca"),
    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)

class Blues(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("Blues Rock","Blues Rock"),
        ("Rhythm & Blues", "Rhythm & Blues"),
        ("Rock & Roll", "Rock & Roll"),
        ("Electric Blues", "Electric Blues"),
        ("Country Blues", "Country Blues"),
        ("Chicago Blues", "Chicago Blues"),
        ("Soul", "Soul"),
        ("Pop Rock", "Pop Rock"),
        ("Classic Rock", "Classic Rock"),
        ("Folk", "Folk"),
        ("Vocal", "Vocal"),
        ("Psychedelic Rock", "Psychedelic Rock"),
        ("Folk Rock", "Folk Rock"),
        ("Piano Blues", "Piano Blues"),
    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)

class Non_Music(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("Comedy","Comedy"),
        ("Spoken Word", "Spoken Word"),
        ("Radioplay", "Radioplay"),
        ("Field Recording", "Field Recording"),
        ("Experimental", "Experimental"),
        ("Audiobook", "Audiobook"),
        ("Poetry", "Poetry"),
        ("Religious", "Religious"),
        ("Interview", "Interview"),
        ("Noise", "Noise"),
        ("Education", "Education"),
        ("Story", "Story"),
        ("Ambient", "Ambient"),
        ("Dialogue", "Dialogue"),
        ("Abstract", "Abstract"),
        ("Promotional", "Promotional"),
        ("Monolog", "Monolog"),
    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)

class Brass(forms.Form):
    styles = [
        ('Random', 'Random'),
        ("Marches","Marches"),
        ("Brass Band","Brass Band"),
        ("Military","Military")
    ]
    style = forms.ChoiceField(label = 'Style',choices = styles)
