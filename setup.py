import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
	name = "Stinky Shoe Clicker",
	options = {"build_exe": {"packages":["pygame"],
				"include_files":["blueBG.jpg", "mudBG.jpg", "stinkyBG.jpg",
				"titleScreen.jpg", "gameOver.jpg", "fume1.png", "fume2.png",
				"mud.png", "napkin.png", "napkinButton.png", "napkinButtonDisabled.png",
				"sneaker.png", "song.mp3", "x2Multiplier1.png",
				"x2Multiplier1Disabled.png", "spraycanButton.png","spraycanButtonDisabled.png",
				"mood1.png", "mood2.png", "mood3.png","mood4.png","mood5.png", 
				"mood6.png", "mood7.png", "spraycan.png"]}},
	executables = executables
	
	)
