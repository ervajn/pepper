from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.1.110", 9559)
tts.say("Hello, world!")
